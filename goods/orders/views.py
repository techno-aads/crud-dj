from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import Http404
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'orders/index.html'
    context_object_name = 'last_products'

    def get_queryset(self):
        """Return the last ten products."""
        return Product.objects.order_by('-name')[:10]


class DetailView(generic.DetailView):
    model = Product
    template_name = 'orders/detail.html'


class ProductCreate(generic.CreateView):
    template_name_suffix = '_create'
    model = Product
    fields = ['name', 'quantity', 'address', 'delivery_date', 'status']
    success_url = reverse_lazy('orders:index')


class ProductDelete(generic.DeleteView):
    template_name_suffix = '_delete'
    model = Product
    success_url = reverse_lazy('orders:index')


class ProductUpdate(generic.UpdateView):
    template_name_suffix = '_update'
    model = Product
    fields = ['name', 'quantity', 'address', 'delivery_date', 'status']
    success_url = reverse_lazy('orders:index')

