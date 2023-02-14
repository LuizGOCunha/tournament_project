from .fighter import Fighter


class Match:
    """A class that contains two fighter data types, representing a tournament singular match"""

    def __init__(self, fighter1: Fighter = None, fighter2: Fighter = None) -> None:
        self._fighter1 = fighter1
        self._fighter2 = fighter2
        self._resolved = False

    def return_fighters(self) -> tuple:
        """Returns a tuple of the present fighters"""
        if self.is_ready():
            return (self._fighter1, self._fighter2)
        elif self._fighter1:
            return (self._fighter1,)
        else:
            return (self._fighter2,)

    def is_ready(self) -> bool:
        """if both fighters are stablished, the match is ready"""
        if self._fighter1 and self._fighter2:
            return True
        else:
            return False

    def add_fighter(self, fighter: Fighter) -> None:
        """Adds fighter to the match, depending on the slot available. Requires a Fighter data type"""
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

    def resolve_match(self, winner_number: int) -> None:
        """Determines the winner based on the number given (1 or 2, depending on the winning fighter)"""
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
                raise ValueError(
                    "Winner number should be 1 or 2, representing fighter1 or fighter2"
                )
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
