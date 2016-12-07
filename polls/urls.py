from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<course_id>[0-9]+)/$', views.details, name='detail'),
    # ex: /polls/5/vote/
    url(r'^(?P<course_id>[0-9]+)/vote/$', views.addStu, name='vote'),
    # ex: /polls/add/
    url(r'^add/$', views.add, name='add'),
    # ex: /polls/remove/5/
    url(r'^remove/$', views.delete, name='delete'),
    # ex: /polls/removeStudent/5/course/4/
    url(r'^removeStudent/$', views.deleteStudent, name='deleteStudent'),
    # ex: /polls/edit/5/
    url(r'^edit/(?P<course_id>[0-9]+)$', views.editCourse, name='edit'),
    # ex: /polls/updateCourse/4/
    url(r'^updateCourse/(?P<course_id>[0-9]+)$', views.updateCourse, name='updateCourse'),
    # ex: /polls/editStu/4
    url(r'^editStu/(?P<student_id>[0-9]+)$', views.editStudent, name='editStu'),
    # ex: /polls/updateStudent
    url(r'^updateStudent/(?P<student_id>[0-9]+)/$', views.updateStudent, name='updateStu')
]