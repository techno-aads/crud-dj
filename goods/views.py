from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError

from goods.models import Good


def index(request):
    goods = Good.objects.order_by('-delivery_date')[:10]
    context = {
        'goods': goods,
    }
    return render(request, 'goods/index.html', context)


def detail(request, good_id):
    good = get_object_or_404(Good, pk=good_id)
    context = {
        'good': good,
    }
    return render(request, 'goods/detail.html', context)


# def create(request, name, count, delivery_address, delivery_date, delivered):
def add(request):
    name = request.POST['name']
    count = request.POST['count']
    delivery_address = request.POST['address']
    delivery_date = request.POST['date']
    try:
        delivered = request.POST['delivered'] == 'on'
    except MultiValueDictKeyError:
        delivered = False
    Good.objects.create(
        name=name, count=count, delivery_address=delivery_address, delivery_date=delivery_date, delivered=delivered
    )
    good_id = Good.objects.latest('id').id
    return HttpResponseRedirect(reverse('goods:index'))


def save(request, good_id):
    good = get_object_or_404(Good, pk=good_id)
    good.name = request.POST['name']
    good.count = request.POST['count']
    good.delivery_address = request.POST['address']
    good.delivery_date = request.POST['date']
    try:
        good.delivered = request.POST['delivered'] == 'on'
    except MultiValueDictKeyError:
        good.delivered = False
    good.save()
    return HttpResponseRedirect(reverse('goods:index'))


def remove(request, good_id):
    get_object_or_404(Good, pk=good_id).delete()
    return HttpResponseRedirect(reverse('goods:index'))


def create(request):
    context = {
        'value': 'value'
    }
    return render(request, 'goods/create.html', context)
