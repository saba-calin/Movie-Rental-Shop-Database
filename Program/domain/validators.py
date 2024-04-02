import datetime


from Program.domain.validation_exceptions import ClientValidationException
from Program.domain.validation_exceptions import MovieValidationException
from Program.domain.validation_exceptions import RentalValidationException


class ClientValidator:
    def __init__(self):
        pass

    @staticmethod
    def validate_client(client, clients):
        errors = ""

        # Validating the id
        for elem in clients:
            if elem.get_client_id() == client.get_client_id():
                errors += "A client with this id already exists\n"

        # Validating the name
        client_name = client.get_name()
        client_name = client_name.strip()
        if client_name == "":
            errors += "The client name cannot be empty\n"
        if not client_name.isalpha():
            errors += "The client name cannot contain any special characters\n"

        if len(errors) > 0:
            raise ClientValidationException(errors)

    @staticmethod
    def validate_client_name(client):
        errors = ""

        client_name = client.get_name()
        client_name = client_name.strip()
        if client_name == "":
            errors += "The client name cannot be empty\n"
        if not client_name.isalpha():
            errors += "The client name cannot contain any special characters\n"

        if len(errors) > 0:
            raise Exception(errors)


class MovieValidator:
    def __init__(self):
        pass

    @staticmethod
    def validate_movie(movie, movies):
        errors = ""

        # Validating the id
        for elem in movies:
            if elem.get_movie_id() == movie.get_movie_id():
                errors += "A movie with this id already exists\n"

        # Validating the title
        movie_title = movie.get_title()
        movie_title = movie_title.strip()
        if movie_title == "":
            errors += "The movie title cannot be empty\n"

        temp = ""
        for char in movie_title:
            if char != " ":
                temp += char
        if not temp.isalpha():
            errors += "The movie title cannot contain any special characters\n"

        # Validating the description
        movie_description = movie.get_description()
        movie_description = movie_description.strip()
        if movie_description == "":
            errors += "The movie description cannot be empty\n"
        if not movie_description.isalpha():
            errors += "The movie description cannot contain any special characters\n"

        # Validating the genre
        movie_genre = movie.get_genre()
        movie_genre = movie_genre.strip()
        if movie_genre == "":
            errors += "The movie genre cannot be empty\n"
        if not movie_genre.isalpha():
            errors += "The movie genre cannot contain any special characters\n"

        if len(errors) > 0:
            raise MovieValidationException(errors)

    @staticmethod
    def validate_movie_title_description_genre(movie):
        errors = ""

        # Validating the title
        movie_title = movie.get_title()
        movie_title = movie_title.strip()
        if movie_title == "":
            errors += "The movie title cannot be empty\n"
        if not movie_title.isalpha():
            errors += "The movie title cannot contain any special characters\n"

        # Validating the description
        movie_description = movie.get_description()
        movie_description = movie_description.strip()
        if movie_description == "":
            errors += "The movie description cannot be empty\n"
        if not movie_description.isalpha():
            errors += "The movie description cannot contain any special characters\n"

        # Validating the genre
        movie_genre = movie.get_genre()
        movie_genre = movie_genre.strip()
        if movie_genre == "":
            errors += "The movie genre cannot be empty\n"
        if not movie_genre.isalpha():
            errors += "The movie genre cannot contain any special characters\n"

        if len(errors) > 0:
            raise Exception(errors)


class RentalValidator:
    def __init__(self):
        pass

    def validate_rental(self, rental, clients, movies, rentals):
        errors = ""

        for elem in rentals:
            if elem.get_rental_id() == rental.get_rental_id():
                errors += "There already is rental with the id you provided\n"
                break

        found = False
        for movie in movies:
            if movie.get_movie_id() == rental.get_movie_id():
                found = True
                break
        if found == False:
            errors += "There is no movie with the id you provided\n"

        found = False
        for client in clients:
            if client.get_client_id() == rental.get_client_id():
                found = True
                break
        if found == False:
            errors += "There is no client with the id you provided\n"

        for elem in rentals:
            if elem.get_movie_id() == rental.get_movie_id() and elem.get_returned_date() == "0":
                errors += "The movie with the id you provided is already rented\n"

        for elem in rentals:
            if elem.get_client_id() == rental.get_client_id():
                if self.is_late_return(elem) == True:
                    errors += "The client has had late returns in the past\n"
                    break

        rented_date = rental.get_rented_date().split("-")
        for i in range(len(rented_date)):
            rented_date[i] = int(rented_date[i])
        if len(rented_date) != 3:
            errors += "The returned date is invalid\n"
        else:
            rented_date = datetime.datetime(rented_date[2], rented_date[1], rented_date[0])

        due_date = rental.get_due_date().split("-")
        for i in range(len(due_date)):
            due_date[i] = int(due_date[i])
        if len(due_date) != 3:
            errors += "The due date is invalid\n"
        else:
            due_date = datetime.datetime(due_date[2], due_date[1], due_date[0])

        if due_date < rented_date:
            errors += "The due date cannot be less than the rented date"

        if len(errors) > 0:
            raise RentalValidationException(errors)

    @staticmethod
    def is_late_return(rental):
        if rental.get_returned_date() == "0":
            return False

        due_date = rental.get_due_date().split("-")
        returned_date = rental.get_returned_date().split("-")
        for i in range(len(due_date)):
            due_date[i] = int(due_date[i])
        for i in range(len(returned_date)):
            returned_date[i] = int(returned_date[i])

        due_time = datetime.datetime(due_date[2], due_date[1], due_date[0])
        returned_time = datetime.datetime(returned_date[2], returned_date[1], returned_date[0])
        if due_time < returned_time:
            return True
        return False
