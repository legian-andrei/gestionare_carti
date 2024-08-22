from Application.Scripts.audit_manager import *
from Application.Scripts.book_manager import *
from Application.Scripts.database_manager import *
from Application.Scripts.print_manager import *
from Application.Scripts.user_manager import *
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
        self.printer = PrintManager()


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
                self.printer.invalid_option()
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
                self.search_books_by_title()

            case '2':
                # 2. Cauta un autor
                self.search_books_by_author()

            case '3':
                # 3. Cauta autori dupa nationalitate
                self.search_authors_by_nationality()

            case '4':
                # 4. Cauta dupa ISBN
                self.search_book_by_isbn()

            case _:
                self.printer.invalid_option()
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
                self.search_books_by_title()

            case '2':
                # 2. Cauta un autor
                self.search_books_by_author()

            case '3':
                # 3. Cauta autori dupa nationalitate
                self.search_authors_by_nationality()

            case '4':
                # 4. Cauta dupa ISBN
                self.search_book_by_isbn()

            case '5':
                # 5. Adauga un autor
                self.create_author()

            case '6':
                # 6. Adauga o carte
                self.create_book()

            case '7':
                # 7. Afiseaza logurile pentru un anumit user
                self.show_audit()

            case '8':
                # 8. Cauta un user si promoveaza-l la admin
                self.search_user()

            case _:
                self.printer.invalid_option()
                return


    def create_account(self):
        print('\t\t\t\t\tIntrodu numele de utilizator:')
        username = input('\t\t\t\t\t-> ').strip()

        # Verific ca username-ul sa nu fie deja ales de un alt utilizator
        if self.db_manager.username_used(username):
            self.printer.username_used()
            return

        print('\t\t\t\t\tIntrodu parola:')
        password = pwinput.pwinput(prompt='\t\t\t\t\t-> ', mask='*').strip()

        print('\t\t\t\t\tConfirma parola:')
        confirm_password = pwinput.pwinput('\t\t\t\t\t-> ', mask='*').strip()

        # Verific ca parola sa fie aceeasi cu confirmarea
        if password != confirm_password:
            self.printer.password_mismatch()
            return

        # Verific ca numele si parola sa aiba o lungime minima de 3 caractere
        if len(username) < 3 or len(password) < 3:
            self.printer.invalid_credentials()
            return

        self.user_manager.create_account(username, password)
        self.printer.successful_register()


    def log_into_account(self):
        if self.user_manager.auth_attempts == 0:
            self.printer.limit_reached()
            return

        print('\t\t\t\t\tIntrodu numele de utilizator:')
        username = input('\t\t\t\t\t-> ').strip()
        print('\t\t\t\t\tIntrodu parola:')
        password = pwinput.pwinput('\t\t\t\t\t-> ', mask='*').strip()

        if len(username) == 0 or len(password) == 0:
            self.user_manager.auth_attempts -= 1
            self.printer.invalid_credentials(self.user_manager.auth_attempts)
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
            self.printer.invalid_data()
            return

        author = Author(first_name, last_name, nationality)

        if self.db_manager.author_exists(author):
            self.printer.author_already_exists()
            return

        self.author_manager.add_author(author)
        self.audit_manager.log_action(self.user_manager.current_user, f"adaugare autor {author.get_full_name()};")
        self.printer.author_added_successfully()


    def create_book(self):
        print('\t\t\t\t\tIntrodu titlul cartii:')
        title = input('\t\t\t\t\t-> ').strip().lower()
        if len(title) == 0:
            self.printer.invalid_data()
            return

        print('\t\t\t\t\tIntrodu anul publicarii cartii:')
        year = input('\t\t\t\t\t-> ').strip().lower()
        if not year.isdigit() or int(year) > datetime.datetime.now().year:
            self.printer.invalid_data()
            return

        print('\t\t\t\t\tIntrodu genul cartii:')
        genre = input('\t\t\t\t\t-> ').strip().lower()
        if len(genre) == 0:
            self.printer.invalid_data()
            return

        print('\t\t\t\t\tIntrodu numarul de autori:')
        authors_count = input('\t\t\t\t\t-> ').strip()
        if not authors_count.isdigit() or int(authors_count) < 1:
            self.printer.invalid_data()
            return

        authors_id = []

        for i in range(int(authors_count)):
            print('\t\t\t\t\tIntrodu prenumele autorului:')
            first_name = input('\t\t\t\t\t-> ').strip().lower()

            print('\t\t\t\t\tIntrodu numele autorului:')
            last_name = input('\t\t\t\t\t-> ').strip().lower()

            current_author_id = self.author_manager.get_author_id(Author(first_name, last_name, ''))
            if current_author_id is None or current_author_id in authors_id:
                self.printer.author_not_found()
                return

            authors_id.append(current_author_id)

        book = Book(title=title, authors=authors_id, year=year, genre=genre)
        self.book_manager.add_book(book)
        self.audit_manager.log_action(self.user_manager.current_user, f"adaugare carte {book.title};")
        self.printer.book_added_successfully()


    def search_book_by_isbn(self):
        """
        Functie pentru cautarea unei carti dupa ISBN.
        """
        print('\t\t\t\t\tIntrodu ISBN-ul cartii:')
        isbn = input('\t\t\t\t\t-> ').strip().lower()
        if len(isbn) == 0:
            self.printer.invalid_data()
            return

        self.audit_manager.log_action(self.user_manager.current_user, f"cautare carte dupa ISBN: {isbn};")

        book = self.db_manager.get_book_by_isbn(isbn)
        if book is None:
            self.printer.book_not_found()
            return

        self.printer.book_found(book)


    def search_authors_by_nationality(self):
        """
        Functie pentru cautarea autorilor dupa nationalitate.
        """
        print('\t\t\t\t\tIntrodu tara dorita:')
        nationality = input('\t\t\t\t\t-> ').strip().lower()

        if len(nationality) == 0:
            self.printer.invalid_data()
            return

        self.audit_manager.log_action(self.user_manager.current_user, f"cautare autori dupa nationalitate: {nationality};")

        authors = self.author_manager.get_authors_by_nationality(nationality)

        if authors is None:
            self.printer.author_with_nationality_not_found()
            return

        self.printer.authors_found(authors)


    def search_books_by_author(self):
        """
        Functie pentru cautarea unor carti dupa autor.
        """
        print('\t\t\t\t\tIntrodu prenumele autorului:')
        first_name = input('\t\t\t\t\t-> ').strip().lower()

        print('\t\t\t\t\tIntrodu numele autorului:')
        last_name = input('\t\t\t\t\t-> ').strip().lower()

        if len(first_name) == 0 or len(last_name) == 0:
            self.printer.invalid_data()
            return

        self.audit_manager.log_action(self.user_manager.current_user, f"cautare carti dupa autor: {first_name} {last_name};")

        author_id = self.author_manager.get_author_id(Author(first_name, last_name, ''))
        if author_id is None:
            self.printer.author_not_found()
            return

        books = self.author_manager.get_books_by_author(author_id)
        if books is None:
            self.printer.author_without_books()
            return

        self.printer.books_found(books)


    def search_books_by_title(self):
        """
        Functie pentru cautarea unei carti dupa titlu.
        """
        print('\t\t\t\t\tIntrodu titlul cartii:')
        title = input('\t\t\t\t\t-> ').strip().lower()
        if len(title) == 0:
            self.printer.invalid_data()
            return

        self.audit_manager.log_action(self.user_manager.current_user, f"cautare carti dupa titlu: {title};")

        books = self.book_manager.get_books_by_title(title)

        if books is None:
            self.printer.books_with_title_not_found()
            return

        self.printer.books_found(books)


    def search_user(self):
        """
        Functie pentru cautarea unui user si promovarea acestuia la admin.
        """
        print('\t\t\t\t\tIntrodu numele de utilizator:')
        username = input('\t\t\t\t\t-> ').strip()

        if len(username) == 0:
            self.printer.invalid_data()
            return

        self.audit_manager.log_action(self.user_manager.current_user, f"cautare user: {username};")

        user = self.user_manager.get_user_by_username(username)

        if user is None:
            self.printer.user_not_found()
            return

        print(user)
        if isinstance(user, LoggedInUser):
            self.printer.promote_user_message()
            inp = input('\t\t\t\t\t-> ').strip()
            if len(inp) == 0:
                return
            elif inp == '1':
                self.user_manager.promote_user_to_admin(user)
                self.audit_manager.log_action(self.user_manager.current_user, f"promovare user la admin: {username};")
                self.printer.user_promoted_successfully()
                return
        else:
            input('\t\t\t\t\tApasa ENTER pentru a continua.')
            return

    def show_audit(self):
        """
        Functie pentru afisarea logurilor pentru un anumit user.
        """
        print('\t\t\t\t\tIntrodu numele de utilizator:')
        username = input('\t\t\t\t\t-> ').strip()

        if len(username) == 0:
            self.printer.invalid_data()
            return

        self.audit_manager.log_action(self.user_manager.current_user, f"cautare loguri pentru user: {username};")

        user = self.user_manager.get_user_by_username(username)

        if user is None:
            self.printer.user_not_found()
            return

        logs = self.audit_manager.get_logs_for_user(user)

        if logs is None:
            self.printer.logs_not_found()
            return

        self.printer.logs_found(logs)
