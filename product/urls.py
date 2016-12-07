from django.conf.urls import url
from . import views
app_name = 'product'
urlpatterns = urlpatterns = [

    url(r'new/', views.product_new, name='product_new'),
    url(r'^$', views.product_list, name="product_list"),
    url(r'^(?P<id>[0-9]+)/delete/$', views.delete, name="product_delete"),
]
