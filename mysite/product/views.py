from django.shortcuts import render, get_object_or_404, redirect
from  .models import InfoProd
from  .forms import ProdForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse



def prod_list(request):
    prods = InfoProd.objects.all().order_by('prod_date')
    return render(request, 'product/prod_list.html', {'prods': prods})

def prod_detail(request, pk):
    prod = get_object_or_404(InfoProd, pk=pk)
    return render(request, 'product/prod_detail.html', {'prod': prod})


def prod_new(request):
    if request.method == "POST":
        form = ProdForm(request.POST)
        if form.is_valid():
            prod = form.save()
            prod.save()
            #return HttpResponseRedirect(reverse('product.views.prod_list'))
            return redirect('prod_list')
    else:
        form = ProdForm()
    return render(request, 'product/prod_edit.html', {'form': form, 'isNew': True})

def prod_edit(request, pk):
    prod = get_object_or_404(InfoProd, pk=pk)
    if request.method == "POST":
        form = ProdForm(request.POST, instance=prod)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.save()
            return redirect('prod_detail', pk=prod.pk)
    else:
        form = ProdForm(instance=prod)
    return render(request, 'product/prod_edit.html', {'form': form, 'isNew': False})

def prod_remove(request, pk):
    if request.method == "GET":
        prod = get_object_or_404(InfoProd, pk=pk)
        prod.delete()
    return redirect('prod_list')
# Create your views here.
