from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone

from .forms import ProgramForm, UserForm
from .models import Program


def index(request):
    list = Program.objects.all()
    context = {
        "list": list
    }
    return render(request, 'tv/index.html', context)


def edit(request, id):
    if 'username' in request.session:
        username = request.session['username']
        obj = get_object_or_404(Program, pk=id)
        return render(request, 'tv/edit.html', {'obj': obj})
    else:
        # return HttpResponseRedirect(reverse('tv:register'))
        return render(request, 'tv/not_enough_rights.html')


def save(request, id):
    if 'username' in request.session:
        username = request.session['username']
        obj = get_object_or_404(Program, pk=id)
        try:
            obj.description = request.POST['description']
            obj.timeLen = request.POST['timeLen']
            obj.ad = request.POST['ad']
            obj.dateTime = request.POST['dateTime']
            obj.name = request.POST['name']
            obj.save()
        except:
            obj = get_object_or_404(Program, pk=id)
            return render(request, 'tv/edit.html', {'obj': obj})
        else:
            return HttpResponseRedirect(reverse('tv:index'))
    else:
        # return HttpResponseRedirect(reverse('tv:register'))
        return render(request, 'tv/not_enough_rights.html')


def delete(request, id):
    if 'username' in request.session:
        username = request.session['username']
        obj = get_object_or_404(Program, pk=id)
        obj.delete()
        return HttpResponseRedirect(reverse('tv:index'))
    else:
        # return HttpResponseRedirect(reverse('tv:register'))
        return render(request, 'tv/not_enough_rights.html')


def register(request):
    if 'username' in request.session:
        username = request.session['username']
        return render(request, 'tv/log_is_fine.html', {'username': username})
    else:
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.published_date = timezone.now()

                # хэш
                user.set_password(request.POST['password'])

                user.save()

                username = form.cleaned_data['username']
                request.session['username'] = username

                return redirect('../', pk=user.pk)
        else:
            form = UserForm()
        return render(request, 'tv/register.html', {'form': form})


def add(request):
    if 'username' in request.session:
        username = request.session['username']
        if request.method == "POST":
            form = ProgramForm(request.POST)
            if form.is_valid():
                program = form.save(commit=False)
                program.published_date = timezone.now()
                program.save()
                return redirect('../', pk=program.pk)
        else:
            form = ProgramForm()
        return render(request, 'tv/add.html', {'form': form})
    else:
        return render(request, 'tv/not_enough_rights.html')
        # return HttpResponseRedirect(reverse('tv:register'))


def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return HttpResponseRedirect(reverse('tv:register'))


def login(request):
    try:
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.get(username=username)
        pwd_valid = user.check_password(password)

        if pwd_valid:
            request.session['username'] = username
            return render(request, 'tv/log_is_fine.html', {'username': username})
        else:
            return HttpResponseRedirect(reverse('tv:register'))
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse('tv:register'))
