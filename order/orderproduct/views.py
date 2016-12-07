from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import OrderProd


# Create your views here.


def index(request):
	listOfOrders = OrderProd.objects.order_by('order_title')[:3]
	template = loader.get_template('orderproduct/index.html')
	context = {
		'listOfOrders': listOfOrders
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
        })

def add(request):
    orderNew = OrderProd(order_title=request.POST['order_title'], order_count=request.POST['order_count'], order_address=request.POST['order_address'], order_date=request.POST['order_date'], oredr_status=request.POST['order_status'])
    orderNew.save()
    return HttpResponseRedirect(reverse('orderprod:index'))

def delete(request):
    OrderProd.objects.filter(id=request.POST["id"]).delete()
    return HttpResponseRedirect(reverse('orderproduct:index'))

def edit(request, orderprod_id):
    orderproduct = get_object_or_404(OrderProd, pk=orderprod_id)
    return render(request, 'orderproduct/edit.html', {'orderproduct': orderproduct})

def update(request, orderprod_id):
    OrderProd.objects.filter(id=orderprod_id).update(order_title=request.POST['order_title'], order_count=request.POST['order_count'], order_address=request.POST['order_address'], order_date=request.POST['order_date'], oredr_status=request.POST['order_status'])
    return HttpResponseRedirect(reverse('orderproduct:index'))