from abc import ABC, abstractmethod


class User(ABC):
    """
    Interfata abstracta pentru utilizatori.
    """

    @abstractmethod
    def show_menu(self):
        """
        Afiseaza meniul specific utilizatorului.
        """
        pass


class GuestUser(User):
    """
    Clasa pentru utilizatorii neconectati.
    """

    def show_menu(self):
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|               Sa incepem!              |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|          1. Creeaza un cont            |')
        print('\t\t\t\t|          2. Conecteaza-te              |')
        print('\t\t\t\t------------------------------------------')


class LoggedInUser(User):
    """
    Clasa pentru utilizatorii conectati.
    """
    def __init__(self, id, username):
        self.id = id
        self.username = username

    def show_menu(self):
        print('\t\t\t\t------------------------------------------')
        print(f'\t\t\t\t          Bine ai venit, {self.username}!             ')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|    1. Cauta o carte                    |')
        print('\t\t\t\t|    2. Cauta un autor                   |')
        print('\t\t\t\t|    3. Cauta autori dupa nationalitate  |')
        print('\t\t\t\t|    4. Cauta dupa ISBN                  |')
        print('\t\t\t\t------------------------------------------')


class AdminUser(LoggedInUser):
    """
    Clasa pentru administratori.
    """
    def show_menu(self):
        print('\t\t\t\t------------------------------------------')
        print(f'\t\t\t\t          Bine ai venit, {self.username}!             ')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|    1. Cauta o carte                    |')
        print('\t\t\t\t|    2. Cauta un autor                   |')
        print('\t\t\t\t|    3. Cauta autori dupa nationalitate  |')
        print('\t\t\t\t|    4. Cauta dupa ISBN                  |')
        print('\t\t\t\t|    5. Adauga un autor                  |')
        print('\t\t\t\t|    6. Adauga o carte                   |')
        print('\t\t\t\t------------------------------------------')
