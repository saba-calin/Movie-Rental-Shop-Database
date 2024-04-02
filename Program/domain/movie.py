class Movie:
    def __init__(self, movie_id, title, description, genre):
        self.__movie_id = movie_id
        self.__title = title
        self.__description = description
        self.__genre = genre

    def __str__(self):
        return (f"id: {self.__movie_id}, title: {self.__title}, description: {self.__description}, "
                f"genre: {self.__genre}")

    def get_movie_id(self):
        return self.__movie_id

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_genre(self):
        return self.__genre

    def set_movie_id(self, movie_id):
        self.__movie_id = movie_id

    def set_title(self, title):
        self.__title = title

    def set_description(self, description):
        self.__description = description

    def set_genre(self, genre):
        self.__genre = genre

    def to_text_file_format(self):
        return f"{self.__movie_id}, {self.__title}, {self.__description}, {self.__genre}\n"

    def to_binary_file_format(self):
        return self.__movie_id, self.__title, self.__description, self.__genre
