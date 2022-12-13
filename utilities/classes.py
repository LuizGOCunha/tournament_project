import uuid

class Belt:
    '''A class of Belt, created so we can have a mroe strict choice, instead of having open strings'''
    colors = ["White", "Blue", "Purple", "Brown", "Black"]

    def __init__(self, my_belt_number) -> None:
        '''When initiated, the class asks for a number between 0-4, so it can represent a color'''
        self._my_belt = self.colors[my_belt_number]

    def return_my_belt(self) -> str:
        return self._my_belt

    def change_my_belt(self, new_belt_number) -> None:
        self._my_belt = self.colors[new_belt_number]


class Fighter:
    '''Class that holds informations of all fighters in memory, its methods change and return info'''
    def __init__(self, name:str, weight:float, belt_number:int, age:int, sex:str, uid:uuid.UUID=None) -> None:
        self._name = name
        self._weight = float(weight)
        # Belt number are 0 to 4, representing white to black
        self._belt = Belt(belt_number)
        self._age = age
        # Here we test if the sex obeys the the binary categories
        if sex == "M" or sex == "F":
            self._sex = sex
        else: 
            raise ValueError("Sex must be either 'M' or 'F'")
        # Creates new UID if the Fighter doesnt have one pulled from a data base
        if not uid:
            self._id = uuid.uuid4()
        else: 
            self._id = uid


#    def check_ageclass(self):
#        age = self._age
#
#        if (15<age<18):
#            return "Juvenile"
#
#        elif (17<age<30):
#            return "Adult"
#
#        elif (29<age<35):
#            return "Master"
#
#        elif (34<age<41): 
#            return "Senior"
#
#        else:
#            print("idade inválida")

    def return_id(self) -> uuid.UUID:
        return self._id

    def change_name(self, new_name:str) -> None:
        self._name = new_name

    def change_weight(self, new_weight:float) -> None:
        self._weight = float(new_weight)

    def change_belt(self, new_belt_number:int) -> None:
        self._belt.change_my_belt(new_belt_number)

    def change_age(self, new_age:int) -> None:
        self._age = new_age

    def change_sex(self, new_sex:str) -> None:
        if new_sex == "M" or new_sex == "F":
            self._sex = new_sex
        else:
            raise ValueError("Sex must be either 'M' or 'F'")

    def return_name(self) -> str:
        return self._name

    def return_weight(self) -> float:
        return self._weight

    def return_belt(self) -> str:
        return self._belt.return_my_belt()
    
    def return_age(self) -> int:
        return self._age
    
    def return_sex(self) -> str:
        return self._sex
        
    def __str__(self) -> str:
        return f"{self.return_name()} - {self.return_belt()} belt, {self.return_age()} years old, {self.return_weight()}kg"


class Match:
    '''A class that contains two fighter data types, representing a tournament singular match'''
    def __init__(self, fighter1:Fighter=None, fighter2:Fighter=None) -> None:
        self._fighter1 = fighter1
        self._fighter2 = fighter2
        self._resolved = False

    def return_fighters(self) -> tuple:
        '''Returns a tuple of the present fighters'''
        if self.is_ready():
            return (self._fighter1, self._fighter2)
        elif self._fighter1:
            return (self._fighter1,)
        else:
            return (self._fighter2,)

    def is_ready(self) -> bool:
        '''if both fighters are stablished, the match is ready'''
        if self._fighter1 and self._fighter2:
            return True
        else:
            return False

    def add_fighter(self, fighter:Fighter) -> None:
        '''Adds fighter to the match, depending on the slot available. Requires a Fighter data type'''
        # Checks if its a fighter data type
        if type(fighter) == Fighter:
            # Checks where the new fighter should be allocated
            if not self._fighter1:
                self._fighter1 = fighter
            elif not self._fighter2:
                self._fighter2 = fighter
            else:
                raise IndexError("Both fighter slots are occupied")
        else:
            raise TypeError("New fighter must be a Fighter data type")

    def resolve_match(self, winner_number:int) -> None:
        '''Determines the winner based on the number given (1 or 2, depending on the winning fighter)'''
        if self.is_ready():
            if winner_number == 1:
                self._winner = self._fighter1
                self._loser = self._fighter2
                self._resolved = True
            elif winner_number == 2:
                self._winner = self._fighter2
                self._loser = self._fighter1
                self._resolved = True
            else:
                raise ValueError("Winner number should be 1 or 2, representing fighter1 or fighter2")
        else:
            raise TypeError("The match is not ready yet")

    def return_winner(self) -> Fighter:
        return self._winner

    def return_loser(self) -> Fighter:
        return self._loser

    def is_resolved(self) -> bool:
        return self._resolved

    def __str__(self) -> str:
        if not self.is_resolved(): 
            return f"Fighter 1: {self._fighter1}; Fighter 2: {self._fighter2}"
        if self.is_resolved():
            return f"Fighter 1: {self._fighter1}; Fighter 2: {self._fighter2}. Winner: {self._winner}"


class Category:
    '''A class that initiates with a fighters_list of fighters that will work like a staging area to create a fighters_list
     of matches in the future. Then, it will advance those matches until it has nothing but one match 
     with one winner. He will be the category winner.'''
    def __init__(self, fighter_list:"list[Fighter]" = []) -> None:
        self._fighters = fighter_list
        self._matches_ready = False # Not sure if we're going to use this after all
        self._matches_are_resolved = False
        self._category_is_resolved = False

    def add_fighter(self, *fighters: Fighter):
        '''Add fighters to the original fighters_list of fighters that will be later used to create matches'''
        for fighter in fighters:
            if type(fighter) == Fighter:
                self._fighters.append(fighter)
            else:
                raise TypeError("New fighter must be a Fighter data type")
    
    def return_fighters(self):
        return self._fighters

    def remove_fighter(self, *fighters: Fighter) -> None:
        '''Function that creates a fighters_list through *args that progressively removes all specified fighter 
        values in the original staging area'''
        for fighter in fighters:
            self._fighters.remove(fighter)
    
    def create_matches(self, imposed_list:"list[Fighter]"=None):
        '''Create matches based on the fighters on this category. If the number of fighters is uneven
        it will return a match with one fighter alone. There is also a possibility to impose a determined
        List of fighters, instead of creating one from the properties initiated on the class (used to
        advance the phase of the category)'''
        fighters_list = self.return_fighters()
        if imposed_list:
            fighters_list = imposed_list
        i = 0
        matches = []
        for _ in fighters_list:
            if i%2 == 0:
                try:
                    new_match = Match(fighters_list[i], fighters_list[i+1])
                    matches.append(new_match)
                    print(new_match)
                except IndexError:
                    new_match = Match(fighters_list[i])
                    matches.append(new_match)
                    print(new_match)
            i+=1
        self._matches = matches
            
        self._matches_ready = True

    def return_matches(self):
        if self.matches_are_ready():
            return self._matches

    def matches_are_ready(self):
        # Pedantic, surely, but better safe than sorry.
        return self._matches_ready

    def resolve_category(self, *match_winners) -> None:
        '''This method is responsible for resolving all matches in the category, then using the winners
        and losers to create new matches, so advancing the category to the next phase.'''
        matches = self.return_matches()
        # checks if we have theright amount of winners for the matches
        i = 0
        if len(match_winners) == len(self.return_matches()):
            for match, winner in zip(matches, match_winners):
                if match.is_ready():
                    # This is for when the match is ready (has two fighters in it)
                    match.resolve_match(winner)
                else:
                    # This is for when the match is not ready (just one fighter in it)
                    # In this case he will fight the loser of the previous match
                     missing_opponent = matches[i-1].return_loser()
                     match.add_fighter(missing_opponent)
                     match.resolve_match(winner)
                i+=1
        else:
            raise ValueError("Number of winners must be equal to number of matches")

        self._matches_are_resolved = True
        self.check_for_winner()

    def advance_category(self) -> None:
        '''This method creates new matches for a new phase based on resolved matches of a past phase'''
        winners = []
        matches = self.return_matches()
        for match in matches:
            winner = match.return_winner()
            winners.append(winner)
        self.create_matches(winners)

        self._matches_are_resolved = False

    def check_for_winner(self) -> None:
        '''This method checks if all matches were done and if there is only one match with one winner.
        That would mean that we have a category winner, and when that happens we need to instantiate some
        necessary properties.'''
        # Check if theres only one match
        if len(self.return_matches()) == 1:
            # Check if the match is resolved
            if self.return_matches()[0].is_resolved():
                self._winner = self.return_matches()[0].return_winner()
                self._category_is_resolved = True

    def is_resolved(self) -> bool:
        return self._category_is_resolved

    def return_winner(self) -> Fighter:
        if self.is_resolved():
            return self._winner
        else:
            raise TypeError("Category is not resolved yet")

    
    def __str__(self) -> str:
        if self.matches_are_ready() and not self.is_resolved():
            return_string = ""
            for match in self.return_matches():
                return_string += match.__str__() + "\n"
            return return_string
        elif self.is_resolved():
            return "WINNER:" + self.return_winner().__str__() + "\n"

        else:
            return self.return_fighters().__str__() + "\n"


class Tournament:
    '''Class that is responsible for creating and organizing different Categories based on sex,
     age and weight. It will receive a group of fighters and organize them in their respective
     Categories, based on the characteristics in their Fighter object.'''
    # Creating the values below with a null value just so we can use them in the following comparations
    sex = ""
    age = 0
    weight = 0.0
    sex_categories = {
        "Male": (sex=="M"),
        "Female": (sex=="F")
     }
    age_categories = {
        "Juvenile": (15<=age<18),
        "Adult": (18<=age<30),
        "Master": (30<=age<41),
        "Senior": (age>=41)
    }
    # Weight categories vary for each age and sex category
    # We will have to create different ones according to the rules
    weight_categories_female = {
        "Rooster": (weight<=48.5),
        "Light Feather": (48.5<=weight<53.5),
        "Feather": (53.5<=weight<58.5),
        "Light": (58.5<=weight<64.0),
        "Middle": (64.0<=weight<69.0),
        "Medium Heavy": (69.0<=weight<74.0),
        "Heavy": (74.0<=weight<79.3),
        "Super Heavy": (79.3<=weight)
    }
    weight_categories_juvenile_female = {
        "Rooster": (weight<=44.3),
        "Light Feather": (44.3<=weight<48.3),
        "Feather": (48.3<=weight<52.6),
        "Light": (52.6<=weight<56.5),
        "Middle": (56.5<=weight<60.5),
        "Medium Heavy": (60.5<=weight<65.0),
        "Heavy": (65.0<=weight<69.0),
        "Super Heavy": (69.0<=weight)
    }
    weight_categories_male = {
        "Rooster": (weight<=57.5),
        "Light Feather": (57.5<=weight<64.0),
        "Feather": (64.0<=weight<70.0),
        "Light": (70.0<=weight<76.0),
        "Middle": (76.0<=weight<82.3),
        "Medium Heavy": (82.3<=weight<88.3),
        "Heavy": (88.3<=weight<94.3),
        "Super Heavy": (94.3<=weight<100.3),
        "Ultra Heavy": (100.3<=weight)
    }
    weight_categories_juvenile_male = {
        "Rooster": (weight<=53.5),
        "Light Feather": (53.5<=weight<58.5),
        "Feather": (58.5<=weight<64.0),
        "Light": (64.0<=weight<69.0),
        "Middle": (69.0<=weight<74.0),
        "Medium Heavy": (74.0<=weight<79.3),
        "Heavy": (79.3<=weight<84.3),
        "Super Heavy": (84.3<=weight<89.3),
        "Ultra Heavy": (89.3<=weight)
    }

if __name__ == "__main__":
    pass