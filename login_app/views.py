from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.core.urlresolvers import reverse

from .forms import MyRegistrationForm

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('tv:index'))
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('tv:index'))
        else:
            args['login_error'] = 'User not found'
            return render(request, 'login_app/login.html', args)
    else:
        return render(request, 'login_app/login.html', args)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('tv:index'))

def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('tv:index'))
    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    if request.POST:
        new_user_form = MyRegistrationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = auth.authenticate(username=new_user_form.cleaned_data['username'], password=new_user_form.cleaned_data['password2'])
            auth.login(request, new_user)
            return HttpResponseRedirect(reverse('tv:index'))
        else:
            args['form'] = new_user_form
    return render(request, 'login_app/register.html', args)