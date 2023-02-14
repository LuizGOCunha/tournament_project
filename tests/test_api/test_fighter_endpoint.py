import pytest

from django.test import Client, RequestFactory
from django.urls import reverse

from tournament_website.models import FighterDjangoModel


@pytest.mark.django_db
class TestFighterEndpoint:
    client = Client()
    request = RequestFactory()

    def test_if_we_can_access_api(self):
        # response = self.client.get(reverse('fighters-list'))
        # getting a reverse for /api/fighters viewset work using reverse('fighters-list')
        # Why??? Find out!
        response = self.client.get(reverse("fighters-list"))
        assert response.status_code == 200

    def test_if_we_can_return_fighter_data_with_get(
        self, fighter_django_data, fighter_django_object
    ):
        response = self.client.get(reverse("fighters-list"))
        fighter_db = response.json()[0]
        assert fighter_db["name"] == fighter_django_data["name"]
        # Here we need to turn all into the same data type just like before \/
        assert float(fighter_db["weight"]) == float(fighter_django_data["weight"])
        assert fighter_db["sex"] == fighter_django_data["sex"]
        assert fighter_db["age"] == fighter_django_data["age"]
        assert fighter_db["belt"] == fighter_django_data["belt"]

    def test_if_we_can_retrieve_a_get_request(self, multiple_fighter_django_object):
        pk = 3
        response = self.client.get(reverse("fighters-list") + f"{pk}/")
        assert response.json()["id"] == pk

    def test_if_we_can_create_a_fighter(self, fighter_django_data):
        response = self.client.post(
            reverse("fighters-list"),
            data={
                "name": "Distinct Name",
                "weight": fighter_django_data["weight"],
                "sex": fighter_django_data["sex"],
                "age": fighter_django_data["age"],
                "belt": fighter_django_data["belt"],
            },
        )
        assert response.status_code == 201
        filter = FighterDjangoModel.objects.filter(name="Distinct Name")
        assert len(filter) == 1
