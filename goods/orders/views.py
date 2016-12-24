from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import Http404
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'orders/index.html'
    context_object_name = 'last_products'

    def get_queryset(self):
        """Return the last ten products."""
        return Product.objects.order_by('-name')[:10]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class DetailView(generic.DetailView):
    model = Product
    template_name = 'orders/detail.html'


class ProductCreate(generic.CreateView):
    template_name_suffix = '_create'
    model = Product
    fields = ['name', 'quantity', 'address', 'delivery_date', 'status']
    success_url = reverse_lazy('orders:index')

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('orders:login'))
        else:
            return super(ProductCreate, self).get(request, args, kwargs)


class ProductDelete(generic.DeleteView):
    template_name_suffix = '_delete'
    model = Product
    success_url = reverse_lazy('orders:index')

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('orders:login'))
        else:
            return super(ProductDelete, self).get(request, args, kwargs)


class ProductUpdate(generic.UpdateView):
    template_name_suffix = '_update'
    model = Product
    fields = ['name', 'quantity', 'address', 'delivery_date', 'status']
    success_url = reverse_lazy('orders:index')

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('orders:login'))
        else:
            return super(ProductUpdate, self).get(request, args, kwargs)

class RegisterFormView(generic.FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('orders:login')
    template_name = 'orders/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(generic.FormView):
    form_class = AuthenticationForm
    template_name = 'orders/login.html'
    success_url = reverse_lazy('orders:index')

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(generic.View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('orders:index'))
