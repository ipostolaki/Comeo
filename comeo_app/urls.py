from django.conf.urls import patterns, url

from comeo_app import views

urlpatterns = patterns(
    '',

    # Campaigns
    url(r'^campaigns/$', views.campaigns_public, name='campaigns_public'),
    url(r'^campaigns/(?P<pk>\d+)/$', views.campaign_details, name='campaign_details'),
    url(r'^campaigns/donate/(?P<pk>\d+)/$', views.campaign_donate, name='campaign_donate'),
    url(r'^campaigns/donate_instruction/transaction_pk=(?P<transaction_pk>\d+)&campaign_pk=(?P<campaign_pk>\d+)/$',  # noqa flake8
        views.donate_instruction, name='donate_instruction'),

    url(r'^profile/campaigns/create$', views.campaign_create, name='campaign_create'),
    url(r'^profile/campaigns/publish$/(?P<pk>\d+)/', views.campaign_edit, name='campaign_publish'),
    url(r'^profile/campaigns/(?P<pk>\d+)/$', views.campaign_edit, name='campaign_edit'),

    # Mail
    url(r'^email-subscribe/$', views.email_subscribe, name='email_subscribe'),
)
