from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader
from django.http import Http404

from .models import Order

def index(request):
	list = Order.objects.all()
	template = loader.get_template("index.html")
	context = {"list": list}
	return HttpResponse(template.render(context,request))

def edit(request, id):
	obj = get_object_or_404(Order, pk=id)
	return render(request, 'edit.html', {'obj': obj})

def save(request, id):
	obj = get_object_or_404(Order, pk=id)
	try:
		obj.description = request.POST['description']
	except KeyError:
		return render(request, 'edit.html', {'obj': obj})
	else:
		return HttpResponseRedirect(reverse('index.html'));

def add(request):
	obj = get_object_or_404(Order, pk=id)
	name = request.POST['name']
	amount = request.POST['amount']
	addres = request.POST['addres']
	date = request.POST['date']
	status = request.POST['status']
	return render(request, 'detail.html', {'obj': obj})

def detail(request, id):
    obj = get_object_or_404(Order, pk=id)
    return render(request, 'detail.html', {'obj': obj})