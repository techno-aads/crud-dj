from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Order, OrderForm
from django.contrib.auth.forms import UserCreationForm
from datetime import date
from django.forms.utils import ErrorList


def index(request):
    order_list = Order.objects.all()
    context = {'order_list': order_list, 'date': date.today()}
    return render(request, 'orders/index.html', context)


@login_required()
def add(request):
    form = OrderForm()
    return render(request, 'orders/add.html', {'form': form})


@login_required()
def addDone(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            product = request.POST['product']
            count = request.POST['count']
            delivery_address = request.POST['delivery_address']
            delivery_date = request.POST['delivery_date_year'] + "-" + \
                            request.POST['delivery_date_month'] + "-" + \
                            request.POST['delivery_date_day']
            customer = request.user.get_username()
            newOrder = Order(product=product, count=count, delivery_address=delivery_address,
                             delivery_date=delivery_date,
                             customer=customer)
            newOrder.save()
            messages.info(request, "Add successful")
            return HttpResponseRedirect(reverse('orders:index'))
        else:
            messages.info(request, "Data is not valid")
            return render(request, 'orders/add.html', {'form': form})
    return redirect('orders:index')


@login_required()
def edit(request):
    if request.method == 'POST':
        order = get_object_or_404(Order, pk=request.POST['id'])
        form = OrderForm(initial={'product': order.product,
                                  'count': order.count,
                                  'delivery_address': order.delivery_address,
                                  'delivery_date': order.delivery_date,
                                  'customer': order.customer
                                  })
        context = {'form': form, 'order_id': request.POST['id']}
        return render(request, 'orders/edit.html', context)
    return redirect('orders:index')


@login_required()
def editDone(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            editableOrder = get_object_or_404(Order, pk=request.POST['id'])
            editableOrder.product = request.POST['product']
            editableOrder.count = request.POST['count']
            editableOrder.delivery_address = request.POST['delivery_address']
            editableOrder.delivery_date = request.POST['delivery_date_year'] + "-" + \
                                          request.POST['delivery_date_month'] + "-" + \
                                          request.POST['delivery_date_day']
            editableOrder.customer = request.POST['customer']
            editableOrder.save()
            messages.info(request, "Edit successful")
            return redirect('orders:index')
        else:
            return render(request, 'orders/edit.html', {'form': form})
    return redirect('orders:index')


@login_required()
def remove(request):
    if request.method == 'POST':
        orderForRemove = get_object_or_404(Order, pk=request.POST['id'])
        orderForRemove.delete()
        return HttpResponseRedirect(reverse('orders:index'))
    return redirect('orders:index')


def registration(request):
    if not request.user.is_authenticated():
        if not request.method == 'POST':
            form = UserCreationForm()
            return render(request, 'orders/registration.html', {'form': form})
        else:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.info(request, "Thanks for registering. You are now logged in.")
                new_user = authenticate(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password1'],
                                        )
                login(request, new_user)
                return redirect('orders:index')
            else:
                return render(request, 'orders/registration.html', {'form': form})
    else:
        messages.info(request, "You have to logout to register new user")
        # test it
        return redirect('orders:index')
