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

    def __str__(self):
        lines = [
            f"ID: {self.id}",
            f"Username: {self.username}",
            "Role: Regular User"
        ]

        max_length = 38

        # Formateaza fiecare linie sa inceapa si sa se termine cu '|'
        formatted_fields = [f"| {line.ljust(max_length)} |" for line in lines]
        formatted_fields[0] = "\t\t\t\t" + formatted_fields[0]

        # Adauga linia de sus si linia de jos
        border_line = f"\t\t\t\t{'-' * (max_length + 4)}"

        return f"{border_line}\n" + '\n\t\t\t\t'.join(formatted_fields) + f"\n{border_line}"


class AdminUser(User):
    """
    Clasa pentru administratori.
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
        print('\t\t\t\t|    5. Adauga un autor                  |')
        print('\t\t\t\t|    6. Adauga o carte                   |')
        print('\t\t\t\t|    7. Afiseaza logurile pentru         |')
        print('\t\t\t\t|    un anumit user                      |')
        print('\t\t\t\t|    8. Cauta un utilizator              |')
        print('\t\t\t\t------------------------------------------')

    def __str__(self):
        lines = [
            f"ID: {self.id}",
            f"Username: {self.username}",
            "Role: Admin"
        ]

        max_length = 38

        # Formateaza fiecare linie sa inceapa si sa se termine cu '|'
        formatted_fields = [f"| {line.ljust(max_length)} |" for line in lines]
        formatted_fields[0] = "\t\t\t\t" + formatted_fields[0]

        # Adauga linia de sus si linia de jos
        border_line = f"\t\t\t\t{'-' * (max_length + 4)}"

        return f"{border_line}\n" + '\n\t\t\t\t'.join(formatted_fields) + f"\n{border_line}"
