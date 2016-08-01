"""
This module manages connection to neo4j database to store and retrieve data related to Person's
graph.
Every Person(django user) is related to these primary entities:
- Resource
- Skill
- InterestTag

Thread safe connection and sessions needed to access
neo4j database are managed by "neomodel" package.
An env var NEO4J_REST_URL is needed to establish connection.
"""

"""
# TODO:
- Exceptions handling
- Transactions support, when connecting nodes
"""

from neomodel import StructuredNode, StringProperty, RelationshipTo


class CommonMixin:

    metadata = StringProperty(required=True)

    def get_node_id(self):
        # this may be used to access value in the templates
        return self._id

    def update_node_with_data(self, title, metadata):
        self.title = title
        self.metadata = metadata
        self.save()

    @classmethod
    def get_by_id(cls, node_id):
        node_to_find = cls(_id=int(node_id))
        node_to_find.refresh()  # this will load node with given _id from neo db
        return node_to_find


class Resource(StructuredNode, CommonMixin):
    title = StringProperty(required=True)


class Skill(StructuredNode, CommonMixin):
    title = StringProperty(required=True)


class InterestTag(StructuredNode, CommonMixin):
    """
    Data contained in this node should be crowdsourced.
    Any Person may tag other person's interest, and merge it into it's own graph.
    """
    title = StringProperty(required=True)


class Person(StructuredNode):
    # django_user_id property is used as Primary Key to bind
    # postgreSQL django auth system with neo4j graph db
    django_user_id = StringProperty(unique_index=True, required=True)

    resources = RelationshipTo(Resource, 'OWNS')
    skills = RelationshipTo(Skill, 'CAN_DO')
    interests = RelationshipTo(InterestTag, 'INTERESTED')

    @classmethod
    def create_person(cls, django_user_id):
        Person(django_user_id=django_user_id).save()

    @classmethod
    def get_by_django_id(cls, django_user_id):
        """
        :param name: django user id
        :return: neomodel Person instance
        """
        return cls.nodes.get(django_user_id=django_user_id)

    @classmethod
    def add_skill(cls, user_id, title, metadata):
        new_skill = Skill(title=title, metadata=metadata).save()
        person = cls.get_by_django_id(user_id)
        person.skills.connect(new_skill)
        
    @classmethod
    def add_resource(cls, user_id, title, metadata):
        new_resource = Resource(title=title, metadata=metadata).save()
        person = cls.get_by_django_id(user_id)
        person.resources.connect(new_resource)

    @classmethod
    def add_interest(cls, user_id, title, metadata):
        new_interest = InterestTag(title=title, metadata=metadata).save()
        person = cls.get_by_django_id(user_id)
        person.interests.connect(new_interest)

    @classmethod
    def get_skills(cls, user_id):
        person = cls.get_by_django_id(user_id)
        skills_list = [skill for skill in person.skills.all()]
        return skills_list

    @classmethod
    def get_resources(cls, user_id):
        person = cls.get_by_django_id(user_id)
        resources_list = [resource for resource in person.resources.all()]
        return resources_list

    @classmethod
    def get_interests(cls, user_id):
        person = cls.get_by_django_id(user_id)
        interests_list = [interest for interest in person.interests.all()]
        return interests_list


class Groups(StructuredNode):
    """
    Person may belong to many groups.
    Thus some persons may have ability to limit access to their profile graph data only to
    specific groups.
    """


#### Utils

def get_node_class_by_label(item_label):
    if item_label == 'skill':
        return Skill
    elif item_label == 'resource':
        return Resource
    elif item_label == 'interest':
        return InterestTag


