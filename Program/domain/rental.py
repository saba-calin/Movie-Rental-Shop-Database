class Rental:
    def __init__(self, rental_id, movie_id, client_id, rented_date, due_date, returned_date):
        self.__rental_id = rental_id
        self.__movie_id = movie_id
        self.__client_id = client_id
        self.__rented_date = rented_date
        self.__due_date = due_date
        self.__returned_date = returned_date

    def __str__(self):
        return (f"rental id: {self.__rental_id}, movie id: {self.__movie_id}, client id: {self.__client_id}, "
                f"rented date: {self.__rented_date}, due date: {self.__due_date}, "
                f"returned date: {self.__returned_date}")

    def get_rental_id(self):
        return self.__rental_id

    def get_movie_id(self):
        return self.__movie_id

    def get_client_id(self):
        return self.__client_id

    def get_rented_date(self):
        return self.__rented_date

    def get_due_date(self):
        return self.__due_date

    def get_returned_date(self):
        return self.__returned_date

    def set_returned_date(self, returned_date):
        self.__returned_date = returned_date

    def to_text_file_format(self):
        return (f"{self.__rental_id}, {self.__movie_id}, {self.__client_id}, "
                f"{self.__rented_date}, {self.__due_date}, {self.__returned_date}\n")

    def to_binary_file_format(self):
        return (self.__rental_id, self.__movie_id, self.__client_id,
                self.__rented_date, self.__due_date, self.__returned_date)
