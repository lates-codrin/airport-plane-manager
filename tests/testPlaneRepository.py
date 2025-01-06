import unittest
from domain.plane.plane import MyPlane
from infrastructure.planes.planeRepository import planeRepository
from domain.passenger.passenger import MyPassenger
from infrastructure.passengers.passengerRepository import passengerRepository

class TestVectorRepository(unittest.TestCase):

    def setUp(self):
        self.pass_repo = passengerRepository([MyPassenger("A","B","123"),MyPassenger("A1","B1","2123")])
        self.vector1 = MyPlane(0,"Delta Airlines", 84, "Australia", self.pass_repo)
        self.vector2 = MyPlane(1,"Spirit Airlines", 84, "United Kingdom", self.pass_repo)
        self.vector3 = MyPlane(2,"TAROM", 100, "Romania", self.pass_repo)
        self.vector4 = MyPlane(3,"Caryophyllaceae Airlines",82,"China", self.pass_repo)
        self.vector5=MyPlane(4,"Blechnaceae Airlines",68,"Indonesia", self.pass_repo)
        self.vector6=MyPlane(5,"Lamiaceae Airlines",43,"Philippines", self.pass_repo)
        self.vector7=MyPlane(6,"Cyperaceae Airlines",89,"China", self.pass_repo)
        self.vector8=MyPlane(7,"Rosaceae Airlines",46,"Indonesia", self.pass_repo)
        self.vector9=MyPlane(8,"Cyperaceae Airlines",52,"Cameroon", self.pass_repo)
        self.vector10=MyPlane(9,"Bruh Airlines",11,"Zimbabwe", self.pass_repo)
        self.repo = planeRepository([self.vector1, self.vector2])

    def test_get_all_planes(self):
        self.assertEqual(self.repo.get_all_planes(), [self.vector1, self.vector2])

    def test_get_plane_by_index(self):
        self.assertEqual(self.repo.get_plane_by_index(0), self.vector1)
        with self.assertRaises(Exception):
            self.repo.get_plane_by_index(999)

    def test_add_planes_to_repository(self):
        self.repo.add_planes_to_repository([self.vector3])
        self.assertIn(self.vector3, self.repo.get_all_planes())
        with self.assertRaises(Exception):
            self.repo.add_planes_to_repository("not a vector")


    def test_delete_plane(self):
        self.repo.delete_plane(("index", 0))
        self.assertEqual(len(self.repo.get_all_planes()), 1)
        with self.assertRaises(Exception):
            self.repo.delete_plane(("index", 5))
    
    def test_update_plane(self):
        new_plane = {
                        "plane_id": 3,
                        "plane_name": "Bluesky Airlines",
                        "capacity": 114,
                        "destination": "France",
                        "passengers_list": self.pass_repo
                    }
        self.repo.update_plane(("index",
                               0,new_plane))
        with self.assertRaises(Exception):
            self.repo.update_plane(1,2,3,4)


if __name__ == "__main__":
    unittest.main()
