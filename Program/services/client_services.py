import random
from datetime import date
from copy import deepcopy


from Program.domain.client import Client
from Program.repository.repository_exceptions import ClientDoesntExistsException


class ClientServices:
    def __init__(self, client_repository, client_validator, canGenerate):
        self.__client_repository = client_repository
        self.__client_validator = client_validator

        if canGenerate == True:
            self.generate_clients()

    def validate_and_add_client(self, client_id, client_name, clients):
        clients = self.get_clients()
        client = Client(client_id, client_name)
        self.__client_validator.validate_client(client, clients)
        self.__client_repository.add_client(client)

    def remove_client(self, client_id):
        clients = self.get_clients()
        for client in clients:
            if client.get_client_id() == client_id:
                self.__client_repository.remove_client(client)
                return client

        raise ClientDoesntExistsException("No client with the id you provided was found")

    def get_clients_by_id(self, client_id):
        arr = []
        clients = self.get_clients()
        for client in clients:
            if client.get_client_id() == client_id:
                arr.append(client)
        return arr

    def get_clients_by_name(self, client_name):
        arr = []
        clients = self.get_clients()
        for client in clients:
            temp = client.get_name()
            temp = temp.lower()
            if client_name in temp:
                arr.append(client)
        return arr

    def get_clients(self):
        return self.__client_repository.get_clients()

    def modify_client(self, old_id, new_id, new_name):
        new_client = Client(new_id, new_name)
        clients = self.get_clients()

        if old_id == new_id:
            self.__client_validator.validate_client_name(new_client)
            for client in clients:
                if client.get_client_id() == old_id:
                    cpy = deepcopy(client)
                    client.set_name(new_name)
                    return cpy
            raise ClientDoesntExistsException("No client with the id you provided was found")

        self.__client_validator.validate_client(new_client, clients)
        for client in clients:
            if client.get_client_id() == old_id:
                cpy = deepcopy(client)
                client.set_client_id(new_id)
                client.set_name(new_name)
                return cpy
        raise ClientDoesntExistsException("No client with the id you provided was found")

    def get_client_name_by_id(self, client_id):
        clients = self.get_clients()
        for client in clients:
            if client.get_client_id() == client_id:
                return client.get_name()
        raise ClientDoesntExistsException("No client with the id you provided was found")

    @staticmethod
    def get_most_active_clients(rentals):
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
            client_id = rental.get_client_id()

            if client_id in dict:
                dict[client_id] += days
            else:
                dict[client_id] = days

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

    def get_next_client_id(self):
        client_id = 0
        clients = self.get_clients()
        for client in clients:
            if client.get_client_id() > client_id:
                client_id = client.get_client_id()
        return client_id + 1

    def generate_clients(self):
        names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Henry", "Ivy", "Jack",
                 "Kate", "Leo", "Mia", "Nathan", "Olivia", "Peter", "Quinn", "Rachel", "Sam", "Tina",
                 "Ulysses", "Victoria", "Walter", "Xena", "Yasmine", "Zach"]
        for i in range(20):
            client = Client(i, random.choice(names))
            self.__client_repository.add_client(client)
