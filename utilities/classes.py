

class Match:
    def __init__(self, fighter1=False, fighter2=False):
        self._fighter1 = fighter1
        self._fighter2 = fighter2

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

class Fighter:
    def __init__(self, name, weight, belt):
        self._name = name
        self._weight = weight
        self._belt = belt
        self._weightclass = self.check_weightclass()

    def check_weightclass():
        pass

    def change_name(self, new_name):
        self._name = new_name

    def change_weight(self, new_weight):
        self._weight = new_weight
        self._weightclass = self.check_weightclass()

    def change_belt(self, new_belt):
        self._belt = new_belt

    