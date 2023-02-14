import pytest

from django.contrib.auth.models import User
from tournament_website.models import FighterDjangoModel

# Scopes available for fixture:
# "function" - Run once per function
# "class" - Run once per class of tests
# "module" - Run once per module of tests
# "session" - Runs once in the whole session


@pytest.fixture(scope="class")
# the 'db' fixture can be passed when creating a fixture, so we can create a database with it
def registration_data():
    registration_form_data = {
        "first_name": "First Name",
        "last_name": "Last Name",
        "username": "Username",
        "email": "email@test.com",
        "password": "Passw0rd*",
        "password_conf": "Passw0rd*",
    }
    return registration_form_data


@pytest.fixture()
def dummy_user(db, registration_data):
    user = User.objects.create_user(
        first_name=registration_data["first_name"],
        last_name=registration_data["last_name"],
        username=registration_data["username"],
        email=registration_data["email"],
        password=registration_data["password"],
    )
    return user


@pytest.fixture()
def multiple_users(db, registration_data):
    user_list = []
    for n in range(10):
        user = User.objects.create_user(
            first_name=registration_data["first_name"] + f"{n}",
            last_name=registration_data["last_name"] + f"{n}",
            username=registration_data["username"] + f"{n}",
            email=registration_data["email"] + f"{n}",
            password=registration_data["password"] + f"{n}",
        )
        user_list.append(user)
    return user_list


@pytest.fixture()
def fighter_django_data():
    fighter_data = {
        "name": "Fighter Name",
        "weight": 50.3,
        "age": 30,
        "belt": 3,
        "sex": "M",
    }
    return fighter_data


@pytest.fixture()
def fighter_django_object(fighter_django_data):
    fighter = FighterDjangoModel.objects.create(
        name=fighter_django_data["name"],
        weight=fighter_django_data["weight"],
        age=fighter_django_data["age"],
        belt=fighter_django_data["belt"],
        sex=fighter_django_data["sex"],
    )
    return fighter


@pytest.fixture()
def multiple_fighter_django_object(fighter_django_data):
    fighter_list = []
    for fighter in range(10):
        fighter = FighterDjangoModel.objects.create(
            name=fighter_django_data["name"],
            weight=fighter_django_data["weight"],
            age=fighter_django_data["age"],
            belt=fighter_django_data["belt"],
            sex=fighter_django_data["sex"],
        )
        fighter_list.append(fighter)

    return fighter_list
