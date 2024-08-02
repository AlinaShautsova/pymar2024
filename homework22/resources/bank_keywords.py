"""This module contains keywords for the "Deposit" and "Bank" classes from the
homework11_bank_deposit module."""

from robot.api.deco import keyword
from homework11_bank_deposit import Deposit, Bank
from logging_module import setup_logging

logger = setup_logging()


@keyword
def create_deposit(sum_of_deposit, deposit_term, annual_rate=10):
    """Creates a new Deposit instance."""
    return Deposit(sum_of_deposit, deposit_term, annual_rate)


@keyword
def create_bank():
    """Creates a new Bank instance."""
    return Bank()


@keyword
def withdraw(bank, user):
    """Withdraws the deposit amount for a user from the bank."""
    return bank.withdraw(user)


@keyword
def final_amount(deposit):
    """Calculates the final amount of the deposit after the term."""
    return deposit.final_amount()


@keyword
def get_deposit_amount(deposit):
    """Returns the initial deposit amount."""
    return deposit.get_deposit_amount()


@keyword
def get_annual_rate(deposit):
    """Returns the annual interest rate of the deposit."""
    return deposit.get_annual_rate()


@keyword
def get_deposit_term(deposit):
    """Returns the term of the deposit in years."""
    return deposit.get_deposit_term()


@keyword
def deposit_to_bank(bank, user, sum_of_deposit, deposit_term):
    """Makes a deposit to the bank for a specific user."""
    return bank.deposit(user, sum_of_deposit, deposit_term)


@keyword
def get_user_amount(user):
    """Returns the amount associated with a user."""
    return user()


@keyword
def log_message(message):
    """Logs a message to the console."""
    logger.info(message)
