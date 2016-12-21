
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse
from tele.forms import TelevisionForm
from tele.models import Television

def tele_list(request):
    teles = Television.objects.all().order_by('time')
    return render(request, 'tele/tele_list.html', {'teles': teles})


def tele_new(request):
    if request.method == "POST":
        form = TelevisionForm(request.POST)
        if form.is_valid():
            tele = form.save()
            tele.save()
            return redirect('tele:tele_list')
    else:
        form = TelevisionForm()
    return render(request, 'tele/tele_edit.html', {'form': form, 'isNew': True})


def tele_remove(request, pk):
    if request.method == "GET":
        tele = get_object_or_404(Television, pk=pk)
        tele.delete()
    return redirect('tele:tele_list')


def tele_edit(request, pk=1):
    tele = get_object_or_404(Television, pk=pk)
    if request.method == "POST":
        form = TelevisionForm(request.POST, instance=tele)
        if form.is_valid():
            tele = form.save(commit=False)
            tele.publish()
            tele.save()
            return redirect('tele:tele_list')
    else:
        form = TelevisionForm(instance=tele)
    return render(request, 'tele/tele_edit.html', {'form': form, 'isNew': False})