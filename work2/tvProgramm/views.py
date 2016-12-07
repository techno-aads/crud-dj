from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Programm
from .forms import AddProgrammForm

def index(request):
    template = loader.get_template('index.html')
    listPrograms = Programm.objects.all()
    context = {
        "programms": listPrograms,
    }
    return render(request, 'index.html', context)

def saveProgramm(request, id):
    form = AddProgrammForm(request.POST or None)
    obj = get_object_or_404(Programm, pk=id)
    try:
        obj.name = request.POST['name']
        obj.length = request.POST['length']
        obj.description = request.POST['description']
        obj.date = request.POST['date']
        obj.ad = False
        if obj.ad == 'on':
            obj.ad = True
        else:
            obj.ad = False

    except KeyError:
        return render(request, 'edit.html', {'form': form})
    else:
        obj.save()
        return HttpResponseRedirect(reverse('index'))

def addProgramm(request):
    form = AddProgrammForm(request.POST or None)
    obj = form
    try:
        obj.name = request.POST['name']
        obj.length = request.POST['length']
        obj.description = request.POST['description']
        obj.date = request.POST['date']
        obj.ad = request.POST['ad']
        if obj.ad == 'on':
            obj.ad = True
        else:
            obj.ad = False

    except KeyError:
        return render(request, 'edit.html', {'form': form})
    else:
        obj.save()
        return HttpResponseRedirect(reverse('index'))

def deleteProgramm(request, id):
    toDelete = get_object_or_404(Programm, pk=id)
    toDelete.delete()
    return HttpResponseRedirect(reverse('index'))