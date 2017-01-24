from django.shortcuts import render, get_object_or_404
from django.views import generic
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import User

def authentication(request):
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
            'error_message': "We have not user with this login",
        })
    else:
        if user.password != request.POST['password']:
            return render(request, 'authorization/authentication.html', {
                'error_message': "password is incorrect",
            })
        else:
            request.session['user_id'] = user.id
            return HttpResponseRedirect(reverse('telecast:telecast'))


def registration(request):
    return render(request, 'authorization/registration.html')

def guest(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return render(request, 'telecast/telecast.html')

def addUser(request):
    login = request.POST['login']
    password = request.POST['password']
    isAbleToEdit = request.POST.get('isAbleToEdit', 'off')
    if isAbleToEdit == 'on':
        isAbleToEdit = True
    else:
        isAbleToEdit = False
    user = User(login=login, password=password, isAbleToEdit=isAbleToEdit)
    try:
        user.save()
    except (KeyError, forms.ValidationError):
        return render(request, 'telecast/telecast.html', {
            'error_message': "Too many letters.",
        })
    else:
        return HttpResponseRedirect(reverse('authorization:authentication'))



