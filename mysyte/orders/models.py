from django.db import models
from django.forms import ModelForm
from django import forms


class Order(models.Model):
    product = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
    delivery_address = models.CharField(max_length=200)
    delivery_date = models.DateField()  # 'Delivery date'
    customer = models.CharField(max_length=300)

    def __str__(self):
        return "product=" + self.product + " " \
        "count=" + str(self.count) + " " \
        "address=" + self.address + " " \
        "delivery_date=" + str(self.delivery_date) + " " \
        "status=" + str(self.status) + " " \
        "customer=" + str(self.customer)


class OrderForm(ModelForm):
    count = forms.DecimalField(min_value=1, max_value=9)
    delivery_date = forms.DateTimeField(widget=forms.SelectDateWidget)

    class Meta:
        model = Order
        fields = "__all__"
