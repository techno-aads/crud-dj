
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

from tv.models import Program


class IndexView(generic.ListView):
    template_name = 'tv/index.html'
    context_object_name = 'program_list'

    def get_queryset(self):
        return Program.objects.order_by('date')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class DetailView(generic.DetailView):
    model = Program
    template_name = 'tv/detail.html'


class ProgramCreate(generic.CreateView):
    template_name_suffix = '_create'
    model = Program
    fields = ['name', 'description', 'length', 'date', 'add_advert']
    success_url = reverse_lazy('tv:index')

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('tv:login'))
        else:
            return super(ProgramCreate, self).get(request, args, kwargs)


class ProgramUpdate(generic.UpdateView):
    template_name_suffix = '_update'
    model = Program
    fields = ['name', 'description', 'length', 'date', 'add_advert']
    success_url = reverse_lazy('tv:index')

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('tv:login'))
        else:
            return super(ProgramUpdate, self).get(request, args, kwargs)


class ProgramDelete(generic.DeleteView):
    template_name_suffix = '_delete'
    model = Program
    success_url = reverse_lazy('tv:index')

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('tv:login'))
        else:
            return super(ProgramDelete, self).get(request, args, kwargs)


class RegisterFormView(generic.FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('tv:login')
    template_name = 'tv/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(generic.FormView):
    form_class = AuthenticationForm
    template_name = 'tv/login.html'
    success_url = reverse_lazy('tv:index')

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(generic.View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('tv:index'))
