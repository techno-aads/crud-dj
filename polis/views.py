from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.template.context_processors import csrf
from django.urls import reverse
from .models import Shows
# Create your views here.

def index(request):
    listOfShows = Shows.objects.order_by('name')
    template = loader.get_template('polis/index.html')
    context = {
        'listOfShows': listOfShows,
        'username': auth.get_user(request).username
    }
    return HttpResponse(template.render(context, request))


def add(request):
    shows = Shows(name=request.POST['name'], description=request.POST['description'],
                  duration=request.POST['duration'],
                  date=request.POST['date'],
                  hasAd=request.POST['hasAd'])
    shows.save()
    return HttpResponseRedirect(reverse('polis:index'))


def delete(request):
    Shows.objects.filter(id=request.POST["id"]).delete()
    return HttpResponseRedirect(reverse('polis:index'))


def editShows(request, shows_id):
    shows = get_object_or_404(Shows, id=shows_id)
    return render(request, 'polis/edit.html', {'shows': shows, 'user': auth.get_user(request).username})


def updateShows(request, shows_id):
    shows = get_object_or_404(Shows, id=shows_id)
    try:
        shows.name = request.POST['name']
        shows.description = request.POST['description']
        shows.duration = request.POST['duration']
        shows.date = request.POST['date']
        shows.hasAd = request.POST['hasAd']
        shows.save()
    except KeyError:
        return render(request, 'polis/edit.html', {'shows': shows})
    
    return HttpResponseRedirect(reverse('polis:index'))


def login(request):
    template = loader.get_template('polis/login.html')
    return HttpResponse(template.render({}, request))


def userlogin(request):
    login = request.POST['login']
    password = request.POST['pass']
    user = auth.authenticate(username=login, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('polis:index'))
    else:
        template = loader.get_template('polis/login.html')
        return HttpResponse(template.render({'error': 'wrong login or password'}, request))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('polis:index'))


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
            return HttpResponseRedirect(reverse('polis:index'))
        else:
            args['form'] = newuser_form
    template = loader.get_template('polis/register.html')
    return HttpResponse(template.render(args, request))