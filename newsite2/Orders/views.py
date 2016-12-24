from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib.auth import logout
from django.conf import settings

import datetime

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
		return render(request, 'Orders/edit.html',{'order': order, 'status_list': status_list,})


def save(request, order_id):
	order = get_object_or_404(Order, pk=order_id)
	status_list = Status.objects.order_by('-name')
	try:
		order.count=int(request.POST['count'])
		order.address=request.POST['address']
		#order.date=datetime.datetime.now()
		#order.status=request.POST['status']
	except (KeyError,ValueError):
		# Redisplay the question voting form.
		return render(request, 'Orders/edit.html', {
			'order': order,
			'status_list': status_list,
			'error_message': "Uncorrect data input!",})
	else:
		#order.count = request.POST
		order.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
		return HttpResponseRedirect(reverse('Orders:detail', args=(order.id,)))

def new(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('Orders:login'))
	else:
		status_list = Status.objects.order_by('-name')
		try:
			new_order=Order(title=request.POST['title'],count=int(request.POST['count']),address=request.POST['address'],date=request.POST['date'],status=request.POST['status'])
		except (KeyError,ValueError):
		# Redisplay the question voting form.
			return render(request, 'Orders/new.html', {
				'status_list': status_list,
				'error_message': "Uncorrect data input!",})
		else:
		#order.count = request.POST
			new_order.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
			return HttpResponseRedirect(reverse('Orders:index'))
		
		
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
