from django.conf.urls import include, url

from . import views

app_name='Orders'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<order_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<order_id>[0-9]+)/edit/$', views.edit, name='edit'),
	url(r'^(?P<order_id>[0-9]+)/save/$', views.save, name='save'),
	url(r'^new/$', views.new, name='new'),
	url(r'^login/$', views.LoginFormView.as_view(), name='login'),
	url(r'^logout/$', views.logout_view, name='logout')
	]
	
