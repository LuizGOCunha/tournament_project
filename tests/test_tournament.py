from model.fighter import Fighter
from model.tournament import Tournament
from model.category import Category

class TestTournamentClass:
    df1 = Fighter(name="df1", weight=50, belt_number=0, age=20, sex="M")
    df2 = Fighter(name="df2", weight=50, belt_number=0, age=20, sex="M")
    df3 = Fighter(name="df3", weight=50, belt_number=0, age=20, sex="M")
    df4 = Fighter(name="df4", weight=50, belt_number=0, age=20, sex="M")
    df5 = Fighter(name="df5", weight=60, belt_number=0, age=20, sex="M")
    df6 = Fighter(name="df6", weight=60, belt_number=0, age=20, sex="M")
    df7 = Fighter(name="df7", weight=60, belt_number=0, age=20, sex="M")
    df8 = Fighter(name="df8", weight=80, belt_number=0, age=20, sex="M")
    df9 = Fighter(name="df9", weight=80, belt_number=0, age=20, sex="M")
    df10 = Fighter(name="df10", weight=80, belt_number=4, age=30, sex="F")
    df11 = Fighter(name="df11", weight=80, belt_number=4, age=30, sex="F")
    df12 = Fighter(name="df12", weight=80, belt_number=3, age=30, sex="F")
    df13 = Fighter(name="df13", weight=80, belt_number=3, age=30, sex="F")
    df14 = Fighter(name="df14", weight=80, belt_number=3, age=30, sex="F")
    df15 = Fighter(name="df15", weight=80, belt_number=2, age=30, sex="F")
    df16 = Fighter(name="df16", weight=80, belt_number=2, age=30, sex="F")
    df17 = Fighter(name="df17", weight=80, belt_number=2, age=30, sex="F")
    df18 = Fighter(name="df18", weight=80, belt_number=2, age=30, sex="F")
    fighter_list = [df1,df2,df3,df4,df5,df6,df7,df8,df9]
    absolute_fighter_list = [df10,df11,df12,df13,df14,df15,df16,df17,df18]
    dtournament = Tournament(fighter_list, absolute_fighter_list)

    def test_if_determine_category_returns_right_category(self):
        category = self.dtournament.determine_category(self.df1)
        assert category == "M-Adult-Rooster-White"
        category = self.dtournament.determine_category(self.df5)
        assert category == "M-Adult-LightFeather-White"
        category = self.dtournament.determine_category(self.df8)
        assert category == "M-Adult-Middle-White"

    def test_weight_class_check_female_adult(self):
        assert self.dtournament.check_weight_class_female(40) == "Rooster"
        assert self.dtournament.check_weight_class_female(50) == "LightFeather"
        assert self.dtournament.check_weight_class_female(55) == "Feather"
        assert self.dtournament.check_weight_class_female(60) == "Light"
        assert self.dtournament.check_weight_class_female(65) == "Middle"
        assert self.dtournament.check_weight_class_female(70) == "MediumHeavy"
        assert self.dtournament.check_weight_class_female(75) == "Heavy"
        assert self.dtournament.check_weight_class_female(80) == "SuperHeavy"

    def test_weight_class_check_male_adult(self):
        assert self.dtournament.check_weight_class_male(55) == "Rooster"
        assert self.dtournament.check_weight_class_male(60) == "LightFeather"
        assert self.dtournament.check_weight_class_male(65) == "Feather"
        assert self.dtournament.check_weight_class_male(70) == "Light"
        assert self.dtournament.check_weight_class_male(80) == "Middle"
        assert self.dtournament.check_weight_class_male(85) == "MediumHeavy"
        assert self.dtournament.check_weight_class_male(90) == "Heavy"
        assert self.dtournament.check_weight_class_male(95) == "SuperHeavy"
        assert self.dtournament.check_weight_class_male(105) == "UltraHeavy"

    def test_weight_class_check_female_juvenile(self):
        assert self.dtournament.check_weight_class_juvenile_female(40) == "Rooster"
        assert self.dtournament.check_weight_class_juvenile_female(45) == "LightFeather"
        assert self.dtournament.check_weight_class_juvenile_female(50) == "Feather"
        assert self.dtournament.check_weight_class_juvenile_female(55) == "Light"
        assert self.dtournament.check_weight_class_juvenile_female(60) == "Middle"
        assert self.dtournament.check_weight_class_juvenile_female(64) == "MediumHeavy"
        assert self.dtournament.check_weight_class_juvenile_female(68) == "Heavy"
        assert self.dtournament.check_weight_class_juvenile_female(70) == "SuperHeavy"

    def test_weight_class_check_male_juvenile(self):
        assert self.dtournament.check_weight_class_juvenile_male(50) == "Rooster"
        assert self.dtournament.check_weight_class_juvenile_male(55) == "LightFeather"
        assert self.dtournament.check_weight_class_juvenile_male(60) == "Feather"
        assert self.dtournament.check_weight_class_juvenile_male(65) == "Light"
        assert self.dtournament.check_weight_class_juvenile_male(70) == "Middle"
        assert self.dtournament.check_weight_class_juvenile_male(75) == "MediumHeavy"
        assert self.dtournament.check_weight_class_juvenile_male(80) == "Heavy"
        assert self.dtournament.check_weight_class_juvenile_male(85) == "SuperHeavy"
        assert self.dtournament.check_weight_class_juvenile_male(90) == "UltraHeavy"

    def test_age_class_check(self):
        assert self.dtournament.check_age_class(16) == "Juvenile"
        assert self.dtournament.check_age_class(25) == "Adult"
        assert self.dtournament.check_age_class(34) == "Master"
        assert self.dtournament.check_age_class(45) == "Senior"

    def test_if_the_categories_have_been_appropriately_established(self):
        category_dict = self.dtournament.return_active_categories()
        assert type(category_dict) == dict
        categories = tuple(self.dtournament.return_active_categories().keys())
        assert categories == ("M-Adult-Rooster-White", "M-Adult-LightFeather-White", "M-Adult-Middle-White")
        rooster_category = tuple(category_dict["M-Adult-Rooster-White"])
        assert rooster_category == (self.df1, self.df2, self.df3, self.df4)
        lightfeather_category = tuple(category_dict["M-Adult-LightFeather-White"])
        assert lightfeather_category == (self.df5, self.df6, self.df7)
        middle_category = tuple(category_dict["M-Adult-Middle-White"])
        assert middle_category == (self.df8, self.df9)

    def test_if_the_absolute_categories_have_been_appropriately_established(self):
        category_dict = self.dtournament.return_active_absolute_categories()
        assert type(category_dict) == dict
        categories = tuple(self.dtournament.return_active_absolute_categories().keys())
        print(categories)
        assert categories == ("F-Master-Absolute-Black", "F-Master-Absolute-Brown", "F-Master-Absolute-Purple")
        blackbelt_category = category_dict["F-Master-Absolute-Black"]
        assert blackbelt_category == [self.df10,self.df11]
        brownbelt_category = category_dict["F-Master-Absolute-Brown"]
        assert brownbelt_category == [self.df12,self.df13,self.df14]
        purplebelt_category = category_dict["F-Master-Absolute-Purple"]
        assert purplebelt_category == [self.df15,self.df16,self.df17,self.df18]

    def test_if_we_can_create_category_objects_in_category_dict(self):
        self.dtournament.create_category_objects()
        category_dict = self.dtournament.return_active_categories()
        for category in category_dict.values():
            assert type(category) == Category