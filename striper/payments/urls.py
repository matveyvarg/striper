from django.urls import path
from django.views.generic import TemplateView

from .views import (
    OrderList,
    OrderDetail,
    OrderCreate,
    OrderBuy,

    ItemDetail,
    ItemBuy,
    ItemList
)

urlpatterns = [
    path('', OrderList.as_view(), name='index'),

    # Orders
    path('orders/', OrderCreate.as_view(), name='create_order'),
    path('orders/<int:pk>', OrderDetail.as_view(), name='order_detail'),
    path('orders/<int:pk>/buy', OrderBuy.as_view(), name='order_buy'),
    path('item/<int:pk>', ItemDetail.as_view(), name='item_detail'),
    path('buy/<int:pk>', ItemBuy.as_view(), name='item_buy'),

    # Items
    path('items/', ItemList.as_view(), name='items'),

    # callbacks
    path('success', TemplateView.as_view(template_name='success.html'), name='success'),
    path('cancel', TemplateView.as_view(template_name='cancel.html'), name='cancel'),
]
