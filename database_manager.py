import hashlib

import mysql.connector
from mysql.connector import errorcode


class DatabaseManager:
    """
    Clasa pentru gestionarea bazei de date.
    """
    def __init__(self, host='localhost', user='root', password='rootpa55', database='BookLibrary'):
        """
        Constructor pentru DatabaseManager cu parametrii de conectare

        :param host: Database host
        :param user: Database user
        :param password: Database password
        :param database: Database name
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

        self.connect()

    def connect(self):
        """
        Functie pentru conectarea la baza de date si creerea cursorului
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\tConectarea la server s-a realizat cu succes.')
            print('\t\t\t\t------------------------------------------')
            self.setup_database()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('\t\t\t\t------------------------------------------')
                print('\t\t\tCeva este in neregula. Credentialele bazei de date sunt gresite.')
                print('\t\t\t\t------------------------------------------')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('\t\t\t\t------------------------------------------')
                print('\t\t\t\tCeva este in neregula. Baza de date nu exista.')
                print('\t\t\t\t------------------------------------------')
            else:
                print(f"Error: {err}")


    def setup_database(self):
        """
        Functie pentru crearea tabelelor si inserarea unor valori default
        """
        self.create_tables()
        self.insert_default_data()

    def create_tables(self):
        """
        Functie pentru crearea tabelelor (daca nu exista)
        """
        TABLES = {}
        TABLES['users'] = (
            "CREATE TABLE users ("
            "  id INT AUTO_INCREMENT,"
            "  username VARCHAR(50) NOT NULL UNIQUE,"
            "  password VARCHAR(255) NOT NULL,"
            "  role ENUM('user', 'admin') NOT NULL,"
            "  PRIMARY KEY (id)"
            ")"
        )

        TABLES['audit'] = (
            "CREATE TABLE audit ("
            "  id INT AUTO_INCREMENT,"
            "  user_id INT,"
            "  time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
            "  action VARCHAR(255) NOT NULL,"
            "  PRIMARY KEY (id),"
            "  CONSTRAINT audit_users_fk FOREIGN KEY (user_id)"
            "    REFERENCES users(id)"
            ")"
        )

        TABLES['authors'] = (
            "CREATE TABLE authors ("
            "  id INT AUTO_INCREMENT,"
            "  last_name VARCHAR(255) NOT NULL,"
            "  first_name VARCHAR(255) NOT NULL,"
            "  nationality VARCHAR(50),"
            "  PRIMARY KEY (id)"
            ")"
        )

        TABLES['nationalities'] = (
            "CREATE TABLE nationalities ("
            "  code VARCHAR(8),"
            "  country VARCHAR(255) NOT NULL,"
            "  PRIMARY KEY (code)"
            ")"
        )

        TABLES['books'] = (
            "CREATE TABLE books ("
            "  isbn VARCHAR(14),"
            "  title VARCHAR(255) NOT NULL,"
            "  year INT,"
            "  genre VARCHAR(50),"
            "  PRIMARY KEY (isbn)"
            ")"
        )

        TABLES['books_authors'] = (
            "CREATE TABLE books_authors ("
            "  book_isbn VARCHAR(14),"
            "  author_id INT,"
            "  PRIMARY KEY (book_isbn, author_id),"
            "  CONSTRAINT books_authors_book_isbn_fk FOREIGN KEY (book_isbn)"
            "    REFERENCES books(isbn) ON DELETE CASCADE,"
            "  CONSTRAINT books_authors_author_id_fk FOREIGN KEY (author_id)"
            "    REFERENCES authors(id) ON DELETE CASCADE"
            ")"
        )

        for table_name in TABLES:
            try:
                self.cursor.execute(TABLES[table_name])
                print(f"Creating table {table_name}.")
            except mysql.connector.Error as err:
                if err.errno != errorcode.ER_TABLE_EXISTS_ERROR:
                    print(f"Error: {err}")


    def insert_default_data(self):
        """
        Functie pentru inserarea datelor default
        """
        self.insert_default_nationalities()
        self.insert_default_users()
        self.connection.commit()

    def insert_default_nationalities(self):
        """
        Functie pentru inserarea nationalitatilor si a codurilor aferente lor
        """
        nationalitati = [
            ('978-000', 'sua'),
            ('978-111', 'marea britanie'),
            ('978-600', 'iran'),
            ('978-601', 'kazahstan'),
            ('978-602', 'indonezia'),
            ('978-603', 'arabia saudita'),
            ('978-604', 'vietnam'),
            ('978-605', 'turcia'),
            ('978-606', 'romania'),
            ('978-607', 'mexic'),
            ('978-608', 'macedonia'),
            ('978-609', 'lituania'),
            ('978-611', 'thailanda'),
            ('978-612', 'peru'),
            ('978-613', 'mauritius'),
            ('978-614', 'liban'),
            ('978-615', 'ungaria'),
            ('978-616', 'thailanda'),
            ('978-617', 'ucraina'),
            ('978-618', 'grecia'),
            ('978-619', 'bulgaria'),
            ('978-620', 'mauritius'),
            ('978-621', 'filipine'),
            ('978-950', 'argentina'),
            ('978-951', 'finlanda'),
            ('978-952', 'finlanda'),
            ('978-953', 'croatia'),
            ('978-954', 'bulgaria'),
            ('978-955', 'sri lanka'),
            ('978-956', 'chile'),
            ('978-957', 'taiwan'),
            ('978-958', 'columbia'),
            ('978-959', 'cuba'),
            ('978-960', 'grecia'),
            ('978-961', 'slovenia'),
            ('978-962', 'hong kong'),
            ('978-963', 'ungaria'),
            ('978-964', 'iran'),
            ('978-965', 'israel'),
            ('978-966', 'ucraina'),
            ('978-967', 'malaezia'),
            ('978-968', 'mexic'),
            ('978-969', 'pakistan'),
            ('978-970', 'mexic'),
            ('978-971', 'filipine'),
            ('978-972', 'portugalia'),
            ('978-973', 'romania'),
            ('978-974', 'thailanda'),
            ('978-975', 'turcia'),
            ('978-976', 'caraibe'),
            ('978-977', 'egipt'),
            ('978-978', 'nigeria'),
            ('978-979', 'indonezia'),
            ('978-980', 'venezuela'),
            ('978-981', 'singapore'),
            ('978-982', 'pacificul de sud'),
            ('978-983', 'malaezia'),
            ('978-984', 'bangladesh'),
            ('978-985', 'belarus'),
            ('978-986', 'taiwan'),
            ('978-987', 'argentina'),
            ('978-988', 'hong kong'),
            ('978-989', 'portugalia'),
            ('979-010', 'franta')]
        add_nationality = (
            "INSERT INTO nationalities (code, country) "
            "VALUES (%s, %s)"
        )

        for nat in nationalitati:
            try:
                self.cursor.execute(add_nationality, nat)
            except mysql.connector.Error as err:
                if err.errno != errorcode.ER_DUP_ENTRY:
                    print(f"Error: {err}")


    def insert_default_users(self):
        """
        Functie pentru inserarea utilizatorilor default
        """
        users = [
            ('admin', hashlib.sha256('admin'.encode()).hexdigest(), 'admin'),
            ('user', hashlib.sha256('user'.encode()).hexdigest(), 'user')
        ]
        add_user = (
            "INSERT INTO users (username, password, role) "
            "VALUES (%s, %s, %s)"
        )

        for user_info in users:
            try:
                self.cursor.execute(add_user, user_info)
            except mysql.connector.Error as err:
                if err.errno != errorcode.ER_DUP_ENTRY:
                    print(f"Error: {err}")


    def close(self):
        """
        Functie pentru inchiderea conexiunii la baza de date
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()


    def add_entry(self, table, entry):
        """
        Functie pentru adaugarea unei intrari in tabela specificata\

        :param table: Tabela in care se adauga intrarea
        :param entry: Continutul intrarii
        """
        placeholders = ', '.join(['%s'] * len(entry))
        columns = ', '.join(entry.keys())
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, list(entry.values()))
        self.connection.commit()


    def username_used(self, username):
        """
        Functie pentru a verifica daca un nume de utilizator este deja folosit

        :param username: Numele de utilizator
        :return: True daca numele de utilizator este folosit, False altfel
        """
        query = "SELECT COUNT(*) FROM users WHERE username = %s"
        self.cursor.execute(query, (username, ))
        return self.cursor.fetchone() == 1


    def authenticate_user(self, user_data):
        """
        Functie pentru autentificarea unui utilizator
        :param user_data: credentialele utilizatorului
        :return: datele utilizatorului autentificat sau None, daca autentificarea a esuat
        """
        query = "SELECT id, username, role FROM users WHERE username = %s AND password = %s"
        self.cursor.execute(query, (user_data['username'], user_data['password']))
        return self.cursor.fetchone()