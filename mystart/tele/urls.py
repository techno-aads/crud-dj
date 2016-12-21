from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tele_list, name='tele_list'),
    url(r'^tele/(?P<pk>[0-9]+)/$', views.tele_detail, name='tele_detail'),
    url(r'^tele/new/$', views.tele_new, name='tele_new'),
    url(r'^tele/(?P<pk>[0-9]+)/edit/$', views.tele_edit, name='tele_edit'),
]