from django.conf.urls import url

from control import views

urlpatterns = [
    url(r'^$', views.product, name='product'),
    url(r'^(?P<product_id>[0-9]+)/$', views.details, name='details'),
    url(r'^(?P<product_id>[0-9]+)/edit/$', views.edit, name='edit'),
]