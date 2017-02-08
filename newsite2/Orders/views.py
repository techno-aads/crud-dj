from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ValidationError
from django.http import Http404
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.conf import settings

import datetime
import re

from .models import Status, Order

# Create your views here.

def index (request):
	order_list = Order.objects.order_by('-date')
	context = { 'order_list': order_list}
	return render(request, 'Orders/index.html',context)
	
def detail(request, order_id):
	order = get_object_or_404(Order, pk=order_id)
	return render(request, 'Orders/detail.html',{'order': order})
	

def edit(request, order_id):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('Orders:login'))
	else:
		order = get_object_or_404(Order, pk=order_id)
		status_list = Status.objects.order_by('-name')
		dt=order.date.strftime('%Y-%m-%d %H:%M')
		return render(request, 'Orders/edit.html',{'order': order, 'status_list': status_list, 'dt': dt,})


def save(request, order_id):
		order = get_object_or_404(Order, pk=order_id)
		status_list = Status.objects.order_by('-name')
		dt=order.date.strftime('%Y-%m-%d %H:%M')
		tpl='\d\d\d\d-\d\d-\d\d \d\d:\d\d'
		strd=str(request.POST['date'])
		if re.fullmatch(tpl,strd) is not None:
			try:
				order.count=int(request.POST['count'])
				order.address=request.POST['address']
				order.date=request.POST['date']
				if str(request.POST['status'])==str(status_list[1]):
					stat=status_list[1]
				if str(request.POST['status'])==str(status_list[0]):
					stat=status_list[0]
				order.status=stat
			except (KeyError,ValueError):
				return render(request, 'Orders/edit.html', {
					'order': order,
					'status_list': status_list,
					'dt': dt,
					'error_message': "Uncorrect data input!",})
			else:
				order.save()
				return HttpResponseRedirect(reverse('Orders:detail', args=(order.id,)))
		else:
			return render(request, 'Orders/edit.html', {
				'order': order,
				'status_list': status_list,
				'dt': dt,
				'error_message': "Uncorrect data input!",})
				

def new(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('Orders:login'))
	else:
		status_list = Status.objects.order_by('-name')
		if request.method == 'POST':
			tpl='\d\d\d\d-\d\d-\d\d \d\d:\d\d'
			strd=str(request.POST['date'])
			if re.fullmatch(tpl,strd) is not None:
				try:
					if str(request.POST['status'])==str(status_list[1]):
						stat=status_list[1]
					if str(request.POST['status'])==str(status_list[0]):
						stat=status_list[0]
					new_order=Order(title=request.POST['title'],count=int(request.POST['count']),address=request.POST['address'],date=request.POST['date'], status=stat)
				except (KeyError,ValueError):
					return render(request, 'Orders/new.html', {
						'status_list': status_list,
						'error_message': "Uncorrect data input!",})
				else:
					new_order.save()
					return HttpResponseRedirect(reverse('Orders:index'))
			else:
				return render(request, 'Orders/new.html', {
						'status_list': status_list,
						'error_message': "Uncorrect data input!",})
		else:
			return render(request, 'Orders/new.html', {
					'status_list': status_list,
					})
			
			
			
def remove(request, order_id):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('Orders:login'))
	else:
		order = get_object_or_404(Order, pk=order_id)
		order.delete()
		return HttpResponseRedirect(reverse('Orders:index'))
			
			
class RegisterFormView(FormView):
	form_class = UserCreationForm

	success_url = "/Orders/login/"

	template_name = "Orders/register.html"

	def form_valid(self, form):
		form.save()

		return super(RegisterFormView, self).form_valid(form)
		
		
class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "Orders/login.html"
    success_url = "/Orders/"

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('Orders:index'))
