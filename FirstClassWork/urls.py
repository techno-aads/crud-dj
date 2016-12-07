
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'show/$', views.show_items, name='show_items'),
    url(r'show/add_item/$', views.add_item, name='add_item'),
    url(r'save_item/(?P<uid>[^/]+)/$', views.save_item, name='save_item'),
    url(r'show/show_full/(?P<uid>[^/]+)/$', views.show_full, name='show_full'),
    url(r'show/delete_item/(?P<uid>[^/]+)/$', views.delete_item, name='delete_item'),
]
