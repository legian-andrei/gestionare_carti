

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
        return (f"""
                    \t\tNume          : {self.last_name}
                    \t\tPrenume       : {self.first_name}
                    \t\tNationalitate : {self.nationality}""")