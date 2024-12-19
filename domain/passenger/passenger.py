from domain.passenger.passengerException import PassengerException
from domain.passenger.passengerValidator import PassengerValidator
class MyPassenger:
    def __init__(self, first_name : str, last_name : str, passport_number: str):
        if not isinstance(first_name, str) or not isinstance(last_name, str) or not isinstance(passport_number, str):
            raise PassengerException("One of the arguments provided is not of type `str`.")
        
        self.__first_name = first_name
        self.__last_name = last_name
        self.__passport_number = passport_number


    # GETTERS

    def get(self) -> tuple:
        return self.__first_name, self.__last_name, self.__passport_number
    
    def get_first_name(self) -> str:
        return self.__first_name
    
    def get_last_name(self) -> str:
        return self.__last_name
    
    def get_passport_number(self) -> str:
        return self.__passport_number
    
    # SETTERS
    def set(self, coords) -> None:
        self.__first_name, self.__last_name, self.__passport_number = coords[0], coords[1], coords[2]
    
    def set_first_name(self, name : str) -> None:
        self.__first_name = name

    def set_last_name(self, name: str) -> None:
        self.__last_name = name
    
    def set_passport_number(self, new : str)->None:
        self.__passport_number = new

    
    def __repr__(self):
            return str("First name: "+str(self.__first_name)+"\t\t"+"Last name: "+str(self.__last_name)+"\t\t"+"Passport number: "+str(self.__passport_number)+"\n")
                
    
    