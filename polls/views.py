from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Course, Student, Goods


# Create your views here.


def index(request):
    listOfGoods = Goods.objects.order_by('name')
    template = loader.get_template('polls/index.html')
    context = {
        'listOfGoods': listOfGoods
    }
    return HttpResponse(template.render(context, request))


def details(request, course_id):
    try:
        currentCourse = Course.objects.get(pk=course_id)
        listOfStudents = currentCourse.student_set.all()
        mainTitle = "Student list of " + currentCourse.name
    except Course.DoesNotExist:
        raise Http404("Course Does not exist")
    return render(request, 'polls/details.html', {
        'studentsList': listOfStudents,
        'mainTitle': mainTitle,
        'myId': course_id,
        'desc': currentCourse.description})


def addStu(request, course_id):
    courseCurr = get_object_or_404(Course, pk=course_id)
    try:
        courseCurr.student_set.create(name=request.POST['name'],
                                      family=request.POST['family'])
    except (KeyError, Course.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question': courseCurr,
            'error_message': "You don't select a choice!"
        })
    else:
        courseCurr.save()
        return HttpResponseRedirect(reverse('polls:detail', args=(courseCurr.id,)))


def add(request):
    goods = Goods(name=request.POST['name'], count=request.POST['count'],
                  address=request.POST['address'],
                  date=request.POST['date'],
                  isArrive=request.POST['arrived'])
    goods.save()
    return HttpResponseRedirect(reverse('polls:index'))


def delete(request):
    Goods.objects.filter(id=request.POST["id"]).delete()
    return HttpResponseRedirect(reverse('polls:index'))


def deleteStudent(request):
    Student.objects.filter(id=request.POST["student_id"]).delete()
    return HttpResponseRedirect(reverse('polls:detail', args=(request.POST["course_id"],)))


def editCourse(request, goods_id):
    goods = get_object_or_404(Goods, id=goods_id)
    return render(request, 'polls/editCourse.html', {'goods': goods})


def updateCourse(request, course_id):
    Goods.objects.filter(id=course_id).update(name=request.POST['name'], count=request.POST['count'],
                                              address=request.POST['address'],
                                              date=request.POST['date'],
                                              isArrive=request.POST['arrived'])
    return HttpResponseRedirect(reverse('polls:index'))


def editStudent(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    courses = Course.objects.all()
    return render(request, 'polls/editStu.html', {
        'student': student, 'courses': courses})


def updateStudent(request, student_id):
    course = get_object_or_404(Course, name=request.POST['course'])
    Student.objects.filter(id=student_id).update(name=request.POST['name'],
                                                 family=request.POST['family'],
                                                 learnSubj=course)
    return HttpResponseRedirect(reverse('polls:index'))
