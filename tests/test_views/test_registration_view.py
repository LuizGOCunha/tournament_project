from django.test import Client, RequestFactory
from django.urls import reverse

class TestRegistrationView:
    client = Client()

    def test_if_view_is_accessible(self):
        response = self.client.get(reverse("registration"))
        assert response.status_code == 200
        