from django.conf.urls import patterns, url

from registry import views, forms

urlpatterns = [
    url(r'^profile/graph/$', views.profile_graph, name='profile_graph'),
    url(r'^profile/graph/edit/(?P<item_label>[A-Za-z]+)/$',
        views.profile_graph_item_create,
        name='profile_graph_item_create'),

    url(r'^profile/graph/edit/(?P<item_label>[A-Za-z]+)/(?P<node_id>\d+)/$',
        views.profile_graph_item_edit,
        name='profile_graph_item_edit')
    ]
