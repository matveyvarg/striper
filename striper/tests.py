import pytest

from .payments.tests.factories import ItemFactory, OrderFactory
from .stripe_service import get_checkout_items

pytestmark = pytest.mark.django_db


def check_result(result: list, items: list):
    """
    Check names, prices, and descriptions
    :param result:
    :param items:
    :return:
    """
    for index, item in enumerate(items):
        assert result[index]['description'] == item.description
        assert result[index]['price_data']['unit_amount'] == item.price
        assert result[index]['price_data']['product_data']['name'] == item.name


def test_get_checkout_items_for_items():
    """
    Check generation correct data for item
    :return:
    """
    item = ItemFactory()
    result = get_checkout_items(item)

    assert result and len(result) == 1
    check_result(result, [item])


def test_get_checkout_items_for_order():
    """
    Check generation correct data for order
    :return:
    """
    items_count = 2
    order = OrderFactory.create(items=ItemFactory.create_batch(items_count))
    result = get_checkout_items(order)

    assert result and len(result) == items_count
    check_result(result, order.items.all())
