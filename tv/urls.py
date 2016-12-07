from django.conf.urls import url

from . import views

app_name = 'tv'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^create/$', views.ProgramCreate.as_view(), name='create'),
    # ex: /tv/5/
    url(r'^(?P<pk>[0-9]+)/detail/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.ProgramUpdate.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.ProgramDelete.as_view(), name='delete'),
    # url(r'^(?P<student_id>[0-9]+)/$', views.choose, name='choose'),
]
