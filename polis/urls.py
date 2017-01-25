from django.conf.urls import url

from . import views

app_name = 'polis'
urlpatterns = [
    # ex: /polis/
    url(r'^$', views.index, name='index'),
    # ex: /polis/add/
    url(r'^add/$', views.add, name='add'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^userlogin/', views.userlogin, name='Userlogin'),
    # ex: /polis/remove/5/
    url(r'^remove/$', views.delete, name='delete'),
    # ex: /polis/edit/5/
    url(r'^edit/(?P<shows_id>[0-9]+)$', views.editShows, name='edit'),
    # ex: /polis/updateShows/4/
    url(r'^updateCourse/(?P<shows_id>[0-9]+)$', views.updateShows, name='updateShows'),
]