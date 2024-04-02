import datetime
import random
from datetime import date


from Program.domain.rental import Rental
from Program.repository.repository_exceptions import InvalidReturnDateException
from Program.repository.repository_exceptions import MovieDoesntExistsException
from Program.repository.repository_exceptions import MovieAlreadyReturnedException
from Program.repository.repository_exceptions import RentalDoesntExistsException

from Program.repository.rental_repository import RentalTextFileRepository
from Program.repository.rental_repository import RentalBinaryFileRepository


class RentalServices:
    def __init__(self, rental_repository, repository_validator, canGenerate, client_repository, movie_repository):
        self.__rental_repository = rental_repository
        self.__repository_validator = repository_validator
        self.__client_repository = client_repository
        self.__movie_repository = movie_repository

        if canGenerate == True:
            self.generate_rentals()

    def validate_and_add_rental(self, rental_id, movie_id, client_id, rented_date, due_date, returned_date,
                                clients, movies, rentals):
        clients = self.__client_repository.get_clients()
        movies = self.__movie_repository.get_movies()
        rentals = self.get_rentals()
        rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
        self.__repository_validator.validate_rental(rental, clients, movies, rentals)
        self.__rental_repository.add_rental(rental)

    def nullify_returned_date(self, rental_id):
        rentals = self.get_rentals()
        for rental in rentals:
            if rental.get_rental_id() == rental_id:
                rental.set_returned_date("0")

                if (isinstance(self.__rental_repository, RentalTextFileRepository) or
                        isinstance(self.__rental_repository, RentalBinaryFileRepository)):
                    for elem in rentals:
                        self.__rental_repository.remove_rental(elem)
                    for elem in rentals:
                        self.__rental_repository.add_rental(elem)

                return

    def return_movie(self, movie_id, returned_date):
        cpy = returned_date
        returned_date = returned_date.split("-")
        for i in range(len(returned_date)):
            returned_date[i] = int(returned_date[i])
        if len(returned_date) != 3:
            raise InvalidReturnDateException("The return date is invalid")
        else:
            returned_date = datetime.datetime(returned_date[2], returned_date[1], returned_date[0])

        found = False
        rentals = self.get_rentals()
        for rental in rentals:
            if rental.get_movie_id() == movie_id:
                found = True
                if rental.get_returned_date() == "0":

                    rented_date = rental.get_rented_date().split("-")
                    for i in range(len(rented_date)):
                        rented_date[i] = int(rented_date[i])
                    rented_date = datetime.datetime(rented_date[2], rented_date[1], rented_date[0])
                    if rented_date > returned_date:
                        raise InvalidReturnDateException("The returned date cannot be lower that the rented date")

                    rental.set_returned_date(cpy)

                    if (isinstance(self.__rental_repository, RentalTextFileRepository) or
                        isinstance(self.__rental_repository, RentalBinaryFileRepository)):
                        for elem in rentals:
                            self.__rental_repository.remove_rental(elem)
                        for elem in rentals:
                            self.__rental_repository.add_rental(elem)

                    return rental
        if found == False:
            raise MovieDoesntExistsException("There is no movie with the id you provided")
        raise MovieAlreadyReturnedException("The movie has already been returned")

    def get_late_rentals(self, current_date):
        arr1, arr2 = [], []

        date_time = current_date.split("-")
        for i in range(len(date_time)):
            date_time[i] = int(date_time[i])
        date_time = date(date_time[2], date_time[1], date_time[0])

        rentals = self.get_rentals()
        for rental in rentals:
            if rental.get_returned_date() == "0":
                due_time = rental.get_due_date().split("-")
                for i in range(len(due_time)):
                    due_time[i] = int(due_time[i])
                due_time = date(due_time[2], due_time[1], due_time[0])

                if date_time > due_time:
                    arr1.append(rental.get_movie_id())
                    arr2.append((date_time - due_time).days)

        for i in range(len(arr2)):
            for j in range(i, len(arr2)):
                if arr2[i] < arr2[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                    arr2[i], arr2[j] = arr2[j], arr2[i]

        arr = []
        for i in range(len(arr1)):
            arr.append((arr1[i], arr2[i]))
        return arr

    def remove_client_based_rentals(self, client_id):
        arr = []
        rentals = self.get_rentals()
        for rental in rentals:
            if rental.get_client_id() == client_id:
                arr.append(rental)
                self.__rental_repository.remove_rental(rental)
        return arr

    def add_multiple_rentals(self, rentals):
        for rental in rentals:
            self.__rental_repository.add_rental(rental)

    def remove_movie_based_rentals(self, movie_id):
        arr = []
        rentals = self.get_rentals()
        for rental in rentals:
            if rental.get_movie_id() == movie_id:
                arr.append(rental)
                self.__rental_repository.remove_rental(rental)
        return arr

    def remove_rental(self, rental_id):
        rentals = self.get_rentals()
        for rental in rentals:
            if rental.get_rental_id() == rental_id:
                self.__rental_repository.remove_rental(rental)
                return rental

        raise RentalDoesntExistsException("No rental with the id you provided was found")

    def get_rentals(self):
        return self.__rental_repository.get_rentals()

    def get_next_rental_id(self):
        rental_id = 0
        rentals = self.get_rentals()
        for rental in rentals:
            if rental.get_rental_id() > rental_id:
                rental_id = rental.get_rental_id()
        return rental_id + 1

    def generate_rentals(self):
        for i in range(20):
            rental_id = i
            movie_id = i
            client_id = i
            lower_bound = random.randint(1, 15)
            upper_bound = random.randint(15, 30)
            rented_date = str(lower_bound) + "-11-2023"
            returned_date = str(random.randint(lower_bound, upper_bound)) + "-11-2023"
            due_date = str(upper_bound) + "-11-2023"
            rental = Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)
            self.__rental_repository.add_rental(rental)
