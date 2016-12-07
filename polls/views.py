from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Goods


# Create your views here.


def index(request):
    listOfGoods = Goods.objects.order_by('name')
    template = loader.get_template('polls/index.html')
    context = {
        'listOfGoods': listOfGoods
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
    return render(request, 'polls/edit.html', {'goods': goods})


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
