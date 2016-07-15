from django.shortcuts import render, redirect

from .forms import EditGraphItemForm
from . import graph_interface as graph


def profile_graph(request):

    context = {
        'resources': graph.Person.get_resources(request.user.id),
        'skills': graph.Person.get_skills(request.user.id),
        'interests': graph.Person.get_interests(request.user.id)
    }

    return render(request, 'registry/profile_graph.html', context)


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

            return redirect('registry:profile_graph')

    context = {'edit_item_form': edit_item_form, 'item_label': item_label}
    return render(request, 'registry/profile_graph_item_create.html', context)


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
        else:
            # validate form and save modified data
            edit_item_form = EditGraphItemForm(data=request.POST)
            if edit_item_form.is_valid():
                item_title = edit_item_form.cleaned_data['title']
                item_metadata = edit_item_form.cleaned_data['metadata']
                loaded_node.update_node_with_data(item_title, item_metadata)
                return redirect('registry:profile_graph')

    if request.method == 'GET':
        initial_data = {'title':loaded_node.title, 'metadata':loaded_node.metadata}
        edit_item_form = EditGraphItemForm(initial=initial_data)

    context.update({'edit_item_form': edit_item_form, 'item_label': item_label})
    return render(request, 'registry/profile_graph_item_edit.html', context)

