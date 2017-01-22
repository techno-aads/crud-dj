from django.conf.urls import url, include

from . import views

app_name = 'tvshows'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^userlogin/', views.userlogin, name='Userlogin'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^register/', views.register, name='register'),
    url(r'^edit/', views.edit, name='edit'),
    url(r'^delete/', views.delete, name='delete'),
    url(r'^editshow/', views.editshow, name='editshow'),
    url(r'^add/', views.add, name='add'),
]