from django.shortcuts import render, redirect, get_object_or_404

from laba.forms import ProgrammeForm
from laba.models import Programme


def programme_list(request):
    programmes = Programme.objects.all().order_by('date')
    return render(request, 'laba/programme_list.html', {'programmes': programmes})


def programme_new(request):
    if request.method == "POST":
        form = ProgrammeForm(request.POST)
        if form.is_valid():
            programme = form.save()
            programme.save()
            return redirect('laba.views.programme_list')
    else:
        form = ProgrammeForm()
    return render(request, 'laba/programme_edit.html', {'form': form, 'isNew': True})


def programme_remove(request, pk):
    if request.method == "GET":
        programme = get_object_or_404(Programme, pk=pk)
        programme.delete()
    return redirect('laba.views.programme_list')


def programme_edit(request, pk):
    programme = get_object_or_404(Programme, pk=pk)
    if request.method == "POST":
        form = ProgrammeForm(request.POST, instance=programme)
        if form.is_valid():
            programme = form.save()
            programme.save()
            return redirect('laba.views.programme_list')
    else:
        form = ProgrammeForm(instance=programme)
    return render(request, 'laba/programme_edit.html', {'form': form, 'isNew': False})
