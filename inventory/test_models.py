"""Real tests for inventory business logic (see root CLAUDE.md for why this matters)."""
import pytest
from mixer.backend.django import mixer

from inventory.models import StockMovement

pytestmark = pytest.mark.django_db


class TestProductCurrentStock:
    def test_current_stock_is_zero_with_no_movements(self, make_product):
        product = make_product()
        assert product.current_stock == 0

    def test_current_stock_sums_positive_movements(self, make_product):
        product = make_product()
        mixer.blend(StockMovement, product=product, movement_type="IN", quantity_change=50)
        mixer.blend(StockMovement, product=product, movement_type="IN", quantity_change=25)

        assert product.current_stock == 75

    def test_current_stock_nets_out_and_in_movements(self, make_product):
        product = make_product()
        mixer.blend(StockMovement, product=product, movement_type="IN", quantity_change=100)
        mixer.blend(StockMovement, product=product, movement_type="OUT", quantity_change=-40)

        assert product.current_stock == 60

    def test_current_stock_can_go_negative_on_over_withdrawal(self, make_product):
        product = make_product()
        mixer.blend(StockMovement, product=product, movement_type="IN", quantity_change=10)
        mixer.blend(StockMovement, product=product, movement_type="OUT", quantity_change=-30)

        assert product.current_stock == -20

    def test_current_stock_only_counts_movements_for_this_product(self, make_product):
        product_a = make_product()
        product_b = make_product()
        mixer.blend(StockMovement, product=product_a, movement_type="IN", quantity_change=100)
        mixer.blend(StockMovement, product=product_b, movement_type="IN", quantity_change=999)

        assert product_a.current_stock == 100


class TestProductStockThresholds:
    def test_stock_below_minimum_threshold(self, make_product):
        product = make_product(minimum_stock=20, maximum_stock=200)
        mixer.blend(StockMovement, product=product, movement_type="IN", quantity_change=5)

        assert product.current_stock < product.minimum_stock

    def test_stock_above_maximum_threshold(self, make_product):
        product = make_product(minimum_stock=10, maximum_stock=100)
        mixer.blend(StockMovement, product=product, movement_type="IN", quantity_change=150)

        assert product.current_stock > product.maximum_stock
