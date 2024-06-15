"""Module contains a solution to the task: library."""


class Book:
    """This class include function for initializes."""
    def __init__(self, title, author, number_of_pages, isbn):
        """Function initializes a new instance of the Book class. """
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.reserved_by = ""
        self.took_by = ""


class User:
    """This class include 4 functions for initializes, for reserve, take and
     return the book."""
    def __init__(self, name):
        """Function initializes a new instance of the User class. """
        self.name = name

    def reserve_the_book(self, book):
        """This function is reserved the book and print a message, if the book
         is already taken or reserved or if you reserved the book."""
        if book.took_by:
            print(f"This book {book.title} has already been taken by"
                  f" {book.took_by}.")
        elif book.reserved_by:
            print(f"This book {book.title} has already been reserved by "
                  f"{book.reserved_by}.")
        else:
            book.reserved_by = self.name
            print(f"{self.name} reserved the {book.title}")

    def take_the_book(self, book):
        """User takes the book and if this book is taken or reserved,
        print a message."""
        if book.took_by:
            print(f"This book {book.title} has already been taken by"
                  f" {book.took_by}.")
        elif book.reserved_by and book.reserved_by != self.name:
            print(f"This book {book.title} was reserved by "
                  f"{book.reserved_by}.")
        else:
            book.took_by = self.name
            book.reserved_by = ""
            print(f"{self.name} took the {book.title}")

    def return_the_book(self, book):
        """This function print a message, if you returned the book,
        or if you hadn't taken it before."""
        if book.took_by == self.name:
            book.took_by = ""
            print(f"{self.name} returned the {book.title}")
        else:
            print(f"{self.name} can not return {book.title} because it has"
                  f"been not taken by her/ him.")


my_book = Book("Harry Potter", "Joanne Rowling", 500,
               "932-994-555")
my_book2 = Book("Dune", "Frank Herbert", 400,
                "56454-6775")

user1 = User("Kate")
user2 = User("Ira")

user1.reserve_the_book(my_book)
user1.take_the_book(my_book)
user2.return_the_book(my_book2)
