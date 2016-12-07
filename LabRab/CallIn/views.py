from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Telecast
from django.template import loader
from django.utils import timezone

def index(request):
    latest_telecast_list = Telecast.objects.order_by('-tel_date')
    context = {'latest_telecast_list': latest_telecast_list}
    return render(request, 'CallIn/index.html', context)

def detail(request, telecast_id):
    telecast = get_object_or_404(Telecast, pk=telecast_id)
    return render(request, 'CallIn/detail.html', {'telecast': telecast})

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
        return HttpResponseRedirect(reverse('polls:detail', args=(telecastTel.id,)))


def add(request):
    telecastNew = Telecast(tel_name=request.POST['name'], tel_descr=request.POST['description'])
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
    return render(request, 'CallIn/editTelecast.html', {'telecast': telecast})


def updateTelecast(request, telecast_id):
    Telecast.objects.filter(id=telecast_id).update(tel_name=request.POST['name'],
                                               tel_descr=request.POST['description'])
    return HttpResponseRedirect(reverse('CallIn:index'))

