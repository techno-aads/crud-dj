from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Student

def index(request):
    student_list = Student.objects.order_by('-id')
    #template = loader.get_template('practice/index.html')
    context = {
        'student_list': student_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'practice/index.html', context)

def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)  
    return render(request, 'practice/detail.html', {'student': student})
