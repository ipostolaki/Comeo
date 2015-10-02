from django.conf.urls import patterns, url

from comeo_app import views, forms

urlpatterns = patterns(
    '',
    # Base
    url(r'^$', views.home, name='home'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^about/$', views.about, name='about'),
    url(r'^ro/$', views.ro, name='ro'),

    # Campaigns
    url(r'^campaigns/$', views.campaigns_public, name='campaigns_public'),
    url(r'^campaigns/(?P<pk>\d+)/$', views.campaign_details, name='campaign_details'),
    url(r'^campaigns/donate/(?P<pk>\d+)/$', views.campaign_donate, name='campaign_donate'),
    url(r'^campaigns/donate_instruction/transaction_pk=(?P<transaction_pk>\d+)&campaign_pk=(?P<campaign_pk>\d+)/$',  # noqa flake8
        views.donate_instruction, name='donate_instruction'),

    # Mail
    url(r'^email-subscribe/$', views.email_subscribe, name='email_subscribe'),

    # Profile
    url(r'^profile/campaigns/create$', views.campaign_create, name='campaign_create'),
    url(r'^profile/campaigns/publish$/(?P<pk>\d+)/', views.campaign_edit, name='campaign_publish'),
    url(r'^profile/campaigns$', views.profile_campaigns, name='profile_campaigns'),
    url(r'^profile/campaigns/(?P<pk>\d+)/$', views.campaign_edit, name='campaign_edit'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.profile_edit, name='profile_edit'),

    # Auth
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'comeo_app/auth/login.html', 'authentication_form': forms.LoginForm},
        name='login'),

    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'comeo_app/auth/logout.html'}, name='logout'),

    url(r'^password-change/$', 'django.contrib.auth.views.password_change',
        {'template_name': 'comeo_app/auth/password_change.html',
         'post_change_redirect': 'comeo_app:password_change_done'}, name='password_change'),

    url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done',
        {'template_name': 'comeo_app/auth/password_change_done.html'}, name='password_change_done'),

    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset',
        {'template_name': 'comeo_app/auth/password_reset.html',
         'post_reset_redirect': 'comeo_app:password_reset_done',
         'email_template_name': 'comeo_app/auth/password_reset_email.html'}, name='password_reset'),

    url(r'^password_reset_done/$', 'django.contrib.auth.views.password_reset_done',
        {'template_name': 'comeo_app/auth/password_reset_done.html'}, name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'template_name': 'comeo_app/auth/password_reset_confirm.html',
         'post_reset_redirect': 'comeo_app:password_reset_complete'},
        name='password_reset_confirm'),

    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'comeo_app/auth/password_reset_complete.html'},
        name='password_reset_complete'),
    )
