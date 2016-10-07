import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.cache import cache

from apps.profiles.models import ComeoUser
from . import graph_interface as graph
from .forms import EditGraphItemForm


@login_required
def profile_graph_item_create(request, item_label):
    """
    Abstract view to create one of: Resource, Skill, Interest
    :param item_label: type of node to create
    """
    edit_item_form = EditGraphItemForm(data=request.POST or None)

    if request.method == 'POST':
        if edit_item_form.is_valid():
            item_title = edit_item_form.cleaned_data['title']
            item_metadata = edit_item_form.cleaned_data['metadata']

            if item_label == 'skill':
                graph.Person.add_skill(request.user.id, item_title, item_metadata)
            if item_label == 'resource':
                graph.Person.add_resource(request.user.id, item_title, item_metadata)
            if item_label == 'interest':
                graph.Person.add_interest(request.user.id, item_title, item_metadata)

            # invalidate cached personal graph data
            cache.delete(get_personal_cache_key(request.user.id))

            return redirect('profiles:profile')

    context = {'edit_item_form': edit_item_form, 'item_label': item_label}
    return render(request, 'registry/profile_graph_item_create.html', context)


@login_required
def profile_graph_item_edit(request, item_label, node_id):
    """
    Abstract view to edit one of: Resource, Skill, Interest

    :param item_label: type of node to edit
    :param node_id: unique identifier of a node in the neo4j database
    """
    node_class = graph.get_node_class_by_label(item_label)

    # load node of given kind from neo db
    loaded_node = node_class.get_by_id(node_id)

    context = {'loaded_node': loaded_node}

    if request.method == 'POST':
        if request.POST.get("delete", False):
            loaded_node.delete()
            cache.delete(get_personal_cache_key(request.user.id))  # invalidate cached personal graph data
            return redirect('profiles:profile')
        else:
            # validate form and save modified data
            edit_item_form = EditGraphItemForm(data=request.POST)
            if edit_item_form.is_valid():
                item_title = edit_item_form.cleaned_data['title']
                item_metadata = edit_item_form.cleaned_data['metadata']
                loaded_node.update_node_with_data(item_title, item_metadata)
                cache.delete(get_personal_cache_key(request.user.id))  # invalidate cached personal graph data
                return redirect('profiles:profile')

    if request.method == 'GET':
        initial_data = {'title': loaded_node.title, 'metadata': loaded_node.metadata}
        edit_item_form = EditGraphItemForm(initial=initial_data)

    context.update({'edit_item_form': edit_item_form, 'item_label': item_label})
    return render(request, 'registry/profile_graph_item_edit.html', context)


def get_personal_graph_json(request, django_user_id):
    cached_graph_data = cache.get(get_personal_cache_key(django_user_id))
    if cached_graph_data is None:
        graph_data = retrieve_personal_graph_ui_data(django_user_id)
        cache.set(get_personal_cache_key(django_user_id), graph_data)
        return_graph_data = graph_data
    else:
        return_graph_data = cached_graph_data

    return HttpResponse(return_graph_data, content_type='application/json')


# –––––––––– Helpers ––––––––––

def get_personal_cache_key(django_user_id):
    key_base = 'personal_graph_data'
    return key_base + str(django_user_id)


def retrieve_personal_graph_ui_data(django_user_id):
    """
    This method prepares data needed for d3.js to render personal graph visualization

    There are base nodes and links, which should be displayed for every person.
    D3.js graph data notation:
        "id" – used both as identifier and as text which will be rendered
        "group" – used for colouring of nodes of the same kind
    """

    """
    TODO:
    - id's separated from labels/titles
    - colouring based on type of node instead of group
    - localize base nodes labels
    """
    RESOURCES_LABEL = "Resources"
    SKILLS_LABEL = "Skills"
    INTERESTS_LABEL = "Interests"

    user = ComeoUser.objects.get(id=django_user_id)
    person_name = user.get_full_name()

    base_nodes = [
        {"id": person_name, "group": 0, "type": "person"},
        {"id": RESOURCES_LABEL, "group": 1, "type": "asset"},
        {"id": SKILLS_LABEL, "group": 2, "type": "asset"},
        {"id": INTERESTS_LABEL, "group": 3, "type": "asset"}
    ]
    base_links = [
        {"source": person_name, "target": RESOURCES_LABEL},
        {"source": person_name, "target": SKILLS_LABEL},
        {"source": person_name, "target": INTERESTS_LABEL}
    ]

    skills = graph.Person.get_skills(user.id)
    for skill in skills:
        skill_node = {"id": skill.title, "group": 4}
        skill_link = {"source": SKILLS_LABEL, "target": skill.title}
        base_nodes.append(skill_node)
        base_links.append(skill_link)

    interests = graph.Person.get_interests(user.id)
    for interest in interests:
        interest_node = {"id": interest.title, "group": 5}
        interest_link = {"source": INTERESTS_LABEL, "target": interest.title}
        base_nodes.append(interest_node)
        base_links.append(interest_link)

    resources = graph.Person.get_resources(user.id)
    for resource in resources:
        resource_node = {"id": resource.title, "group": 0}
        resource_link = {"source": RESOURCES_LABEL, "target": resource.title}
        base_nodes.append(resource_node)
        base_links.append(resource_link)

    graph_data = {"nodes": base_nodes, "links": base_links}

    return json.dumps(graph_data)
