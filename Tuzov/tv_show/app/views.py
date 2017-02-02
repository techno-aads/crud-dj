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

from .forms import ShowForm
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


@login_required(login_url='app:login')
def add(request):
    #TODO:add validation on the server side
    show = TVShow(name=request.POST['name'],
                  broadcast_date=request.POST['date'],
                  duration=request.POST['time'],
                  description=request.POST['descrip'],
                  advertisement=(request.POST['advert']) == 'Yes')
    show.save()
    return HttpResponseRedirect(reverse('app:index'))


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
            return HttpResponseRedirect(reverse('app:index'))
        else:
            args['form'] = newuser_form
    template = loader.get_template('app/register.html')
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
        'form': ShowForm
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='app:login')
def editShow(request, show_id):
    show = get_object_or_404(TVShow, id=show_id)
    return render(request, 'app/edit_show.html', {'show': show, 'user': auth.get_user(request).username})


@login_required(login_url='app:login')
def delete(request):
    user=auth.get_user(request).username
    if user is not None:
        TVShow.objects.filter(id=request.POST["id"]).delete()
        return HttpResponseRedirect(reverse('app:index'))
    else:
        return HttpResponseRedirect(reverse('app:index'))


@login_required(login_url='app:login')
def updateShow(request, show_id):
    show = get_object_or_404(TVShow, id=show_id)
    try:
        show.name=request.POST['name']
        show.duration=request.POST['time']
        show.description=request.POST['descrip']
        show.broadcast_date=request.POST['date']
        show.advert=request.POST['advert']
        show.save()
    except KeyError:
        return render(request, 'app/index.html', {'show': show})
    else:
        return HttpResponseRedirect(reverse('app:index'))




    
