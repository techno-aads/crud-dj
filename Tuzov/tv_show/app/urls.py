from django.conf.urls import url
from . import views

app_name = 'app'
urlpatterns = [
    # ex: /app/
    url(r'^$', views.index, name='index'),
    # ex: /app/5/
    url(r'^(?P<tv_show_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /app/add/
    url(r'^add/$', views.add, name='add'),


    # ex: /polls/5/
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # ex: /polls/add/
    #url(r'^add/$', views.add, name='add'),
    # ex: /polls/remove/
    #url(r'^remove/$', views.remove, name='remove'),
]
