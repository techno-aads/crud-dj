from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, Http404
from django.template import loader
from datetime import datetime
from .models import Product
import math

from . import views

def index(request):
	return render(request, 'index.html')



def products(request):
	count = Product.objects.count()

	products = Product.objects.all()

	context = {
		'products': products
	}

	return render(request, 'products.html', context)

def add_product(request):
	return render(request, 'new-product.html')

def product(request, product_id):
	product = get_object_or_404(Product, pk = product_id)
	context = {}

	context['product'] = product

	return render(request, 'product.html', context)

def remove_product(request):
	if ('product_id' in request.POST):
		product_id = int(request.POST['product_id'].strip())
	else:
		raise Http404()

	product = get_object_or_404(Product, pk = product_id)
	product.delete();
	return redirect('products')

def save_product(request):
	if ('product_id' in request.POST):
		product_id = int(request.POST['product_id'].strip())
	else:
		raise Http404()

	if (product_id > 0):
		product = get_object_or_404(Product, pk = product_id)
	else:
		product = Product.objects.create()

	if ('name' in request.POST):
		product.name = request.POST['name'].strip()
	else:
		raise Http404()

	if ('count' in request.POST):
		try:
			product.count = int(request.POST['count'].strip())
		except ValueError:
			product.count = 0
	else:
		raise Http404()

	if ('address' in request.POST):
		product.address = request.POST['address'].strip()
	else:
		raise Http404()

	if ('delivery_date' in request.POST):
		product.delivery_date = datetime.strptime(request.POST['delivery_date'].strip(), "%d.%m.%Y").date()
	else:
		raise Http404()

	product.status = ('status' in request.POST)

	product.save()
	return redirect('product', product.id)
