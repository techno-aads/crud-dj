from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/add/
    url(r'^add/$', views.add, name='add'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^userlogin/', views.userlogin, name='Userlogin'),
    # ex: /polls/remove/5/
    url(r'^remove/$', views.delete, name='delete'),
    # ex: /polls/edit/5/
    url(r'^edit/(?P<goods_id>[0-9]+)$', views.editGoods, name='edit'),
    # ex: /polls/updateGoods/4/
    url(r'^updateCourse/(?P<goods_id>[0-9]+)$', views.updateGoods, name='updateGoods'),
]