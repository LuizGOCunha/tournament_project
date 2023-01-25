from django.test import Client, RequestFactory
from django.urls import reverse

class TestSignoutView:
    client = Client()

    def test_if_view_is_accessible(self):
        response = self.client.get(reverse("signout"))
        assert response.status_code == 302
        