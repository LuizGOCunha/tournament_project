import pytest

from django.test import Client, RequestFactory
from django.urls import reverse

from tournament_website.views import addfighter
from tournament_website.models import FighterDjangoModel


@pytest.mark.django_db
class TestAddfighterView:
    client = Client()
    factory = RequestFactory()

    def test_if_view_is_accessible(self, dummy_user, registration_data):
        response = self.client.get(reverse("addfighter"))
        assert (
            response.status_code == 302
        ), "Could not redirect when user is not authenticated"
        self.client.login(
            username=registration_data["username"],
            password=registration_data["password"],
        )
        response = self.client.get(reverse("addfighter"))
        assert response.status_code == 200, "Could not connect to view"

    def test_if_we_can_create_fighter_for_user(self, dummy_user, fighter_django_data):
        request = self.factory.post(
            path=reverse("addfighter"),
            data=fighter_django_data,
        )
        request.user = dummy_user
        addfighter(request)
        assert FighterDjangoModel.objects.count() == 1, "No Fighter object was created"
        fighter = FighterDjangoModel.objects.first()
        assert (
            fighter.name == fighter_django_data["name"]
        ), "Fighters name value is not correct"
        assert (
            fighter.belt == fighter_django_data["belt"]
        ), "Fighters belt value is not correct"
        # Had to convert the value below to float, otherwise it would compare djangos Decimal class to float
        assert (
            float(fighter.weight) == fighter_django_data["weight"]
        ), "Fighters weight value is not correct"
        assert (
            fighter.age == fighter_django_data["age"]
        ), "Fighters age value is not correct"
        assert (
            fighter.sex == fighter_django_data["sex"]
        ), "Fighters sex value is not correct"
