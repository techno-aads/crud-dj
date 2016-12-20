from django.conf.urls import url
from . import views

app_name = 'goods'
urlpatterns = [
    url(r'^$', views.order_list, name='order_list'),
    url(r'^order/new/$', views.order_new, name='order_new'),
    url(r'^order/(?P<pk>\d+)/edit/$', views.order_edit, name='order_edit'),
    url(r'^order/(?P<pk>\d+)/remove/$', views.order_remove, name='order_remove'),
]