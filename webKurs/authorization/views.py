from django.shortcuts import render, get_object_or_404
from django.views import generic
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import User

def authentication(request):
    #logout
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return render(request, 'authorization/authentication.html')

def login(request):
    try:
        user = User.objects.get(login=request.POST['login'])
    except (KeyError, User.DoesNotExist):
        return render(request, 'authorization/authentication.html', {
            'error_message': "Нет пользователя с таким логином",
        })
    else:
        if user.password != request.POST['password']:
            return render(request, 'authorization/authentication.html', {
                'error_message': "Неверный пароль",
            })
        else:
            request.session['user_id'] = user.id
            return HttpResponseRedirect(reverse('list'))


def registration(request):
    return render(request, 'authorization/registration.html')

def guest(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return render(request, 'teleshow/list.html')

def addUser(request):
    login = request.POST['login']
    if len(User.objects.filter(login=login)) > 0:
        return render(request, 'authorization/registration.html', {
            'error_message': "Пользователь с таким логином уже зарегистрирован",
        })
    password = request.POST['password']
    allowedToEdit = request.POST.get('allowedToEdit', 'off')
    if allowedToEdit == 'on':
        allowedToEdit = True
    else:
        allowedToEdit = False
    user = User(login=login, password=password, allowedToEdit=allowedToEdit)
    try:
        user.save()
    except (KeyError, forms.ValidationError):
        return render(request, 'teleshow/add.html', {
            'error_message': "Слишком много буков",
        })
    else:
        return HttpResponseRedirect(reverse('authorization:authentication'))
