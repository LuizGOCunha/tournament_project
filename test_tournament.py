from utilities.classes import Tournament, Match, Fighter

class TestFighterClass:
    dummy = Fighter(name="Dummy", weight=80, belt_number=3, age=18, sex="M")

    def test_fighter_info(self):
        assert self.dummy.return_name() == "Dummy"
        assert self.dummy.return_weight() == 80
        assert self.dummy.return_belt() == "Brown"
        assert self.dummy.return_age() == 18
        assert self.dummy.return_sex() == "M" 

    def test_change_name(self):
        self.dummy.change_name("Dummy2")
        assert not self.dummy.return_name() == "Dummy"
        assert self.dummy.return_name() == "Dummy2"

    def test_change_weight(self):
        self.dummy.change_weight(85)
        assert not self.dummy.return_weight() == 80
        assert self.dummy.return_weight() == 85

    def test_change_belt(self):
        self.dummy.change_belt(4)
        assert not self.dummy.return_belt() == "Brown"
        assert self.dummy.return_belt() == "Black"

    def test_change_age(self):
        self.dummy.change_age(25)
        assert not self.dummy.return_age() == 18
        assert self.dummy.return_age() == 25

    def test_change_sex(self):
        self.dummy.change_sex("F")
        assert not self.dummy.return_sex() == "M"
        assert self.dummy.return_sex() == "F"