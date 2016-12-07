from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'app/new/$', views.add_new, name='add_new'),
    url(r'^(?P<id>[0-9]*)/remove/$', views.delete, name='delete'),
    url(r'^(?P<id>[0-9]*)/$', views.edit, name='edit'),
    url(r'^$', views.index, name='index')
]