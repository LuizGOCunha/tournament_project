import pytest

from django.contrib.auth.models import User
from django.test import Client, RequestFactory
from django.urls import reverse

from tournament_website.views import registration

@pytest.mark.django_db
class TestRegistrationView:
    client = Client()
    factory = RequestFactory()

    def test_if_view_is_accessible(self):
        response = self.client.get(reverse("registration"))
        assert response.status_code == 200
    
    def test_to_see_if_we_can_create_user(self, registration_data):
        request = self.factory.post(path=reverse('registration'), data=registration_data)
        response = registration(request)
        assert User.objects.count() == 1

    def test_the_data_from_our_created_user(self, registration_data):
        pass
        # assert User.objects.count() == 1
        