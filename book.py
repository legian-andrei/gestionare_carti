

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
        author_names = [author.get_full_name() for author in self.authors]

        lines = [
            f"Titlu           : {self.title}",
            f"Autori          : {author_names[0]}"]

        # Daca sunt mai multi autori, adauga fiecare autor pe cate o linie
        if len(author_names) > 1:
            lines[1] += ','
            author_lines = [f"{' '*18}{author}," for author in author_names[1:]]
            # Sterge virgula de la ultimul autor
            author_lines[-1] = author_lines[-1][:-1]
            lines.extend(author_lines)

        lines.append(f"Gen             : {self.genre}")
        lines.append(f"Anul aparitiei  : {self.year}")
        lines.append(f"ISBN            : {self.isbn}")

        max_length = 38

        # Formateaza fiecare linie sa inceapa si sa se termine cu '|'
        formatted_fields = [f"| {line.ljust(max_length)} |" for line in lines]
        formatted_fields[0] = "\t\t\t\t" + formatted_fields[0]

        # Adauga linia de sus si linia de jos
        border_line = f"\t\t\t\t{'-' * (max_length + 4)}"

        return f"{border_line}\n" + '\n\t\t\t\t'.join(formatted_fields) + f"\n{border_line}"