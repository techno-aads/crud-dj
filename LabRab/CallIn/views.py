from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, request
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.urls import reverse
from django.views import generic

from .models import Telecast
from django.template import loader
from django.utils import timezone
from django.contrib import auth

def index(request):
    latest_telecast_list = Telecast.objects.order_by('-tel_date')
    context = {'latest_telecast_list': latest_telecast_list,
        'username': auth.get_user(request).username,
    }
    return render(request, 'CallIn/index.html', context)

def detail(request, telecast_id):
    telecast = get_object_or_404(Telecast, pk=telecast_id)
    return render(request, 'CallIn/detail.html', {'telecast': telecast, 'username': auth.get_user(request).username})

def results(request, telecast_id):
    response = "You're looking at the results of t %s."
    return HttpResponse(response % telecast_id)

def vote(request, telecast_id):
    return HttpResponse("You're voting on question %s." % telecast_id)

class IndexView(generic.ListView):
    template_name = 'CallIn/index.html'
    context_object_name = 'latest_telecast_list'

    def get_queryset(self):
        """Return the last published telecast."""
        return Telecast.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-tel_date')

class DetailView(generic.DetailView):
    model = Telecast
    template_name = 'CallIn/detail.html'
    def get_queryset(self):
        return Telecast.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Telecast
    template_name = 'CallIn/results.html'

def addTelecast(request, telecast_id):
    telecastTel = get_object_or_404(Telecast, pk=telecast_id)
    try:
        telecastTel.student_set.create(tel_name=request.POST['name'],
                                      tel_descr=request.POST['decsription'])
    except (KeyError, Telecast.DoesNotExist):
        return render(request, 'CallIn/details.html', {
            'telecast': telecastTel,
            'error_message': "You don't select a choice!"

        })
    else:
        telecastTel.save()
        return HttpResponseRedirect(reverse('CallIn:detail', args=(telecastTel.id,)))


def add(request):
    tel_name_get = request.POST['name']
    tel_descr_get= request.POST['description']
    tel_duration_get = request.POST['duration']
    tel_date_get = str(request.POST['date'])
    if (len(tel_name_get) > 0) & (len(tel_descr_get)> 0) & (len(tel_duration_get)> 0):
        telecastNew = Telecast(tel_name=tel_name_get,
                           tel_descr=tel_descr_get,
                           tel_duration=tel_duration_get,
                               tel_date=tel_date_get)
        telecastNew.save()
    return HttpResponseRedirect(reverse('CallIn:index'))


def delete(request):
    Telecast.objects.filter(id=request.POST["id"]).delete()
    return HttpResponseRedirect(reverse('CallIn:index'))


def deleteTelecast(request):
    Telecast.objects.filter(id=request.POST["telecast_id"]).delete()
    return HttpResponseRedirect(reverse('CallIn:detail', args=(request.POST["telecast_id"],)))


def editTelecast(request, telecast_id):
    telecast = get_object_or_404(Telecast, pk=telecast_id)
    return render(request, 'CallIn/editTelecast.html', {'telecast': telecast,})


def updateTelecast(request, telecast_id):
    tel_name_get = request.POST['name']
    tel_descr_get = request.POST['description']
    tel_duration_get = request.POST['duration']
    tel_date_get = str(request.POST['date'])
    if (len(tel_name_get) > 0) & (len(tel_descr_get) > 0):
        Telecast.objects.filter(id=telecast_id).update(tel_name=request.POST['name'],
                                               tel_descr=request.POST['description'],tel_duration=tel_duration_get,tel_date=tel_date_get)
    return HttpResponseRedirect(reverse('CallIn:index'))

def login(request):
    args={}
    args.update(csrf(request))
    if request.POST:
        username=request.POST.get('username', '')
        password=request.POST.get('password', '')
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect(reverse('CallIn:index'))
        else:
            args['login_error']="Пользователь не найден"
            return render_to_response('CallIn/login.html',args)

    else:
        return render_to_response('CallIn/login.html', args)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('CallIn:index'))

def register(request):
    args={}
    args.update(csrf(request))
    args['form']=UserCreationForm()
    if request.POST:
        newuser_form=UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser=auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return HttpResponseRedirect(reverse('CallIn:index'))
        else:
            args['form']=newuser_form
    return render_to_response('CallIn/register.html', args)
