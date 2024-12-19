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
    
    # 2
    def get_all_planes(self) -> list:
        """Get the planes inside the repository

        Returns:
            self._planes: List containing planes in repository
        """
        return self._planes
    
    # 3
    def get_plane_by_index(self, index : int) -> MyPlane:
        """Get the plane at the specified index.

        Raises:
            PlaneRepositoryException: In case the index is negative, out of bounds or non integer.

        Returns:
            self._planes[index]: plane at specified index.
        """
        if index < 0 or index >= len(self._planes) or type(index) != int:
            raise PlaneRepositoryException("Index is out of bounds.")
        return self._planes[index]
    
    def add_planes_to_repository(self, planes):
        if type(planes) != list:
            raise Exception("[P-R] Not a list.")
        for plane in planes:
            self._planes.append(plane)
    
    
    '''def sort_by_number_of_passengers(self):
        def criteria(p):
            return len(p.get_passengers_list())
        self._planes.sort(reverse=True,key=criteria)

    def sort_by_number_of_passengers_with_first_name(self, sub):
        def criteria(p):
            return len([x for x in p.get_passengers_list() if x.get_first_name().startswith(sub)])
        self._planes.sort(reverse=True,key=criteria)
    
    def sort_by_concatenation(self):
        def criteria(p):
            new_str = str(len(p.get_passengers_list())) + str(p.get_destination())
            return new_str
        self._planes.sort(reverse=True,key=criteria)'''
    
    def sort_planes(self, criteria=None, sub=None):
        if criteria == 1:
            key_function = lambda p: len(p.get_passengers_list())
        elif criteria == 2:
            key_function = lambda p: len([x for x in p.get_passengers_list() if x.get_first_name().startswith(sub)])
        elif criteria == 3:
            key_function = lambda p: str(len(p.get_passengers_list())) + str(p.get_destination())
        else:
            raise ValueError("Invalid sorting criteria")
        print(type(criteria))
        self._planes.sort(reverse=True, key=key_function)
        


    
    # identify planes that have passengers with passport numbers starting with the same 3 letters 

    def get_planes_by_passport_number(self):
        found_planes = []
        for plane in self._planes:
            passengers = plane.get_passengers_list()

            if passengers:
                to_search = passengers[0].get_passport_number()[0:3]
                found_mismatch = False
                for passenger in passengers:
                    if passenger.get_passport_number()[0:3] != to_search:
                        found_mismatch = True
                        continue
                if not found_mismatch:
                    found_planes.append(plane)
        return found_planes
    
    def get_planes_by_passenger_name(self, name):
        found_planes = []
        for plane in self._planes:
            passengers = plane.get_passengers_list()
            if passengers:
                found_passenger = False
                for passenger in passengers:
                    if passenger.get_first_name() == name or passenger.get_last_name() == name:
                        found_passenger = True
                        continue
                if found_passenger:
                    found_planes.append(plane)
        
        if len(found_planes) == 0:
            return f"No planes found with name {name}"
        return found_planes
    
    def get_passengers_with_name(self, name):
        found_passengers = []
        for plane in self._planes:
            passengers = plane.get_passengers_list()
            for passenger in passengers:
                if passenger.get_first_name().find(name) != -1 or passenger.get_last_name().find(name) != -1:
                    found_passengers.append(passenger)
    
        if len(found_passengers) == 0:
            return f"No passengers found with name {name}"
        return found_passengers
    
    """def update_plane(self, new_plane):
        if len(new_plane) == 3:
            command = new_plane[0]
            
            if command == "index":
                index, new = new_plane[1], new_plane[2]
                pass_list = []
                for passenger in new['passengers_list']:
                    v = MyPassenger(passenger[0], passenger[1], passenger[2])
                    pass_list.append(v)
                new['passengers_list'] = pass_list
                repo = passengerRepository(new['passengers_list'])
                new['passengers_list'] = repo
                plane = MyPlane(
                    int(new['number']),
                    new['airline'],
                    int(new['seats']),
                    new['destination'],
                    new['passengers_list']
                )
                self._planes[index] = plane
            
            elif command == "sort":
                criteria = new_plane[1]
                sub = new_plane[2] if criteria == 2 else None
                self.sort_planes(criteria, sub)
                return f"Planes sorted successfully!"""
    
    def update_plane(self, new_plane):
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

        
    def delete_plane(self, criteria):
        if criteria[0] == "index":
            index = criteria[1]
            del self._planes[index]
        elif criteria[0]== "all":
            self._planes.clear()
    
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
    
    '''def backtrack(self, domain: list, k: int, current_list: list, mode: str):
        group_count = 0
        if len(current_list) == k:
            group_count += 1
            if mode == "k-passengers":
                print(f"\n\n\n>>>>>>>>>>>>>>>>>> Generated passenger group {group_count} <<<<<<<<<<<<<<<<<<<\n", current_list, f"\n>>>>>>>>>>>>>>>>>>> End of passenger group {group_count} <<<<<<<<<<<<<<<<<<<<<")
            elif mode == "k-planes":
                print(f"\n\n\n>>>>>>>>>>>>>>>>>> Generated plane group {group_count} <<<<<<<<<<<<<<<<<<<\n", current_list, f"\n>>>>>>>>>>>>>>>>>>> End of plane group {group_count} <<<<<<<<<<<<<<<<<<<<<")
            return
        for i in range(len(domain)):
            if mode == "k-planes":
                if len(current_list) == 0 or self.is_safe_plane(domain[i], current_list):
                    current_list.append(domain[i])
                    self.backtrack(domain, k, current_list, mode)
                    current_list.pop()
            elif mode == "k-passengers":
                if len(current_list) == 0 or self.is_safe_passenger(domain[i], current_list):
                    current_list.append(domain[i])
                    self.backtrack(domain, k, current_list, mode)
                    current_list.pop()'''

    def backtrack(self, domain: list, k: int, current_list: list, mode: str, results: list):
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


    def __len__(self):
        return len(self._planes)