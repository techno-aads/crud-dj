from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Programm
from .forms import AddProgrammForm, LoginForm
from django.views import generic
from django.contrib.auth import authenticate, login, logout

def index(request):
    isLogged = request.user.is_authenticated
    username = ""
    if isLogged:
        username = request.user.username

    template = loader.get_template('index.html')
    listPrograms = Programm.objects.all() 

    context = {
        "programms": listPrograms,
        "isLogged": isLogged,
        "name": username,
    }
    return render(request, 'index.html', context)

def saveProgramm(request, id):
    if request.user.is_authenticated():
        form = AddProgrammForm(request.POST or None)
        if form.is_valid():
            obj = get_object_or_404(Programm, pk=id)
            try:
                obj.name = request.POST['name']
                obj.length = request.POST['length']
                obj.description = request.POST['description']
                obj.date = request.POST['date']
                obj.ad = False
                if obj.ad == 'on':
                    obj.ad = True
                else:
                    obj.ad = False

            except KeyError:
                return render(request, 'edit.html', {'form': form})
            else:
                obj.save()
                return HttpResponseRedirect(reverse('index'))
        return render(request, 'edit.html', {'form': form})
    else:
        return HttpResponseRedirect(reverse('index'))

def addProgramm(request):
    if request.user.is_authenticated():
        form = AddProgrammForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'edit.html', {'form': form})
    else:
        return HttpResponseRedirect(reverse('index'))
    

def deleteProgramm(request, id):
    if request.user.is_authenticated():
        toDelete = get_object_or_404(Programm, pk=id)
        toDelete.delete()
    return HttpResponseRedirect(reverse('index'))

def loginView(request):
    form = LoginForm
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'edit.html', {'form': form})

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))