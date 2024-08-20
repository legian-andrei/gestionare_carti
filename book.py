

class Book:
    def __init__(self, title, authors, year, genre, isbn = None):
        self.title = title
        self.authors = authors
        self.isbn = isbn
        self.year = year
        self.genre = genre


    def __str__(self):
        """
        Functie pentru afisarea datelor despre carte.

        :return: Paginarea informatiilor despre autor
        """
        author_names = ', \n\t\t\t\t\t\t'.join([author.get_full_name() for author in self.authors])
        return (f"""
                    \t\tTitlu         : {self.title}
                    \t\tAutori        : {author_names}
                    \t\tISBN          : {self.isbn}""")