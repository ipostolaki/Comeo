from django.conf.urls import patterns, url
from comeo_app import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    )