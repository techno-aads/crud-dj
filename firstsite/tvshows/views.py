from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.template.context_processors import csrf
from django.urls import reverse

from .forms import ShowForm
from .models import Show


def index(request):
    list_shows = Show.objects.order_by('broadcast_date', 'time')
    template = loader.get_template('tvshows/index.html')
    context = {
        'list_shows': list_shows,
        'username': auth.get_user(request).username
    }
    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template('tvshows/login.html')
    return HttpResponse(template.render({}, request))


def userlogin(request):
    login = request.POST['login']
    password = request.POST['pass']
    user = auth.authenticate(username=login, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('tvshows:index'))
    else:
        template = loader.get_template('tvshows/login.html')
        return HttpResponse(template.render({'error': 'Логин или пароль введены неверно'}, request))


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

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('tvshows:index'))


@login_required(login_url='tvshows:login.html')
def edit(request):
    list_shows = Show.objects.order_by('broadcast_date', 'time')
    template = loader.get_template('tvshows/edit.html')
    context = {
        'list_shows': list_shows,
        'username': auth.get_user(request).username,
        'form': ShowForm,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='tvshows:login')
def delete(request):
    user=auth.get_user(request).username
    if user is not None:
        Show.objects.filter(id=request.POST["id"]).delete()
        return HttpResponseRedirect(reverse('tvshows:edit'))
    else:
        return HttpResponseRedirect(reverse('tvshows:editshow'))


@login_required(login_url='tvshows:login')
def editShow(request, show_id):
    show = get_object_or_404(Show, id=show_id)
    return render(request, 'tvshows/editshow.html', {'show': show, 'user': auth.get_user(request).username})


@login_required(login_url='tvshows:login')
def updateShow(request, show_id):
    show = get_object_or_404(Show, id=show_id)
    try:
        show.name=request.POST['name']
        show.time=request.POST['time']
        show.description=request.POST['descrip']
        show.broadcast_date=request.POST['date']
        show.advert=request.POST['advert']
        show.save()
    except KeyError:
        return render(request, 'tvshow/edit.html', {'show': show})
    else:
        return HttpResponseRedirect(reverse('tvshows:edit'))

@login_required(login_url='tvshows:login')
def add(request):
    show = Show(name=request.POST['name'], broadcast_date=request.POST['date'],
                  time=request.POST['time'],
                  description=request.POST['descrip'],
                  advert=request.POST['advert'])
    show.save()
    return HttpResponseRedirect(reverse('tvshows:edit'))