from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from tvprogram.models import TVShow


def index(request):
    latest_tv_shows_list = TVShow.objects.order_by('-broadcasting_date')[:7]
    context = {
        'latest_tv_shows_list': latest_tv_shows_list,
    }
    return render(request, 'tvprogram/index.html', context)


def detail(request, tv_show_id):
    tv_show = get_object_or_404(TVShow, pk=tv_show_id)
    context = {
        'tv_show': tv_show,
    }
    return render(request, 'tvprogram/detail.html', context)


def save(request, tv_show_id):
    tv_show = get_object_or_404(TVShow, pk=tv_show_id)
    tv_show.save()
    return HttpResponseRedirect(reverse('tvprogram:detail', args=tv_show_id))


def create(request, name, duration, description, broadcasting_date, contains_advertisement):
    TVShow.objects.create(TVShow(
        name=name,
        duration=duration,
        description=description,
        broadcasting_date=broadcasting_date,
        contains_advertisement=contains_advertisement)
    )
    return HttpResponseRedirect(reverse('tvprogram:index'))


def delete(request, tv_show_id):
    get_object_or_404(TVShow, pk=tv_show_id).delete()
    return HttpResponseRedirect(reverse('tvprogram:index'))
