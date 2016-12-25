from django.shortcuts import render
from .models import Order
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django import forms

# Create your views here.

def register(request):
    return render(request,"registration/registration.html")

def create_new_user(request):
    try:
        user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
    except Exception:
        return HttpResponse("User already exist!")
    user.save()
    return HttpResponse("You are log on, now you can go to <a href='/app/login'>your account</a>")

def show_orders(request):
    myOrders = Order.objects.filter()
    if not request.user.is_authenticated():
        return render(request,"app/Orders.html",{"orders":myOrders,"flag":False})
    else:
        return render(request,"app/Orders.html",{"orders":myOrders,"flag":True})

def delete_order(request, uid):
    myOrder = Order.objects.get(id=uid)
    myOrder.delete()
    return HttpResponseRedirect(reverse('show_orders'))

def add_order(request):
    foo = False
    if (request.POST.get('status',False)=='on'):
        foo = True
    try:
        myOrder = Order.objects.get(name=request.POST.get('name',False), amount=request.POST.get('amount',False),addres=request.POST.get('addres',False),date=request.POST.get('date',False), status=foo)
    except (KeyError, Order.DoesNotExist):
        i = Order(name=request.POST.get('name',False), amount=request.POST.get('amount',False),addres=request.POST.get('addres',False),date=request.POST.get('date',False), status=foo)
        i.save()
        return HttpResponseRedirect(reverse('show_orders'))
    return HttpResponse("Order with same parameters already exist!")

def show_full(request, uid):
    myOrder = Order.objects.get(id=uid)
    if not request.user.is_authenticated():
        return render(request,"app/full.html",{"order":myOrder,"flag":False})
    else:
        return render(request,"app/full.html",{"order":myOrder,"flag":True})


def save_order(request, uid):
    myOrder = Order.objects.get(id=uid)
    myOrder.name = request.POST.get('name',False)
    myOrder.amount = request.POST.get('amount',False)
    myOrder.addres = request.POST.get('addres',False)
    myOrder.date = request.POST.get('date',False)
    if (request.POST.get('status',False)=='on'):
        myOrder.status = True
    else:
        myOrder.status = False
    myOrder.save()
    return HttpResponseRedirect(reverse('show_orders')) 