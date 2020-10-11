import pytest

from striper.payments.models import Item, Order
from striper.payments.tests.factories import ItemFactory

pytestmark = pytest.mark.django_db


class TestItem:
    """
    TestSuite for Item model
    """
    def test_item_creation(self):
        """
        Tests Model's creation
        """
        item = Item.objects.create(
            name="test_item",
            description="test description",
            price=2.0
        )

        assert item is not None
        assert Item.objects.last() == item


class TestOrder:
    """
    TestSuit for Orders
    """

    def test_order_creation(self):
        """
        Tests model creation
        """
        items = ItemFactory.create_batch(3)

        order = Order.objects.create()
        assert order is not None
        assert Order.objects.last() == order

        order.items.set(items)

        assert len(order.items.all()) == len(items)

    def test_price_calculation(self):
        """
        Test's price property
        """
        items = ItemFactory.create_batch(3)

        order = Order.objects.create()
        order.items.set(items)

        price = sum([item.price for item in items])  # .create_batch returns list, so we can't use aggregation
        assert order.price == price
