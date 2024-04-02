class Client:
    def __init__(self, client_id, name):
        self.__client_id = client_id
        self.__name = name

    def __str__(self):
        return f"id: {self.__client_id}, name: {self.__name}"

    def get_client_id(self):
        return self.__client_id

    def get_name(self):
        return self.__name

    def set_client_id(self, client_id):
        self.__client_id = client_id

    def set_name(self, name):
        self.__name = name

    def to_text_file_format(self):
        return f"{self.__client_id}, {self.__name}\n"

    def to_binary_file_format(self):
        return self.__client_id, self.__name
