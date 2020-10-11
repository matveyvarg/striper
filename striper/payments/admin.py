from django.contrib import admin

from .models import Order, Item, Discount, Tax


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin class for manging order in django-admin
    """


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """
    Admin class for manging items in django-admin
    """


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    """
    Admin class for manging discounts in django-admin
    """


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    """
    Admin class for manging taxes in django-admin
    """
