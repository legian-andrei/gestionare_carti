# Book Management System

## Descriere

**Book Management System** este o aplicație simplă pentru gestionarea cărților, autorilor și utilizatorilor într-o bază 
de date. Aplicația permite utilizatorilor să caute cărți, autori și să gestioneze aceste date. Administratorii au 
privilegii suplimentare, cum ar fi adăugarea de noi autori și cărți în baza de date. Proiectul include un sistem de 
audit pentru a urmări acțiunile utilizatorilor.

## Caracteristici Cheie

- ### Gestionarea utilizatorilor
  - Crearea unui cont de utilizator
  
    ![Create Account](/Application/ScreenShots/creaza_cont.png)
  
  - Autentificare
  
    ![Login](/Application/ScreenShots/conectare.png)
  
- ### Gestionarea cărților și autorilor
  - Căutare după titlul cărții 
  
    ![Search Books by Title](/Application/ScreenShots/cauta_carte_titlu.png)
  
  - Căutare după numele autorului (afișarea tuturor cărților aparținând unui autor)
  
    ![Search Books by Author](/Application/ScreenShots/cauta_carte_autor.png)
  
  - Căutare după naționalitatea autorului (afișarea tuturor autorilor dintr-o anumită țară)
        
    ![Search Authors by Nationality](/Application/ScreenShots/cauta_autori_nationalitate.png)

  - Căutare după ISBN

    ![Search Book by ISBN](/Application/ScreenShots/cauta_carte_isbn.png)

  - Adăugarea informațiilor despre un autor nou
    - Nume
    - Prenume
    - Naționalitate
    
    ![Add Author](/Application/ScreenShots/adauga_autor.png)

  - #### Adăugarea informațiilor unei noi cărți
    - Generarea unui ISBN unic pentru fiecare carte, având prefixul și identificatorul țării din care provine autorul, 
    urmat de identificatorul publicației (generat aleator) și cifra de control (suma primelor 12 cifre modulo 13)
    - Titlul cărții
    - Autorii cărții (trebuie sa fie deja introduși în baza de date)
    - Anul publicării
    - Genul cărții
    
      ![Add Book](/Application/ScreenShots/adauga_carte.png)
    
- ### Sistem de audit pentru urmărirea acțiunilor utilizatorilor
  - Afișarea tuturor acțiunilor efectuate de un anumit utilizator
      
     ![Show Audit](/Application/ScreenShots/vizualizeaza_audit.png)
  
- ### Roluri diferite pentru utilizatori
  - Guest: are doar opținea de a-și crea un cont nou sau de a se conecta la un cont existent
  - Logged-in User: are acces doar la căutarea de cărți și autori
  - Admin: are acces la toate funcționalitățile aplicației (inclusiv promovarea unui utilizator obișnuit la rolul de Admin)

    ![Promote User](/Application/ScreenShots/promoveaza_user.png)


## Diagrama Entitate-Relație
```mermaid
erDiagram
    USERS {
      int id PK
      string username 
      string password 
      string role
    }
    AUTHORS{
        int id PK
        string first_name
        string last_name
        string nationality
    }
    NATIONALITIES{
        string code PK
        string country
    }
    BOOKS{
        string isbn PK
        string title
        int year
        string genre
    }
    BOOKS_AUTHORS{
        string book_isbn PK, FK
        int author_id PK, FK
    }
    AUDIT{
        int id PK
        int user_id FK
        string action
        timestamp time
    }

    USERS ||--o{ AUDIT : logs
    AUTHORS ||--o{ BOOKS_AUTHORS : writes
    BOOKS ||--o{ BOOKS_AUTHORS : includes
```

## Diagrama claselor
    
```mermaid
    classDiagram
    class User
    class LoggedInUser {
        -int id
        -string username
    }
    class AdminUser {
        -int id
        -string username
    }
    class UserManager {
        - User current_user
        - DatabaseManager db_manager
        - AuditManager audit_manager
        - int auth_attempts
        
        +show_current_menu()
        +create_account(username, password)
        +login(username, password)
        +get_user_by_username(username)
        +promote_user_to_admin(user)
    }

    class Author {
        -string first_name
        -string last_name
        -string nationality
        +get_full_name()
    }
    class AuthorManager {
        -DatabaseManager db_manager
        +add_author(Author author_details)
        +get_author_id(Author author_details)
        +get_author_nationality_by_id(author_id)
        +get_authors_by_nationality(nationality)
        +get_books_by_author(author_id)
    }

    class Book {
        -string isbn
        -string title
        -list[Author] authors
        -int year
        -string genre
    }
    class BookManager {
        -DatabaseManager db_manager
        -AuthorManager author_manager
        +add_book(Book book_details)
        +generate_isbn(author_id)
        +generate_publication_id()
        +calculate_check_digit(isbn_without_cd)
        +get_books_by_title(title)
        +get_book_by_isbn(isbn)
        +get_authors_by_isbn(isbn)
        +get_books_by_author(author_id)
        +get_books_by_genre(genre)
    }

    class AuditLog {
        -int user_id
        -string action
        timestamp time
    }
    class AuditManager {
        -DatabaseManager db_manager
        +log_action(user_id, action)
        +get_logs_for_user(user_id)
    }

    class DatabaseManager {
        -string host
        -string user
        -string password
        -string database
        -mysql.connector connection
        -mysql.connector.cursor cursor
        
        +connect()
        +setup_database()
        +create_tables()
        +insert_default_data()
        +insert_default_nationalities()
        +insert_default_users()
        +close()
        
        +add_entry()
        +username_used(username)
        +authenticate_user(user_data)
        +author_exists(author_data)
        +execute_query(query, params, fetch_all, fetch_one)
        +get_nationality_code(nationality)
        +is_isbn_used(isbn)
        +get_book_by_isbn(isbn)
        +get_author_by_id(author_id)
        +get_authors_by_isbn(isbn)
    }
    
    class PrintManager {
        + username_used()
        + invalid_credentials(params)
        + invalid_option()
        + invalid_data()
        + successful_register()
        + limit_reached()
        + author_not_found()
        + book_not_found()
        + book_found(book)
        + books_found(books)
        + authors_found(authors)
        + continue_or_exit()
        + print_objects(obs)
        + promote_user()
        + logs_found(logs)
    }
    
    class Application {
        -DatabaseManager db_manager
        -UserManager user_manager
        -AuditManager audit_manager
        -AuthorManager author_manager
        -BookManager book_manager
        -PrintManager printer
        
        +run()
        +handle_guest_user_choice(choice)
        +handle_logged_in_user_choice(choice)
        +handle_admin_user_choice(choice)
        +create_account()
        +log_into_account()
        +search_books_by_title()
        +search_books_by_author()
        +search_authors_by_nationality()
        +search_book_by_isbn()
        +create_author()
        +create_book()
        +show_audit()
        +search_user()
    }

    LoggedInUser <|-- User
    AdminUser <|-- User
    UserManager "1" --> "1" User : manages
    UserManager "1" --> "1" DatabaseManager : uses
    UserManager "1" --> "1" AuditManager : uses
    AuthorManager "1" --> "1" DatabaseManager : uses
    BookManager "1" --> "1" DatabaseManager : uses
    BookManager "1" --> "1" AuthorManager : uses
    AuditManager "1" --> "1" DatabaseManager : uses
    Application "1" --> "1" DatabaseManager : uses
    Application "1" --> "1" UserManager : uses
    Application "1" --> "1" AuditManager : uses
    Application "1" --> "1" AuthorManager : uses
    Application "1" --> "1" BookManager : uses
    Application "1" --> "1" PrintManager : uses
    
```

## Dependente
- Python - 3.x
- MySQL Server
- MySQL Connector for Python - 9.0
- pwinput - 1.0.3