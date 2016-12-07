from django.conf.urls import url
from . import views

app_name = "TV"
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]*)/$', views.edit, name='edit'),
    url(r'^(?P<id>[0-9]*)/save/$', views.save, name='save')
]