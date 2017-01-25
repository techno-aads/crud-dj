from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import auth
from django.template import RequestContext

from .models import Show


# class IndexView(generic.ListView):
#     template_name = 'timetable/index.html'
#     context_object_name = 'show_list'
#     def get_queryset(request):
#         return Show.objects.order_by('show_date')

def IndexView(request):
    return render_to_response('timetable/index.html',
                              {'show_list': Show.objects.all(), 'username': auth.get_user(request).username})

def addShow(request):
    return render(request, 'timetable/addShow.html')

def addShowDone(request):
    name = request.POST['name']
    duration = request.POST['duration']
    description = request.POST['description']
    show_date = request.POST['date']
    adds = request.POST['adds']

    newShow = Show(name=name, duration=duration, description=description, show_date=show_date, adds=adds)
    newShow.save()
    return HttpResponseRedirect(reverse('timetable:index'))

def editShow(request):
    editableShow = get_object_or_404(Show, pk=request.POST['id'])
    context = {'show': editableShow}
    return render(request, 'timetable/editShow.html', context)

def editShowDone(request):
    editableShow = get_object_or_404(Show, pk=request.POST['id'])
    editableShow.name = request.POST['name']
    editableShow.duration = request.POST['duration']
    editableShow.description = request.POST['description']
    editableShow.show_date = timezone.now() #request.POST['delivery_date'] заглушка
    editableShow.adds = request.POST['adds']
    editableShow.save()
    return HttpResponseRedirect(reverse('timetable:index'))

def removeShow(request):
    # show = get_object_or_404(Show, pk=request.POST['id'])
    # show.delete()
    # return render_to_response('timetable/index.html', {'show_list': Show.objects.all(), 'username': auth.get_user(request).username}, context_instance=RequestContext(request))
    Show.objects.filter(id=request.POST["id"]).delete()
    return HttpResponseRedirect(reverse('timetable:index'))
