from django.test import Client, RequestFactory
from django.urls import reverse

class TestIndexView:
    client = Client()
    factory = RequestFactory()

    def test_if_view_is_accessible(self):
        response = self.client.get(reverse("index"))
        assert response.status_code == 200

    # Test if we are able to create a user, log the user in,
    # we can logout and if user has correct info

        
    