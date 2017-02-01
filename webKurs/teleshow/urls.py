from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<pk>-?[0-9]+)/save/$', views.save, name='save'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<pk>[0-9]+)/change/$', views.change, name='change'),
]
