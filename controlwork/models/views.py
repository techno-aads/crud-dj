from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Order

def index(request):
    order_list = Order.objects.all()
    template = loader.get_template('models/index.html')
    context = {
        'order_list': order_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, order_id):
	obj = get_object_or_404(Order, pk=order_id)
	return render(request, 'models/detail.html', {'order': obj})

def add(request):
	return render(request, 'models/add.html')

def added(request):
	obj = Order()
	obj.name = request.POST['name']
	obj.count = request.POST['count']
	obj.address = request.POST['address']
	obj.order_date = request.POST['order_date']
	obj.state = request.POST['state'] == "Yes"
	obj.save()
	return HttpResponseRedirect(reverse('models:index'))

def delete(request, order_id):
    obj = get_object_or_404(Order, pk=order_id)
    try:
        obj.delete()
    except (KeyError, Order.DoesNotExist):
    	# Redisplay the question voting form.
    	return render(request, 'models:detail', {
            'order': obj,
            'error_message': "Order not found.",
        })
    else:
        return HttpResponseRedirect(reverse('models:index'))

def edit(request, order_id):
	obj = get_object_or_404(Order, pk=order_id)
	obj.name = request.POST['name']
	obj.count = request.POST['count']
	obj.address = request.POST['address']
	obj.order_date = request.POST['order_date']
	obj.state = request.POST['state'] == "Yes"
	obj.save()
	return HttpResponseRedirect(reverse('models:index'))