import pytest

from django.test import Client, RequestFactory
from django.urls import reverse

@pytest.mark.django_db
class TestFighterEndpoint:
    client = Client()
    request = RequestFactory()

    def test_if_we_can_access_api(self):
        # getting a reverse for /api/fighters work using reverse('fighters-list')
        # Why??? Find out!
        response = self.client.get(reverse('fighters-list'))
        assert response.status_code == 200
