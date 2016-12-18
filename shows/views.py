from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Show, ShowForm
from .forms import RegistrationForm
#from .forms import ShowForm

# Create your views here.

def index(request):
    show_list = Show.objects.order_by('run_date')
    context = {'show_list': show_list}
    return render(request, 'shows/index.html', context)

@login_required(login_url="/login/")
def edit(request, show_id):
    show = get_object_or_404(Show, pk=show_id)  
    form = ShowForm(instance=show)
    return render(request, 'shows/edit.html', {'show': show, 'form': form})

@login_required(login_url="/login/")    
def add(request):
    form = ShowForm()
    return render(request, 'shows/add.html', {'form': form})

@login_required(login_url="/login/")
def update(request, show_id):
    show = get_object_or_404(Show, pk=show_id)  
    if request.method == 'POST':
        form = ShowForm(request.POST, instance=show)
        if form.is_valid():
            form.save()
            return redirect('shows:index')
        else:
            return render(request, 'shows/edit.html', {'show': show, 'form': form})

@login_required(login_url="/login/")
def create(request):
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shows:index')
        else:
            return render(request, 'shows/add.html', {'form': form})

@login_required(login_url="/login/")
def delete(request, show_id):
    show = get_object_or_404(Show, pk=show_id)  
    show.delete()
    return redirect('shows:index')

def registration(request):
    if not request.user.is_authenticated():
        form = RegistrationForm()
        return render(request, 'shows/registration.html', {'form': form})
    else:
        messages.info(request, "You have to logout to register new user.")
        return redirect('shows:index')

def perform_registration(request):
    if not request.user.is_authenticated():
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.info(request, "Thanks for registering. You are now logged in.")
                new_user = authenticate(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password1'],
                                        )
                login(request, new_user)
                return redirect('shows:index')
            else:
                return render(request, 'shows/registration.html', {'form': form})
    else:
        return redirect('shows:index')
