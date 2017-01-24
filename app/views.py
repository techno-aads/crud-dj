from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import EditForm
from .models import tv_program

def index(request):
    list = tv_program.objects.all()
    context = {
        "list": list
    }
    return render(request, 'tv/index.html', context)

@staff_member_required
def add_new(request):
    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
            elem = form.save(commit=False)
            #elem.author = request.user
            #elem.published_date = timezone.now()
            elem.save()
            return HttpResponseRedirect(reverse('tv:index'));
    else:
        form = EditForm()
    return render(request, 'tv/edit.html', {'form': form})

@staff_member_required
def edit(request, id):
    elem = get_object_or_404(tv_program, pk=id)
    if request.method == "POST":
        form = EditForm(request.POST, instance=elem)
        if form.is_valid():
            elem = form.save(commit=False)
            #elem.author = request.user
            #elem.published_date = timezone.now()
            elem.save()
            return HttpResponseRedirect(reverse('tv:index'));
    else:
        form = EditForm(instance=elem)
    return render(request, 'tv/edit.html', {'form': form})

@staff_member_required
def delete(request, id):
    elem = get_object_or_404(tv_program, pk=id)
    elem.delete()
    return HttpResponseRedirect(reverse('tv:index'));