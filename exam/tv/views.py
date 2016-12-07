from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone

from .forms import ProgramForm
from .models import Program


def index(request):
    list = Program.objects.all()
    context = {
        "list": list
    }
    return render(request, 'tv/index.html', context)


def edit(request, id):
    obj = get_object_or_404(Program, pk=id)
    return render(request, 'tv/edit.html', {'obj': obj})


def save(request, id):
    obj = get_object_or_404(Program, pk=id)
    try:
        obj.name = request.POST['name']
        obj.description = request.POST['description']
        obj.timeLen = request.POST['timeLen']
        obj.ad = request.POST['ad']
        obj.dateTime = request.POST['dateTime']
        obj.save()
    except KeyError:
        return render(request, 'tv/edit.html', {'obj': obj})
    else:
        return HttpResponseRedirect(reverse('tv:index'))


def add(request):
    if request.method == "POST":
        form = ProgramForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.published_date = timezone.now()
            product.save()
            return redirect('../', pk=product.pk)
    else:
        form = ProgramForm()
    return render(request, 'tv/add.html', {'form': form})


def delete(request, id):
    obj = get_object_or_404(Program, pk=id)
    obj.delete()
    return HttpResponseRedirect(reverse('tv:index'))
