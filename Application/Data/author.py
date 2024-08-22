

class Author:
    def __init__(self, first_name, last_name, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality


    def get_full_name(self):
        """
        Functie pentru obtinerea numelui complet al autorului.

        :return: Numele complet al autorului
        """
        return f"{self.first_name} {self.last_name}"


    def __str__(self):
        """
        Functie pentru afisarea datelor autorului.

        :return: Paginarea informatiilor despre autor
        """
        lines = [f"Nume          : {self.last_name}",
                f"Prenume       : {self.first_name}",
                f"Nationalitate : {self.nationality}"]

        max_length = 38

        # Formateaza fiecare linie sa inceapa si sa se termine cu '|'
        formatted_fields = [f"| {line.ljust(max_length)} |" for line in lines]
        formatted_fields[0] = "\t\t\t\t" + formatted_fields[0]

        # Adauga linia de sus si linia de jos
        border_line = f"\t\t\t\t{'-' * (max_length + 4)}"

        return f"{border_line}\n" + '\n\t\t\t\t'.join(formatted_fields) + f"\n{border_line}"