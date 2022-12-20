from model.fighter import Fighter
from model.category import Category

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

    def test_if_its_possible_to_resolve_matches_one_by_one(self):
        tdf1 = Fighter("tripledummy1", 99.9, 0, 30, "F")
        tdf2 = Fighter("tripledummy2", 99.9, 0, 30, "F")
        tdf3 = Fighter("tripledummy3", 99.9, 0, 30, "F")
        fighters_list = [tdf1, tdf2, tdf3]
        dcategory2 = Category(fighters_list)
        dcategory2.create_matches()
        dcategory2.resolve_next_match(1)
        winner_of_the_first_match = dcategory2.return_matches()[0].return_winner()
        # Match 1: fighter1 (tdf1) wins
        assert winner_of_the_first_match.return_id() == tdf1.return_id()
        dcategory2.resolve_next_match(2)
        winner_of_the_second_match = dcategory2.return_matches()[1].return_winner()
        # Match 2: tdf3 fights the loser of the previous match (tdf2), tdf2 wins
        assert winner_of_the_second_match.return_id() == tdf2.return_id() 

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

