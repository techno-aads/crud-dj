from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import Order
from .forms import OrderForm


def order_list(request):
    orders = Order.objects.filter(delivery_date__lte=timezone.now()).order_by('-delivery_date')
    return render(request, 'goods/order_list.html', {'orders': orders})


def order_new(request):
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            return HttpResponseRedirect(reverse('goods:order_list'))
    else:
        form = OrderForm()
    return render(request, 'goods/order_new.html', {'form': form})


def order_edit(request, pk=1):
    order = get_object_or_404(Order, pk=pk)
    if request.POST:
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.deliver()
            order.save()
            return HttpResponseRedirect(reverse('goods:order_list'))
    else:
        form = OrderForm(instance=order)
    return render(request, 'goods/order_new.html', {'form': form})


def order_remove(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return HttpResponseRedirect(reverse('goods:order_list'))
