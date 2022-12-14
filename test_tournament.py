import uuid
from utilities.classes import Tournament, Category, Match, Fighter, Belt

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

    def test_uid(self):
        id = uuid.uuid4()
        fighter = Fighter("dummy", 90.0, 2, 80, "M", uid = id)
        assert fighter.return_id() == id 

class TestMatchClass:
    dummy1 = Fighter("Dummy1", 80, 1, 30, "M")
    dummy2 = Fighter("Dummy2", 81, 1, 32, "M")
    ready_match = Match(dummy1, dummy2)
    not_ready_match = Match(dummy1)

    def test_if_we_can_call_to_return_fighters(self):
        # rm = ready_match
        rm_fighters = self.ready_match.return_fighters()
        # nrm = not_ready_match
        nrm_fighters = self.not_ready_match.return_fighters()
        assert rm_fighters == (self.dummy1, self.dummy2)
        assert nrm_fighters == (self.dummy1,)

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
    df5 = Fighter("dummy5", 50.5, 3, 54, "F")
    df6 = Fighter("dummy6", 50.6, 3, 55, "F")
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
        self.dcategory.add_fighter(self.df5, self.df6)
        assert self.dcategory.return_fighters() == [self.df4, self.df5, self.df6]

    def test_if_we_can_create_proper_matches(self):
        self.dcategory.create_matches()
        matches = self.dcategory.return_matches()
        # Test if we have two matches, as it should
        assert len(matches) == 2
        # Test if we are dealing with the same fighters in those matches
        first_fighter_of_first_match = matches[0].return_fighters()[0]
        second_fighter_of_first_match = matches[0].return_fighters()[1]
        first_fighter_of_second_match = matches[1].return_fighters()[0]
        assert first_fighter_of_first_match.return_id() == self.df4.return_id()
        assert second_fighter_of_first_match.return_id() == self.df5.return_id()
        assert first_fighter_of_second_match.return_id() == self.df6.return_id()

    def test_if_its_possible_to_impose_list_of_fighters_to_create_matches(self):
        ddcategory = Category()
        ddf1 = Fighter("doubledummy1", 99.9, 0, 30, "F")
        ddf2 = Fighter("doubledummy2", 99.9, 0, 30, "F")
        ddcategory.create_matches([ddf1, ddf2])
        assert len(ddcategory.return_matches()) == 1
        fighters = ddcategory.return_matches()[0].return_fighters()
        fighter1 = fighters[0]
        fighter2 = fighters[1]
        assert fighter1.return_id() == ddf1.return_id()
        assert fighter2.return_id() == ddf2.return_id()

    def test_if_its_possible_to_resolve_the_matches(self):
        # We have 2 matches on our category, we give the winning numbers to the method, starting on the first match
        self.dcategory.resolve_category(1,2)
        winner_of_the_first_match = self.dcategory.return_matches()[0].return_winner()
        winner_of_the_second_match = self.dcategory.return_matches()[1].return_winner()
        # Match 1: df4 is the winner
        # Match 2: df6 is alone on an unready match, it will fight the loser of the match before, df5 wins
        assert winner_of_the_first_match.return_id() == self.df4.return_id()
        assert winner_of_the_second_match.return_id() == self.df5.return_id()

    def test_if_its_possible_to_advance_to_next_phase(self):
        self.dcategory.advance_category()
        matches = self.dcategory.return_matches()
        assert len(matches) == 1
        first_fighter_of_finals = matches[0].return_fighters()[0]
        second_fighter_of_finals = matches[0].return_fighters()[1]
        assert first_fighter_of_finals.return_id() == self.df4.return_id()
        assert second_fighter_of_finals.return_id() == self.df5.return_id()

    def test_if_we_can_resolve_the_finals_and_check_for_winner(self):
        self.dcategory.resolve_category(1)
        self.dcategory.check_for_winner()
        assert self.dcategory.is_resolved() == True
        assert self.dcategory.return_winner().return_id() == self.df4.return_id()


class TestTournamentClass:
    df1 = Fighter(name="df1", weight="50", belt_number=0, age=20, sex="M")
    df2 = Fighter(name="df2", weight="50", belt_number=0, age=20, sex="M")
    df3 = Fighter(name="df3", weight="50", belt_number=0, age=20, sex="M")
    df4 = Fighter(name="df4", weight="50", belt_number=0, age=20, sex="M")
    df5 = Fighter(name="df5", weight="60", belt_number=0, age=20, sex="M")
    df6 = Fighter(name="df6", weight="60", belt_number=0, age=20, sex="M")
    df7 = Fighter(name="df7", weight="60", belt_number=0, age=20, sex="M")
    df8 = Fighter(name="df8", weight="80", belt_number=0, age=20, sex="M")
    df9 = Fighter(name="df9", weight="80", belt_number=0, age=20, sex="M")
    dtournament = Tournament()

    


        

        

