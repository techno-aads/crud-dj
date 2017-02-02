from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.prod_list, name='prod_list'),
    url(r'^prod/(?P<pk>[0-9]+)/$', views.prod_detail, name='prod_detail'),
    url(r'^prod/new/$', views.prod_new, name='prod_new'),
    url(r'^prod/(?P<pk>[0-9]+)/edit/$', views.prod_edit, name='prod_edit'),
    url(r'^prod/(?P<pk>[0-9]+)/remove/$', views.prod_remove, name='prod_remove'),
]