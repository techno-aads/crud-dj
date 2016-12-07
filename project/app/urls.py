from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^products$', views.products, name='products'),
    url(r'^products/(?P<product_id>[0-9]+)$', views.product, name='product'),
	url(r'^products/save$', views.save_product, name='save_product'),
	url(r'^products/remove$', views.remove_product, name='remove_product'),
    url(r'^products/add$', views.add_product, name='add_product'),
]
