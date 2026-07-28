"""
Shared pytest fixtures for easyerp.

inventory.Product is imported by both sales and purchasing, so its factory lives here rather
than being duplicated per-app. Use per-app conftest.py for fixtures specific to one app (e.g.
GL's fiscal_year/account chain).
"""
from decimal import Decimal

import pytest
from mixer.backend.django import mixer


@pytest.fixture
def make_company():
    def _make_company(**overrides):
        return mixer.blend("default.Company", **overrides)

    return _make_company


@pytest.fixture
def make_user():
    def _make_user(**overrides):
        return mixer.blend("default.User", **overrides)

    return _make_user


@pytest.fixture
def make_category():
    def _make_category(**overrides):
        return mixer.blend("inventory.Category", **overrides)

    return _make_category


@pytest.fixture
def make_supplier():
    def _make_supplier(**overrides):
        return mixer.blend("inventory.Supplier", **overrides)

    return _make_supplier


@pytest.fixture
def make_product():
    def _make_product(**overrides):
        overrides.setdefault("cost_price", Decimal("10.00"))
        overrides.setdefault("selling_price", Decimal("15.00"))
        overrides.setdefault("minimum_stock", 5)
        overrides.setdefault("maximum_stock", 100)
        return mixer.blend("inventory.Product", **overrides)

    return _make_product


@pytest.fixture
def make_customer():
    def _make_customer(**overrides):
        return mixer.blend("sales.Customer", **overrides)

    return _make_customer


@pytest.fixture
def make_sales_order():
    def _make_sales_order(**overrides):
        return mixer.blend("sales.SalesOrder", **overrides)

    return _make_sales_order
