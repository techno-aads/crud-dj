from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^tvprogram/', include('tvprogram.urls')),
    url(r'^admin/', admin.site.urls),
]
