from django.conf.urls import url

from . import views


app_name = 'orders'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^create/$', views.ProductCreate.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.ProductDelete.as_view(), name='delete'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.ProductUpdate.as_view(), name='update'),

]