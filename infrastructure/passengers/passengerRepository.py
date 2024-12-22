#from utils.distance import dist
from domain.passenger.passenger import MyPassenger
from infrastructure.passengers.passengerRepositoryException import PassengerRepositoryException

class passengerRepository:

    def __init__(self, passengers=None):
        """Constructor/init function

        Args:
            passengers (_type_, optional): _description_. Defaults to None.
        """
        self._passengers = passengers or []

    # -------------------- GETTERS --------------------
    
    # 2
    def get_all_passengers(self) -> list:
        """Get the passengers inside the repository

        Returns:
            self._passengers: List containing passengers in repository
        """
        return self._passengers
    
    # 3
    def get_passenger_by_index(self, index : int) -> MyPassenger:
        """Get the passenger at the specified index.

        Raises:
            PassengerRepositoryException: In case the index is negative, out of bounds or non integer.

        Returns:
            self._passengers[index]: passenger at specified index.
        """
        if index < 0 or index >= len(self._passengers) or type(index) != int:
            raise PassengerRepositoryException("Index is out of bounds.")
        return self._passengers[index]
    
    def get_passenger_by_name(self, name: str) -> MyPassenger:
        """Get passenger by their name.

        Args:
            name (str): Name to search for.
        Returns:
            MyPassenger: The passenger whos first or last name matches the argument.
        """
        return [passenger for passenger in self._passengers if passenger.get_last_name().find(name) != -1 or passenger.get_first_name().find(name) != -1 ]
    
    def sort_by_last_name(self):
        """Sorts the passengers by their last name.
        """
        def getLast(p):
            return p.get_last_name()
        self._passengers.sort(key=getLast)
    
    def __len__(self):
        return len(self._passengers)