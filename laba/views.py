from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404

from laba.forms import ProgrammeForm
from laba.models import Programme


def programme_list(request):
    programmes = Programme.objects.all().order_by('date')
    return render(request, 'laba/programme_list.html', {'programmes': programmes})


@login_required(redirect_field_name='laba.views.programme_list')
def programme_new(request):
    if request.method == "POST":
        form = ProgrammeForm(request.POST)
        if form.is_valid():
            programme = form.save()
            programme.save()
            return redirect('laba.views.programme_list')
    else:
        form = ProgrammeForm()
    return render(request, 'laba/programme_edit.html', {'form': form, 'isNew': True})


@login_required(redirect_field_name='laba.views.programme_list')
def programme_remove(request, pk):
    if request.method == "GET":
        programme = get_object_or_404(Programme, pk=pk)
        programme.delete()
    return redirect('laba.views.programme_list')


@login_required(redirect_field_name='laba.views.programme_list')
def programme_edit(request, pk):
    programme = get_object_or_404(Programme, pk=pk)
    if request.method == "POST":
        form = ProgrammeForm(request.POST, instance=programme)
        if form.is_valid():
            programme = form.save()
            programme.save()
            return redirect('laba.views.programme_list')
    else:
        form = ProgrammeForm(instance=programme)
    return render(request, 'laba/programme_edit.html', {'form': form, 'isNew': False})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
        return redirect('laba.views.programme_list')
    else:
        form = AuthenticationForm(request.POST)
        return render(request, 'laba/login.html', {'form': form, 'isLogin': True})


def logout_user(request):
    logout(request)
    return redirect('laba.views.programme_list')


def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('laba.views.login_user')
        else:
            return render(request, 'laba/login.html', {'form': form, 'isLogin': False})

    return render(request, 'laba/login.html', {'form': UserCreationForm(), 'isLogin': False})
