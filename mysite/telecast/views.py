from django.shortcuts import render

from .models import Telecast


def get_telecast_list(request):
    telecast_list = Telecast.objects.all()
    context = {'telecast_list': telecast_list}
    return render(request, "telecast/telecast.html", context)
