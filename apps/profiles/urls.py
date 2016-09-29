from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views
from . import forms


urlpatterns = [
    url(r'^$', views.profile, name='profile'),
    url(r'^settings/$', views.profile_settings, name='settings'),
    url(r'^public/(?P<django_user_id>[0-9]+)$', views.public_profile, name='public_profile'),

    url(r'^campaigns$', views.profile_campaigns, name='profile_campaigns'),

    # Auth
    url(r'^signup/$', views.signup, name='signup'),

    url(r'^login/$', auth_views.login,
        {'template_name': 'profiles/auth/login.html', 'authentication_form': forms.LoginForm},
        name='login'),

    url(r'^logout/$', auth_views.logout,
        {'template_name': 'profiles/auth/logout.html'}, name='logout'),

    url(r'^password-change/$', auth_views.password_change,
        {'template_name': 'profiles/auth/password_change.html',
         'post_change_redirect': 'profiles:password_change_done'}, name='password_change'),

    url(r'^password_change/done/$', auth_views.password_change_done,
        {'template_name': 'profiles/auth/password_change_done.html'}, name='password_change_done'),

    url(r'^password_reset/$', auth_views.password_reset,
        {'template_name': 'profiles/auth/password_reset.html',
         'post_reset_redirect': 'profiles:password_reset_done',
         'email_template_name': 'profiles/auth/password_reset_email.html'}, name='password_reset'),

    url(r'^password_reset_done/$', auth_views.password_reset_done,
        {'template_name': 'profiles/auth/password_reset_done.html'}, name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {'template_name': 'profiles/auth/password_reset_confirm.html',
         'post_reset_redirect': 'profiles:password_reset_complete'},
        name='password_reset_confirm'),

    url(r'^reset/done/$', auth_views.password_reset_complete,
        {'template_name': 'profiles/auth/password_reset_complete.html'},
        name='password_reset_complete'),
]
