from audit_manager import *
from author import *
from author_manager import *
from book import *
from book_manager import *
from database_manager import *
from user_manager import *
import pwinput
import datetime


class Application:
    """
    Clasa principala care contine toate obiectele si functiile necesare pentru functionarea aplicatiei.
    """
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.audit_manager = AuditManager(self.db_manager)
        self.user_manager = UserManager(self.db_manager, self.audit_manager)
        self.author_manager = AuthorManager(self.db_manager)
        self.book_manager = BookManager(self.db_manager)


    def run(self):
        """
        Functie care ruleaza aplicatia.
        """
        while True:
            self.user_manager.show_current_menu()
            print('\t\t\t\t\tApasa ENTER pentru a iesi.')
            print('\t\t\t\t\tIntrodu optiunea ta:')
            choice = input('\t\t\t\t\t-> ').strip()

            if len(choice) == 0:
                break

            if isinstance(self.user_manager.current_user, GuestUser):
                self.handle_guest_user_choice(choice)
            elif isinstance(self.user_manager.current_user, AdminUser):
                self.handle_admin_user_choice(choice)
            elif isinstance(self.user_manager.current_user, LoggedInUser):
                self.handle_logged_in_user_choice(choice)


    def handle_guest_user_choice(self, choice):
        """
        Functie pentru gestionarea optiunilor utilizatorilor neconectati.
        :param choice: alegerea facuta de utilizator
        """
        match choice:
            case '1':
                # 1. Creeaza un cont
                self.create_account()

            case '2':
                # 2. Conecteaza-te
                self.log_into_account()

            case _:
                self.print_invalid_option()
                return


    def handle_logged_in_user_choice(self, choice):
        """
        Functie pentru gestionarea optiunilor utilizatorilor conectati.
        :param choice: alegerea facuta de utilizator
        :return:
        """
        match choice:
            case '1':
                # 1. Cauta o carte
                pass
            case '2':
                # 2. Cauta un autor
                pass
            case '3':
                # 3. Cauta autori dupa nationalitate
                pass
            case '4':
                # 4. Cauta dupa ISBN
                pass
            case _:
                self.print_invalid_option()
                return


    def handle_admin_user_choice(self, choice):
        """
        Functie pentru gestionarea optiunilor administratorilor.
        :param choice: alegerea facuta de utilizator
        :return:
        """
        match choice:
            case '1':
                # 1. Cauta o carte
                pass
            case '2':
                # 2. Cauta un autor
                pass
            case '3':
                # 3. Cauta autori dupa nationalitate
                pass
            case '4':
                # 4. Cauta dupa ISBN
                pass
            case '5':
                # 5. Adauga un autor
                self.create_author()

            case '6':
                # 6. Adauga o carte
                self.create_book()
            case _:
                self.print_invalid_option()
                return


    def create_account(self):
        print('\t\t\t\t\tIntrodu numele de utilizator:')
        username = input('\t\t\t\t\t-> ').strip()

        # Verific ca username-ul sa nu fie deja ales de un alt utilizator
        if self.db_manager.username_used(username):
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|    Numele de utilizator exista deja.   |')
            print('\t\t\t\t------------------------------------------')
            input('\t\t\t\t\tApasa ENTER pentru a continua.')
            return

        print('\t\t\t\t\tIntrodu parola:')
        password = pwinput.pwinput(prompt='\t\t\t\t\t-> ', mask='*').strip()

        print('\t\t\t\t\tConfirma parola:')
        confirm_password = pwinput.pwinput('\t\t\t\t\t-> ', mask='*').strip()

        # Verific ca parola sa fie aceeasi cu confirmarea
        if password != confirm_password:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|        Parolele nu coincid!           |')
            print('\t\t\t\t------------------------------------------')
            input('\t\t\t\t\tApasa ENTER pentru a continua.')
            return

        # Verific ca numele si parola sa aiba o lungime minima de 3 caractere
        if len(username) < 3 or len(password) < 3:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|          Credentiale invalide!         |')
            print('\t\t\t\t------------------------------------------')
            input('\t\t\t\t\tApasa ENTER pentru a continua.')
            return

        self.user_manager.create_account(username, password)
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|     Contul a fost creat cu succes!     |')
        print('\t\t\t\t------------------------------------------')


    def log_into_account(self):
        if self.user_manager.auth_attempts == 0:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|      Ai atins limita de incercari.     |')
            print('\t\t\t\t------------------------------------------')
            input('\t\t\t\t\tApasa ENTER pentru a continua.')
            return

        print('\t\t\t\t\tIntrodu numele de utilizator:')
        username = input('\t\t\t\t\t-> ').strip()
        print('\t\t\t\t\tIntrodu parola:')
        password = pwinput.pwinput('\t\t\t\t\t-> ', mask='*').strip()

        if len(username) == 0 or len(password) == 0:
            self.user_manager.auth_attempts -= 1
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|          Credentiale invalide!         |')
            print(f'\t\t\t\t|          Incercari ramase: {self.user_manager.auth_attempts}          |')
            print('\t\t\t\t------------------------------------------')
            return

        self.user_manager.login(username, password)


    def create_author(self):
        print('\t\t\t\t\tIntrodu prenumele autorului:')
        first_name = input('\t\t\t\t\t-> ').strip().lower()

        print('\t\t\t\t\tIntrodu numele autorului:')
        last_name = input('\t\t\t\t\t-> ').strip().lower()

        print('\t\t\t\t\tIntrodu tara din care provine autorul:')
        nationality = input('\t\t\t\t\t-> ').strip().lower()

        if len(first_name) == 0 or len(last_name) == 0 or len(nationality) == 0:
            self.print_invalid_data()
            return

        author = Author(first_name, last_name, nationality)

        if self.db_manager.author_exists(author):
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|   Autorul exista deja in baza de date. |')
            print('\t\t\t\t------------------------------------------')
            input('\t\t\t\t\tApasa ENTER pentru a continua.')
            return

        self.author_manager.add_author(author)
        self.audit_manager.log_action(self.user_manager.current_user, f"adaugare autor {author.get_full_name()};")
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|     Autorul a fost adaugat cu succes!  |')
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def create_book(self):
        print('\t\t\t\t\tIntrodu titlul cartii:')
        title = input('\t\t\t\t\t-> ').strip().lower()
        if len(title) == 0:
            self.print_invalid_data()
            return

        print('\t\t\t\t\tIntrodu anul publicarii cartii:')
        year = input('\t\t\t\t\t-> ').strip().lower()
        if not year.isdigit() or int(year) > datetime.datetime.now().year:
            self.print_invalid_data()
            return

        print('\t\t\t\t\tIntrodu genul cartii:')
        genre = input('\t\t\t\t\t-> ').strip().lower()
        if len(genre) == 0:
            self.print_invalid_data()
            return

        print('\t\t\t\t\tIntrodu numarul de autori:')
        authors_count = input('\t\t\t\t\t-> ').strip()
        if not authors_count.isdigit() or int(authors_count) < 1:
            self.print_invalid_data()
            return

        authors_id = []

        for i in range(int(authors_count)):
            print('\t\t\t\t\tIntrodu prenumele autorului:')
            first_name = input('\t\t\t\t\t-> ').strip().lower()

            print('\t\t\t\t\tIntrodu numele autorului:')
            last_name = input('\t\t\t\t\t-> ').strip().lower()

            current_author_id = self.author_manager.get_author_id(Author(first_name, last_name, ''))
            if current_author_id is None or current_author_id in authors_id:
                print('\t\t\t\t------------------------------------------')
                print('\t\t\t\t|   Autorul nu exista in baza de date.   |')
                print('\t\t\t\t------------------------------------------')
                input('\t\t\t\t\tApasa ENTER pentru a continua.')
                return

            authors_id.append(current_author_id)

        book = Book(title=title, authors=authors_id, year=year, genre=genre)
        self.book_manager.add_book(book)
        self.audit_manager.log_action(self.user_manager.current_user, f"adaugare carte {book.title};")

        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|     Cartea a fost adaugata cu succes!  |')
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def print_invalid_option(self):
        """
        Functie pentru afisarea unui mesaj de eroare pentru optiunile invalide.
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|   Optiunea aleasa nu este una valita.  |')
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def print_invalid_data(self):
        """
        Functie pentru afisarea unui mesaj de eroare pentru date invalide.
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|              Date invalide!            |')
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')