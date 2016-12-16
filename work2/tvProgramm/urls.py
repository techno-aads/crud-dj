from django.conf.urls import url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', CreateView.as_view(
            template_name='edit.html',
            form_class=UserCreationForm,
            success_url='/programms')
            , name='registration'),
    url(r'^login/$', views.loginView, name='login'),
    url(r'^logout/$', views.logoutView, name='logout'),
    url(r'^add/$', views.addProgramm, name='add'),
    url(r'^(?P<id>[0-9]*)/save/$', views.saveProgramm, name='save'),
    url(r'^(?P<id>[0-9]*)/delete/$', views.deleteProgramm, name='delete'),
]