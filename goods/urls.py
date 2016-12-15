from django.conf.urls import url
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

from goods import views

app_name = 'goods'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', login, {'template_name': 'goods/login.html'}, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^create/', views.create, name='create'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<good_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<good_id>[0-9]+)/save/$', views.save, name='save'),
    url(r'^(?P<good_id>[0-9]+)/remove/$', views.remove, name='remove'),
]