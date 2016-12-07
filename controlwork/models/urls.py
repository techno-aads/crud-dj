from django.conf.urls import url

from . import views

app_name = 'models'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<order_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add, name='add'),
    url(r'^added/$', views.added, name='added'),
    url(r'^delete(?P<order_id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^edit(?P<order_id>[0-9]+)/$', views.edit, name='edit'),
]