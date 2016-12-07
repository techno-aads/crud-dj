from django.conf.urls import url

from . import views

app_name = 'tvprogram'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<tvShowId>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<tvShowId>[0-9]+)/save/$', views.save, name='save'),
    url(r'^(?P<tvShowId>[0-9]+)/create/$', views.create, name='create'),
    url(r'^(?P<tvShowId>[0-9]+)/delete/$', views.delete, name='delete'),
]
