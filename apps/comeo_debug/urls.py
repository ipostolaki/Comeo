from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^intended500/', views.intended500, name='intended500'),
    url(r'^mail_logger_check/', views.mail_logger_check, name='mail_logger_check'),
]
