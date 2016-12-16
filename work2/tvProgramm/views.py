from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Programm
from .forms import AddProgrammForm
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'programms'

    def get_queryset(self):
        return Programm.objects.all()

def saveProgramm(request, id):
    form = AddProgrammForm(request.POST or None)
    if form.is_valid():
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
    return render(request, 'edit.html', {'form': form})

def addProgramm(request):
    form = AddProgrammForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'edit.html', {'form': form})

def deleteProgramm(request, id):
    toDelete = get_object_or_404(Programm, pk=id)
    toDelete.delete()
    return HttpResponseRedirect(reverse('index'))