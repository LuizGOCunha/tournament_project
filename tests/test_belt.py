from tournament_website.tournament_models.belt import Belt

class TestBeltClass:
    dummy = Belt(0)

    def test_belt_color(self):
        assert self.dummy.return_my_belt() == "White"

    def test_change_color(self):
        self.dummy.change_my_belt(1)
        assert self.dummy.return_my_belt() == "Blue"
