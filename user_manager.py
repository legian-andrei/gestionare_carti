import hashlib
from users import *


class UserManager:
    """
    Clasa pentru gestionarea utilizatorilor.
    """
    def __init__(self, db_manager, audit_manager):
        self.current_user = GuestUser()
        self.db_manager = db_manager
        self.audit_manager = audit_manager

    def show_current_menu(self):
        """
        Functie pentru afisarea meniului utilizatorului curent.
        """
        self.current_user.show_menu()

    def create_account(self, username, password):
        """
        Functie pentru crearea unui utilizator nou.

        :param username: numele de utilizator
        :param password: parola
        """
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user_data = {
            'username': username,
            'password': hashed_password,
            'role': 'user'
        }
        self.db_manager.add_entry('users', user_data)
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|     Contul a fost creat cu succes!     |')
        print('\t\t\t\t------------------------------------------')
        # self.audit_manager.log_action(self.current_user, "creare cont;")


    def login(self, username, password):
        """
        Functie pentru conectarea unui utilizator.

        :param username:
        :param password:
        """
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user_data = {
            'username': username,
            'password': hashed_password
        }
        user = self.db_manager.authenticate_user(user_data)
        if user:
            if user[2] == 'admin':
                self.current_user = AdminUser(user[0], user[1])
            elif user[2] == 'user':
                self.current_user = LoggedInUser(user[0], user[1])
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|        Te-ai conectat cu succes!       |')
            print('\t\t\t\t------------------------------------------')
            self.audit_manager.log_action(self.current_user, "conectare;")
        else:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t| Nume de utilizator sau parola gresite! |')
            print('\t\t\t\t------------------------------------------')