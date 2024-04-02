from Program.services.undo_services import UndoServices, FunctionCall, Operation


class UserInterface:
    def __init__(self, client_services, movie_services, rental_services, undo_services):
        self.__client_services = client_services
        self.__movie_services = movie_services
        self.__rental_services = rental_services
        self.__undo_services = undo_services

    def start_program(self):
        while True:
            self.__print_menu()
            option = input()

            try:
                if option == "1":
                    # Managing the clients
                    self.__print_manage_clients_menu()
                    op = input()
                    if op == "1":
                        self.__add_client()
                    elif op == "2":
                        self.__remove_client()
                    elif op == "3":
                        self.__modify_client()
                    elif op == "4":
                        self.__print_clients()
                    else:
                        raise Exception("The input is invalid!")

                elif option == "2":
                    # Managing the movies
                    self.__print_manage_movies_menu()
                    op = input()
                    if op == "1":
                        self.__add_movie()
                    elif op == "2":
                        self.__remove_movie()
                    elif op == "3":
                        self.__modify_movie()
                    elif op == "4":
                        self.__print_movies()
                    else:
                        raise Exception("The input is invalid!")

                elif option == "3":
                    # Managing the rentals
                    self.__print_manage_rentals_menu()
                    op = input()
                    if op == "1":
                        self.__rent_movie()
                    elif op == "2":
                        self.__return_movie()
                    elif op == "3":
                        self.__print_rentals()
                    else:
                        raise Exception("The input in invalid!")

                elif option == "4":
                    # Searching for clients
                    self.__print_search_for_clients_menu()
                    op = input()
                    if op == "1":
                        self.__search_for_clients_by_id()
                    elif op == "2":
                        self.__search_for_clients_by_name()
                    else:
                        raise Exception("The input is invalid!")

                elif option == "5":
                    # Searching for movies
                    self.__print_search_for_movies_menu()
                    op = input()
                    if op == "1":
                        self.__search_for_movies_by_id()
                    elif op == "2":
                        self.__search_for_movies_by_title()
                    elif op == "3":
                        self.__search_for_movies_by_description()
                    elif op == "4":
                        self.__search_for_movies_by_genre()
                    else:
                        raise Exception("The input is invalid!")

                elif option == "6":
                    self.__print_statistics_menu()
                    op = input()
                    if op == "1":
                        self.__print_most_rented_movies()
                    elif op == "2":
                        self.__print_most_active_clients()
                    elif op == "3":
                        self.__print_late_rentals()
                    else:
                        raise Exception("The input is invalid!")

                elif option == "7":
                    self.__undo_services.undo()

                elif option == "8":
                    self.__undo_services.redo()

                elif option == "exit":
                    exit()
                else:
                    raise Exception("The input is invalid!")
            except Exception as exception:
                print(str(exception))

    @staticmethod
    def __print_menu():
        print("")
        print("Press 1 to manage clients.")
        print("Press 2 to manage movies.")
        print("Press 3 to manage rentals.")
        print("Press 4 to search for clients.")
        print("Press 5 to search for movies.")
        print("Press 6 to create statistics.")
        print("Press 7 to undo the last operation.")
        print("Press 8 to redo the last operation.")
        print("Type \"exit\" to exit the application.")

    @staticmethod
    def __print_manage_clients_menu():
        print("")
        print("Press 1 to add a client.")
        print("Press 2 to delete a client.")
        print("Press 3 to modify the list of clients.")
        print("Press 4 to display the list of clients.")

    @staticmethod
    def __print_manage_movies_menu():
        print("")
        print("Press 1 to add a movie.")
        print("Press 2 to delete a movie")
        print("Press 3 to modify the list of movies")
        print("Press 4 to display the list movies.")

    @staticmethod
    def __print_manage_rentals_menu():
        print("")
        print("Press 1 to rent a movie.")
        print("Press 2 to return a movie")
        print("Press 3 to display the list of rentals")

    @staticmethod
    def __print_search_for_clients_menu():
        print("")
        print("Press 1 to search for clients by id.")
        print("Press 2 to search for clients by name.")

    @staticmethod
    def __print_search_for_movies_menu():
        print("")
        print("Press 1 to search for movies by id.")
        print("Press 2 to search for movies by title")
        print("Press 3 to search for movies by description")
        print("Press 4 to search for movies by genre")

    @staticmethod
    def __print_statistics_menu():
        print("")
        print("Press 1 to display the most rented movies.")
        print("Press 2 to display the most active clients.")
        print("Press 3 to display the late rentals.")

    def __search_for_clients_by_id(self):
        client_id = int(input("id = "))
        clients = self.__client_services.get_clients_by_id(client_id)

        if len(clients) == 0:
            print("There are no clients with the id you provided")
            return

        for client in clients:
            print(client)

    def __search_for_clients_by_name(self):
        client_name = input("name = ")
        client_name = client_name.lower()
        clients = self.__client_services.get_clients_by_name(client_name)

        if len(clients) == 0:
            print("There are no clients with the id you provided")
            return

        for client in clients:
            print(client)

    def __search_for_movies_by_id(self):
        movie_id = int(input("id = "))
        movies = self.__movie_services.get_movies_by_id(movie_id)

        if len(movies) == 0:
            print("There are no movies with the id you provided")
            return

        for movie in movies:
            print(movie)

    def __search_for_movies_by_title(self):
        movie_title = input("title = ")
        movie_title = movie_title.lower()
        movies = self.__movie_services.get_movies_by_title(movie_title)

        if len(movies) == 0:
            print("There are no movies with the title you provided")
            return

        for movie in movies:
            print(movie)

    def __search_for_movies_by_description(self):
        movie_description = input("description = ")
        movie_description = movie_description.lower()
        movies = self.__movie_services.get_movies_by_description(movie_description)

        if len(movies) == 0:
            print("There are no movies with the description you provided")
            return

        for movie in movies:
            print(movie)

    def __search_for_movies_by_genre(self):
        movie_genre = input("genre = ")
        movie_genre = movie_genre.lower()
        movies = self.__movie_services.get_movies_by_genre(movie_genre)

        if len(movies) == 0:
            print("There are no movies with the genre you provided")
            return

        for movie in movies:
            print(movie)

    def __print_most_rented_movies(self):
        movies = self.__movie_services.get_most_rented_movies(self.__rental_services.get_rentals())

        if len(movies) == 0:
            print("There are no movies in the list")
            return

        for movie in movies:
            print("title: " + movie[0] + ", days: " + str(movie[1]))

    def __print_most_active_clients(self):
        clients = self.__client_services.get_most_active_clients(self.__rental_services.get_rentals())

        if len(clients) == 0:
            print("The are no clients in the list")
            return

        for client in clients:
            print("client: " + self.__client_services.get_client_name_by_id(client[0]) + ", days: " + str(client[1]))

    def __print_late_rentals(self):
        current_date = input("current date(dd-mm-yyyy) = ")
        rentals = self.__rental_services.get_late_rentals(current_date)

        if len(rentals) == 0:
            print("There are no late rentals in the list")
            return

        for rental in rentals:
            print("movie id: " + str(rental[0]) + ", days: " + str(rental[1]))

    def __rent_movie(self):
        rental_id = self.__rental_services.get_next_rental_id()
        movie_id = int(input("movie id = "))
        client_id = int(input("client id = "))
        rented_date = input("rented date(dd-mm-yyyy) = ")
        due_date = input("due date(dd-mm-yyyy) = ")
        returned_date = "0"
        self.__rental_services.validate_and_add_rental(rental_id, movie_id, client_id, rented_date, due_date,
                                                       returned_date, self.__client_services.get_clients(),
                                                       self.__movie_services.get_movies(),
                                                       self.__rental_services.get_rentals())

        redo = FunctionCall(self.__rental_services.validate_and_add_rental, rental_id, movie_id,
                            client_id, rented_date, due_date, returned_date,
                            self.__client_services.get_clients(), self.__movie_services.get_movies(),
                            self.__rental_services.get_rentals())
        undo = FunctionCall(self.__rental_services.remove_rental, rental_id)
        self.__undo_services.record(Operation(undo, redo))

    def __return_movie(self):
        movie_id = int(input("movie id = "))
        returned_date = input("returned date(dd-mm-yyyy) = ")
        rental = self.__rental_services.return_movie(movie_id, returned_date)

        redo = FunctionCall(self.__rental_services.return_movie, movie_id, returned_date)
        undo = FunctionCall(self.__rental_services.nullify_returned_date, rental.get_rental_id())
        self.__undo_services.record(Operation(undo, redo))

    def __add_client(self):
        client_id = self.__client_services.get_next_client_id()
        client_name = input("name = ")
        self.__client_services.validate_and_add_client(client_id, client_name, self.__client_services.get_clients())

        undo = FunctionCall(self.__client_services.remove_client, client_id)
        redo = FunctionCall(self.__client_services.validate_and_add_client, client_id, client_name,
                            self.__client_services.get_clients())
        self.__undo_services.record(Operation(undo, redo))


    def __add_movie(self):
        movie_id = self.__movie_services.get_next_movie_id()
        movie_title = input("title = ")
        movie_description = input("description = ")
        movie_genre = input("genre = ")
        self.__movie_services.validate_and_add_movie(movie_id, movie_title, movie_description, movie_genre,
                                                     self.__movie_services.get_movies())

        undo = FunctionCall(self.__movie_services.remove_movie, movie_id)
        redo = FunctionCall(self.__movie_services.validate_and_add_movie, movie_id, movie_title,
                            movie_description, movie_genre, self.__movie_services.get_movies())
        self.__undo_services.record(Operation(undo, redo))

    def __remove_client(self):
        client_id = int(input("id = "))
        removed_client = self.__client_services.remove_client(client_id)

        redo = FunctionCall(self.__client_services.remove_client, client_id)
        undo = FunctionCall(self.__client_services.validate_and_add_client, client_id,
                            removed_client.get_name(),
                            self.__client_services.get_clients())
        self.__undo_services.record(Operation(undo, redo))

        removed_rentals = self.__rental_services.remove_client_based_rentals(client_id)

        redo = FunctionCall(self.__rental_services.remove_client_based_rentals, client_id)
        undo = FunctionCall(self.__rental_services.add_multiple_rentals, removed_rentals)
        self.__undo_services.record(Operation(undo, redo))

    def __remove_movie(self):
        movie_id = int(input("id = "))
        removed_movie = self.__movie_services.remove_movie(movie_id)

        redo = FunctionCall(self.__movie_services.remove_movie, movie_id)
        undo = FunctionCall(self.__movie_services.validate_and_add_movie, movie_id,
                            removed_movie.get_title(), removed_movie.get_description(),
                            removed_movie.get_genre(), self.__movie_services.get_movies())
        self.__undo_services.record(Operation(undo, redo))

        removed_rentals = self.__rental_services.remove_movie_based_rentals(movie_id)

        redo = FunctionCall(self.__rental_services.remove_movie_based_rentals, movie_id)
        undo = FunctionCall(self.__rental_services.add_multiple_rentals, removed_rentals)
        self.__undo_services.record(Operation(undo, redo))

    def __modify_client(self):
        old_id = int(input("id of the client you want to modify = "))
        new_id = int(input("new id = "))
        new_name = input("new name = ")
        modified_client = self.__client_services.modify_client(old_id, new_id, new_name)

        redo = FunctionCall(self.__client_services.modify_client, old_id, new_id, new_name)
        undo = FunctionCall(self.__client_services.modify_client, new_id, old_id, modified_client.get_name())
        self.__undo_services.record(Operation(undo, redo))

    def __modify_movie(self):
        old_id = int(input("id of the movie you want to modify = "))
        new_id = int(input("new id = "))
        new_title = input("mew title = ")
        new_description = input("new description = ")
        new_genre = input("new genre = ")
        modified_movie = self.__movie_services.modify_movie(old_id, new_id, new_title, new_description, new_genre)

        redo = FunctionCall(self.__movie_services.modify_movie, old_id, new_id, new_title, new_description,
                            new_genre)
        undo = FunctionCall(self.__movie_services.modify_movie, new_id, old_id, modified_movie.get_title(),
                            modified_movie.get_description(), modified_movie.get_genre())
        self.__undo_services.record(Operation(undo, redo))

    def __print_clients(self):
        clients = self.__client_services.get_clients()

        if len(clients) == 0:
            print("There are no clients in the list")
            return

        for client in clients:
            print(client)

    def __print_movies(self):
        movies = self.__movie_services.get_movies()

        if len(movies) == 0:
            print("There are no movies in the list")
            return

        for movie in movies:
            print(movie)

    def __print_rentals(self):
        rentals = self.__rental_services.get_rentals()

        if len(rentals) == 0:
            print("There are no rentals in the list")
            return

        for rental in rentals:
            print(rental)
