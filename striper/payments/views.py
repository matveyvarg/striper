from django.http import HttpRequest
from django.views.generic import DetailView, CreateView, ListView
from django.http.response import JsonResponse
from django.urls import reverse_lazy

from ..stripe_service import create_payment

from .models import Order, Item
from .forms import OrderForm


class OrderList(ListView):
    """
    Index page with list of orders
    """
    model = Order
    template_name = "pages/home.html"


class OrderCreate(CreateView):
    """
    Page with form for create order
    """
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("index")


class OrderDetail(DetailView):
    """
    View with detailed information about order
    """
    model = Order


class ItemDetail(DetailView):
    """
    View with detailed information about item
    """
    model = Item


# Split to 2 views, cause we have to identify model. Also possible to use one view with UUID
class BuyView(DetailView):
    def get(self, request: HttpRequest, *args, **kwargs):
        """
        Return json with payment id
        :param request:
        :return:
        """
        return JsonResponse({'key': create_payment(self.get_object(), request)})


class OrderBuy(BuyView):
    """
    Create Payment Intent for order and return
    """
    model = Order


class ItemBuy(BuyView):
    """
    Create Payment Intent for order and return
    """
    model = Item
