from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Order

def index(request):
    latest_order_list = Order.objects.order_by('-date')[:5]
    context = {'latest_order_list': latest_order_list}
    return render(request, 'polls/index.html', context)

def detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'polls/detail.html', {'order': order})

def add(request):
    OrderNew = Order(product_name=request.POST['product_name'], quantity=request.POST['quantity'], address=request.POST['address'], date=request.POST['date'], status=request.POST['status'])
    OrderNew.save()
    return HttpResponseRedirect(reverse('polls:index'))

def delete(request):
    Order.objects.filter(id=request.POST["id"]).delete()
    return HttpResponseRedirect(reverse('polls:index'))

def editOrder(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'polls/editOrder.html', {'course': order})

def updateOrder(request, order_id):
    Order.objects.filter(id=order_id).update(name=request.POST['name'],
                                               description=request.POST['description'])
    return HttpResponseRedirect(reverse('polls:index'))