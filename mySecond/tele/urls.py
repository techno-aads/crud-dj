from django.conf.urls import url
from tele import views

app_name = 'tele'
urlpatterns = [
    url(r'^$', views.tele_list, name='tele_list'),
    url(r'^order/new/$', views.tele_new, name='tele_new'),
    url(r'^order/(?P<pk>\d+)/edit/$', views.tele_edit, name='tele_edit'),
    url(r'^order/(?P<pk>\d+)/remove/$', views.tele_remove, name='tele_remove'),
    ]