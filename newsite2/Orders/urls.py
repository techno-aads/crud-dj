from django.conf.urls import url

from . import views

app_name='Orders'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<order_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<question_id>[0-9]+)/edit/$', views.edit, name='edit'),
	url(r'^(?P<question_id>[0-9]+)/save/$', views.save, name='save')
	]
	
