import mysql.connector
from mysql.connector import errorcode


class DatabaseManager:
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
            print("Connected to database") # de refacut afisarea in pagina
            self.setup_database()
        except mysql.connector.Error as error:
            self.handle_error(error)

    def handle_error(self, err):
        """
        Functie pentru tratarea erorilor

        :param err: Eroarea primita
        """
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Ceva este in neregula. Userul sau parola sunt gresite.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Baza de date nu exista.")
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
            "  FOREIGN KEY (book_isbn) REFERENCES books(isbn),"
            "  FOREIGN KEY (author_id) REFERENCES authors(id),"
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
                    self.handle_error(err)

    def execute_query(self, query):
        """
        Functie pentru executarea unui query SQL

        :param query: Query-ul de executat
        """
        self.cursor.execute(query)
        self.connection.commit()

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
                    self.handle_error(err)


    def insert_default_users(self):
        """
        Functie pentru inserarea utilizatorilor default
        """
        users = [
            ('admin', 'admin', 'admin'),
            ('user', 'user', 'user')
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
                    self.handle_error(err)


    def close(self):
        """
        Functie pentru inchiderea conexiunii la baza de date
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()