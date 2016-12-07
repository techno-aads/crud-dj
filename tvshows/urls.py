from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='index.html')),
    url(r'input', views.input, name='input'),
    url(r'shows', views.shows, name='shows'),
    url(r'index', views.index, name='index'),
]