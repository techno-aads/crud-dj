
from django.conf.urls import url
<<<<<<< HEAD
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login, logout
=======
>>>>>>> e5aa9da59321a6318a92a2c80dbe808ee851327f
from . import views

urlpatterns = [
    url(r'show/$', views.show_items, name='show_items'),
    url(r'show/add_item/$', views.add_item, name='add_item'),
    url(r'save_item/(?P<uid>[^/]+)/$', views.save_item, name='save_item'),
    url(r'show/show_full/(?P<uid>[^/]+)/$', views.show_full, name='show_full'),
    url(r'show/delete_item/(?P<uid>[^/]+)/$', views.delete_item, name='delete_item'),
<<<<<<< HEAD
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}),
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logged_out.html'}),
    url(r'^registration/$', views.register),
    url(r'^create_user/$', views.create_new_user),
=======
>>>>>>> e5aa9da59321a6318a92a2c80dbe808ee851327f
]
