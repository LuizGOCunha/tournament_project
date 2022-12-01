

class Match:
    def __init__(self, fighter1=False, fighter2=False):
        self._fighter1 = fighter1
        self._fighter2 = fighter2
        self._resolved = True

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

class Fighter:
    def __init__(self, name, weight, belt):
        self._name = name
        self._weight = weight
        self._belt = belt
        self._weightclass = self.check_weightclass()

    def check_weightclass(self):
        pass

    def change_name(self, new_name):
        self._name = new_name

    def change_weight(self, new_weight):
        self._weight = new_weight
        self._weightclass = self.check_weightclass()

    def change_belt(self, new_belt):
        self._belt = new_belt

    def show_fighter(self):
        print(self._name)
        print(self._weight)
        print(self._belt)

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



gabriel = Fighter("gabriel", 76, "purple")
fabio = Fighter("fabio", 76, "purple")
trnmt = Tournament()
trnmt.add_fighter(gabriel)
trnmt.add_fighter(fabio)
trnmt.create_matches()
trnmt._matches[0].show_match()
trnmt._matches[0].resolve_match(gabriel)
trnmt.check_for_winner()
