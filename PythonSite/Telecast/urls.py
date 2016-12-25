from django.conf.urls import url
from . import views

app_name = "Telecast"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]*)/$', views.edit, name='edit'),
    url(r'^(?P<id>[0-9]*)/save/$', views.save, name='save'),
    url(r'^(?P<id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^program_new/', views.program_new, name='program_new'),
    url(r'^create/', views.create, name='create'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^userlogin/', views.userlogin, name='Userlogin'),
]