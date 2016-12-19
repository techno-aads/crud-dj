from django.conf.urls import url

from . import views

from .views import IndexView, ItemNewView, ItemShowView, ItemEditView, UserNew, UserLogin


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),	
    url(r'^items/new/$', ItemNewView.as_view(), name='item_new'),	
    url(r'^items/(?P<pk>[0-9]+)/$', ItemShowView.as_view(), name='item_show'),	
    url(r'^items/(?P<pk>[0-9]+)/edit$', ItemEditView.as_view(), name='item_edit'),
    url(r'^items/(?P<item_id>[0-9]+)/update$', views.item_update, name='item_update'),
    url(r'^items/create/$', views.item_create, name='item_create'),

		# url(r'^signup/$', CreateView.as_view( template_name='edit.html',
		# 																			form_class=UserCreationForm,
		# 																			success_url='/index'), 
		# 																			name='registration'),

		
		# url(r'^login/$', UserLogin.as_view(), name='login'),
		# url(r'^logout/$', views.user_logout, name='logout'),

]