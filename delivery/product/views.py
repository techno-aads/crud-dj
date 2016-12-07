from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from .models import Product
	
def all(request):
	latest_product_list = Product.objects.order_by('-date_delivery')[:5]
	template = loader.get_template('product/index.html')
	context = RequestContext(request, {
		'latest_product_list': latest_product_list,
	})
	return HttpResponse(template.render(context))
	
def index(request):
    latest_product_list = Product.objects.order_by('-date_delivery')[:5]
    context = {'latest_product_list': latest_product_list}
    return render(request, 'product/index.html', context)	
	
def detail(request, id):
	latest_product_list = Product.objects.get(name_product=id)
	context = {'latest_product_list': latest_product_list}
	return render(request, 'product/edit.html', context)	
	
def add(request, id):
    return HttpResponse("You're looking at question %s." % id)

def edit(request, id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % id)

def delete(request, id):
    return HttpResponse("You're voting on question %s." % id)