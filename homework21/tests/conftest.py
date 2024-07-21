"""Contest for Homework 21. Task : bank deposit, task : library."""
import pytest

from homework21.source.homework11_bank_deposit import Bank, Deposit
from homework21.source.homework11_library import Book, User
from logging_module import setup_logging


logger = setup_logging()


@pytest.fixture(scope="function")
def setup_bank():
    """Set up the test environment."""
    logger.info("Setting up the Bank instance.")
    bank = Bank()
    yield bank
    logger.info("Tearing down the Bank instance.")
    del bank


@pytest.fixture(scope="function")
def setup_deposit():
    """Set up the test environment."""
    logger.info("Setting up the Deposit instance.")
    deposit = Deposit(100, 2)
    yield deposit
    logger.info("Tearing down the Deposit instance.")
    del deposit


@pytest.fixture(scope="function")
def setup_user1_bank():
    """Set up the test environment."""
    logger.info("Setting up the User1 instance.")
    user1 = "Petya"
    yield user1
    logger.info("Tearing down the User1 instance.")
    del user1


@pytest.fixture(scope="function")
def setup_user2_bank():
    """Set up the test environment."""
    logger.info("Setting up the User2 instance.")
    user2 = "Katya"
    yield user2
    logger.info("Tearing down the User2 instance.")
    del user2


@pytest.fixture(scope="function")
def setup_initial_amount():
    """Set up the test environment."""
    logger.info("Setting up the Initial amount instance.")
    initial_amount = 100
    yield initial_amount
    logger.info("Tearing down the Initial amount instance.")
    del initial_amount


@pytest.fixture(scope="function")
def setup_years():
    """Set up the test environment."""
    logger.info("Setting up years instance.")
    years = 2
    yield years
    logger.info("Tearing down years instance.")
    del years


@pytest.fixture(scope="function")
def setup_book():
    """Set up the test environment."""
    logger.info("Create a book with these parameters: title, author, "
                "number of pages, isbn.")
    book = Book("Harry Potter", "Joanne Rowling",
                500, "932-994-555")
    yield book
    logger.info("Tearing down the Book instance.")
    del book


@pytest.fixture(scope="function")
def setup_user1_library():
    """Set up the test environment."""
    logger.info("Create user1 name.")
    user1 = User("Kate")
    yield user1
    logger.info("Tearing down the User1 instance.")
    del user1


@pytest.fixture(scope="function")
def setup_user2_library():
    """Set up the test environment."""
    logger.info("Create user2 name.")
    user2 = User("Ira")
    yield user2
    logger.info("Tearing down the User2 instance.")
    del user2
