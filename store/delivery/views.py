from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Item
from .forms import ItemForm, UserLoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(generic.ListView):
	template_name = 'delivery/index.html'
	context_object_name = 'items'

	def get_queryset(self):
		return Item.objects.all()

class ItemShowView(generic.DetailView):
	model = Item
	template_name = 'delivery/items/show.html'

class ItemNewView(LoginRequiredMixin, generic.FormView):
	login_url = '/login/'
	model = Item
	form_class = ItemForm
	template_name = 'delivery/items/new.html'


	def post(self, request):
		item = Item(name = request.POST['name'],
					 		amount = request.POST['amount'],
							address = request.POST['address'],
						 )
		item.save()
		return HttpResponseRedirect(reverse('item_show', args=(item.id,)))

class ItemEditView(LoginRequiredMixin, generic.FormView):
	login_url = '/login/'
	model = Item
	form_class = ItemForm
	template_name = 'delivery/items/new.html'


	def post(self, request, *args, **kwargs):
		self.name = request.POST['name']
		self.amount = request.POST['amount']
		self.address = request.POST['address']
		self.save()
		return HttpResponseRedirect(reverse('item_show', args=(self.id,)))

@login_required
def item_create(request):
	item = Item(name = request.POST['name'],
			 		amount = request.POST['amount'],
					address = request.POST['address'],
					delivery_time = request.POST['delivery_time'],
				 )
	item.save()
	return HttpResponseRedirect(reverse('item_show', args=(item.id,)))

@login_required
def item_update(request, item_id):
	item = Item(name = request.POST['name'],
					 		amount = request.POST['amount'],
							address = request.POST['address'],
							delivery_time = request.POST['delivery_time'],
						 )
	item.save()
	return HttpResponseRedirect(reverse('item_show', args=(item.id,)))


class UserLogin(generic.FormView):
	form_class = UserLoginForm
	template_name = 'delivery/users/session/new.html'

	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				render(request, self.template_name, {'form': self.form_class})
		else:
			render(request, self.template_name, {'form': self.form_class})
		

def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

class UserNew(generic.FormView):
	form_class = UserCreationForm
	template_name = 'delivery/users/new.html'

	# def post(self, request):
	# 	if form.is_valid():
	# 		form.save()
	# 		return HttpResponseRedirect(reverse('index'))


# def user_new(request):
# 	if request.method == "POST":
# 		form = UserCreationForm(request.POST) # filled form/i'm skipping validation for this example
# 		form.save
# 		return HttpResponseRedirect(reverse('index')) # go to some other page if successfully saved
# 	else:
# 		form = UserCreationForm # if the user accessed the register url directly, just display the empty form
# 		return render(request, 'delivery/users/new.html',  {'form': form})