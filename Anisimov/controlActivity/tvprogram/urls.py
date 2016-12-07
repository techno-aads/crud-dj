from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<tvprogram_id>[0-9]+)/details/$', views.detail, name = 'detail'),
    url(r'^(?P<tvprogram_id>[0-9]+)/edit/$', views.edit, name = 'edit'),
    url(r'^(?P<tvprogram_id>[0-9]+)/save/$', views.save, name = 'save')
]
