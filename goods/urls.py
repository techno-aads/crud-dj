from django.conf.urls import url

from goods import views

app_name = 'goods'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/', views.create, name='create'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<good_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<good_id>[0-9]+)/save/$', views.save, name='save'),
    url(r'^(?P<good_id>[0-9]+)/remove/$', views.remove, name='remove'),
]