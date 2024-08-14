from abc import ABC, abstractmethod


class User(ABC):
    """Interfata abstracta pentru utilizatori."""

    @abstractmethod
    def show_menu(self):
        """Afiseaza meniul specific utilizatorului."""
        pass


class GuestUser(User):
    """Clasa pentru utilizatorii neconectati."""

    def show_menu(self):
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|               Sa incepem!              |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|          1. Creeaza un cont            |')
        print('\t\t\t\t|          2. Conecteaza-te              |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t\tApasa ENTER pentru a iesi.')
        print('\t\t\t\t\tIntrodu optiunea ta:')


class LoggedInUser(User):
    """Clasa pentru utilizatorii conectati."""

    def show_menu(self):
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|             Bine ai venit!             |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|    1. Cauta o carte                    |')
        print('\t\t\t\t|    2. Cauta un autor                   |')
        print('\t\t\t\t|    3. Cauta autori dupa nationalitate  |')
        print('\t\t\t\t|    4. Cauta dupa ISBN                  |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t\tApasa ENTER pentru a iesi.')
        print('\t\t\t\t\tIntrodu optiunea ta:')


class AdminUser(User):
    """Clasa pentru administratori."""

    def show_menu(self):
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|             Bine ai venit!             |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|    1. Cauta o carte                    |')
        print('\t\t\t\t|    2. Cauta un autor                   |')
        print('\t\t\t\t|    3. Cauta autori dupa nationalitate  |')
        print('\t\t\t\t|    4. Cauta dupa ISBN                  |')
        print('\t\t\t\t|    5. Adauga un autor                  |')
        print('\t\t\t\t|    6. Adauga o carte                   |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t\tApasa ENTER pentru a iesi.')
        print('\t\t\t\t\tIntrodu optiunea ta:')


# GuestUser().show_menu()
# LoggedInUser().show_menu()
# AdminUser().show_menu()
