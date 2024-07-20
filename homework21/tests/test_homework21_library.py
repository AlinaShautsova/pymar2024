"""Pytest for Homework 11: library."""
import pytest


def test_book_initialization(setup_book, logger):
    """Testing book initialization."""
    logger.info("Testing: book initialization.")
    logger.debug("Book details: %s", setup_book)

    book = setup_book
    assert book.title == "Harry Potter"
    assert book.author == "Joanne Rowling"
    assert book.number_of_pages == 500
    assert book.isbn == "932-994-555"
    assert book.reserved_by == ""
    assert book.took_by == ""


def test_get_details(setup_book, logger):
    """Testing getting detailed information about a book."""
    logger.info("Testing: get_details method.")
    logger.debug("Book details: %s", setup_book.get_details())
    details = setup_book.get_details()
    expected_details = ("Title: Harry Potter, Author: Joanne Rowling, "
                        "Pages: 500, ISBN: 932-994-555")
    assert details == expected_details


def test_is_reserved(setup_book, setup_user1, logger):
    """Testing whether the user can reserve an already reserved book or
    not."""
    logger.info("Testing: is_reserved method. Check whether the user can "
                "reserve an already reserved book or not.")
    logger.debug("Book reserved: %s", setup_book.is_reserved())
    assert not setup_book.is_reserved()
    setup_user1.reserve_book(setup_book)
    logger.debug("Book reserved after reserving: %s", setup_book.is_reserved())
    assert setup_book.is_reserved()


def test_take_secondary_reservation_book(setup_book, setup_user1, setup_user2,
                                         logger):
    """Testing user2 tries to reserve a book that user1 has already
     reserved."""
    logger.info("Testing: user2 wants to reserve a book that user1 has "
                "already reserved.")
    setup_user1.reserve_book(setup_book)
    logger.debug("Book reserved_by: %s", setup_book.reserved_by)
    assert setup_book.reserved_by == setup_user1.name
    logger.debug("Book reserved_by after second attempt: %s",
                 setup_book.reserved_by)
    setup_user2.reserve_book(setup_book)
    assert setup_book.reserved_by == setup_user1.name


def test_is_taken(setup_book, setup_user1, logger):
    """Testing whether the user can take an already taken book or not."""
    logger.info("Testing: is_taken method. Check whether the user can take "
                "an already taken book or not.")
    logger.debug("Book taken: %s", setup_book.is_taken())
    assert not setup_book.is_taken()
    setup_user1.take_book(setup_book)
    logger.debug("Book taken after taking: %s", setup_book.is_taken())
    assert setup_book.is_taken()


def test_take_secondary_take_book(setup_book, setup_user1, setup_user2,
                                  logger):
    """Testing user2 tries to take a book that user1 has already taken."""
    logger.info("Testing: take_book method. User2 tries to take a book "
                "that user1 has already taken.")
    setup_user1.take_book(setup_book)
    logger.debug("Book took_by: %s", setup_book.took_by)
    assert setup_book.took_by == setup_user1.name
    logger.debug("Book took_by after second attempt: %s", setup_book.took_by)
    setup_user2.take_book(setup_book)
    assert setup_book.took_by == setup_user1.name


def test_reserve_secondary_taken_book(setup_book, setup_user1, setup_user2,
                                      logger):
    """Testing: user2 wants to reserve a book that user1 has already
    taken."""
    logger.info("Testing: user2 wants to reserve a book that user1 has "
                "already taken.")
    setup_user1.take_book(setup_book)
    logger.debug("Book took_by: %s", setup_book.took_by)
    assert setup_book.took_by == setup_user1.name
    setup_user2.reserve_book(setup_book)
    logger.debug("Book reserved_by after it was taken by another "
                 "user: %s", setup_book.took_by)
    assert not setup_book.reserved_by == setup_user2.name


def test_take_secondary_reserved_book(setup_book, setup_user1, setup_user2,
                                      logger):
    """Testing user2 wants to take a book that user1 has already reserved."""
    logger.info("Testing: user2 wants to take a book that user1 has already "
                "reserved.")
    setup_user1.reserve_book(setup_book)
    logger.debug("Book reserved_by: %s", setup_book.reserved_by)
    assert setup_book.reserved_by == setup_user1.name
    setup_user2.take_book(setup_book)
    logger.debug("Book take by after it was reserved_by another user: %s",
                 setup_book.reserved_by)
    assert not setup_book.took_by == setup_user2.name


def test_return_book(setup_book, setup_user1, logger):
    """Testing if the book can be returned."""
    logger.info("Testing: return_book method. Check if the book can be "
                "returned.")
    setup_user1.take_book(setup_book)
    setup_user1.return_book(setup_book)
    logger.debug("Book took_by after returning: %s", setup_book.took_by)
    assert setup_book.took_by == ""


def test_return_book_not_taken(setup_book, setup_user1, setup_user2, logger):
    """Testing user2 is trying to return the book that the user1 took."""
    logger.info("Testing: user2 is trying to return the book that the user1 "
                "took.")
    setup_user1.take_book(setup_book)
    assert setup_book.took_by == setup_user1.name
    setup_user2.return_book(setup_book)
    logger.debug("Book was not returned_by after it was taken by another "
                 "user: %s", setup_book.took_by)
    assert setup_book.took_by == setup_user1.name


if __name__ == "__main__":
    pytest.main()
