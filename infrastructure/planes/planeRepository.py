#from utils.distance import dist
from domain.plane.plane import MyPlane
from domain.passenger.passenger import MyPassenger
from infrastructure.planes.planeRepositoryException import PlaneRepositoryException
from infrastructure.passengers.passengerRepository import passengerRepository
class planeRepository:

    def __init__(self, planes=None):
        """Constructor/init function

        Args:
            planes (_type_, optional): _description_. Defaults to None.
        """
        self._planes = planes or []
        self._backtracked = []

    # -------------------- GETTERS --------------------
    
    def get_planes(self, index=None, by_same_passport_prefix=False, by_passenger_name=None):
        """
        Get plane(s) from the repository based on specified criteria.

        This function can be used to:
        - Get all planes.
        - Get a plane by its index.
        - Get planes where passengers share the same first 3 digits of their passport numbers.
        - Get planes with a passenger matching a specific first or last name.

        Args:
            index (int, optional): The index of the plane to retrieve.
            by_same_passport_prefix (bool, optional): Whether to search for planes with passengers sharing the same first 3 digits of their passport numbers.
            by_passenger_name (str, optional): The first or last name of the passenger to filter planes.

        Raises:
            PlaneRepositoryException: If the index is negative, out of bounds, or not an integer.

        Returns:
            list or MyPlane: A list of planes matching the criteria or a single plane if `index` is specified.

        """
        if index is not None:
            if not isinstance(index, int) or index < 0 or index >= len(self._planes):
                raise PlaneRepositoryException("Index is out of bounds.")
            return self._planes[index]

        if by_same_passport_prefix:
            found_planes = []
            for plane in self._planes:
                passengers = plane.get_passengers_list()
                if passengers:
                    prefix = passengers[0].get_passport_number()[:3]
                    if all(passenger.get_passport_number()[:3] == prefix for passenger in passengers):
                        found_planes.append(plane)
            return found_planes

        if by_passenger_name is not None:
            found_planes = []
            for plane in self._planes:
                passengers = plane.get_passengers_list()
                if passengers:
                    if any(
                        passenger.get_first_name() == by_passenger_name or
                        passenger.get_last_name() == by_passenger_name
                        for passenger in passengers
                    ):
                        found_planes.append(plane)
            return found_planes if found_planes else f"No planes found with name {by_passenger_name}"

        return self._planes

    def get_passengers_with_name(self, name):
        """Get passenger(s) with name that starts with provided string.

        Args:
            name (_type_): Sub-string to search for.

        Returns:
            found_passengers: Found passengers.
        """
        found_passengers = []
        for plane in self._planes:
            passengers = plane.get_passengers_list()
            for passenger in passengers:
                if passenger.get_first_name().find(name) != -1 or passenger.get_last_name().find(name) != -1:
                    found_passengers.append(passenger)
    
        if len(found_passengers) == 0:
            return f"No passengers found with name {name}"
        return found_passengers

    
    # -------------------- SETTERS --------------------
    def add_planes_to_repository(self, planes):
        """Add plane(s) to the repository.

        Args:
            planes (_type_): List of planes to add to the repository.

        Raises:
            PlaneRepositoryException: If argument is not a list.
        """
        if type(planes) != list:
            raise PlaneRepositoryException("Not a list.")
        for plane in planes:
            self._planes.append(plane)
    
    
    # --------------------      MISC     --------------------

    # -------------------- SORT FUNCTION --------------------
    def sort_planes(self, criteria=None, sub=None):
        """A function that sorts planes based on different criteria.

        Args:
            criteria (_type_, optional): Number of the criteria.
            sub (_type_, optional): Sub-string for criteria 2.

        Raises:
            PlaneRepositoryException: If criteria is invalid.
        """
        if criteria == 1:
            key_function = lambda p: len(p.get_passengers_list())
        elif criteria == 2:
            key_function = lambda p: len([x for x in p.get_passengers_list() if x.get_first_name().startswith(sub)])
        elif criteria == 3:
            key_function = lambda p: str(len(p.get_passengers_list())) + str(p.get_destination())
        else:
            raise PlaneRepositoryException("Invalid sorting criteria.")
        self._planes.sort(reverse=True, key=key_function)
    #-------------------- -------------------- --------------------


    # -------------------- UPDATE FUNCTION --------------------
    def update_plane(self, new_plane):
        """Function to update plane with a new plane or to sort planes.

        Args:
            new_plane (_type_): New plane that will replace the old plane.
        """
        if len(new_plane) == 3:
            command = new_plane[0]

            if command == "index":
                index, new = new_plane[1], new_plane[2]
                pass_list = []

                if new.get('passengers'):
                    for passenger in new['passengers']:
                        v = MyPassenger(passenger[0], passenger[1], passenger[2])
                        pass_list.append(v)
                    new['passengers'] = pass_list
                    repo = passengerRepository(pass_list)
                    new['passengers_list'] = repo

                passengers = passengerRepository(self._planes[index].get_passengers_list())
                plane = MyPlane(
                    int(new['plane_id']),
                    new['plane_name'],
                    int(new['capacity']),
                    new['destination'],
                    new.get('passengers_list', passengers)
                )
                self._planes[index] = plane
            elif command == "sort":
                criteria = new_plane[1]
                sub = new_plane[2] if criteria == 2 else None
                self.sort_planes(criteria, sub)
                return f"Planes sorted successfully!"
    #-------------------- -------------------- --------------------


    # -------------------- DELETE FUNCTION --------------------    
    def delete_plane(self, criteria):
        """A function to delete plane based on criteria.

        Args:
            criteria (_type_): Criteria for deletion.
        """
        if criteria[0] == "index":
            index = criteria[1]
            del self._planes[index]
        elif criteria[0]== "all":
            self._planes.clear()
    #-------------------- -------------------- --------------------



    # -------------------- BACKTRACKING FUNCTIONS --------------------
    @staticmethod
    def is_safe_plane(elem, current_list):
        if (elem.get_destination() != current_list[0].get_destination() or elem.get_airline() in [e.get_airline() for e in current_list]):
            return False
        return True
    @staticmethod
    def is_safe_passenger(elem, current_list):

       existing_last_names = {passenger.get_last_name() for passenger in current_list}

       if elem.get_last_name() in existing_last_names:
           return False
        
       return True
    

    def backtrack(self, domain: list, k: int, current_list: list, mode: str, results: list):
        """Backtrack function to form groups based on certain criteria.

        Args:
            domain (list): Domain to look into.
            k (int): Number of elements in the group.
            current_list (list): Current list we are working with.
            mode (str): Criteria to form groups.
            results (list): Final list of groups.
        """
        if len(current_list) == k:
            results.append(current_list.copy())
            
            group_count = len(results)
            if mode == "k-passengers":
                print(f"\n\n\n>>>>>>>>>>>>>>>>>> Generated passenger group {group_count} <<<<<<<<<<<<<<<<<<<\n", current_list, f"\n>>>>>>>>>>>>>>>>>>> End of passenger group {group_count} <<<<<<<<<<<<<<<<<<<<<")
            elif mode == "k-planes":
                print(f"\n\n\n>>>>>>>>>>>>>>>>>> Generated plane group {group_count} <<<<<<<<<<<<<<<<<<<\n", current_list, f"\n>>>>>>>>>>>>>>>>>>> End of plane group {group_count} <<<<<<<<<<<<<<<<<<<<<")
            return

        for i in range(len(domain)):
            if mode == "k-planes":
                if len(current_list) == 0 or self.is_safe_plane(domain[i], current_list):
                    current_list.append(domain[i])
                    self.backtrack(domain, k, current_list, mode, results)
                    current_list.pop()
            elif mode == "k-passengers":
                if len(current_list) == 0 or self.is_safe_passenger(domain[i], current_list):
                    current_list.append(domain[i])
                    self.backtrack(domain, k, current_list, mode, results)
                    current_list.pop()

    # -------------------- -------------------- --------------------
    def __len__(self):
        return len(self._planes)