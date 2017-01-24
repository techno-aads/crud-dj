from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib import auth
from django import forms

from .models import Telecast
from authorization.models import User


def get_telecast_list(request):
    telecast_list = Telecast.objects.all()
    context = {'telecast_list': telecast_list}
    return render(request, "telecast/telecast.html", context)

def get_telecast_guest_list(request):
    telecast_list = Telecast.objects.all()
    context = {'telecast_list': telecast_list}
    return render(request, "telecast/telecast_guest.html", context)

def add_telecast(request):
    if request.method == 'GET':
        return render(request, 'telecast/add_telecast.html')
    else:
        try:
            title = request.POST['title']
            duration = request.POST['duration']
            description = request.POST['description']
            broadcastDate = request.POST['broadcastDate']
            isAdvertising = request.POST['isAdvertising']
            telecast = Telecast(title=title, duration=duration,
                                description=description, broadcastDate=broadcastDate,
                                isAdvertising=isAdvertising)
            telecast.save()
            telecast_list = Telecast.objects.all()
            context = {'telecast_list': telecast_list}
            return render(request, "telecast/telecast.html", context)
        except KeyError:
            return render(request, 'telecast/add_telecast.html')


def edit_telecast(request, id):
    isAbleToEdit = request.session.get('user_id', False)
    if isAbleToEdit != False:
        telecast = get_object_or_404(Telecast, pk=id)
        context = {'telecast': telecast}
        return render(request, 'telecast/edit_telecast.html', context)
    else:
        telecast_list = Telecast.objects.all()
        context = {'telecast_list': telecast_list}
        return render(request, "telecast/telecast.html", context)


def save_telecast(request, id):
    telecast = get_object_or_404(Telecast, pk=id)
    try:
        telecast.title = request.POST['title']
        telecast.duration = request.POST['duration']
        telecast.description = request.POST['description']
        telecast.broadcastDate = request.POST['broadcastDate']
        telecast.isAdvertising = request.POST['isAdvertising']
        telecast.save()
    except KeyError:
        context = {'telecast': telecast}
        return render(request, 'telecast/edit_telecast.html', context)
    else:
        return HttpResponseRedirect(reverse('telecast:telecast'))


def delete_telecast(request, id):
    telecast = get_object_or_404(Telecast, pk=id)
    telecast.delete()
    return HttpResponseRedirect(reverse('telecast:telecast'))