from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Show, ShowForm
from django.contrib.auth.forms import UserCreationForm


def index(request):
    show_list = Show.objects.all()
    context = {'show_list': show_list}
    return render(request, 'shows/index.html', context)


@login_required()
def add(request):
    form = ShowForm()
    return render(request, 'shows/add.html', {'form': form})


@login_required()
def addDone(request):
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            duration = request.POST['duration']
            description = request.POST['description']
            show_date = request.POST['show_date_year'] + "-" + \
                        request.POST['show_date_month'] + "-" + \
                        request.POST['show_date_day']
            adds = request.POST['adds']
            newShow = Show(name=name, duration=duration, show_date=show_date,
                           description=description, adds=adds)
            newShow.save()
            messages.info(request, "Show added successfully")
            return HttpResponseRedirect(reverse('shows:index'))
        else:
            return render(request, 'shows/add.html', {'form': form})
    return redirect('shows:index')


@login_required()
def edit(request):
    if request.method == 'POST':
        show = get_object_or_404(Show, pk=request.POST['id'])
        form = ShowForm(initial={'name': show.name,
                             'duration': show.duration,
                             'description': show.description,
                             'show_date': show.show_date,
                             'adds': show.adds
                             })
        context = {'form': form, 'show_id': request.POST['id']}
        return render(request, 'shows/edit.html', context)
    return redirect('shows:index')


@login_required()
def editDone(request):
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            show = get_object_or_404(Show, pk=request.POST['id'])
            show.name = request.POST['name']
            show.duration = request.POST['duration']
            show.description = request.POST['description']
            show.show_date = request.POST['show_date_year'] + "-" + \
                                     request.POST['show_date_month'] + "-" + \
                                     request.POST['show_date_day']
            show.adds = request.POST['adds']
            show.save()
            messages.info(request, "Edited successfully")
            return redirect('shows:index')
        else:
            return render(request, 'shows/edit.html', {'form': form})
    return redirect('shows:index')


@login_required()
def remove(request):
    if request.method == 'POST':
        show = get_object_or_404(Show, pk=request.POST['id'])
        show.delete()
        return HttpResponseRedirect(reverse('shows:index'))
    return redirect('shows:index')


def registration(request):
    if not request.user.is_authenticated():
        if not request.method == 'POST':
            form = UserCreationForm()
            return render(request, 'shows/registration.html', {'form': form})
        else:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                new_user = authenticate(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password1'],
                                        )
                login(request, new_user)
                return redirect('shows:index')
            else:
                return render(request, 'shows/registration.html', {'form': form})
    else:
        messages.info(request, "Logout to register new user")
        return redirect('shows:index')
