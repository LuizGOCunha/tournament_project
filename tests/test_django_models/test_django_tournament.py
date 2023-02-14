import pytest

from tournament_website.models import TournamentDjangoModel


@pytest.mark.django_db
class TestTournamentDjangoModel:
    def test_if_we_can_create_a_tournament_django_model(self):
        name = "Test_Tournament"
        participant_limit = 32
        description = "A great Tournament"
        TournamentDjangoModel.objects.create(
            name=name, participant_limit=participant_limit, description=description
        )
        number_of_objects = TournamentDjangoModel.objects.count()
        assert number_of_objects == 1
        db_tournament = TournamentDjangoModel.objects.first()
        assert db_tournament.name == name
        assert db_tournament.participant_limit == participant_limit
        assert db_tournament.description == description

    def test_if_we_can_create_foreign_key_relationships_with_fighter_object(
        self, tournament_django_object, fighter_django_object
    ):
        tournament = tournament_django_object
        fighter = fighter_django_object
        tournament.participants.add(fighter)
        assert len(tournament.participants.all()) == 1
