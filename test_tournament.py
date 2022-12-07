from utilities.classes import Category, Match, Fighter, Belt

class TestBeltClass:
    dummy = Belt(0)

    def test_belt_color(self):
        assert self.dummy.return_my_belt() == "White"

    def test_change_color(self):
        self.dummy.change_my_belt(1)
        assert self.dummy.return_my_belt() == "Blue"


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

class TestMatchClass:
    dummy1 = Fighter("Dummy1", 80, 1, 30, "M")
    dummy2 = Fighter("Dummy2", 81, 1, 32, "M")
    ready_match = Match(dummy1, dummy2)
    not_ready_match = Match(dummy1)

    def test_if_match_is_ready(self):
        assert self.ready_match.is_ready() == True
        assert self.not_ready_match.is_ready() == False

    def test_if_resolving_match_is_possible(self):
        assert self.ready_match.is_resolved() == False
        self.ready_match.resolve_match(1)
        assert self.ready_match.is_resolved() == True
        assert self.ready_match.return_winner() == self.dummy1

    def test_if_we_can_add_fighter_then_resolve_match(self):
        dummy3 = Fighter("Dummy3", 82.3, 1, 34, "M")
        self.not_ready_match.add_fighter(dummy3)
        assert self.not_ready_match.is_ready() == True
        self.not_ready_match.resolve_match(2)
        assert self.not_ready_match.is_resolved() == True
        assert self.not_ready_match._winner == dummy3

class TestCategoryClass:
    # df = dummy_fighter
    df1 = Fighter("dummy1", 50.1, 3, 50, "F")
    df2 = Fighter("dummy2", 50.2, 3, 51, "F")
    df3 = Fighter("dummy3", 50.3, 3, 52, "F")
    df4 = Fighter("dummy4", 50.4, 3, 53, "F")
    print(df1, df2, df3, df4)
    fighter_list = [df1, df2, df3, df4]
    dcategory = Category(fighter_list)

    def test_if_its_possible_to_return_fighters(self):
        assert self.dcategory.return_fighters() == [self.df1, self.df2, self.df3, self.df4]

    def test_if_its_possible_to_remove_fighter(self):
        self.dcategory.remove_fighter(self.df1, self.df2)
        assert self.dcategory.return_fighters() == [self.df3, self.df4]
        self.dcategory.remove_fighter(self.df3)
        assert self.dcategory.return_fighters() == [self.df4,]

    def test_if_its_possible_to_add_fighter(self):
        self.df5 = Fighter("dummy5", 50.5, 3, 54, "F")
        self.df6 = Fighter("dummy6", 50.6, 3, 55, "F")
        self.dcategory.add_fighter(self.df5, self.df6)
        assert self.dcategory.return_fighters() == [self.df4, self.df5, self.df6]

    def test_if_we_can_create_proper_matches(self):
        self.dcategory.create_matches()
        assert self.dcategory.return_fighters() == []
        assert self.dcategory.__str__() == (
            Match(self.df2, self.df3).__str__() + "\n" + Match(self.df4, self.df5).__str__() + "\n"
        )

