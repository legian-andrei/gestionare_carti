

class PrintManager:
    """
    Clasa pentru gestionarea afisarilor.
    """
    def username_used(self):
        """
        Functie pentru afisarea unui mesaj de eroare ca utilizatorul exista deja.
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|    Numele de utilizator exista deja.   |')
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def password_mismatch(self):
        """
        Functie pentru afisarea  parolele nu coincid.
        :return:
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|        Parolele nu coincid!           |')
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def invalid_credentials(self, params = None):
        """
        Functie pentru afisarea unui mesaj de eroare ca datele de conectare sunt invalide.
        :param params: numarul de incarcari ramase (optional)
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|          Credentiale invalide!         |')
        if params:
            print(f'\t\t\t\t|          Incercari ramase: {params}          |')
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def successful_register(self):
        """
        Functie pentru afisarea unui mesaj de succes la crearea contului.
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|     Contul a fost creat cu succes!     |')
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def limit_reached(self):
        """
        Functie pentru afisarea unui mesaj de eroare ca s-a atins limita de incercari de conectare.
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|     Ai atins limita de incercari!      |')
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def author_already_exists(self):
        """
        Functie pentru afisarea unui mesaj de eroare ca autorul exista deja.
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|   Autorul exista deja in baza de date. |')
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def author_added_successfully(self):
        """
        Functie pentru afisarea unui mesaj de succes la adaugarea autorului.
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|     Autorul a fost adaugat cu succes!  |')
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def author_not_found(self):
        """
        Functie pentru afisarea unui mesaj de eroare ca autorul nu a fost gasit.
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|   Autorul nu exista in baza de date.   |')
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def book_added_successfully(self):
        """
        Functie pentru afisarea unui mesaj de succes la adaugarea cartii.
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|    Cartea a fost adaugata cu succes!   |')
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def invalid_option(self):
        """
        Functie pentru afisarea unui mesaj de eroare pentru optiunile invalide.
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|   Optiunea aleasa nu este una valita.  |')
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def invalid_data(self):
        """
        Functie pentru afisarea unui mesaj de eroare pentru date invalide.
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|              Date invalide!            |')
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def book_not_found(self):
        """
        Functie pentru afisarea unui mesaj de eroare ca ISBN-ul nu a fost gasit.
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|   ISBN-ul nu exista in baza de date.   |')
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def book_found(self, book):
        """
        Functie pentru afisarea informatiilor despre o carte.
        :param book: obiect de tip Book
        """
        print('\t\t\t\t------------------------------------------')
        print(book)
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def author_with_nationality_not_found(self):
        """
        Functie pentru afisarea unui mesaj de eroare ca autorul cu aceasta nationalitate nu a fost gasit.
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|             Nu exista autori           |')
        print('\t\t\t\t|         cu aceasta nationalitate.      |')
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def authors_found(self, authors):
        """
        Functie pentru afisarea informatiilor despre autorii gasisti.
        :param authors: list(Author)
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|             Autorii cautati:            |')
        print('\t\t\t\t------------------------------------------')
        self.print_objects(authors)
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def books_found(self, books):
        """
        Functie pentru afisarea informatiilor despre cartile gasiste.
        :param books: list(Book)
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|               Carti gasite:            |')
        print('\t\t\t\t------------------------------------------')
        self.print_objects(books)
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def author_without_books(self):
        """
        Functie pentru afisarea unui mesaj de eroare ca autorul nu are carti.
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|   Autorul nu are carti in baza de date. |')
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def continue_or_exit(self):
        """
        Functie pentru afisarea unui mesaj pentru a continua sau a iesi.
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|     Apasa ENTER pentru a continua.     |')
        print('\t\t\t\t|     Apasa alta tasta pentru a iesi.    |')
        print('\t\t\t\t------------------------------------------')


    def books_with_title_not_found(self):
        """
        Functie pentru afisarea unui mesaj de eroare ca nu au fost gasite carti cu un titlu specific.
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|     Nu exista carti cu acest titlu     |')
        print('\t\t\t\t|            in baza de date.            |')
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def print_objects(self, obs):
        """
        Functie pentru afisarea paginata.
        :param obs: list(Obj) - lista de obiecte pentru a fi afisate
        """
        count = 1
        for ob in obs:
            print(ob)

            # Afisarea a cate 4 carti pe pagina
            if count % 4 == 0 and len(obs) > count:
                self.continue_or_exit()
                inp = input('\t\t\t\t\t-> ')
                if len(inp) != 0:
                    break
            count += 1


    def user_not_found(self):
        """
        Functie pentru afisarea unui mesaj de eroare ca utilizatorul nu a fost gasit.
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|         Utilizatorul nu exista         |')
        print('\t\t\t\t|             in baza de date.           |')
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def promote_user_message(self):
        """
        Functie pentru afisarea unui mesaj de informare referitor la promovarea unui utilizator.
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|     Apasa 1 pentru a promova acest     |')
        print('\t\t\t\t|      utilizator la rolul de admin.     |')
        print('\t\t\t\t|     Apasa ENTER pentru a continua.     |')
        print('\t\t\t\t------------------------------------------')


    def user_promoted_successfully(self):
        """
        Functie pentru afisarea unui mesaj de succes la promovarea utilizatorului.
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|          Utilizatorul a fost           |')
        print('\t\t\t\t|          promovat cu succes!           |')
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def logs_not_found(self):
        """
        Functie pentru afisarea unui mesaj de eroare ca nu au fost gasite loguri.
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|    Nu exista loguri pentru acest user.  |')
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')


    def logs_found(self, logs):
        """
        Functie pentru afisarea logurilor gasiste.
        :param logs: list(AuditLog)
        """
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|       Logurile utilizatorului:         |')
        print('\t\t\t\t------------------------------------------')
        self.print_objects(logs)
        print('\t\t\t\t------------------------------------------')
        input('\t\t\t\t\tApasa ENTER pentru a continua.')
