from decimal import Decimal

from django.db import models
from django.urls import reverse
from django.utils.text import gettext_lazy as _


class Item(models.Model):
    """
    Base class for Item
    Keep such info as name, description price
    """

    name = models.CharField(_("Item's name"), max_length=255)
    description = models.TextField(_("Item's description"))
    price = models.PositiveIntegerField(_("Item's price"), default=50)

    @property
    def url(self):
        """
        Return url for item detail page
        :return:
        """
        return reverse('item_detail', kwargs={'pk': self.id})

    def __str__(self) -> str:
        return f"{self.name}:{self.price}$"


class Discount(models.Model):
    """
    Discount for order
    """
    amount = models.PositiveSmallIntegerField(_("How big is discount"), default=0)


class Tax(models.Model):
    """
    Taxes for order
    """
    amount = models.PositiveSmallIntegerField(_("How big is tax"), default=0)


class Order(models.Model):
    """
    Base class for order
    Order keep multiple Items inside
    """
    items = models.ManyToManyField(Item, verbose_name=_("Items to purchase"), related_name='orders')

    discount = models.ForeignKey(Discount, models.CASCADE, verbose_name=_(" Discount applied for order"), null=True,
                                 blank=True)
    tax = models.ForeignKey(Tax, models.CASCADE, verbose_name=_("Tax applied for order"), null=True, blank=True)

    @property
    def url(self) -> str:
        """
        Return url for detail page
        :return:
        """
        return reverse('order_detail', kwargs={'pk': self.id})

    @property
    def price(self) -> Decimal:
        """
        :return: price of all items
        """
        return self.items.aggregate(models.Sum('price')).get('price__sum')

    def __str__(self) -> str:
        return f"Order #{self.id} ({self.items.count()} items)"
