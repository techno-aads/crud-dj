from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.template.context_processors import csrf
from django.urls import reverse
from .models import Goods


# Create your views here.


def index(request):
    listOfGoods = Goods.objects.order_by('name')
    template = loader.get_template('polls/index.html')
    context = {
        'listOfGoods': listOfGoods,
        'username': auth.get_user(request).username
    }
    return HttpResponse(template.render(context, request))


def add(request):
    goods = Goods(name=request.POST['name'], count=request.POST['count'],
                  address=request.POST['address'],
                  date=request.POST['date'],
                  isArrive=request.POST['arrived'])
    goods.save()
    return HttpResponseRedirect(reverse('polls:index'))


def delete(request):
    Goods.objects.filter(id=request.POST["id"]).delete()
    return HttpResponseRedirect(reverse('polls:index'))


def editGoods(request, goods_id):
    goods = get_object_or_404(Goods, id=goods_id)
    return render(request, 'polls/edit.html', {'goods': goods, 'user': auth.get_user(request).username})


def updateGoods(request, goods_id):
    goods = get_object_or_404(Goods, id=goods_id)
    try:
        goods.name = request.POST['name']
        goods.count = request.POST['count']
        goods.address = request.POST['address']
        goods.date = request.POST['date']
        goods.isArrive = request.POST['arrived']
        goods.save()
    except KeyError:
        return render(request, 'polls/edit.html', {'goods': goods})
    else:
        return HttpResponseRedirect(reverse('polls:index'))


def login(request):
    template = loader.get_template('polls/login.html')
    return HttpResponse(template.render({}, request))


def userlogin(request):
    login = request.POST['login']
    password = request.POST['pass']
    user = auth.authenticate(username=login, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('polls:index'))
    else:
        template = loader.get_template('polls/login.html')
        return HttpResponse(template.render({'error': 'wrong login or password'}, request))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('polls:index'))


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return HttpResponseRedirect(reverse('polls:index'))
        else:
            args['form'] = newuser_form
    template = loader.get_template('polls/register.html')
    return HttpResponse(template.render(args, request))