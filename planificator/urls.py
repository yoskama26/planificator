from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls import include, url

urlpatterns = [
    path('', include('home.urls')),
    path('organisation/', include('organisation.urls')),
    path('grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^userprofile/', include('userprofile.urls')),
]
