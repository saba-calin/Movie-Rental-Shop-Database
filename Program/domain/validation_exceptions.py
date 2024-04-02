class ValidationException(Exception):
    def __init__(self, errors):
        self.__errors = errors

    def __str__(self):
        return "Validation Error: " + self.__errors


class ClientValidationException(ValidationException):
    def __init__(self, errors):
        ValidationException.__init__(self, errors)


class MovieValidationException(ValidationException):
    def __init__(self, errors):
        ValidationException.__init__(self, errors)


class RentalValidationException(ValidationException):
    def __init__(self, errors):
        ValidationException.__init__(self, errors)
