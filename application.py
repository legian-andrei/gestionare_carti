from audit_manager import *
from database_manager import *
from user_manager import *
import pwinput


class Application:
    """
    Clasa principala care contine toate obiectele si functiile necesare pentru functionarea aplicatiei.
    """
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.audit_manager = AuditManager(self.db_manager)
        self.user_manager = UserManager(self.db_manager, self.audit_manager)


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
            elif isinstance(self.user_manager.current_user, LoggedInUser):
                self.handle_logged_in_user_choice(choice)
            elif isinstance(self.user_manager.current_user, AdminUser):
                self.handle_admin_user_choice(choice)


    def handle_guest_user_choice(self, choice):
        """
        Functie pentru gestionarea optiunilor utilizatorilor neconectati.
        :param choice: alegerea facuta de utilizator
        """
        match choice:
            case '1':
                # 1. Creeaza un cont
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

            case '2':
                # 2. Conecteaza-te
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
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|          Credentiale invalide!         |')
                    print(f'\t\t\t\t|          Incercari ramase: {self.user_manager.auth_attempts}          |')
                    print('\t\t\t\t------------------------------------------')
                    self.user_manager.auth_attempts -= 1
                    return

                self.user_manager.login(username, password)

            case _:
                self.print_invalid_option()
                return


    def print_invalid_option(self):
        """
        Functie pentru afisarea unui mesaj de eroare pentru optiunile invalide.
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|   Optiunea aleasa nu este una valita.  |')
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def handle_logged_in_user_choice(self, choice):
        """
        Functie pentru gestionarea optiunilor utilizatorilor conectati.
        :param choice: alegerea facuta de utilizator
        :return:
        """
        match choice:
            case 1:
                # 1. Cauta o carte
                pass
            case 2:
                # 2. Cauta un autor
                pass
            case 3:
                # 3. Cauta autori dupa nationalitate
                pass
            case 4:
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
            case 1:
                # 1. Cauta o carte
                pass
            case 2:
                # 2. Cauta un autor
                pass
            case 3:
                # 3. Cauta autori dupa nationalitate
                pass
            case 4:
                # 4. Cauta dupa ISBN
                pass
            case 5:
                # 5. Adauga un autor
                pass
            case 6:
                # 6. Adauga o carte
                pass
            case _:
                self.print_invalid_option()
                return
