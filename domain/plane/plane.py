from domain.plane.planeException import PlaneException
from domain.plane.planeValidator import PlaneValidator
from infrastructure.passengers.passengerRepository import passengerRepository
class MyPlane:
    def __init__(self, number : int, airline : str, seats : int, destination : str, passengers_list: passengerRepository):
        if not isinstance(number, int) or not isinstance(airline, str) or not isinstance(seats, int) or not isinstance(destination, str) or not isinstance(passengers_list, passengerRepository):
            raise PlaneException("[D-P] One of the arguments provided not of correct type.")
        if len(passengers_list) > seats:
            raise PlaneException("[D-P] Too many passengers are aboard the plane.")
        
        self.__number = number
        self.__airline = airline
        self.__seats = seats
        self.__destination = destination
        self.__passengers_list = passengers_list.get_all_passengers()


    # GETTERS

    def get(self) -> tuple:
        return self.__number, self.__airline, self.__seats, self.__destination, self.__passengers_list
    
    def get_number(self) -> str:
        return self.__number
    
    def get_airline(self) -> str:
        return self.__airline
    
    def get_seats(self) -> str:
        return self.__seats
    
    def get_destination(self) -> str:
        return self.__destination
    
    def get_passengers_list(self) -> list:
        return self.__passengers_list
    
    # SETTERS
    def set(self, coords) -> None:
        self.__number, self.__airline, self.__seats, self.__destination, self.__passengers_list = coords[0], coords[1], coords[2], coords[3], coords[4]
    
    def set_number(self, name : int) -> None:
        self.__number= name

    def set_airline(self, name: str) -> None:
        self.__airline = name
    
    def set_seats(self, new : int)->None:
        self.__seats = new
    
    def set_destination(self, new: str)->None:
        self.__destination = new

    def set_passengers_list(self, new: list)->None:
        self.__passengers_list = new

    
    def __repr__(self):
            return str("\n------------------------------- [[  "+str(self.__number)+"  ]] -------------------------------"+"\nPlane number: "+str(self.__number)+"\t\t"+"Airline: "+str(self.__airline)+"\n"+"Number of seats: "+str(self.__seats)+"\t"+"Destination: "+str(self.__destination)+"\n\t\t\t\t"+"List of passengers: \n"+str(self.__passengers_list)+"\n------------------------------------"+"-------------------------------------\n")
