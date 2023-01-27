import pytest

from tournament_website.models import FighterDjangoModel

class TestFighterDjangoModel:

    @pytest.mark.django_db
    def test_if_we_can_create_a_fighter_django_model(self, dummy_user):
        fighter = FighterDjangoModel.objects.create(
            name=(dummy_user.first_name+" "+dummy_user.last_name),
            weight=86.6,
            belt=2,
            age=30,
            sex="M",
            user=dummy_user
        )
        fighter.save()
        assert FighterDjangoModel.objects.count() == 1, "Fighter could not be created in database"
        assert fighter.user == dummy_user, "Fighter is not related to correct user"
        assert fighter.uid, "Fighter does not have UID"