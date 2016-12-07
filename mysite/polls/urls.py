from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<order_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<order_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add, name='add'),
    url(r'^edit/(?P<order_id>[0-9]+)$', views.editOrder, name='edit'),
    url(r'^remove/$', views.delete, name='delete'),
]