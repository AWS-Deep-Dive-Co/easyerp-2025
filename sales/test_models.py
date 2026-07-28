"""Real tests for sales business logic (see root CLAUDE.md for why this matters)."""
from decimal import Decimal

import pytest
from mixer.backend.django import mixer

from sales.models import SalesOrderLine, Invoice

pytestmark = pytest.mark.django_db


class TestSalesOrderLineTotal:
    def test_line_total_with_no_discount(self, make_product, make_sales_order):
        product = make_product()
        order = make_sales_order()
        line = mixer.blend(
            SalesOrderLine,
            sales_order=order,
            product=product,
            quantity=3,
            unit_price=Decimal("20.00"),
            discount_percent=Decimal("0"),
        )
        assert line.line_total == Decimal("60.00")

    def test_line_total_applies_discount_percent(self, make_product, make_sales_order):
        product = make_product()
        order = make_sales_order()
        line = mixer.blend(
            SalesOrderLine,
            sales_order=order,
            product=product,
            quantity=10,
            unit_price=Decimal("50.00"),
            discount_percent=Decimal("20"),
        )
        # 10 * 50.00 * (1 - 0.20) = 400.00
        assert line.line_total == Decimal("400.00")

    def test_line_total_recalculates_on_save(self, make_product, make_sales_order):
        product = make_product()
        order = make_sales_order()
        line = mixer.blend(
            SalesOrderLine,
            sales_order=order,
            product=product,
            quantity=2,
            unit_price=Decimal("10.00"),
            discount_percent=Decimal("0"),
        )
        assert line.line_total == Decimal("20.00")

        line.quantity = 5
        line.save()
        assert line.line_total == Decimal("50.00")


class TestInvoiceBalanceDue:
    def test_balance_due_with_no_payment(self, make_customer):
        invoice = mixer.blend(
            Invoice,
            customer=make_customer(),
            total_amount=Decimal("500.00"),
            paid_amount=Decimal("0.00"),
        )
        assert invoice.balance_due == Decimal("500.00")

    def test_balance_due_with_partial_payment(self, make_customer):
        invoice = mixer.blend(
            Invoice,
            customer=make_customer(),
            total_amount=Decimal("500.00"),
            paid_amount=Decimal("200.00"),
        )
        assert invoice.balance_due == Decimal("300.00")

    def test_balance_due_with_overpayment_is_negative(self, make_customer):
        invoice = mixer.blend(
            Invoice,
            customer=make_customer(),
            total_amount=Decimal("500.00"),
            paid_amount=Decimal("600.00"),
        )
        assert invoice.balance_due == Decimal("-100.00")

    def test_balance_due_fully_paid_is_zero(self, make_customer):
        invoice = mixer.blend(
            Invoice,
            customer=make_customer(),
            total_amount=Decimal("500.00"),
            paid_amount=Decimal("500.00"),
        )
        assert invoice.balance_due == Decimal("0.00")
