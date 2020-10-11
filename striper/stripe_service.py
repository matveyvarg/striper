import stripe

from typing import Union, List

from django.conf import settings
from django.urls import reverse
from django.http.request import HttpRequest

from striper.payments.models import Order, Item

stripe.api_key = settings.STRIPE_SECRET_KEY


def get_checkout_items(item: Union[Item, Order]) -> List[dict]:
    """
    Generate structure for checkout
    :param item:
    :return:
    """
    if isinstance(item, Item):
        products = [item]
    else:
        products = item.items.all()

    return [
        {
            'price_data': {
                'currency': 'usd',
                'unit_amount': item.price,
                'product_data': {
                    'name': item.name
                }
            },
            'quantity': 1,
            'description': item.description
        } for item in products
    ]


def create_payment(item: Union[Item, Order], request: HttpRequest) -> str:
    """
    Creates PaymentIntent of Stripe
    :return:
    """
    if settings.STRIPE_USE_INTENT:
        intent = stripe.PaymentIntent.create(
            amount=item.price,
            currency='usd'
        )
        return intent['client_secret']

    items = get_checkout_items(item)
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=items,
        mode='payment',
        success_url=request.build_absolute_uri(reverse('success')),
        cancel_url=request.build_absolute_uri(reverse('cancel'))
    )
    return checkout_session.id
