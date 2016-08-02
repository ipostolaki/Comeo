from django.test import TestCase, SimpleTestCase

from comeo_app.models import ComeoUser

from . import users_generator as ug

from registry import graph_interface


class TestUserGenerator(TestCase):

    def test_generate_user_registration_data(self):
        """ Checks that data generated for new user is consistent """
        data = ug.generate_user_registration_data()

        # passwords for simulated users should equal their first name
        self.assertEqual(data['first_name'], data['password'])

        # email for simulated user should be firstname@comeo.domain
        splitted_email = data['email'].split("@")
        self.assertEqual(splitted_email[0], data['first_name'])

    def test_sign_up_user(self):
        """ Checks that user is created and persisted """
        mock_first_name = "mock_first_name"
        data = {
            "first_name": mock_first_name,
            "last_name": "mock_last_name",
            "password": mock_first_name,
            "email": mock_first_name + "@comeo.domain"
        }
        ug.sign_up_user(data)
        loaded_user = ComeoUser.objects.get(first_name=mock_first_name)
        loaded_person = graph_interface.Person.get_by_django_id(loaded_user.id)
        self.assertTrue(loaded_user)
        self.assertTrue(loaded_person)

    def test_smoke_make_many_users(self):
        ug.make_many_users(3)


class TestGraphFilling(SimpleTestCase):

    def test_get_random_noun(self):
        noun = ug.get_random_noun()
        self.assertIsInstance(noun, str)

