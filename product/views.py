from django.shortcuts import render
from .models import Product
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.utils import timezone
from .forms import ProductForm
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
def product_list(request):
    products = Product.objects.order_by('date')
    return render(request, 'product/product_list.html', {'products': products})


def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.published_date = timezone.now()
            product.save()
            return redirect('../', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'product/product_edit.html', {'form' : form})

def delete(request, id):
   prod = get_object_or_404(Product, pk=id)
   prod.delete()
   return HttpResponseRedirect(reverse('product:product_list'))

def edit(request, id):
    article = get_object_or_404(Product, pk=id)

    form = ProductForm(request.POST or None, instance=article)
    if request.POST and form.is_valid():
        form.save()

        return HttpResponseRedirect(reverse('product:product_list'))

    return render(request, 'product/product_edit.html', {
        'form': form
    })
