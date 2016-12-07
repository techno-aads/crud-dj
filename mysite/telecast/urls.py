from django.conf.urls import url

from . import views

app_name = 'telecast'
urlpatterns = [
    url(r'^telecast/$', views.get_telecast_list, name='telecast'),
    # url(r'^telecast/add/$', views.add_telecast, name='add_telecast'),
    # url(r'^telecast/store/$', views.add_telecast, name='add_telecast'),
    # url(r'^telecast/edit/(?P<id>[0-9]+)/$', views.edit_telecast, name='edit_telecast'),
    # url(r'^telecast/delete/(?P<id>[0-9]+)/$', views.delete_telecast, name='delete_telecast'),
    # url(r'^telecast/save/(?P<id>[0-9]+)/$', views.save_telecast, name='save_telecast'),
]