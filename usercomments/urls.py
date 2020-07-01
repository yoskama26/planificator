from django.conf.urls import url
from . import views

app_name = 'usercomments'

urlpatterns = [
    url(r'^$',views.comments_list, name="list"),
    url(r'^create/$', views.comments_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$',views.comments_detail, name="detail"),
    ]
