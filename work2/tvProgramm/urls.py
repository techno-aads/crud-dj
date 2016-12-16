from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add/$', views.addProgramm, name='add'),
    url(r'^(?P<id>[0-9]*)/save/$', views.saveProgramm, name='save'),
    url(r'^(?P<id>[0-9]*)/delete/$', views.deleteProgramm, name='delete'),
]