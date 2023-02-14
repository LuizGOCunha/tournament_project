from .fighter import Fighter
from .category import Category


class Tournament:
    """Class that is responsible for creating and organizing different Categories based on sex,
    age and weight. It will receive a group of fighters and organize them in their respective
    Categories, based on the characteristics in their Fighter object."""

    # Here we will separate the fighters in their respective categories, creating a Category object after it's done
    _active_categories = {}
    _active_absolute_categories = {}

    def __init__(
        self,
        fighter_list: "list[Fighter]" = None,
        absolute_fighter_list: "list[Fighter]" = None,
    ) -> None:
        if fighter_list:
            # Fighter list that will obey category standards
            self.fighter_list = fighter_list
            for fighter in fighter_list:
                category_string = self.determine_category(fighter, absolute=False)
                self.add_to_active_categories(category_string, fighter)
        if absolute_fighter_list:
            # Fighter list that will obey open weight standards
            self.absolute_fighter_list = absolute_fighter_list
            for fighter in absolute_fighter_list:
                category_string = self.determine_category(fighter, absolute=True)
                self.add_to_active_categories(category_string, fighter, absolute=True)

    def determine_category(self, fighter: Fighter, absolute: bool = False) -> str:
        """This method received a fighter, extracts all of its relevant information and, through a switch,
        determines how to create a string that appropriately describes its category, then adds it into
        the active category dictionary on a key named after its category string."""
        sex = fighter.return_sex()
        age = fighter.return_age()
        weight = fighter.return_weight()
        # This string will be created piece by piece to classify the fighter category
        # It should appear like this: "{sexclass}-{ageclass}-{weightclass}-{belt}"
        # Or, if the fighter is on open weight category, like this: "{sexclass}-{ageclass}-Absolute-{belt}"
        category_string = ""

        # If on open weight category and is Male
        if absolute and sex == "M":
            category_string += "M-"
            age_class_name = self.check_age_class(age)
            category_string += f"{age_class_name}-"
            category_string += "Absolute-"

        # If on open weight category and is Female
        elif absolute and sex == "F":
            category_string += "F-"
            age_class_name = self.check_age_class(age)
            category_string += f"{age_class_name}-"
            category_string += "Absolute-"

        # If Male and Juvenile
        elif sex == "M" and 15 <= age < 18:
            category_string += "M-"
            age_class_name = self.check_age_class(age)
            category_string += f"{age_class_name}-"
            weight_class_name = self.check_weight_class_juvenile_male(weight)
            category_string += f"{weight_class_name}-"

        # If Male and Adult (older than 18, not the age class)
        elif sex == "M" and 18 <= age:
            category_string += "M-"
            age_class_name = self.check_age_class(age)
            category_string += f"{age_class_name}-"
            weight_class_name = self.check_weight_class_male(weight)
            category_string += f"{weight_class_name}-"

        # If Female and Juvenile
        elif sex == "F" and 15 <= age < 18:
            category_string += "F-"
            age_class_name = self.check_age_class(age)
            category_string += f"{age_class_name}-"
            weight_class_name = self.check_weight_class_juvenile_female(weight)
            category_string += f"{weight_class_name}-"

        # If Female and Adult (older than 18, not the age class)
        elif sex == "F" and 18 <= age:
            category_string += "F-"
            age_class_name = self.check_age_class(age)
            category_string += f"{age_class_name}-"
            weight_class_name = self.check_weight_class_female(weight)
            category_string += f"{weight_class_name}-"

        category_string += fighter.return_belt()
        return category_string

    def check_weight_class_female(self, weight: float) -> str:
        """Receives a weight and checks to see which adult female weight class it belongs to"""
        weight_classes_female = {
            "Rooster": (weight <= 48.5),
            "LightFeather": (48.5 <= weight < 53.5),
            "Feather": (53.5 <= weight < 58.5),
            "Light": (58.5 <= weight < 64.0),
            "Middle": (64.0 <= weight < 69.0),
            "MediumHeavy": (69.0 <= weight < 74.0),
            "Heavy": (74.0 <= weight < 79.3),
            "SuperHeavy": (79.3 <= weight),
        }
        for weight_class, weight_check in weight_classes_female.items():
            if weight_check:
                return weight_class
        raise ValueError("Fighter Does not belong in any weight category")

    def check_weight_class_male(self, weight: float) -> str:
        """Receives a weight and checks to see which adult male weight class it belongs to"""
        weight_classes_male = {
            "Rooster": (weight <= 57.5),
            "LightFeather": (57.5 <= weight < 64.0),
            "Feather": (64.0 <= weight < 70.0),
            "Light": (70.0 <= weight < 76.0),
            "Middle": (76.0 <= weight < 82.3),
            "MediumHeavy": (82.3 <= weight < 88.3),
            "Heavy": (88.3 <= weight < 94.3),
            "SuperHeavy": (94.3 <= weight < 100.3),
            "UltraHeavy": (100.3 <= weight),
        }
        for weight_class, weight_check in weight_classes_male.items():
            if weight_check:
                return weight_class
        raise ValueError("Fighter Does not belong in any weight category")

    def check_weight_class_juvenile_female(self, weight: float) -> str:
        """Receives a weight and checks to see which juvenile female weight class it belongs to"""
        weight_classes_juvenile_female = {
            "Rooster": (weight <= 44.3),
            "LightFeather": (44.3 <= weight < 48.3),
            "Feather": (48.3 <= weight < 52.6),
            "Light": (52.6 <= weight < 56.5),
            "Middle": (56.5 <= weight < 60.5),
            "MediumHeavy": (60.5 <= weight < 65.0),
            "Heavy": (65.0 <= weight < 69.0),
            "SuperHeavy": (69.0 <= weight),
        }
        for weight_class, weight_check in weight_classes_juvenile_female.items():
            if weight_check:
                return weight_class
        raise ValueError("Fighter Does not belong in any weight category")

    def check_weight_class_juvenile_male(self, weight: float) -> str:
        """Receives a weight and checks to see which juvenile male weight class it belongs to"""
        weight_classes_juvenile_male = {
            "Rooster": (weight <= 53.5),
            "LightFeather": (53.5 <= weight < 58.5),
            "Feather": (58.5 <= weight < 64.0),
            "Light": (64.0 <= weight < 69.0),
            "Middle": (69.0 <= weight < 74.0),
            "MediumHeavy": (74.0 <= weight < 79.3),
            "Heavy": (79.3 <= weight < 84.3),
            "SuperHeavy": (84.3 <= weight < 89.3),
            "UltraHeavy": (89.3 <= weight),
        }
        for weight_class, weight_check in weight_classes_juvenile_male.items():
            if weight_check:
                return weight_class
        raise ValueError("Fighter Does not belong in any weight category")

    def check_age_class(sef, age: int) -> str:
        """Receives an age number and checks to see which age class it belongs to"""
        age_classes = {
            "Juvenile": (15 <= age < 18),
            "Adult": (18 <= age < 30),
            "Master": (30 <= age < 41),
            "Senior": (age >= 41),
        }
        for age_class, age_check in age_classes.items():
            if age_check:
                return age_class
        raise ValueError("Fighter Does not belong in any age category")

    def return_active_categories(self) -> dict:
        return self._active_categories

    def return_active_absolute_categories(self) -> dict:
        return self._active_absolute_categories

    def add_to_active_categories(
        self, category_string: str, fighter: Fighter, absolute: bool = False
    ):
        """A method that adds fighters to the category dict. It does this by checking if the category string
        already exists in the keys for the categories, if it does it adds to the list of fighters of that
        category, if it doesnt it initiates the list of fighters in that category"""
        if not absolute:
            if category_string not in self._active_categories.keys():
                self._active_categories[category_string] = [
                    fighter,
                ]
            else:
                self._active_categories[category_string].append(fighter)
        elif absolute:
            if category_string not in self._active_absolute_categories.keys():
                self._active_absolute_categories[category_string] = [
                    fighter,
                ]
            else:
                self._active_absolute_categories[category_string].append(fighter)

    def create_category_objects(self):
        """Method that transforms the list of fighters in the category dictionaries into a Category
        object that can initialize the tournament."""
        # Normal categories
        category_dict = self.return_active_categories()
        for category_name, category_fighters in category_dict.items():
            category_dict[category_name] = Category(category_fighters)

        # Absolute categories
        absolute_category_dict = self.return_active_absolute_categories()
        for category_name, category_fighters in absolute_category_dict.items():
            category_dict[category_name] = Category(category_fighters)
