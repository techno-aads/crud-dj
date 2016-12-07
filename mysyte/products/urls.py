from django.conf.urls import url

from . import views

app_name = 'products'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^addOrder/$', views.addOrder, name='addOrder'),
    url(r'^addOrderDone/$', views.addOrderDone, name='addOrderDone'),
    url(r'^editOrder/$', views.editOrder, name='editOrder'),
    url(r'^editOrderDone/$', views.editOrderDone, name='editOrderDone'),
    url(r'^removeOrder/$', views.removeOrder, name='removeOrder'),
]
