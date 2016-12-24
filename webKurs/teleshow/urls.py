from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<pk>-?[0-9]+)/save/$', views.save, name='save'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<pk>[0-9]+)/change/$', views.change, name='change'),
]
