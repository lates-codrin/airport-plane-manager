from domain.plane.plane import MyPlane
from domain.plane.planeValidator import PlaneValidator
from infrastructure.passengers.passengerRepository import passengerRepository
from infrastructure.passengers.passengerRepository import PassengerRepositoryException
from domain.passenger.passenger import MyPassenger
from domain.passenger.passenger import PassengerException

class PlaneController():

    def __init__(self, repo,v):
        self.__repo = repo
        self.__validator = v

    def createPlane(self, planes : list) -> MyPlane:
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
                    print("ERR")
                s = MyPlane(number, airline, seats, destination, passengers)
                self.__validator.validate(s)
                created_planes.append(s)
        return created_planes
    
    # warning: cursed error handling below
    # to explain: errors are catched from the repository and forwarded to the console
    def addPlane(self, coords : tuple) -> None:
        try:
            s = self.createPlane(coords)
            self.__repo.add_planes_to_repository(s)
        except Exception as err:
            raise Exception(f"[⚡] Error while adding plane, try again!, here: {err}")
    
    def updatePlane(self, command : tuple) -> None:
        try:
            return self.__repo.update_plane(command)
        except Exception as err:
            raise Exception(f"[⚡] Error while updating plane, try again!, here: {err}")

        
    def deletePlane(self, command : tuple) -> None:
        try:
            return self.__repo.delete_plane(command)
        except Exception as err:
            raise Exception(f"[⚡] Error while deleting plane, try again!, here: {err}")

    def getPlanes(self, command:tuple) -> any:
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
        
    def groupPlanes(self, command):
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
            raise Exception(f"[⚡] Error while getting plane(s), try again!, here: {err}")
    
    def viewShape(self, *args) -> any:
        try:
            result = self.__repo.visualize_shape(*args)
            return result
        except Exception as err:
            raise Exception(f"[⚡] Error while plotting planes, try again! Here: {err}")


        
