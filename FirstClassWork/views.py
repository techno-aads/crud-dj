from django.shortcuts import render
from .models import Item
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
<<<<<<< HEAD
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
        return HttpResponse("Такой пользователь уже существует!")
    user.save()
    return HttpResponse("Вы успешно зарегистрировались, теперь вы можете <a href='/FirstClassWork/login'>зайти</a> под своим аккаунтом")

def show_items(request):
    myItems = Item.objects.filter()
    if not request.user.is_authenticated():
        return render(request,"FirstClassWork/Items.html",{"items":myItems,"flag":False})
    else:
        return render(request,"FirstClassWork/Items.html",{"items":myItems,"flag":True})
=======

# Create your views here.

def show_items(request):
    myItems = Item.objects.filter()
    return render(request,"FirstClassWork/Items.html",{"items":myItems})
>>>>>>> e5aa9da59321a6318a92a2c80dbe808ee851327f

def delete_item(request, uid):
    myItem = Item.objects.get(id=uid)
    myItem.delete()
    return HttpResponseRedirect(reverse('show_items'))

def add_item(request):
    foo = False
    if (request.POST.get('complete',False)=='on'):
        foo = True
    try:
        myItem = Item.objects.get(name=request.POST.get('name',False), count=request.POST.get('count',False),to=request.POST.get('to',False),date=request.POST.get('date',False), complete=foo)
    except (KeyError, Item.DoesNotExist):
        i = Item(name=request.POST.get('name',False), count=request.POST.get('count',False),to=request.POST.get('to',False),date=request.POST.get('date',False), complete=foo)
        i.save()
        return HttpResponseRedirect(reverse('show_items'))
    return HttpResponse("Товар с такими параметрами уже есть!")

def show_full(request, uid):
    myItem = Item.objects.get(id=uid)
<<<<<<< HEAD
    if not request.user.is_authenticated():
        return render(request,"FirstClassWork/full.html",{"item":myItem,"flag":False})
    else:
        return render(request,"FirstClassWork/full.html",{"item":myItem,"flag":True})


=======
    return render(request,"FirstClassWork/full.html",{"item":myItem})
>>>>>>> e5aa9da59321a6318a92a2c80dbe808ee851327f
def save_item(request, uid):
    myItem = Item.objects.get(id=uid)
    myItem.name = request.POST.get('name',False)
    myItem.count = request.POST.get('count',False)
    myItem.to = request.POST.get('to',False)
    myItem.date = request.POST.get('date',False)
    if (request.POST.get('complete',False)=='on'):
        myItem.complete = True
    else:
        myItem.complete = False
    myItem.save()
    return HttpResponseRedirect(reverse('show_items'))
