class Belt:
    '''A class of Belt, created so we can have a mroe strict choice, instead of having open strings'''
    colors = ["White", "Blue", "Purple", "Brown", "Black"]

    def __init__(self, my_belt_number) -> None:
        '''When initiated, the class asks for a number between 0-4, so it can represent a color'''
        self._my_belt = self.colors[my_belt_number]

    def return_my_belt(self):
        return self._my_belt


class Fighter:
    def __init__(self, name:str, weight:float, belt_number:int, age:int, sex:str):
        self._name = name
        self._weight = weight
        # Belt number are 0 to 4, representing white to black
        belt_object = Belt(belt_number)
        self._belt = belt_object.return_my_belt()
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

    def change_name(self, new_name):
        self._name = new_name

    def change_weight(self, new_weight):
        self._weight = new_weight

    def change_belt(self, new_belt_number):
        belt_object = Belt(new_belt_number)
        self._belt = belt_object.return_my_belt()

    def change_age(self, new_age):
        self._age = new_age

    def change_sex(self, new_sex):
        if new_sex == "M" or new_sex == "F":
            self._sex = new_sex
        else:
            raise ValueError("Sex must be either 'M' or 'F'")

    def return_name(self):
        return self._name

    def return_weight(self):
        return self._weight

    def return_belt(self):
        return self._belt
    
    def return_age(self):
        return self._age
    
    def return_sex(self):
        return self._sex
        
    def __str__(self):
        return f"{self.return_name()} - {self.return_belt()}"


class Match:
    def __init__(self, fighter1=False, fighter2=False):
        self._fighter1 = fighter1
        self._fighter2 = fighter2
        self._resolved = False

    def is_ready(self):
        '''if both fighters are stablished, the match is ready'''
        if self.fighter1 and self.fighter2:
            return True
        else:
            return False

    def add_fighter(self, fighter):
        # Checks if its a fighter data type
        if type(fighter) == Fighter:
            # Checks where the new fighter should be allocated
            if not self._fighter1:
                self._fighter1 = fighter
            elif not self._fighter2:
                self._fighter2 = fighter
            else:
                print("Both fighter slots are occupied")
        else:
            print("New fighter must be a Fighter data type")

    def resolve_match(self, winner):
        self._winner = winner
        self._resolved = True

    def show_match(self):
        self._fighter1.show_fighter()
        print("*****VS*****")
        self._fighter2.show_fighter()


class Tournament:
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
                print(f"tournament winner is {final_match._winner._name}")



if __name__ == "__main__":
    dummy = Fighter("dummy", 80.0, "purple", 20, "M")
    print(dir(bool))
    print(dummy)