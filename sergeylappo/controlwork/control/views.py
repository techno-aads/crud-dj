from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import logging
from django.contrib.auth.decorators import login_required

from .models import Product


# Create your views here.


def product(request):
    if request.method == 'POST' and 'name' in request.POST:

        product = Product(name=(request.POST['name']), count=(request.POST['count']), address=(request.POST['address']),
                          date=(request.POST['date']), deliveryStatus=("CR"))
        if (product.name != "" and product.count != "" and product.address != "" and product.date != ""):
            product.save()
        return HttpResponseRedirect(reverse('product'))
    product_list = Product.objects.order_by('name')
    context = {
        'product_list': product_list,
    }
    return render(request, 'control/index.html', context)

@login_required(login_url='/login/')
def details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'control/details.html', {'product': product})


def edit(request, product_id):
    if request.method == 'POST' and 'name' in request.POST:
        product = get_object_or_404(Product, pk=product_id)
        try:

            product.name = (request.POST['name'])
            product.count = (request.POST['count'])
            product.address = (request.POST['address'])
            product.date = (request.POST['date'])
            product.deliveryStatus = (request.POST['status'][2] + request.POST['status'][3])
        except (KeyError, product.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, 'practise/edit.html', {
                'Product': Product,
                'error_message': "Wrong data received.",
            })
        else:
            if (product.name != "" and product.count != "" and product.address != "" and product.date != ""):
                product.save();
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('product'))
    elif request.method == 'POST' and 'delete' in request.POST:
        logger = logging.getLogger(__name__)
        logger.error("something bad")
        product = get_object_or_404(Product, pk=product_id)
        product.delete()

        return HttpResponseRedirect(reverse('product'))
