from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from django.urls import reverse
from django.http import Http404
from django.views import generic

from .models import TVShow


def index(request):
    template = loader.get_template('app/index.html')
    tv_show_list = TVShow.objects.order_by('broadcast_date')
    context = {
        'tv_show_list': tv_show_list,
        'username': auth.get_user(request).username
    }
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


def login(request):
    template = loader.get_template('app/login.html')
    return HttpResponse(template.render({}, request))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('app:index'))


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
            return HttpResponseRedirect(reverse('tvshows:index'))
        else:
            args['form'] = newuser_form
    template = loader.get_template('tvshows/register.html')
    return HttpResponse(template.render(args, request))


def userLogin(request):
    login = request.POST['login']
    password = request.POST['pass']
    user = auth.authenticate(username=login, password=password)
    if user is not None:
        auth.login(request, user)

        return HttpResponseRedirect(reverse('app:index'))
    else:
        template = loader.get_template('app/login.html')
        return HttpResponse(template.render({'error': 'Wrong login or password'}, request))


@login_required(login_url='app:login.html')
def edit(request):
    list_shows = TVShow.objects.order_by('broadcast_date')
    template = loader.get_template('app/edit.html')
    context = {
        'list_shows': list_shows,
        'username': auth.get_user(request).username,
        'form': ShowForm,
    }
    return HttpResponse(template.render(context, request))


    
