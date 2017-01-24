from django.conf.urls import url

from . import views

app_name = 'tv'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'app/new/$', views.add_new, name='add_new'),
    url(r'^(?P<id>[0-9]*)/remove/$', views.delete, name='delete'),
    url(r'^(?P<id>[0-9]*)/$', views.edit, name='edit')
]