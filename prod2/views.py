from django.shortcuts import render, redirect, get_object_or_404

from prod2.forms import ProdForm
from prod2.models import Prod


def prod_list(request):
    prods = Prod.objects.all().order_by('date')
    return render(request, 'prod/prod_list.html', {'prods': prods})


def prod_new(request):
    if request.method == "POST":
        form = ProdForm(request.POST)
        if form.is_valid():
            prod = form.save()
            prod.save()
            return redirect('prod2.views.prod_list')
    else:
        form = ProdForm()
    return render(request, 'prod2/programme_edit.html', {'form': form, 'isNew': True})


def prod_remove(request, pk):
    if request.method == "GET":
        prod = get_object_or_404(Prod, pk=pk)
        prod.delete()
    return redirect('prod2.views.programme_list')


def prod_edit(request, pk):
    prod = get_object_or_404(Prod, pk=pk)
    if request.method == "POST":
        form = ProdForm(request.POST, instance=prod)
        if form.is_valid():
            prod = form.save()
            prod.save()
            return redirect('prod2.views.prod_list')
    else:
        form = ProgrammeForm(instance=programme)
    return render(request, 'prod2/prod_edit.html', {'form': form, 'isNew': False})
