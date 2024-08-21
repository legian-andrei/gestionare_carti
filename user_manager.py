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
        self.auth_attempts = 5


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
            self.auth_attempts = 5
            self.audit_manager.log_action(self.current_user, "conectare;")
        else:
            self.auth_attempts -= 1
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t| Nume de utilizator sau parola gresite! |')
            print(f'\t\t\t\t|          Incercari ramase: {self.auth_attempts}          |')
            print('\t\t\t\t------------------------------------------')

    def get_user_by_username(self, username):
        """
        Functie pentru obtinerea unui utilizator dupa username.
        :param username: numele de utilizator
        :return: obiect de tip User sau None daca nu exista utilizatorul
        """
        user_query = "SELECT id, username, role FROM users WHERE username = %s"
        user_query_result = self.db_manager.execute_query(query=user_query, params=(username,), fetch_one=True)
        if user_query_result is None:
            return None

        if user_query_result[2] == 'admin':
            user = AdminUser(user_query_result[0], user_query_result[1])
        elif user_query_result[2] == 'user':
            user = LoggedInUser(user_query_result[0], user_query_result[1])
        return user

    def promote_user_to_admin(self, user):
        """
        Functie pentru promovarea unui utilizator la rol de admin.
        :param user: obiect de tip User
        """
        update_query = "UPDATE users SET role = 'admin' WHERE id = %s"
        self.db_manager.execute_query(query=update_query, params=(user.id,))
