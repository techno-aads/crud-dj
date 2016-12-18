from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError

from goods.models import Good


def index(request):
    goods = Good.objects.order_by('delivered', '-delivery_date')
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
    return render(request, 'goods/create.html')


def signup(request):
    context = {}
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            user_form = auth.authenticate(username=user_form.cleaned_data['username'],
                                          password=user_form.cleaned_data['password2'])
            auth.login(request, user_form)
            return HttpResponseRedirect(reverse('goods:index'))
        else:
            context['form'] = user_form
    else:
        context['form'] = UserCreationForm()

    return render(request, 'goods/signup.html', context)
