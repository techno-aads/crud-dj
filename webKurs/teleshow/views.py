from django.shortcuts import render, get_object_or_404
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Program
from authorization.models import User

def list(request):
    allowedToEdit = request.session.get('user_id', False)
    if allowedToEdit != False:
        allowedToEdit = User.objects.get(pk=allowedToEdit).allowedToEdit
    return render(request, 'teleshow/list.html', {
        'program_list' : Program.objects.order_by('broadcast_date'),
        'allowedToEdit' : allowedToEdit })

def detail(request, pk):
    program = get_object_or_404(Program, pk=pk)
    allowedToEdit = request.session.get('user_id', False)
    if allowedToEdit != False:
        allowedToEdit = User.objects.get(pk=allowedToEdit).allowedToEdit
    return render(request, 'teleshow/detail.html', {
        'program' : program,
        'allowedToEdit' : allowedToEdit })

def add(request):
    allowedToEdit = request.session.get('user_id', False)
    if allowedToEdit != False:
        allowedToEdit = User.objects.get(pk=allowedToEdit).allowedToEdit
    if allowedToEdit == False:
        return HttpResponse('Unauthorized', status=401)
    return render(request, 'teleshow/add.html')

def change(request, pk):
    allowedToEdit = request.session.get('user_id', False)
    if allowedToEdit != False:
        allowedToEdit = User.objects.get(pk=allowedToEdit).allowedToEdit
    if allowedToEdit == False:
        return HttpResponse('Unauthorized', status=401)
    program = get_object_or_404(Program, pk=pk)
    return render(request, 'teleshow/add.html', {'program': program})

def save(request, pk):
    allowedToEdit = request.session.get('user_id', False)
    if allowedToEdit != False:
        allowedToEdit = User.objects.get(pk=allowedToEdit).allowedToEdit
    if allowedToEdit == False:
        return HttpResponse('Unauthorized', status=401)
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
    allowedToEdit = request.session.get('user_id', False)
    if allowedToEdit != False:
        allowedToEdit = User.objects.get(pk=allowedToEdit).allowedToEdit
    if allowedToEdit == False:
        return HttpResponse('Unauthorized', status=401)
    program = get_object_or_404(Program, pk=pk)
    program.delete()
    return HttpResponseRedirect(reverse('list'))
