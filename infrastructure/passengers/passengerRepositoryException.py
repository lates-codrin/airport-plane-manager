class PassengerRepositoryException(Exception):
    '''
    Handles the errors appearing when working with class Passenger Repository.
    '''

    def __init__(self, message):
        self.__message = message
        
        
    def __str__(self):
        return "[PA-R]" + self.__message