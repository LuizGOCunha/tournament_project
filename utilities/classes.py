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
    def __init__(self, name:str, weight:float, belt_number:int, age:int, sex:str) -> None:
        self._name = name
        self._weight = float(weight)
        # Belt number are 0 to 4, representing white to black
        self._belt = Belt(belt_number)
        self._age = age
        if sex == "M" or sex == "F":
            self._sex = sex
        else: 
            raise ValueError("Sex must be either 'M' or 'F'")

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
        if winner_number == 1:
            self._winner = self._fighter1
            self._resolved = True
        elif winner_number == 2:
            self._winner = self._fighter2
            self._resolved = True
        else:
            raise ValueError("Winner number should be 1 or 2, representing fighter1 or fighter2")

    def return_winner(self) -> Fighter:
        return self._winner

    def is_resolved(self) -> bool:
        return self._resolved

    def __str__(self) -> str:
        if not self.is_resolved(): 
            return f"Fighter 1: {self._fighter1}; Fighter 2: {self._fighter2}"
        if self.is_resolved():
            return f"Fighter 1: {self._fighter1}; Fighter 2: {self._fighter2}. Winner: {self._winner}"


class Category:
    def __init__(self) -> None:
        self._fighters = []

    def add_fighter(self, fighter):
        if type(fighter) == Fighter:
            self._fighters.append(fighter)
        else:
            print("New fighter must be a Fighter data type")
    
    def return_fighters(self):
        return self._fighters
    
    def create_matches(self):
        self._matches = []
        fighters_to_be_arranged = []
        for fighter in self.return_fighters():
            fighters_to_be_arranged.append(fighter)
            if len(fighters_to_be_arranged) == 2:
                arranged_match = Match(fighters_to_be_arranged[0], fighters_to_be_arranged[1])
                self._matches.append(arranged_match)

    def check_for_winner(self):
        if len(self._matches) == 1:
            final_match = self._matches[0]
            if final_match._resolved:
                print(f"Category winner is {final_match._winner._name}")



if __name__ == "__main__":
    dummy = Fighter("dummy", 80.0, 2, 20, "M")
    print(dummy)