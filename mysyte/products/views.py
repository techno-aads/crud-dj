from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Product
from django.contrib.auth.forms import UserCreationForm


class IndexView(generic.ListView):
    template_name = 'products/index.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.all()


@login_required()
def addOrder(request):
    return render(request, 'products/addOrder.html')


@login_required()
def addOrderDone(request):
    name = request.POST['name']
    count = request.POST['count']
    address = request.POST['address']
    delivery_date = request.POST['delivery_date']
    customer = request.user.get_username()

    newOrder = Product(name=name, count=count, address=address, delivery_date=delivery_date, customer=customer)
    newOrder.save()
    return HttpResponseRedirect(reverse('products:index'))


@login_required()
def editOrder(request):
    editableOrder = get_object_or_404(Product, pk=request.POST['id'])
    context = {'product': editableOrder}
    return render(request, 'products/editOrder.html', context)


@login_required()
def editOrderDone(request):
    editableOrder = get_object_or_404(Product, pk=request.POST['id'])
    editableOrder.name = request.POST['name']
    editableOrder.count = request.POST['count']
    editableOrder.address = request.POST['address']
    editableOrder.delivery_date = timezone.now()  # request.POST['delivery_date'] заглушка
    editableOrder.save()
    return HttpResponseRedirect(reverse('products:index'))


@login_required()
def removeOrder(request):
    orderForRemove = get_object_or_404(Product, pk=request.POST['id'])
    orderForRemove.delete()
    return HttpResponseRedirect(reverse('products:index'))


def registration(request):
    if not request.user.is_authenticated():
        if not request.method == 'POST':
            form = UserCreationForm()
            return render(request, 'products/registration.html', {'form': form})
        else:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.info(request, "Thanks for registering. You are now logged in.")
                new_user = authenticate(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password1'],
                                        )
                login(request, new_user)
                return redirect('products:index')
            else:
                return render(request, 'products/registration.html', {'form': form})
    else:
        messages.info(request, "You have to logout to register new user")
        # test it
        return redirect('products:index')
