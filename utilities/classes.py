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
    '''A class that intiates with a list of fighters that will work like a staging area to create a list
     of matches in the future. Then, it will advance those matches until it has nothing but one match 
     with one winner. He will be the category winner.'''
    def __init__(self, fighter_list:"list[Fighter]" = []) -> None:
        self._fighters = fighter_list
        self._matches_are_ready = False

    def add_fighter(self, *fighters: Fighter):
        '''Add fighters to the original list of fighters that will be later used to create matches'''
        for fighter in fighters:
            if type(fighter) == Fighter:
                self._fighters.append(fighter)
            else:
                raise TypeError("New fighter must be a Fighter data type")
    
    def return_fighters(self):
        return self._fighters

    def remove_fighter(self, *fighters: Fighter) -> None:
        '''Function that creates a list through *args that progressively removes all specified fighter 
        values in the original staging area'''
        for fighter in fighters:
            self._fighters.remove(fighter)
    
    def create_matches(self):
        '''Create matches based on the fighters on this category. If the number of fighters is uneven
        it will return a match with one fighter alone.'''
        # Here we need to iterate half the times the length of the list of fighters
        # The reason is because we will be using 2 items at the same time
        # for that we need a for loop, C style
        self._matches = []
        # Initiate counter
        i=0
        list_of_fighters = self.return_fighters()
        # Disregard Python logic
        for _ in list_of_fighters:
            # Make sure we only run the code every other iteration
            if i%2 == 0:
                # try and except so the code doesnt break when we reach the end of uneven list
                try:
                    fighter1 = list_of_fighters[i]
                    fighter2 = list_of_fighters[i+1]
                    new_match = Match(fighter1, fighter2)
                    self._matches.append(new_match)
                    self.remove_fighter(fighter1, fighter2)
                except IndexError:
                    fighter1 = list_of_fighters[i]
                    new_match = Match(fighter1,)
                    self._matches.append(new_match)
                    self.remove_fighter(fighter1)
            # Make the counter increase
            i+=1 
        self._matches_are_ready = True

    def return_matches(self):
        return self._matches

    def matches_are_ready(self):
        # Pedantic, surely, but better safe than sorry.
        return self._matches_are_ready

    def check_for_winner(self):
        if len(self._matches) == 1:
            final_match = self._matches[0]
            if final_match._resolved:
                print(f"Category winner is {final_match._winner._name}")

    def __str__(self) -> str:
        if self.matches_are_ready():
            return_string = ""
            for match in self.return_matches():
                return_string += match.__str__() + "\n"
            return return_string
        else:
            return self.return_fighters().__str__()
        


if __name__ == "__main__":
    dummy = Fighter("dummy", 80.0, 2, 20, "M")
    print(dummy)