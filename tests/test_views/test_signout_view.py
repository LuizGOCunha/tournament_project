import pytest

from django.test import Client, RequestFactory
from django.urls import reverse
from django.contrib.auth import login


@pytest.mark.django_db
class TestSignoutView:
    client = Client()
    factory = RequestFactory()

    def test_if_view_is_accessible(self):
        response = self.client.get(reverse("signout"))
        # View ends in a redirection, so it should return 302
        assert response.status_code == 302, "Could not connect to view"

    def test_if_we_can_log_out_user(self, dummy_user, registration_data):
        self.client.login(
            username=registration_data["username"],
            password=registration_data["password"],
        )
        assert self.client.session.session_key, "Session key does not exist"
        self.client.get(reverse("signout"))
        assert (
            not self.client.session.session_key
        ), "Session key exist when it should not"
