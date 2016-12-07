from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^all/$', views.all, name='all'),
	# ex: /polls/5/
    url(r'^add/$', views.add, name='add'),
	# ex: /polls/5/
    url(r'^index/$', views.index, name='index'),
	# ex: /polls/5/results/
    url(r'^(?P<id>[A-Za-z]+)/detail/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<id>[A-Za-z]+)/edit/$', views.edit, name='edit'),
    # ex: /polls/5/vote/
    url(r'^(?P<id>[A-Za-z]*)/delete/$', views.delete, name='delete'),
]