from django.shortcuts import render
from .models import Show

# Create your views here.

def index(request):
    return render(request, 'tvshows/index.html', {})

def input(request):
    return render(request, 'tvshows/input.html', {})

def shows(request):
    shows = Show.objects.order_by('date')
    return render(request, 'tvshows/shows.html', {'shows': shows})