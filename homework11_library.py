"""Module contains a solution to the task: library."""


class Book:
    """This class include functions for initializes, getting details, checks
     reserved or taken."""

    def __init__(self, title, author, number_of_pages, isbn):
        """Function initializes a new instance of the Book class."""
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.reserved_by = ""
        self.took_by = ""

    def __str__(self):
        """Function shows that the object is used as a string."""
        return (f"Book {self.title}, {self.author}, {self.number_of_pages}, "
                f"{self.isbn}, {self.reserved_by}, {self.took_by}")

    def get_details(self):
        """Returns a string with the book's details."""
        return (f"Title: {self.title}, Author: {self.author},"
                f" Pages: {self.number_of_pages}, ISBN: {self.isbn}")

    def is_reserved(self):
        """Returns True if the book is reserved, False otherwise."""
        return bool(self.reserved_by)

    def is_taken(self):
        """Returns True if the book is taken, False otherwise."""
        return bool(self.took_by)


class User:
    """This class include 4 functions for initializes, for reserve, take and
     return the book."""

    def __init__(self, name):
        """Function initializes a new instance of the User class."""
        self.name = name

    def reserve_book(self, book):
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

    def take_book(self, book):
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

    def return_book(self, book):
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

user1.reserve_book(my_book)
user1.take_book(my_book)
user2.return_book(my_book2)
