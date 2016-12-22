from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Order
from datetime import datetime, date, time
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    order_list = Order.objects.all()
    template = loader.get_template('models/index.html')
    context = {
        'order_list': order_list,
        'auth': request.user.is_authenticated,
    }
    return HttpResponse(template.render(context, request))

def detail(request, order_id):
	if request.user.is_authenticated:
		obj = get_object_or_404(Order, pk=order_id)
		return render(request, 'models/detail.html', {'order': obj})
	else:
		return HttpResponseRedirect(reverse('models:index'))

def add(request):
	if request.user.is_authenticated:
		return render(request, 'models/add.html', {'date_now': datetime.now})
	else:
		return HttpResponseRedirect(reverse('models:index'))

def added(request):
	obj = Order()
	obj.name = request.POST['name']
	obj.count = request.POST['count']
	obj.address = request.POST['address']
	obj.order_date = datetime.now() #request.POST['order_date']
	obj.state = request.POST.get('state', False)
	obj.save()
	return HttpResponseRedirect(reverse('models:index'))

def delete(request, order_id):
	if request.user.is_authenticated:
		obj = get_object_or_404(Order, pk=order_id)
		try:
			obj.delete()
		except (KeyError, Order.DoesNotExist):
			return render(request, 'models:detail', {
     	       'order': obj,
     	       'error_message': "Order not found.",
    	    })
		else:
			return HttpResponseRedirect(reverse('models:index'))
	else:
		return HttpResponseRedirect(reverse('models:index'))

def edit(request, order_id):
	try:
		obj = get_object_or_404(Order, pk=order_id)
		obj.name = request.POST['name']
		obj.count = request.POST['count']
		obj.address = request.POST['address']
		obj.order_date = request.POST['order_date']
		obj.state = request.POST.get('state', False)
		obj.save()
	except (KeyError, Order.DoesNotExist):
		return render(request, 'models:detail', {
    		'order': obj,
    		'error_message': "Order not found.",
    		})
	else:
		return HttpResponseRedirect(reverse('models:index'))

def signin(request):
	return render(request, 'models/signin.html')

def login_view(request):
    username = request.POST['login']
    password = request.POST['pass']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('models:index'))
    else:
    	return render(request, 'models/signin.html', {'error_message':"Неверный логин/пароль"})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('models:index'))

def signup(request):
	return render(request, 'models/signup.html')

def add_user(request):
    username = request.POST['login']
    password = request.POST['pass']
    password2 = request.POST['pass2']    
    if password !=  password2:
    	return render(request, 'models/signup.html', {'error_message':"Пароли не совпадают"})
    try:
    	u = User.objects.get(username=username)
    except (KeyError, User.DoesNotExist):
    	user = User()
    	user.username = username
    	user.set_password(password)
    	user.save()
    	login(request, user)
    	return HttpResponseRedirect(reverse('models:index'))
    else:
    	return render(request, 'models/signup.html', {'error_message':"Пользователь уже существует"})