class ServicesException(Exception):
    def __init__(self, errors):
        self.__errors = errors

    def __str__(self):
        return "Repository exception: " + self.__errors


class ClientDoesntExistsException(ServicesException):
    def __init__(self, errors):
        ServicesException.__init__(self, errors)


class MovieDoesntExistsException(ServicesException):
    def __init__(self, errors):
        ServicesException.__init__(self, errors)


class RentalDoesntExistsException(ServicesException):
    def __init__(self, errors):
        ServicesException.__init__(self, errors)


class InvalidReturnDateException(ServicesException):
    def __init__(self, errors):
        ServicesException.__init__(self, errors)


class MovieAlreadyReturnedException(ServicesException):
    def __init__(self, errors):
        ServicesException.__init__(self, errors)


class InvalidRepositoryException(ServicesException):
    def __init__(self, errors):
        ServicesException.__init__(self, errors)
