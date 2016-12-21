from django.conf.urls import url

from laba import views

urlpatterns = [
    url(r'^$', views.programme_list, name='programme_list'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^programme/new/$', views.programme_new, name='programme_new'),
    url(r'^programme/(?P<pk>[0-9]+)/edit/$', views.programme_edit, name='programme_edit'),
    url(r'^programme/(?P<pk>[0-9]+)/remove/$', views.programme_remove, name='programme_remove'),
]
