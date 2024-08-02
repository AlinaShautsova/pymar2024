"""This module contains keywords for the "Book" and "User" classes from the
homework11_library module."""

from robot.api.deco import keyword
from homework11_library import Book, User
from logging_module import setup_logging

logger = setup_logging()


@keyword
def create_book(title, author, number_of_pages, isbn):
    """Create a book and return it."""
    return Book(title, author, number_of_pages, isbn)


@keyword
def create_user(name):
    """Create a user with the given name."""
    return User(name)


@keyword
def get_book_details(book):
    """Returns a string with the book's details."""
    return book.get_details()


@keyword
def is_book_reserved(book):
    """Returns True if the book is reserved, False otherwise."""
    return book.is_reserved()


@keyword
def is_book_taken(book):
    """Returns True if the book is taken, False otherwise."""
    return book.is_taken()


@keyword
def book_reserved_by(book):
    """Returns True if the book is taken, False otherwise."""
    return book.reserved_by


@keyword
def book_took_by(book):
    """Returns True if the book is taken, False otherwise."""
    return book.took_by


@keyword
def reserve_book(user, book):
    """Reserve the given book using the user."""
    user.reserve_book(book)


@keyword
def take_book(user, book):
    """Take the given book using the user."""
    user.take_book(book)


@keyword
def return_book(user, book):
    """Return the given book using the user."""
    user.return_book(book)


@keyword
def log_message(message):
    """Logs a message to the console."""
    logger.info(message)
