from django.test import Client, RequestFactory
from django.urls import reverse

class TestSigninView:
    client = Client()
    factory = RequestFactory()

    def test_if_view_is_accessible(self):
        response = self.client.get(reverse("signin"))
        assert response.status_code == 200, "Could not connect to view"

    def test_if_we_can_sign_user_in(self, dummy_user, registration_data):
        response = self.client.post(path=reverse("signin"), data={
            'username': registration_data['username'],
            'password': registration_data['password']
        })
        # If signin is successful, user is redirected to the home page, returning a 302
        assert response.status_code == 302, "Failed to redirect"
        assert self.client.session.session_key, "Failed to sign in"
        