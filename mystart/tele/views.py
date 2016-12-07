import tele
from django.shortcuts import render
from .models import Television
from django.shortcuts import render, get_object_or_404
from .forms import TelevisionForm
from django.shortcuts import redirect

# Create your views here.
def tele_list(request):
    teles = Television.objects.order_by('time')
    return render(request, 'tele/tele_list.html', {'teles': teles})


def tele_detail(request, pk):
    post = get_object_or_404(Television, pk=pk)
    return render(request, 'tele/tele_detail.html', {'tele': tele})


def tele_new(request):
    if request.method == "POST":
        form = TelevisionForm(request.POST)
        if form.is_valid():
            tele = form.save(commit=False)
            tele.save()
            return redirect('tele.views.tele_detail', pk=tele.pk)
    else:
        form = TelevisionForm()
    return render(request, 'tele/tele_edit.html', {'form': form})


def tele_edit(request, pk):
    tele = get_object_or_404(Television, pk=pk)
    if request.method == "POST":
        form = TelevisionForm(request.POST, instance=tele)
        if form.is_valid():
            tele = form.save(commit=False)
            tele.save()
            return redirect('tele.views.tele_detail', pk=tele.pk)
    else:
        form = TelevisionForm(instance=tele)
    return render(request, 'tele/tele_edit.html', {'form': form})
