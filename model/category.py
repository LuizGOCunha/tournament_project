from .fighter import Fighter
from .match import Match

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