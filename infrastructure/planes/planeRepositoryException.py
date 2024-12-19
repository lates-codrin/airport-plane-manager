class PlaneRepositoryException(Exception):
    '''
    Handles the errors appearing when working with class Vector Repository.
    '''

    def __init__(self, message):
        self.__message = message
        
        
    def __str__(self):
        return self.__message