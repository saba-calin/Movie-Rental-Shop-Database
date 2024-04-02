import pickle


from Program.domain.client import Client


class ClientMemoryRepository:
    def __init__(self):
        self.__clients = []

    def get_clients(self):
        return self.__clients

    def add_client(self, client):
        self.__clients.append(client)

    def remove_client(self, client):
        self.__clients.remove(client)


class ClientTextFileRepository:
    def __init__(self, path):
        self.__clients_text_file = path

    def get_clients(self):
        clients = []

        f = open(self.__clients_text_file, "r")
        lines = f.readlines()
        for line in lines:
            info = line.split(", ")
            client = Client(int(info[0]), info[1].split("\n")[0])
            clients.append(client)
        f.close()

        return clients

    def add_client(self, client):
        f = open(self.__clients_text_file, "a")
        f.write(client.to_text_file_format())
        f.close()

    def remove_client(self, client):
        clients = self.get_clients()
        f = open(self.__clients_text_file, "w")
        for elem in clients:
            if elem.get_client_id() != client.get_client_id():
                f.write(elem.to_text_file_format())
        f.close()


class ClientBinaryFileRepository:
    def __init__(self, path):
        self.__clients_binary_file = path

    def get_clients(self):
        clients = []

        f = open(self.__clients_binary_file, "rb")
        data = b' '
        try:
            while data:
                data = pickle.load(f)
                client = Client(data[0], data[1])
                clients.append(client)
        except Exception:
            pass
        f.close()

        return clients

    def add_client(self, client):
        f = open(self.__clients_binary_file, "ab")
        pickle.dump(client.to_binary_file_format(), f)
        f.close()

    def remove_client(self, client):
        clients = self.get_clients()
        f = open(self.__clients_binary_file, "wb")
        for elem in clients:
            if elem.get_client_id() != client.get_client_id():
                pickle.dump(elem.to_binary_file_format(), f)
        f.close()
