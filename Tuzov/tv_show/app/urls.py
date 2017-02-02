from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'app'
urlpatterns = [

    url(r'^accounts/login/$', auth_views.login),

    # ex: /app/
    url(r'^$', views.index, name='index'),
    # ex: /app/5/
    #url(r'^(?P<tv_show_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /app/add/
    url(r'^add/$', views.add, name='add'),

    url(r'^register/', views.register, name='register'),
    url(r'^userLogin/', views.userLogin, name='userLogin'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^edit/', views.edit, name='edit'),
    url(r'^delete/', views.delete, name='delete'),
    url(r'^edit_show/(?P<show_id>[0-9]+)$', views.editShow, name='edit_show'),
    url(r'updateshow/(?P<show_id>[0-9]+)$', views.updateShow, name='update_show'),
    url(r'^login/', views.login, name='login')

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
