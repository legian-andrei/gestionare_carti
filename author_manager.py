from author import *


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