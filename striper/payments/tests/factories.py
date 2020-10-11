from decimal import Decimal
from factory.django import DjangoModelFactory
from factory import Faker


class ItemFactory(DjangoModelFactory):
    """
    Factory for Item models
    """
    price = Decimal("3.0")
    description = Faker('paragraph')
    name = Faker('first_name')

    class Meta:
        model = 'payments.Item'
