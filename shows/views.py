from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Show

class ShowList(ListView):
    model = Show

class ShowCreate(CreateView):
    model = Show
    success_url = reverse_lazy('shows:show_list')
    fields = ['name', 'description', 'running_time', 'run_date', 'has_ads']

class ShowUpdate(UpdateView):
    model = Show
    success_url = reverse_lazy('shows:show_list')
    fields = ['name', 'description', 'running_time', 'run_date', 'has_ads']

class ShowDelete(DeleteView):
    model = Show
    success_url = reverse_lazy('shows:show_list')