from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.urls import reverse

from .models import Status, Order

# Create your views here.

def index (request):
	order_list = Order.objects.order_by('-date')
	context = { 'order_list': order_list}
	return render(request, 'Orders/index.html',context)
	
def detail(request, order_id):
	order = get_object_or_404(Order, pk=order_id)
	return render(request, 'Orders/detail.html',{'order': order})
	

def edit(request, id):
  order = get_object_or_404(Order, pk=id)
  return render(request, 'edit.html', {'order': order})
   

def save(request, id):
    order = get_object_or_404(Order, pk=id)
    try:
        order.count=request.POST['count']
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {'order': order})
    else:
        order.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('detail.html'))   
   
   

   
