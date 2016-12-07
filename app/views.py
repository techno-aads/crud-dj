from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import EditForm
from .models import tv_program

# Create your views here.

def index(request):
    list = tv_program.objects.all()
    context = {
        "list": list
    }
    return render(request, 'index.html', context)

def add_new(request):
    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
            elem = form.save(commit=False)
            #elem.author = request.user
            #elem.published_date = timezone.now()
            elem.save()
            return HttpResponseRedirect(reverse('index'));
    else:
        form = EditForm()
    return render(request, 'edit.html', {'form': form})

def edit(request, id):
    elem = get_object_or_404(tv_program, pk=id)
    if request.method == "POST":
        form = EditForm(request.POST, instance=elem)
        if form.is_valid():
            elem = form.save(commit=False)
            #elem.author = request.user
            #elem.published_date = timezone.now()
            elem.save()
            return HttpResponseRedirect(reverse('index'));
    else:
        form = EditForm(instance=elem)
    return render(request, 'edit.html', {'form': form})

def delete(request, id):
    elem = get_object_or_404(tv_program, pk=id)
    elem.delete()
    return HttpResponseRedirect(reverse('index'));