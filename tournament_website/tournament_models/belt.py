class Belt:
    """A class of Belt, created so we can have a mroe strict choice, instead of having open strings"""

    colors = ["White", "Blue", "Purple", "Brown", "Black"]

    def __init__(self, my_belt_number) -> None:
        """When initiated, the class asks for a number between 0-4, so it can represent a color"""
        self._my_belt = self.colors[my_belt_number]

    def return_my_belt(self) -> str:
        return self._my_belt

    def change_my_belt(self, new_belt_number) -> None:
        self._my_belt = self.colors[new_belt_number]
