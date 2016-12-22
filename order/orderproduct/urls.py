from django.conf.urls import url

from . import views

app_name = 'orderproduct'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<orderprod_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add/', views.add, name='add'),
    url(r'^remove/$', views.delete, name='delete'),
    url(r'^edit/(?P<orderprod_id>[0-9]+)$', views.edit, name='edit'),
    url(r'^updateC/(?P<orderprod_id>[0-9]+)$', views.update, name='update'),
    url(r'^login/', views.login,name='login'),
    url(r'^logout/', views.logout,name='logout'),

]