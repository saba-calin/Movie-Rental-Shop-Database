import pickle


from Program.domain.movie import Movie


class MovieMemoryRepository:
    def __init__(self):
        self.__movies = []

    def get_movies(self):
        return self.__movies

    def add_movie(self, movie):
        self.__movies.append(movie)

    def remove_movie(self, movie):
        self.__movies.remove(movie)


class MovieTextFileRepository:
    def __init__(self, path):
        self.__movies_text_file = path

    def get_movies(self):
        movies = []

        f = open(self.__movies_text_file, "r")
        lines = f.readlines()
        for line in lines:
            info = line.split(", ")
            movie = Movie(int(info[0]), info[1], info[2], info[3].split("\n")[0])
            movies.append(movie)
        f.close()

        return movies

    def add_movie(self, movie):
        f = open(self.__movies_text_file, "a")
        f.write(movie.to_text_file_format())
        f.close()

    def remove_movie(self, movie):
        movies = self.get_movies()
        f = open(self.__movies_text_file, "w")
        for elem in movies:
            if elem.get_movie_id() != movie.get_movie_id():
                f.write(elem.to_text_file_format())
        f.close()


class MovieBinaryFileRepository:
    def __init__(self, path):
        self.__movies_binary_file = path

    def get_movies(self):
        movies = []

        f = open(self.__movies_binary_file, "rb")
        data = b' '
        try:
            while data:
                data = pickle.load(f)
                movie = Movie(data[0], data[1], data[2], data[3])
                movies.append(movie)
        except Exception:
            pass
        f.close()

        return movies

    def add_movie(self, movie):
        f = open(self.__movies_binary_file, "ab")
        pickle.dump(movie.to_binary_file_format(), f)
        f.close()

    def remove_movie(self, movie):
        movies = self.get_movies()
        f = open(self.__movies_binary_file, "wb")
        for elem in movies:
            if elem.get_movie_id() != movie.get_movie_id():
                pickle.dump(elem.to_binary_file_format(), f)
        f.close()
