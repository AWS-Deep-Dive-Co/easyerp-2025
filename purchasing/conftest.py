import pytest
from mixer.backend.django import mixer


@pytest.fixture
def make_purchase_order():
    def _make_purchase_order(**overrides):
        overrides.setdefault("supplier", mixer.blend("inventory.Supplier"))
        return mixer.blend("purchasing.PurchaseOrder", **overrides)

    return _make_purchase_order
