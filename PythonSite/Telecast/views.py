from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from .models import TVPrograms


def index(request):
    List = TVPrograms.objects.all()
    context = {
        'List': List
    }
    return render(request, 'index.html', context)


def edit(request, id):
    obj = get_object_or_404(TVPrograms, id=id)
    return render(request, 'edit.html', {'obj': obj})


def save(request, id):
    obj = get_object_or_404(TVPrograms, id=id)
    try:
        obj.name = request.POST['name']
        obj.description = request.POST['description']
        obj.save()
    except KeyError:
        return render(request, 'edit.html', {'obj': obj})
    else:
        return HttpResponseRedirect(reverse('Telecast:index'))


def delete(request, id):
    obj = get_object_or_404(TVPrograms, id=id)
    obj.delete()
    return HttpResponseRedirect(reverse('Telecast:index'))


def program_new(request):
    program = TVPrograms(name=request.POST['name'], description=request.POST['description'])
    program.save()
    return HttpResponseRedirect(reverse('Telecast:index'))


def create(request):
    return render(request, 'create.html')


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
            return HttpResponseRedirect(reverse('Telecast:index'))
        else:
            args['form'] = newuser_form
    template = loader.get_template('register.html')
    return HttpResponse(template.render(args, request))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('Telecast:index'))


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))


def userlogin(request):
    login = request.POST['login']
    password = request.POST['pass']
    user = auth.authenticate(username=login, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('Telecast:index'))
    else:
        template = loader.get_template('login.html')
        return HttpResponse(template.render({'error': 'wrong login or password'}, request))
