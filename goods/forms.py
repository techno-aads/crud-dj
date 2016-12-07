from django import forms
from .models import Order


class DateInput(forms.DateTimeInput):
    input_type = 'date'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product_name', 'product_quantity', 'delivery_address', 'delivery_date', 'status']
        widgets = {
            'delivery_date': DateInput(),
        }
