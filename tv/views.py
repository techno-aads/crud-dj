from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
from django.urls import reverse

from tv.models import Program


#
# def choose(request, student_id):
#     course_list = Course.objects.all()
#     student = get_object_or_404(Student, pk=student_id)
#     try:
#         selected_course = Course.objects.get(pk=request.POST['course'])
#     except (KeyError, Course.DoesNotExist):
#         return render(request, 'tv/detail.html', {
#             'student': student,
#             'error_message': "Вы не выбрали курс",
#             'course_list': course_list,
#         })
#     else:
#         if StudentCourses.objects.filter(student=student, course=selected_course):
#             return render(request, 'tv/detail.html', {
#                 'student': student,
#                 'error_message': "Студент уже записан на этот курс",
#                 'course_list': course_list,
#             })
#
#         student_course = StudentCourses(student=student, course=selected_course)
#         student_course.save()
#
#         return HttpResponseRedirect(reverse('tv:courses', args=(student.id,)))


class IndexView(generic.ListView):
    template_name = 'tv/index.html'
    context_object_name = 'program_list'

    def get_queryset(self):
        return Program.objects.order_by('date')


class DetailView(generic.DetailView):
    model = Program
    template_name = 'tv/detail.html'


class ProgramCreate(generic.CreateView):
    template_name_suffix = '_create'
    model = Program
    fields = ['name', 'description', 'length', 'date', 'add_advert']
    success_url = reverse_lazy('tv:index')


class ProgramUpdate(generic.UpdateView):
    template_name_suffix = '_update'
    model = Program
    fields = ['name', 'description', 'length', 'date', 'add_advert']
    success_url = reverse_lazy('tv:index')


class ProgramDelete(generic.DeleteView):
    template_name_suffix = '_delete'
    model = Program
    success_url = reverse_lazy('tv:index')
