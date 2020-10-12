from decimal import Decimal
from factory.django import DjangoModelFactory
from factory import Faker, post_generation


class ItemFactory(DjangoModelFactory):
    """
    Factory for Item models
    """
    price = Decimal("3.0")
    description = Faker('paragraph')
    name = Faker('first_name')

    class Meta:
        model = 'payments.Item'


class OrderFactory(DjangoModelFactory):

    @post_generation
    def items(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for item in extracted:
                self.items.add(item)

    class Meta:
        model = 'payments.Order'
