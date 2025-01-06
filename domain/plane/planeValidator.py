from domain.plane.plane import PlaneException
from infrastructure.passengers.passengerRepository import passengerRepository

class PlaneValidator:
    def validate(self, s):
        err = ""
        number = s.get_number()
        airline = s.get_airline()
        seats = s.get_seats()
        destination = s.get_destination()
        passengers_list = s.get_passengers_list()

        if not isinstance(number, int) or not isinstance(airline, str) or not isinstance(seats, int) or not isinstance(destination, str) or not isinstance(passengers_list, list):
            err += "One of the arguments provided not of correct type."
        if len(passengers_list) > seats:
            err += "Too many passengers are aboard the plane."

        if err != "":
            raise PlaneException(err)
