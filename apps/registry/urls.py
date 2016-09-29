from django.conf.urls import url

from apps.registry import views


urlpatterns = [
    url(r'^profile/graph/edit/(?P<item_label>[A-Za-z]+)/$',
        views.profile_graph_item_create,
        name='profile_graph_item_create'),

    url(r'^profile/graph/edit/(?P<item_label>[A-Za-z]+)/(?P<node_id>\d+)/$',
        views.profile_graph_item_edit,
        name='profile_graph_item_edit'),

    url(r'^profile/graph/data/(?P<django_user_id>\d+)$', views.get_personal_graph_json,
        name='personal_graph_json')
]
