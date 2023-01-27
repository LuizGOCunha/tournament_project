import pytest
from django.contrib.auth.models import User

# Scopes available for fixture:
# "function" - Run once per function
# "class" - Run once per class of tests
# "module" - Run once per module of tests
# "session" - Runs once in the whole session

@pytest.fixture(scope="class")
# the 'db' fixture can be passed when creating a fixture, so we can create a database with it
def registration_data():
    registration_form_data = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'username': 'Username',
            'email': 'email@test.com',
            'password': 'Passw0rd*',
            'password_conf': 'Passw0rd*'
    }
    print('******************************')
    return registration_form_data

@pytest.fixture()
def dummy_user(db, registration_data):
    user = User.objects.create_user(
        first_name=registration_data['first_name'],
        last_name=registration_data['last_name'],
        username=registration_data['username'],
        email=registration_data['email'],
        password=registration_data['password'],
    )
    return user