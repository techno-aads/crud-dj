from django.shortcuts import render
from .models import Item
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.

def show_items(request):
    myItems = Item.objects.filter()
    return render(request,"FirstClassWork/Items.html",{"items":myItems})

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
    return render(request,"FirstClassWork/full.html",{"item":myItem})
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
