from django.conf.urls import url

from . import views

app_name = 'CallIn'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<telecast_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<telecast_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<telecast_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^add/$', views.add, name='add'),
    # ex: /polls/remove/5/
    url(r'^remove/$', views.delete, name='delete'),
    # ex: /polls/removeStudent/5/course/4/
    url(r'^removeTelecast/$', views.deleteTelecast, name='deleteTelecast'),
    # ex: /polls/edit/5/
    url(r'^edit/(?P<telecast_id>[0-9]+)$', views.editTelecast, name='edit'),
    # ex: /polls/updateCourse/4/
    url(r'^updateTelecast/(?P<telecast_id>[0-9]+)$', views.updateTelecast, name='updateTelecast'),
]