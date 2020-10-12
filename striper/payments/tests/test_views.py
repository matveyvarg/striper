import pytest

from django.test import Client, RequestFactory

from striper.payments.models import Order
from striper.payments.views import OrderList
from striper.payments.tests.factories import ItemFactory

pytestmark = pytest.mark.django_db

STATUS_OK = 200
STATUS_REDIRECTED = 302


def test_index(rf: RequestFactory):
    """
    Test Index Page
    :param rf:
    :return:
    """
    Order.objects.create()
    request = rf.get('')
    response = OrderList.as_view()(request)

    assert response.status_code == STATUS_OK


def test_order_create_page(client: Client):
    """
    Should return 200 and form
    :param rf:
    :return:
    """
    Order.objects.create()
    response = client.get('/orders/')
    assert response.status_code == STATUS_OK


def test_order_creation(client: Client):
    count = Order.objects.count()
    item = ItemFactory()
    response = client.post('/orders/', {'items': [item.id]})

    assert response.status_code == STATUS_REDIRECTED
    assert Order.objects.count() == count + 1
    assert item in Order.objects.last().items.all()


def test_item_detail_page(client: Client):
    """
    Should return 200 and item info
    :param client:
    :return:
    """
    item = ItemFactory()
    response = client.get(f"/item/{item.id}")
    assert response.status_code == STATUS_OK
