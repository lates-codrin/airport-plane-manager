from domain.passenger.passengerException import PassengerException
class PlaneValidator:
    def validate(self, s):
        err = ""
        # handle stuff here but im too lazy
        if err != "":
            raise PassengerException(err)
