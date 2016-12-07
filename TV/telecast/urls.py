from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /telecast/
    url(r'^$', views.index, name='index'),
    # ex: /telecast/5/data/
    url(r'all_data/', views.all_data, name='all_data'),
	# ex: /telecast/5/add_data/
	#url(r'(?P<name>[a-b]+)/(?P<length>[0-9]+)/(?P<description>[a-b]+)/(?P<spamf>[a-b]+)/add_data/', views.add_data, name='add_data'),
]