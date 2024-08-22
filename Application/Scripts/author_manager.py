from Application.Data.author import *
from Application.Data.book import *


class AuthorManager:
    """
    Clasa pentru gestionarea utilizatorilor.
    """

    def __init__(self, db_manager):
        self.db_manager = db_manager


    def add_author(self, author_details):
        """
        Functie pentru adaugarea unui autor nou in baza de date.

        :param author_details: Datele autorului
        """
        author_entry = {
            'first_name': author_details.first_name,
            'last_name': author_details.last_name,
            'nationality': author_details.nationality
        }
        self.db_manager.add_entry('authors', author_entry)


    def get_author_id(self, author_details):
        """
        Functie pentru obtinerea id-ului unui autor.
        :param author_details:
        :return: id-ul autorului sau None daca autorul nu exista
        """
        author_data = (author_details.first_name, author_details.last_name)
        sql_query = "SELECT id FROM authors WHERE first_name = %s AND last_name = %s"
        author_id = self.db_manager.execute_query(query=sql_query, params=author_data, fetch_one=True)
        return author_id[0] if author_id else None


    def get_author_nationality_by_id(self, author_id):
        """
        Functie pentru obtinerea nationalitatii unui autor.
        :param author_id: id-ul autorului
        :return: nationalitatea autorului
        """
        sql_query = "SELECT nationality FROM authors WHERE id = %s"
        author_nationality = self.db_manager.execute_query(query=sql_query, params=(author_id,), fetch_one=True)
        return author_nationality[0]

    def get_authors_by_nationality(self, nationality):
        """
        Functie pentru obtinerea autorilor in functie de nationalitate.
        :param nationality: nationalitatea autorilor
        :return: list(Author) sau None daca nu exista autori cu aceasta nationalitate
        """
        sql_query = "SELECT first_name, last_name FROM authors where nationality = %s"
        authors = self.db_manager.execute_query(query=sql_query, params=(nationality,), fetch_all=True)
        return [Author(author[0].capitalize(), author[1].capitalize(), nationality.capitalize()) for author in authors] if authors else None


    def get_books_by_author(self, author_id):
        """
        Functie pentru obtinerea cartilor scrise de un autor cu un anumit id.
        :param author_id: id-ul autorului
        :return: list(Book) sau None daca autorul nu a scris nicio carte
        """
        books_query = "SELECT isbn, title, year, genre FROM books JOIN books_authors ON books.isbn = books_authors.book_isbn WHERE author_id = %s"
        books_query_result = self.db_manager.execute_query(query=books_query, params=(author_id,), fetch_all=True)

        books = []

        for book in books_query_result:
            isbn = book[0]
            authors = self.db_manager.get_authors_by_isbn(isbn)
            books.append(Book(title=book[1].capitalize(), authors=authors, year=book[2], genre=book[3].capitalize(), isbn=isbn))

        return books if books else None
