import pytest

from django.test import Client, RequestFactory
from django.urls import reverse

from django.contrib.auth.models import User

@pytest.mark.django_db
class TestFighterEndpoint:
    client = Client()
    request = RequestFactory()

    def test_if_we_can_access_api(self):
        # response = self.client.get(reverse('fighters-list'))
        # getting a reverse for /api/fighters viewset work using reverse('fighters-list')
        # Why??? Find out!
        response = self.client.get(reverse('users-list'))
        assert response.status_code == 200

    def test_if_we_can_return_fighter_data_with_get(self, registration_data, dummy_user):
        response = self.client.get(reverse('users-list'))
        user_db = response.json()[0]
        assert user_db['username'] == registration_data['username']
        assert user_db['first_name'] == registration_data['first_name']
        assert user_db['last_name'] == registration_data['last_name']
        assert user_db['email'] == registration_data['email']

    # Very slow
    def test_if_we_can_retrieve_a_get_request(self, multiple_users):
        pk = 3
        response = self.client.get(reverse('users-list')+f"{pk}/")
        assert response.json()['id'] == pk

    def test_if_we_can_create_a_fighter(self, registration_data):
        response = self.client.post(reverse('users-list'), data={
            'username': "DistinctName",
            'first_name' : registration_data['first_name'], 
            'last_name' : registration_data['last_name'],
            'email' : registration_data['email'], 
        })
        assert response.status_code == 201
        filter = User.objects.filter(username="DistinctName")
        assert len(filter) == 1