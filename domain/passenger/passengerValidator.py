from domain.passenger.passengerException import PassengerException
class PassengerValidator:
    def validate(self, s):
        err = ""
        if not isinstance(s.get_first_name(), str) or not isinstance(s.get_last_name(), str) or not isinstance(s.get_passport_number(), str):
            err+= "One of the arguments provided is not of type `str`."
            
        if err != "":
            raise PassengerException(err)
