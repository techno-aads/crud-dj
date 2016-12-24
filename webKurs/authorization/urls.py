from django.conf.urls import url

from . import views
app_name = 'authorization'
urlpatterns = [
    url(r'^$', views.authentication, name='authentication'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^adduser/$', views.addUser, name='addUser'),
    url(r'^login/$', views.login, name='login'),
]
