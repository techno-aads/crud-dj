import django
from django.conf.urls import url
from django.contrib.auth.views import login

from tvprogram import views

app_name = 'tvprogram'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', django.contrib.auth.views.login, {'template_name': 'tvprogram/login.html'}, name='login'),
    url(r'^logout/$', django.contrib.auth.views.logout, {'next_page': '/tvprogram'}, name='logout'),
    url(r'^create/', views.create, name='create'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<tv_show_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<tv_show_id>[0-9]+)/save/$', views.save, name='save'),
    url(r'^(?P<tv_show_id>[0-9]+)/remove/$', views.delete, name='delete'),
]
