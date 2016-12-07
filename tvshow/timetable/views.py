from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Show


class IndexView(generic.ListView):
    template_name = 'timetable/index.html'
    context_object_name = 'show_list'

    def get_queryset(self):

        return Show.objects.order_by('show_date')


class DetailView(generic.DetailView):
    model = Show
    template_name = 'timetable/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Show.objects
