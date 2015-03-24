from django.conf.urls import patterns, url
from comeo_app import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.profile_edit, name='profile_edit'),
    #auth
    # url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),

    url(r'^password_change/$', 'django.contrib.auth.views.password_change',
        {'template_name': 'comeo_app/auth/password_change.html', 'post_change_redirect': 'comeo_app:password_change_done'},
        name='password_change'),

    url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done',
        {'template_name': 'comeo_app/auth/password_change_done.html'},
        name='password_change_done'),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'comeo_app/auth/login.html'}, name='login'),

    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset',
        {'template_name': 'comeo_app/auth/password_reset.html',
         'post_reset_redirect': 'comeo_app:password_reset_done',
         'email_template_name': 'comeo_app/auth/password_reset_email.html'},
        name='password_reset'),

    url(r'^password_reset_done/$', 'django.contrib.auth.views.password_reset_done',
        {'template_name': 'comeo_app/auth/password_reset_done.html'},
        name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'template_name': 'comeo_app/auth/password_reset_confirm.html',
         'post_reset_redirect': 'comeo_app:password_reset_complete'},
        name='password_reset_confirm'),

    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', {'template_name': 'comeo_app/auth/password_reset_complete.html'}, name='password_reset_complete'),
    )

