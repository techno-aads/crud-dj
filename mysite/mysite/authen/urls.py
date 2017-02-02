from django.conf.urls import url
from . import views

app_name = 'authen'
urlpatterns = [
    url(r'^authen/$', views.authen, name='authen'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
]