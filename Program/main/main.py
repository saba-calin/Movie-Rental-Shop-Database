import configparser


from Program.services.client_services import ClientServices
from Program.repository.client_repository import ClientMemoryRepository
from Program.repository.client_repository import ClientTextFileRepository
from Program.repository.client_repository import ClientBinaryFileRepository
from Program.domain.validators import ClientValidator

from Program.services.movie_services import MovieServices
from Program.repository.movie_repository import MovieMemoryRepository
from Program.repository.movie_repository import MovieTextFileRepository
from Program.repository.movie_repository import MovieBinaryFileRepository
from Program.domain.validators import MovieValidator

from Program.services.rental_services import RentalServices
from Program.repository.rental_repository import RentalMemoryRepository
from Program.repository.rental_repository import RentalTextFileRepository
from Program.repository.rental_repository import RentalBinaryFileRepository
from Program.domain.validators import RentalValidator

from Program.services.undo_services import UndoServices
from Program.repository.repository_exceptions import InvalidRepositoryException
from Program.ui.user_interface import UserInterface

if __name__ == "__main__":
    config = configparser.RawConfigParser()
    config.read("../files/settings.properties")
    repo = config["Repository"]
    clients_path = repo["clients"][1:-1]
    movies_path = repo["movies"][1:-1]
    rentals_path = repo["rentals"][1:-1]

    # Clients
    client_repository = None
    canGenerate = False
    if repo["repository"] == "inmemory":
        client_repository = ClientMemoryRepository()
        canGenerate = True
    elif repo["repository"] == "textfiles":
        client_repository = ClientTextFileRepository(clients_path)
        f = open(clients_path, "r")
        if f.read() == "":
            canGenerate = True
        f.close()
    elif repo["repository"] == "binaryfiles":
        client_repository = ClientBinaryFileRepository(clients_path)
        f = open(clients_path, "rb")
        if f.read() == b"":
            canGenerate = True
        f.close()
    else:
        raise InvalidRepositoryException("Invalid repository")
    client_validator = ClientValidator()
    client_services = ClientServices(client_repository, client_validator, canGenerate)

    # Movies
    movie_repository = None
    canGenerate = False
    if repo["repository"] == "inmemory":
        movie_repository = MovieMemoryRepository()
        canGenerate = True
    elif repo["repository"] == "textfiles":
        movie_repository = MovieTextFileRepository(movies_path)
        f = open(movies_path, "r")
        if f.read() == "":
            canGenerate = True
        f.close()
    elif repo["repository"] == "binaryfiles":
        movie_repository = MovieBinaryFileRepository(movies_path)
        f = open(movies_path, "rb")
        if f.read() == b"":
            canGenerate = True
        f.close()
    else:
        raise InvalidRepositoryException("Invalid repository")
    movie_validator = MovieValidator()
    movie_services = MovieServices(movie_repository, movie_validator, canGenerate)

    # Rentals
    rental_repository = None
    canGenerate = False
    if repo["repository"] == "inmemory":
        rental_repository = RentalMemoryRepository()
        canGenerate = True
    elif repo["repository"] == "textfiles":
        rental_repository = RentalTextFileRepository(rentals_path)
        f = open(rentals_path, "r")
        if f.read() == "":
            canGenerate = True
        f.close()
    elif repo["repository"] == "binaryfiles":
        rental_repository = RentalBinaryFileRepository(rentals_path)
        f = open(rentals_path, "rb")
        if f.read() == b"":
            canGenerate = True
        f.close()
    else:
        raise InvalidRepositoryException("Invalid repository")
    rental_validator = RentalValidator()
    rental_services = RentalServices(rental_repository, rental_validator, canGenerate, client_repository, movie_repository)

    undo_services = UndoServices()

    ui = UserInterface(client_services, movie_services, rental_services, undo_services)
    ui.start_program()



# [Repository]
# repository = inmemory
# clients = ""
# movies = ""
# rentals = ""
#
# [Repository]
# repository = textfiles
# clients = "../files/clients.txt"
# movies = "../files/movies.txt"
# rentals = "../files/rentals.txt"
#
# [Repository]
# repository = binaryfiles
# clients = "../files/clients.dat"
# movies = "../files/movies.dat"
# rentals = "../files/rentals.dat"
