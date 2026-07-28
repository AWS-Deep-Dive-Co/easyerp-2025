"""Real tests for purchasing business logic (see root CLAUDE.md for why this matters)."""
from decimal import Decimal

import pytest
from mixer.backend.django import mixer

from purchasing.models import PurchaseOrderLine

pytestmark = pytest.mark.django_db


class TestPurchaseOrderLineTotal:
    def test_line_total_is_quantity_times_unit_cost(self, make_product, make_purchase_order):
        line = mixer.blend(
            PurchaseOrderLine,
            purchase_order=make_purchase_order(),
            product=make_product(),
            quantity_ordered=8,
            unit_cost=Decimal("12.50"),
        )
        assert line.line_total == Decimal("100.00")

    def test_line_total_recalculates_on_save(self, make_product, make_purchase_order):
        line = mixer.blend(
            PurchaseOrderLine,
            purchase_order=make_purchase_order(),
            product=make_product(),
            quantity_ordered=2,
            unit_cost=Decimal("5.00"),
        )
        assert line.line_total == Decimal("10.00")

        line.quantity_ordered = 6
        line.save()
        assert line.line_total == Decimal("30.00")


class TestQuantityPending:
    def test_quantity_pending_when_nothing_received(self, make_product, make_purchase_order):
        line = mixer.blend(
            PurchaseOrderLine,
            purchase_order=make_purchase_order(),
            product=make_product(),
            quantity_ordered=100,
            quantity_received=0,
            unit_cost=Decimal("1.00"),
        )
        assert line.quantity_pending == 100

    def test_quantity_pending_when_fully_received(self, make_product, make_purchase_order):
        line = mixer.blend(
            PurchaseOrderLine,
            purchase_order=make_purchase_order(),
            product=make_product(),
            quantity_ordered=50,
            quantity_received=50,
            unit_cost=Decimal("1.00"),
        )
        assert line.quantity_pending == 0

    def test_quantity_pending_is_negative_when_over_received(self, make_product, make_purchase_order):
        line = mixer.blend(
            PurchaseOrderLine,
            purchase_order=make_purchase_order(),
            product=make_product(),
            quantity_ordered=20,
            quantity_received=25,
            unit_cost=Decimal("1.00"),
        )
        assert line.quantity_pending == -5
