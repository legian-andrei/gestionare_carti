import random

from Application.Scripts.author_manager import *
from Application.Data.book import *


class BookManager:
    """
    Clasa pentru gestionarea cartilor.
    """
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.author_manager = AuthorManager(db_manager)


    def add_book(self, book_details):
        """
        Functie pentru adaugarea unei carti noi in baza de date.
        :param book_details:
        """
        isbn = self.generate_isbn(book_details.authors[0])
        book_entry = {
            'title': book_details.title,
            'isbn': isbn,
            'year': book_details.year,
            'genre': book_details.genre
        }
        self.db_manager.add_entry('books', book_entry)

        for author_id in book_details.authors:
            author_data = {
                'book_isbn': isbn,
                'author_id': author_id
            }
            self.db_manager.add_entry('books_authors', author_data)


    def generate_isbn(self, author_id):
        """
        Functie pentru generarea unui ISBN unic.
        :param author_id: id-ul autorului
        :return: ISBN-ul generat
        """
        country_code = self.db_manager.get_nationality_code(
            self.author_manager.get_author_nationality_by_id(author_id))
        publication_id = self.generate_publication_id()

        isbn_without_cd = f'{country_code}{publication_id}'
        chech_digit = self.calculate_check_digit(isbn_without_cd)
        isbn = f'{isbn_without_cd}{chech_digit}'

        while self.db_manager.is_isbn_used(isbn):
            publication_id = self.generate_publication_id()
            isbn_without_cd = f'{country_code}{publication_id}'
            chech_digit = self.calculate_check_digit(isbn_without_cd)
            isbn = f'{isbn_without_cd}{chech_digit}'

        return isbn


    def generate_publication_id(self):
        """
        Functie pentru generarea unui id unic pentru publicatie.
        :return:
        """
        return f"{random.randint(0, 999999):06}"


    def calculate_check_digit(self, isbn_without_cd):
        """
        Functie pentru calcularea cifrei de control a unui ISBN.
        :param isbn_without_cd: ISBN-ul fara cifra de control
        :return: cifra de control
        """
        sum = 0
        for digit in isbn_without_cd:
            if digit.isdigit():
                sum += int(digit)

        # Numerele modulo 13 sunt de la 0 la 9 si de la A la C. Pentru a avea doar cifre in codul ISBN
        # se scad 10 de la numerele mai mari sau egale cu 10.
        if sum % 13 >= 10:
            return str(sum % 13 - 10)

        return str(sum % 13)


    def get_books_by_title(self, title):
        """
        Functie pentru obtinerea cartilor in functie de titlu.
        :param title: titlul dupa care se realizeaza cautarea
        :return: list(Book) sau None daca nu exista carti cu acest titlu
        """
        books_query = "SELECT isbn, year, genre FROM books WHERE title = %s"
        books_query_result = self.db_manager.execute_query(query=books_query, params=(title,), fetch_all=True)

        books = []

        for book in books_query_result:
            isbn = book[0]
            authors = self.db_manager.get_authors_by_isbn(isbn)
            books.append(Book(title=title.capitalize(), authors=authors, year=book[1], genre=book[2].capitalize(), isbn=isbn))

        return books if books else None
