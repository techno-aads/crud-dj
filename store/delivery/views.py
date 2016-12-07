from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Item
from .forms import ItemForm

class IndexView(generic.ListView):
	template_name = 'delivery/index.html'
	context_object_name = 'items'

	def get_queryset(self):
		return Item.objects.all()

class ItemShowView(generic.DetailView):
	model = Item
	template_name = 'delivery/items/show.html'

class ItemNewView(generic.FormView):
	model = Item
	form_class = ItemForm
	template_name = 'delivery/items/new.html'

class ItemEditView(generic.FormView):
	model = Item
	form_class = ItemForm
	template_name = 'delivery/items/new.html'

def item_create(request):
	item = Item(name = request.POST['name'],
					 		amount = request.POST['amount'],
							address = request.POST['address'],
							delivery_time = request.POST['delivery_time'],
						 )
	item.save()
	return HttpResponseRedirect(reverse('item_show', args=(item.id,)))

def item_update(request, item_id):
	item = Item(name = request.POST['name'],
					 		amount = request.POST['amount'],
							address = request.POST['address'],
							delivery_time = request.POST['delivery_time'],
						 )
	item.save()
	return HttpResponseRedirect(reverse('item_show', args=(item.id,)))
