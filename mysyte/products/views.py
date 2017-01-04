from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Product


class IndexView(generic.ListView):
    template_name = 'products/index.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.all()


def addOrder(request):
    return render(request, 'products/addOrder.html')


def addOrderDone(request):
    name = request.POST['name']
    count = request.POST['count']
    address = request.POST['address']
    delivery_date = request.POST['delivery_date']

    newOrder = Product(name=name, count=count, address=address, delivery_date=delivery_date)
    newOrder.save()
    return HttpResponseRedirect(reverse('products:index'))


def editOrder(request):
    editableOrder = get_object_or_404(Product, pk=request.POST['id'])
    context = {'product': editableOrder}
    return render(request, 'products/editOrder.html', context)


def editOrderDone(request):
    editableOrder = get_object_or_404(Product, pk=request.POST['id'])
    editableOrder.name = request.POST['name']
    editableOrder.count = request.POST['count']
    editableOrder.address = request.POST['address']
    editableOrder.delivery_date = timezone.now() #request.POST['delivery_date'] заглушка

    editableOrder.save()
    return HttpResponseRedirect(reverse('products:index'))


def removeOrder(request):
    orderForRemove = get_object_or_404(Product, pk=request.POST['id'])
    orderForRemove.delete()
    return HttpResponseRedirect(reverse('products:index'))
