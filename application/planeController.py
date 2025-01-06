from domain.plane.plane import MyPlane
from infrastructure.passengers.passengerRepository import passengerRepository
from domain.passenger.passenger import MyPassenger
from domain.passenger.passenger import PassengerException

class PlaneController():

    def __init__(self, repo,v):
        self.__repo = repo
        self.__validator = v

    def createPlane(self, planes : list) -> list:
        """Function that parses planes list and creates a list containing MyPlane objects.

        Args:
            planes (list): The list of planes to be parsed.

        Raises:
            Exception: If something goes wrong during the parsing/creating.

        Returns:
            list: The final list of MyPlane objects.
        """
        created_planes = []
        for plane in planes:

                number, airline, seats, destination = int(plane['plane_id']), plane['plane_name'], int(plane['capacity']), plane['destination']
                pass_list = []

                for passenger in plane['passengers']:
                    v = MyPassenger(passenger[0], passenger[1], passenger[2])
                    pass_list.append(v)

                try:
                    passengers = passengerRepository(pass_list)
                except PassengerException as err:
                    raise Exception("[A-PC] Something happened while trying to convert passenger list into plane repository.")
                
                s = MyPlane(number, airline, seats, destination, passengers)
                self.__validator.validate(s)

                created_planes.append(s)

        return created_planes
    
    # Errors are caught from the repository and forwarded to the console
    def addPlane(self, planes : list) -> None:
        """Function that adds a plane or planes to the repository.

        Args:
            planes (list): List of planes that will be parsed by an auxiliary function.

        Raises:
            Exception: If something wrong happens during either the parsing or the adding to the repository.
        """
        try:
            s = self.createPlane(planes)
            self.__repo.add_planes_to_repository(s)
        except Exception as err:
            raise Exception(f"[⚡] Error while adding plane, try again!, here: {err}")
    
    def updatePlane(self, command : tuple) -> None:
        """Function that handles the updating of planes.

        Args:
            command (tuple): The arguments for the update event.

        Raises:
            Exception: If something goes wrong during the updating of the plane.
        """
        try:
            return self.__repo.update_plane(command)
        except Exception as err:
            raise Exception(f"[⚡] Error while updating plane, try again!, here: {err}")

        
    def deletePlane(self, command : tuple) -> None:
        """Function that handles the deletion of planes.

        Args:
            command (tuple): The arguments for the delete event.

        Raises:
            Exception: If something goes wrong during the deletion of the plane(s).
        """
        try:
            return self.__repo.delete_plane(command)
        except Exception as err:
            raise Exception(f"[⚡] Error while deleting plane, try again!, here: {err}")

    def getPlanes(self, command:tuple) -> any:
        """Function that fetches planes based on a given criteria.

        Args:
            command (tuple): The criteria.

        Raises:
            Exception: If something goes wrong during the fetch event.

        Returns:
            any: The result of the fetch event.
        """
        try:
            choice = command[0]
            if choice == "all":
                return self.__repo.get_planes()
            elif choice == "index":
                return self.__repo.get_planes(index=command[1])
            elif choice == 1:
                return self.__repo.get_planes(by_same_passport_prefix=True)
            elif choice ==2:
                st = command[1]
                return self.__repo.get_passengers_with_name(st)
            elif choice==3:
                st= command[1]
                return self.__repo.get_planes(by_passenger_name = st)
            elif choice == "count":
                return len(self.__repo)
        except Exception as err:
            raise Exception(f"[⚡] Error while getting plane(s), try again!, here: {err}")
        
    def groupPlanes(self, command: tuple):
        """Function to group planes based on given criteria.

        Args:
            command (tuple): The criteria that will be used during the grouping event.

        Raises:
            Exception: If something happens during the grouping event.

        """
        try:
            choice = command[0]
            given = command[1]
            if choice == "k-planes":
                sol = []
                self.__repo.backtrack(domain=self.__repo.get_all_planes(), k=given, current_list=[], mode=choice, results = sol)
                return sol
            elif choice == "k-passengers":
                sol = []
                for plane in self.__repo.get_all_planes():
                    self.__repo.backtrack(domain=plane.get_passengers_list(), k=given, current_list=[], mode=choice, results = sol)
                return sol
            else:
                print(command, choice, given, sep=" ")
        except Exception as err:
            raise Exception(f"[⚡] Error while grouping plane(s), try again!, here: {err}")
    

        
