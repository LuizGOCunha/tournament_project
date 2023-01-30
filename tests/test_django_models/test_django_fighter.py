import pytest

from tournament_website.models import FighterDjangoModel
from tournament_website.tournament_models.fighter import Fighter
from tournament_website.tournament_models.belt import Belt

@pytest.mark.django_db
class TestFighterDjangoModel:

    def test_if_we_can_create_a_fighter_django_model(self, dummy_user):
        fighter = FighterDjangoModel.objects.create(
            name=(dummy_user.first_name+" "+dummy_user.last_name),
            weight=86.6,
            belt=2,
            age=30,
            sex="M",
            user=dummy_user
        )
        assert FighterDjangoModel.objects.count() == 1, "Fighter could not be created in database"
        assert fighter.user == dummy_user, "Fighter is not related to correct user"
        assert fighter.uid, "Fighter does not have UID"
        assert fighter.user
        assert dummy_user.fighter

    def test_if_we_can_convert_djangomodel_to_tournamentmodel(self, fighter_django_data, fighter_django_object):
        fighterdjango = fighter_django_object
        fightertournament = fighterdjango.convert_to_tournament_model()
        assert type(fightertournament) is Fighter
        assert fightertournament.return_name() == fighterdjango.name
        assert fightertournament.return_weight() == float(fighterdjango.weight)
        assert fightertournament.return_age() == fighterdjango.age
        assert fightertournament.return_sex() == fighterdjango.sex
        # Unnecessarely complicated for testing, yes, but it makes other work easier 
        assert fightertournament.return_belt() == Belt(fighterdjango.belt).return_my_belt()
        assert fightertournament.return_id() == fighterdjango.uid