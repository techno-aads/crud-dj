# -*- coding: utf-8 -*-

from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.urls import reverse
from django.contrib import auth
from django.template.context_processors import csrf

from .models import OrderProd


# Create your views here.


def index(request):
	listOfOrders = OrderProd.objects.order_by('order_title')[:15]
	template = loader.get_template('orderproduct/index.html')
	context = {
		'listOfOrders': listOfOrders,
        'username':auth.get_user(request).username,
	}
	return HttpResponse(template.render(context, request))

def detail(request, orderprod_id):
    try:
        currentOrderProd = OrderProd.objects.get(pk=orderprod_id)
        orderTitle = currentOrderProd.order_title
        orderCount=currentOrderProd.order_count
        orderAddress=currentOrderProd.order_address
        orderDate=currentOrderProd.order_date
        orderStatus=currentOrderProd.oredr_status
    except OrderProd.DoesNotExist:
        raise Http404("Order does not exist")
    return render(request, 'orderproduct/detail.html', {
        'orderTitle': orderTitle,
        'orderCount': orderCount,
        'orderAddress': orderAddress,
        'orderDate': orderDate,
        'orderStatus': orderStatus,
        'o_id':orderprod_id,
        'username':auth.get_user(request).username,
        })

def add(request):
    orderNew = OrderProd(order_title=request.POST['order_title'], order_count=request.POST['order_count'], order_address=request.POST['order_address'], oredr_status=request.POST['order_status'])
    orderNew.save()
    return HttpResponseRedirect(reverse('orderproduct:index'))

def delete(request):
    OrderProd.objects.filter(id=request.POST["id"]).delete()
    return HttpResponseRedirect(reverse('orderproduct:index'))

def edit(request, orderprod_id):
    orderproduct = get_object_or_404(OrderProd, pk=orderprod_id)
    return render(request, 'orderproduct/edit.html', {'orderproduct': orderproduct,'username':auth.get_user(request).username})

def update(request, orderprod_id):
    OrderProd.objects.filter(id=orderprod_id).update(order_title=request.POST['order_title'], order_count=request.POST['order_count'], order_address=request.POST['order_address'], oredr_status=request.POST['order_status'])
    return HttpResponseRedirect(reverse('orderproduct:index'))

def login(request):
    args={}
    args.update(csrf(request))
    if request.POST:
        username=request.POST.get('username', '')
        password=request.POST.get('password', '')
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect(reverse('orderproduct:index'))
        else:
            args['login_error']="Пользователь не найден"
            return render_to_response('orderproduct/login.html',args)

    else:
        return render_to_response('orderproduct/login.html', args)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('orderproduct:index'))