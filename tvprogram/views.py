from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError

from tvprogram.models import TVShow


def index(request):
    tvprogram = TVShow.objects.order_by('name', '-duration')
    context = {
        'tvprogram': tvprogram,
    }
    return render(request, 'tvprogram/index.html', context)


def detail(request, tv_show_id):
    tv_show = get_object_or_404(TVShow, pk=tv_show_id)
    context = {
        'tv_show': tv_show,
    }
    return render(request, 'tvprogram/detail.html', context)


def add(request):
    if not request.user.is_authenticated():
        return render(request, 'tvprogram/need_login.html')
    else:
        name = request.POST['name']
        duration = request.POST['duration']
        description = request.POST['description']
        broadcasting_date = request.POST['broadcasting_date']
        try:
            contains_advertisement = request.POST['contains_advertisement'] == 'on'
        except MultiValueDictKeyError:
            contains_advertisement = False
        TVShow.objects.create(
            name=name,
            duration=duration,
            description=description,
            broadcasting_date=broadcasting_date,
            contains_advertisement=contains_advertisement
        )
        return HttpResponseRedirect(reverse('tvprogram:index'))


def create(request):
    if not request.user.is_authenticated():
        return render(request, 'tvprogram/need_login.html')
    else:
        return render(request, 'tvprogram/create.html')


def delete(request, tv_show_id):
    if not request.user.is_authenticated():
        return render(request, 'tvprogram/need_login.html')
    else:
        get_object_or_404(TVShow, pk=tv_show_id).delete()
        return HttpResponseRedirect(reverse('tvprogram:index'))


def save(request, tv_show_id):
    if not request.user.is_authenticated():
        return render(request, 'tvprogram/need_login.html')
    else:
        tv_show = get_object_or_404(TVShow, pk=tv_show_id)
        tv_show.name = request.POST['name']
        tv_show.duration = request.POST['duration']
        tv_show.description = request.POST['description']
        tv_show.broadcasting_date = request.POST['broadcasting_date']
        try:
            tv_show.contains_advertisement = request.POST['contains_advertisement'] == 'on'
        except MultiValueDictKeyError:
            tv_show.contains_advertisement = False
        tv_show.save()
        return HttpResponseRedirect(reverse('tvprogram:index'))


def signup(request):
    context = {}
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            user_form = auth.authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password2']
            )
            auth.login(request, user_form)
            return HttpResponseRedirect(reverse('tvprogram:index'))
        else:
            context['form'] = user_form
    else:
        context['form'] = UserCreationForm()

    return render(request, 'tvprogram/signup.html', context)
