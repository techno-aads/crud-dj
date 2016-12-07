from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Tvprogram


def index(request):
    tvprograms_list = Tvprogram.objects.order_by('-date')
    template = loader.get_template('tvprogram/index.html')
    context = {
		'tvprograms_list' : tvprograms_list,
	}
    return HttpResponse(template.render(context, request))

def detail(request, tvprogram_id):
    template = loader.get_template('tvprogram/detail.html')
    tvprogram = Tvprogram.objects.get(pk = tvprogram_id)
    context = {
        'tvprogram' : tvprogram,
    }
    return HttpResponse(template.render(context, request))

def edit(request, tvprogram_id):
    tvprogram = Tvprogram.objects.get(pk = tvprogram_id)
    if request.POST:
         tvprogram.title = request.POST['title']
         tvprogram.description = request.POST['description']
         tvprogram.duration = request.POST['duration']
         tvprogram.date = request.POST['date']
         tvprogram.adv_option = request.POST['adv_option']
    return render(request,'tvprogram/edit.html', {'tvprogram' : tvprogram})

def save(request, tvprogram_id):
    tvprogram = Tvprogram.objects.get(pk = tvprogram_id)
    try:
        tvprogram.title = request.POST['title']
        tvprogram.description = request.POST['description']
        tvprogram.duration = request.POST['duration']
        tvprogram.date = request.POST['date']
        tvprogram.adv_option = request.POST['adv_option']
    except KeyError:
        return render(request, '/tvprogram/edit.html',  {'tvprogram' : tvprogram})
    else:
        return HttpResponseRedirect(reverse('/tvprogram/index.html'))
