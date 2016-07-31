from comeo_app.models import ComeoUser
from faker import Faker


fake = Faker()  # abstract fake data generator


def generate_user_registration_data():
    saved_first_name = fake.first_name()

    return {
        "first_name": saved_first_name,
        "last_name": fake.last_name(),
        "password": saved_first_name,
        "email": saved_first_name + "@comeo.domain"
    }


def sign_up_user(reg_data):
    created_user = ComeoUser.objects.create_user(**reg_data)
    # here add user to the graph db
    return created_user
