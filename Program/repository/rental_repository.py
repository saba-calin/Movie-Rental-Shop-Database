import pickle


from Program.domain.rental import Rental


class RentalMemoryRepository:
    def __init__(self):
        self.__rentals = []

    def get_rentals(self):
        return self.__rentals

    def add_rental(self, rental):
        self.__rentals.append(rental)

    def remove_rental(self, rental):
        self.__rentals.remove(rental)


class RentalTextFileRepository:
    def __init__(self, path):
        self.__rentals_text_file = path

    def get_rentals(self):
        rentals = []

        f = open(self.__rentals_text_file, "r")
        lines = f.readlines()
        for line in lines:
            info = line.split(", ")
            rental = Rental(int(info[0]), int(info[1]), int(info[2]), info[3], info[4], info[5].split("\n")[0])
            rentals.append(rental)
        f.close()

        return rentals

    def add_rental(self, rental):
        f = open(self.__rentals_text_file, "a")
        f.write(rental.to_text_file_format())
        f.close()

    def remove_rental(self, rental):
        rentals = self.get_rentals()
        f = open(self.__rentals_text_file, "w")
        for elem in rentals:
            if elem.get_rental_id() != rental.get_rental_id():
                f.write(elem.to_text_file_format())
        f.close()


class RentalBinaryFileRepository:
    def __init__(self, path):
        self.__rentals_binary_file = path

    def get_rentals(self):
        rentals = []

        f = open(self.__rentals_binary_file, "rb")
        data = b' '
        try:
            while data:
                data = pickle.load(f)
                rental = Rental(data[0], data[1], data[2], data[3], data[4], data[5])
                rentals.append(rental)
        except Exception:
            pass
        f.close()

        return rentals

    def add_rental(self, rental):
        f = open(self.__rentals_binary_file, "ab")
        pickle.dump(rental.to_binary_file_format(), f)
        f.close()

    def remove_rental(self, rental):
        rentals = self.get_rentals()
        f = open(self.__rentals_binary_file, "wb")
        for elem in rentals:
            if elem.get_rental_id() != rental.get_rental_id():
                pickle.dump(elem.to_binary_file_format(), f)
        f.close()
