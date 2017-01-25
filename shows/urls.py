from django.conf.urls import url

from . import views

app_name = 'shows'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /shows/edit/5/
    url(r'^edit/(?P<show_id>[0-9]+)/$', views.edit, name='edit'),
    # ex: /shows/update/5/
    url(r'^update/(?P<show_id>[0-9]+)/$', views.update, name='update'),
    # ex: /shows/add
    url(r'^add/$', views.add, name='add'),
    # ex: /shows/create
    url(r'^create$', views.create, name='create'),
     # ex: /shows/delete/5/
    url(r'^delete/(?P<show_id>[0-9]+)/$', views.delete, name='delete'),
]