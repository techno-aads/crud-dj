from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from django.urls import reverse
from django.http import Http404
from django.views import generic

from .models import TVShow


def index(request):
    template = loader.get_template('app/index.html')
    tv_show_list = TVShow.objects.all()
    context = {'tv_show_list': tv_show_list}
    return HttpResponse(template.render(context, request))


def detail(request, tv_show_id):
    tv_show = get_object_or_404(TVShow, pk=tv_show_id)
    return render(request, 'app/detail.html', {'tv_show': tv_show})


def add(request):
    if ('name' in request.POST) and ('dur' in request.POST) and ('descr' in request.POST) and ('date' in request.POST): #default values?!
        #Insert data in DB
        n  = request.POST['name']
        dur   = request.POST['dur']
        descr = request.POST['descr']
        date  = request.POST['date']

        show = TVShow(name = n, description = descr, broadcast_date = date)
        #show = TVShow(name = n, duration = dur, description = descr, broadcast_date = date)
        show.save()

        msg = "Succes"
    else:
        msg = "you submitted an empty or part-empty form"
    return render(request, 'app/add_success.html', {})

    
