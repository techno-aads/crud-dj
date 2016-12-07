from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import TV
from django.urls import reverse


# Create your views here.

def index(request):
    tv_list = TV.objects.all()
    context = {'tv_list': tv_list}
    return render(request, 'TV/index.html', context)


def edit(request, id):
    obj = get_object_or_404(TV, id=id)
    return render(request, 'TV/edit.html', {'obj': obj})


def save(request, id):
    obj = get_object_or_404(TV, id=id)
    try:
        obj.description = request.POST['description']
    except KeyError:
        return render(request, 'TV/edit.html', {'obj': obj})
    else:
        return HttpResponseRedirect(reverse('index.html'))


def add(request):
    tv = TV(name=request.POST['name'], description=request.POST['description'],
            duration=request.POST['duration'],
            date=request.POST['date'],
            advert=request.POST['advert'])
    tv.save()
    return HttpResponseRedirect(reverse('TV:index'))
