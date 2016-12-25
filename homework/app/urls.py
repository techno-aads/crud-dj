from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    url(r'show/$', views.show_orders, name='show_orders'),
    url(r'show/add_order/$', views.add_order, name='add_order'),
    url(r'save_order/(?P<uid>[^/]+)/$', views.save_order, name='save_order'),
    url(r'show/show_full/(?P<uid>[^/]+)/$', views.show_full, name='show_full'),
    url(r'show/delete_order/(?P<uid>[^/]+)/$', views.delete_order, name='delete_order'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}),
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logged_out.html'}),
    url(r'^registration/$', views.register),
    url(r'^create_user/$', views.create_new_user),
]