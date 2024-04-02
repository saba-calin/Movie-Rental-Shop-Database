import random
from datetime import date
from copy import deepcopy


from Program.domain.movie import Movie
from Program.repository.repository_exceptions import MovieDoesntExistsException


class MovieServices:
    def __init__(self, movie_repository, movie_validator, canGenerate):
        self.__movie_repository = movie_repository
        self.__movie_validator = movie_validator

        if canGenerate == True:
            self.generate_movies()

    def validate_and_add_movie(self, movie_id, movie_title, movie_description, movie_genre, movies):
        movies = self.get_movies()
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        self.__movie_validator.validate_movie(movie, movies)
        self.__movie_repository.add_movie(movie)

    def remove_movie(self, movie_id):
        movies = self.get_movies()
        for movie in movies:
            if movie.get_movie_id() == movie_id:
                self.__movie_repository.remove_movie(movie)
                return movie

        raise MovieDoesntExistsException("No movie with the id you provided was found")

    def modify_movie(self, old_id, new_id, new_title, new_description, new_genre):
        new_movie = Movie(new_id, new_title, new_description, new_genre)
        movies = self.get_movies()

        if old_id == new_id:
            self.__movie_validator.validate_movie_title_description_genre(new_movie)
            for movie in movies:
                if movie.get_movie_id() == old_id:
                    cpy = deepcopy(movie)
                    movie.set_title(new_title)
                    movie.set_description(new_description)
                    movie.set_genre(new_genre)
                    return cpy
            raise MovieDoesntExistsException("No movie with the id you provided was found")

        self.__movie_validator.validate_movie(new_movie, movies)
        for movie in movies:
            if movie.get_movie_id() == old_id:
                cpy = deepcopy(movie)
                movie.set_movie_id(new_id)
                movie.set_title(new_title)
                movie.set_description(new_description)
                movie.set_genre(new_genre)
                return cpy
        raise MovieDoesntExistsException("No movie with the id you provided was found")

    def get_movies(self):
        return self.__movie_repository.get_movies()

    def get_movies_by_id(self, movie_id):
        arr = []
        movies = self.get_movies()
        for movie in movies:
            if movie.get_movie_id() == movie_id:
                arr.append(movie)
        return arr

    def get_movies_by_title(self, movie_title):
        arr = []
        movies = self.get_movies()
        for movie in movies:
            temp = movie.get_title()
            temp = temp.lower()
            if movie_title in temp:
                arr.append(movie)
        return arr

    def get_movies_by_description(self, movie_description):
        arr = []
        movies = self.get_movies()
        for movie in movies:
            temp = movie.get_description()
            temp = temp.lower()
            if movie_description in temp:
                arr.append(movie)
        return arr

    def get_movies_by_genre(self, movie_genre):
        arr = []
        movies = self.get_movies()
        for movie in movies:
            temp = movie.get_genre()
            temp = temp.lower()
            if movie_genre in temp:
                arr.append(movie)
        return arr

    def get_most_rented_movies(self, rentals):
        dict = {}

        for rental in rentals:
            if rental.get_returned_date() == "0":
                continue

            rented_time = rental.get_rented_date().split("-")
            for i in range(len(rented_time)):
                rented_time[i] = int(rented_time[i])
            rented_time = date(rented_time[2], rented_time[1], rented_time[0])
            returned_time = rental.get_returned_date().split("-")
            for i in range(len(returned_time)):
                returned_time[i] = int(returned_time[i])
            returned_time = date(returned_time[2], returned_time[1], returned_time[0])

            days = (returned_time - rented_time).days + 1
            movie = self.get_movies_by_id(rental.get_movie_id())[0]

            if movie.get_title() in dict:
                dict[movie.get_title()] += days
            else:
                dict[movie.get_title()] = days

        arr1 = list(dict)
        arr2 = list(dict.values())
        for i in range(len(arr2)):
            for j in range(i, len(arr2)):
                if arr2[i] < arr2[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                    arr2[i], arr2[j] = arr2[j], arr2[i]

        arr = []
        for i in range(len(arr1)):
            arr.append((arr1[i], arr2[i]))
        return arr

    def get_next_movie_id(self):
        movie_id = 0
        movies = self.get_movies()
        for movie in movies:
            if movie.get_movie_id() > movie_id:
                movie_id = movie.get_movie_id()
        return movie_id + 1

    def generate_movies(self):
        arr1 = ["Adventurous", "Mysterious", "Enchanting", "Thrilling", "Epic", "Whimsical",
                "Daring", "Spectacular", "Intriguing", "Fantastic"]
        arr2 = ["Journey", "Quest", "Mystery", "Adventure", "Discovery", "Enigma", "Legacy",
                "Odyssey", "Legend", "Miracle"]
        for i in range(20):
            movie_id = i
            movie_title = random.choice(arr1) + " " + random.choice(arr2)
            movie_description = random.choice(arr1)
            movie_genre = random.choice(arr2)
            movie = Movie(movie_id, movie_title, movie_description, movie_genre)
            self.__movie_repository.add_movie(movie)
