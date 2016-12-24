from django.shortcuts import render, get_object_or_404
from django.views import generic
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Program
class ListView(generic.ListView):
    template_name = 'teleshow/list.html'
    context_object_name = 'program_list'

    def get_queryset(self):
        return Program.objects.order_by('broadcast_date')

class DetailView(generic.DetailView):
    model = Program
    template_name = 'teleshow/detail.html'

def add(request):
    return render(request, 'teleshow/add.html')

def change(request, pk):
    program = get_object_or_404(Program, pk=pk)
    return render(request, 'teleshow/add.html', {'program': program})

def save(request, pk):
    prog = Program()
    if pk != "-1":
        prog = get_object_or_404(Program, pk=pk)
    name = request.POST['name']
    duration = request.POST['duration']
    description = request.POST['description']
    datetime = request.POST['date'] + ' ' + request.POST['time']
    advertisement = request.POST.get('advertisement', 'off')
    if advertisement == 'on':
        advertisement = True
    else:
        advertisement = False
    prog.name = name
    prog.duration = duration
    prog.description = description
    prog.broadcast_date = datetime
    prog.advertisement = advertisement
    try:
        prog.save()
    except (KeyError, forms.ValidationError):
        return render(request, 'teleshow/add.html', {
            'error_message': "Введите корректную дату/время",
        })
    else:
        return HttpResponseRedirect(reverse('list'))

def delete(request, pk):
    program = get_object_or_404(Program, pk=pk)
    program.delete()
    return HttpResponseRedirect(reverse('list'))
