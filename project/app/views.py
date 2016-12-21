from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, Http404
from django.template import loader
from datetime import datetime
from .models import Product
import math, re

from . import views

patternLogin = re.compile("^([a-zA-Z0-9]+[\.\-]?){3,}$")
patternEmail = re.compile("^[^\@]+@[^\@]+$")


def index(request):
	return render(request, 'index.html')

def auth(request):
	if request.user.is_authenticated():
		return redirect('index')

	context = {}
	if ('login' in request.POST):
		user_login = request.POST['login']

		if ('password' in request.POST):
			password = request.POST['password']
		else:
			raise Http404()

		user = authenticate(username=user_login, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('index')
			else:
				context['error'] = "Your account is suspended"
		else:
			context['login'] = user_login
			context['error'] = "Invalid username or password"
	return render(request, 'login.html', context)

def auth_out(request):
	logout(request)
	return redirect('index')

def registration_success(request):
	return render(request, 'registration-success.html')

def registration(request):
	if request.user.is_authenticated():
		return redirect('index')

	context = {}
	if ('login' in request.POST):
		login = request.POST['login'].strip()
		if not patternLogin.match(login):
			context['error'] = "Invalid login"

		if ('email' in request.POST):
			email = request.POST['email'].strip()
			if not patternEmail.match(email):
				context['error'] = "Invalid email"
		else:
			raise Http404()

		if ('password' in request.POST):
			password = request.POST['password']

			b = bool(re.search(r'[a-z]', password))
			b = b and bool(re.search(r'[A-Z]', password))
			b = b and bool(re.search(r'[0-9]', password))
			b = b and (len(password) > 7)
			if not b:
				context['error'] = "Invalid password"
		else:
			raise Http404()

		if ('password-repeat' in request.POST):
			password_repeat = request.POST['password-repeat']
			if (password != password_repeat):
				context['error'] = "Invalid repeated password"
		else:
			raise Http404()

		if (not 'error' in context):
			try:
				User.objects.get(username=login)
			except User.DoesNotExist:
				user = User.objects.create_user(login, email, password)
				return redirect('registration_success')

			context['error'] = "This login already exists"

	return render(request, 'registration.html', context)

def products(request):
	count = Product.objects.count()
	products = Product.objects.all()
	context = {
		'products': products
	}
	return render(request, 'products.html', context)

def add_product(request):
	if request.user.is_authenticated():
		return render(request, 'new-product.html')
	else:
		return redirect('login')

def product(request, product_id):
	product = get_object_or_404(Product, pk = product_id)
	context = {}

	context['product'] = product

	if request.user.is_authenticated():
		return render(request, 'product.html', context)
	else:
		return render(request, 'product-view.html', context)

def remove_product(request):
	if not request.user.is_authenticated():
		return redirect('login')

	if ('product_id' in request.POST):
		product_id = int(request.POST['product_id'].strip())
	else:
		raise Http404()

	product = get_object_or_404(Product, pk = product_id)
	product.delete();
	return redirect('products')

def save_product(request):
	if not request.user.is_authenticated():
		return redirect('login')

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
