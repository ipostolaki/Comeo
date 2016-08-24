"""
TODO:
- nouns data separation by semantics
- distinct django app with views to control simulation
- separate graph filling and user's sign up
"""

import random

from faker import Faker

from apps.registry import graph_interface
from comeo_app.models import ComeoUser
from shared.basic_logger import log
from .data import nouns

fake = Faker(locale='en')  # abstract fake data generator


# Users creation

def generate_user_registration_data():
    saved_first_name = fake.first_name()

    return {
        "first_name": saved_first_name,
        "last_name": 'Sim '+fake.last_name(),
        "password": saved_first_name,
        "email": saved_first_name + "@comeo.domain"
    }


def sign_up_user(reg_data):
    try:
        created_user = ComeoUser.objects.create_user(**reg_data)
    except Exception as e:
        # ignore exceptions related to unique constraints
        log("Skipped exception during user sign up: {}".format(e))
        return
    # after successful sign up – create Person node in the graph db
    graph_interface.Person.create_person(created_user.id)

    return created_user


def make_many_users(count):
    for i in range(count):
        user = sign_up_user(generate_user_registration_data())
        if user:
            attach_nodes_to_person_graph(user.id)


# Person's graph filling

def get_random_noun():
    return random.choice(nouns.nouns_list)


def attach_nodes_to_person_graph(user_id, amount_nodes_to_add=3):
    """
    Adds random skills, interests and resources to Person's graph.
    """
    for i in range(amount_nodes_to_add):
        graph_interface.Person.add_skill(user_id, get_random_noun())
        graph_interface.Person.add_resource(user_id, get_random_noun())
        graph_interface.Person.add_interest(user_id, get_random_noun())

