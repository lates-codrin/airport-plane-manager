class PassengerException(Exception):
    def __init__(self, message):
        self.__message = message
        
        
    def __str__(self):
        return "D-PA"+self.__message
