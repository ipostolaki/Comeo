from django.conf.urls import url
from django.views import i18n

from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    # localization
    url(r'^i18n/setlang/$', i18n.set_language, name='set_language'),
]
