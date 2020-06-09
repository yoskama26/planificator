from django.conf.urls import url
from . import views

app_name = 'userprofile'

urlpatterns = [
    url(r'^signup/$', views.signup_view, name="signup")
]