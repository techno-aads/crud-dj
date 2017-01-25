from django.conf.urls import url

from . import views

app_name = 'orders'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^addDone/$', views.addDone, name='addDone'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^editDone/$', views.editDone, name='editDone'),
    url(r'^remove/$', views.remove, name='remove')
]
