from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Order


class OrderForm(ModelForm):
    """
    Form for order creation
    """
    helper = FormHelper()

    class Meta:
        model = Order
        fields = 'items'  # I hide Discounts and Taxes

    def __init__(self, *args, **kwargs):
        """
        Override for setting helper
        :param args:
        :param kwargs:
        """

        super(OrderForm, self).__init__(*args, **kwargs)
        self.helper.inputs = []
        self.helper.add_input(Submit('submit', 'Submit'))
