from django.conf.urls import url

from . import views

app_name = 'shows'
urlpatterns = [
    url(r'^$', views.ShowList.as_view(), name='show_list'),
    url(r'^new$', views.ShowCreate.as_view(), name='show_new'),
    url(r'^edit/(?P<pk>\d+)$', views.ShowUpdate.as_view(), name='show_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.ShowDelete.as_view(), name='show_delete'),
]