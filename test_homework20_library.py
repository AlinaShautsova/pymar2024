"""Unittest for Homework 11: library."""

import unittest
import logging
from homework11_library import Book, User

formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
file_handler = logging.FileHandler('test_library.log')
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)


class TestLibrary(unittest.TestCase):
    """Test cases for the library class method."""

    def setUp(self):
        """Set up the test environment."""
        logger.info("Assign variables.")
        self.book = Book("Harry Potter", "Joanne Rowling",
                         500, "932-994-555")
        self.book2 = Book("Dune", "Frank Herbert",
                          400, "56454-6775")
        self.user1 = User("Kate")
        self.user2 = User("Ira")

    def tearDown(self):
        """Deleting variables after each test."""
        logger.info("Deleting variables")
        del self.book
        del self.book2
        del self.user1
        del self.user2

    def test_book_initialization(self):
        """Testing book initialization."""
        logger.info("Testing: book initialization.")
        logger.debug("Book details: %s", self.book)
        self.assertEqual(self.book.title, "Harry Potter")
        self.assertEqual(self.book.author, "Joanne Rowling")
        self.assertEqual(self.book.number_of_pages, 500)
        self.assertEqual(self.book.isbn, "932-994-555")
        self.assertEqual(self.book.reserved_by, "")
        self.assertEqual(self.book.took_by, "")

    def test_get_details(self):
        """Testing getting detailed information about a book."""
        logger.info("Testing: get_details method.")
        logger.debug("Book details: %s", self.book.get_details())
        self.assertEqual(self.book.get_details(),
                         "Title: Harry Potter, Author: Joanne Rowling, "
                         "Pages: 500, ISBN: 932-994-555")

    def test_is_reserved(self):
        """Testing whether the user can reserve an already reserved book or
        not."""
        logger.info("Testing: is_reserved method. Check whether the user can "
                    "reserve an already reserved book or not.")
        logger.debug("Book reserved: %s", self.book.is_reserved())
        self.assertFalse(self.book.is_reserved())
        self.user1.reserve_book(self.book)
        logger.debug("Book reserved after reserving: %s",
                     self.book.is_reserved())
        self.assertTrue(self.book.is_reserved())

    def test_secondary_reservation_book(self):
        """Testing user2 tries to reserve a book that user1 has already
        reserved."""
        logger.info("Testing: reserve_book method. User2 tries to reserve a "
                    "book that user1 has already reserved.")
        self.user1.reserve_book(self.book)
        logger.debug("Book reserved_by: %s", self.book.reserved_by)
        self.assertEqual(self.book.reserved_by, self.user1.name)
        self.user2.reserve_book(self.book)
        logger.debug("Book reserved_by after second attempt: %s",
                     self.book.reserved_by)
        self.assertEqual(self.book.reserved_by, self.user1.name)

    def test_is_taken(self):
        """Testing whether the user can take an already taken book or not."""
        logger.info("Testing: is_taken method. Check whether the user can "
                    "take an already taken book or not.")
        logger.debug("Book taken: %s", self.book.is_taken())
        self.assertFalse(self.book.is_taken())
        self.user1.take_book(self.book)
        logger.debug("Book taken after taking: %s",
                     self.book.is_taken())
        self.assertTrue(self.book.is_taken())

    def test_secondary_take_book(self):
        """Testing user2 tries to take a book that user1 has already taken."""
        logger.info("Testing: take_book method. User2 tries to take a "
                    "book that user1 has already taken.")
        self.user1.take_book(self.book)
        logger.debug("Book took_by: %s", self.book.took_by)
        self.assertEqual(self.book.took_by, self.user1.name)
        self.user2.take_book(self.book)
        logger.debug("Book took_by after second attempt: %s",
                     self.book.took_by)
        self.assertEqual(self.book.took_by, self.user1.name)

    def test_reserve_secondary_taken_book(self):
        """Testing: user2 wants to reserve a book that user1 has already
        taken."""
        logger.info("Testing: user2 wants to reserve a book that user1 has "
                    "already taken.")
        self.user1.take_book(self.book)
        logger.debug("Book took_by: %s", self.book.took_by)
        self.assertEqual(self.book.took_by, self.user1.name)
        self.user2.reserve_book(self.book)
        logger.debug("Book reserved_by after it was taken by another "
                     "user: %s", self.book.took_by)
        self.assertNotEqual(self.book.reserved_by, self.user2.name)

    def test_take_secondary_reserved_book(self):
        """Testing user2 wants to take a book that user1 has already
        reserved."""
        logger.info("Testing: user2 wants to take a book that user1 has "
                    "already reserved.")
        self.user1.reserve_book(self.book)
        logger.debug("Book reserved_by: %s", self.book.reserved_by)
        self.assertEqual(self.book.reserved_by, self.user1.name)
        self.user2.take_book(self.book)
        logger.debug("Book take by after it was reserved_by another"
                     " user: %s", self.book.reserved_by)
        self.assertNotEqual(self.book.took_by, self.user2)

    def test_return_book(self):
        """Testing if the book can be returned."""
        logger.info("Testing: return_book method. Check if the book can be "
                    "returned.")
        self.user1.take_book(self.book)
        self.user1.return_book(self.book)
        logger.debug("Book took_by after returning: %s",
                     self.book.took_by)
        self.assertEqual(self.book.took_by, "")

    def test_return_book_not_taken(self):
        """Testing user2 is trying to return the book that the user1 took."""
        logger.info("Testing: user2 is trying to return the book that "
                    "the user1 took.")
        self.user1.take_book(self.book)
        self.assertEqual(self.book.took_by, self.user1.name)
        self.user2.return_book(self.book)
        logger.debug("Book was not returned_by after it was taken by "
                     "another user: %s", self.book.took_by)
        self.assertEqual(self.book.took_by, self.user1.name)


if __name__ == '__main__':
    unittest.main()
