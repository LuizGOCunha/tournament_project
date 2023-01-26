import pytest

from django.contrib.auth.models import User
from django.test import Client, RequestFactory
from django.urls import reverse

from tournament_website.views import registration

# It would be better if we can find a way to keep the same db between tests
# So the setup doesnt slow us down everytime
@pytest.mark.django_db
class TestRegistrationView:
    client = Client()
    factory = RequestFactory()

    def test_if_view_is_accessible(self):
        response = self.client.get(reverse("registration"))
        assert response.status_code == 200, "Could not access page"
    
    def test_to_see_if_we_can_create_user_with_correct_info(self, registration_data):
        request = self.factory.post(path=reverse('registration'), data=registration_data)
        response = registration(request)
        assert User.objects.count() == 1, "New user was not created"
        user = User.objects.first()
        assert user.first_name == registration_data['first_name'], "User's first name isn't correct"
        assert user.last_name == registration_data['last_name'], "User's last name isn't correct"
        assert user.username == registration_data['username'], "User's username isn't correct"
        assert user.email == registration_data['email'], "User's email isn't correct"
        # Django does not allow us to return user password plain, for security reasons
        # So we have to use check_password User method
        assert user.check_password(registration_data['password']), "User's password isn't correct"

    def test_to_see_if_we_can_correctly_handle_integrityerror(self, registration_data):
        request = self.factory.post(path=reverse('registration'), data=registration_data)
        response = registration(request)
        # If the POST request is successful, it redirects to login page, returning 302
        assert response.status_code == 302
        # Send the request again, with the same data, so it should raise an integrityerror
        response = registration(request)
        # If the POST request fails, it will reload the page, returning 200
        assert response.status_code == 200

    
        