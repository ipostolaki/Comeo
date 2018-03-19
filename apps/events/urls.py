from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.events_public, name='events_public'),
    url(r'^tico/$', views.tico_landing, name='tico_landing'),
    url(r'^event_details/$', views.event_details, name='event_details'),
    url(r'^coinpayments-ipn/$', views.coinpayments_ipn, name='coinpayments_ipn')
]
