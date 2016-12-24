from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin

from control import views

urlpatterns = [
    url(r'^$', views.product, name='product'),
    url(r'^(?P<product_id>[0-9]+)/$', views.details, name='details'),
    url(r'^(?P<product_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
]
