from django.conf.urls import url

from . import views

app_name = 'tv'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]*)/$', views.edit, name='edit'),
    url(r'add/$', views.add, name='add'),
    url(r'^(?P<id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<id>[0-9]+)/save/$', views.save, name='save'),
    url(r'register/$', views.register, name='register'),
    url(r'logout/$', views.logout, name='logout'),
    url(r'login/$', views.login, name='login'),

]
