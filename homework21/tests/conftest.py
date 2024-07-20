"""Fixture for homework21: bank deposit, library."""
import pytest

from homework21.source.homework11_bank_deposit import Bank, Deposit
from homework21.source.homework11_library import Book, User
from logging_module import setup_logging


@pytest.fixture(scope="session", autouse=True)
def logger():
    """Set up logger."""
    logger = setup_logging()
    return logger


@pytest.fixture(scope="function")
def setup_bank(logger):
    """Set up the test environment."""
    logger.info("Setting up the Bank instance.")
    bank = Bank()
    yield bank
    logger.info("Tearing down the Bank instance.")
    del bank


@pytest.fixture(scope="function")
def setup_deposit(logger):
    """Set up the test environment."""
    logger.info("Setting up the Deposit instance.")
    deposit = Deposit(100, 2)
    yield deposit
    logger.info("Tearing down the Deposit instance.")
    del deposit


@pytest.fixture(scope="function")
def setup_user1(logger):
    """Set up the test environment."""
    logger.info("Setting up the User1 instance.")
    user1 = "Petya"
    yield user1
    logger.info("Tearing down the User1 instance.")
    del user1


@pytest.fixture(scope="function")
def setup_user2(logger):
    """Set up the test environment."""
    logger.info("Setting up the User2 instance.")
    user2 = "Katya"
    yield user2
    logger.info("Tearing down the User2 instance.")
    del user2


@pytest.fixture(scope="function")
def setup_initial_amount(logger):
    """Set up the test environment."""
    logger.info("Setting up the Initial amount instance.")
    initial_amount = 100
    yield initial_amount
    logger.info("Tearing down the Initial amount instance.")
    del initial_amount


@pytest.fixture(scope="function")
def setup_years(logger):
    """Set up the test environment."""
    logger.info("Setting up years instance.")
    years = 2
    yield years
    logger.info("Tearing down years instance.")
    del years


@pytest.fixture(scope="function")
def setup_book(logger):
    """Set up the test environment."""
    logger.info("Create a book with these parameters: title, author, "
                "number of pages, isbn.")
    book = Book("Harry Potter", "Joanne Rowling",
                500, "932-994-555")
    yield book
    logger.info("Tearing down the Book instance.")
    del book
