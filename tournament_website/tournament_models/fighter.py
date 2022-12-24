import uuid

from .belt import Belt

class Fighter:
    '''Class that holds informations of all fighters in memory, its methods change and return info'''
    def __init__(self, name:str, weight:float, belt_number:int, age:int, sex:str, uid:uuid.UUID=None) -> None:
        self._name = name
        self._weight = float(weight)
        # Belt number are 0 to 4, representing white to black
        self._belt = Belt(belt_number)
        self._age = age
        # Here we test if the sex obeys the binary categories
        if sex == "M" or sex == "F":
            self._sex = sex
        else: 
            raise ValueError("Sex must be either 'M' or 'F'")
        # Creates new UID if the Fighter doesnt have one pulled from a data base
        if not uid:
            self._id = uuid.uuid4()
        else: 
            self._id = uid

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
