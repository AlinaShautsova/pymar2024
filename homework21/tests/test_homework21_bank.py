"""Pytest for Homework 11: bank deposit."""
import pytest
from homework21.source.homework11_bank_deposit import Bank, Deposit
from logging_module import setup_logging


@pytest.fixture(scope="session", autouse=True)
def logger():
    """Set up logger."""
    logger = setup_logging('test_bank.log')
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


def test_deposit_initialization(setup_deposit, logger):
    """Testing deposit initialization."""
    logger.info("Testing deposit initialization.")
    logger.debug("Deposit details: %s", setup_deposit)
    deposit = setup_deposit
    assert deposit.get_deposit_amount() == 100
    assert deposit.get_deposit_term() == 2
    assert deposit.get_annual_rate() == 10


def test_final_amount(setup_deposit, logger):
    """Testing actual final amount the same as expected final amount."""
    logger.info("Testing final amount.")
    actual_final_amount = setup_deposit.final_amount()
    logger.debug("Final amount1: %f", actual_final_amount)
    expected_final_amount = 100 * (1 + 10 / 12 / 100) ** (2 * 12)
    assert round(actual_final_amount, 2) == round(expected_final_amount, 2)


def test_bank_deposit(setup_bank, setup_user1, setup_initial_amount,
                      setup_years, logger):
    """Testing bank deposit."""
    logger.info("Testing bank deposit.")
    final_amount = setup_bank.deposit(setup_user1, setup_initial_amount,
                                      setup_years)
    logger.debug("User %s final amount1: %f", setup_user1,
                 final_amount)
    assert setup_user1 in setup_bank.user_accounts
    assert (round(setup_bank.user_accounts[setup_user1], 2) ==
            round(final_amount, 2))


def test_bank_withdraw(setup_deposit, setup_bank, setup_user1,
                       setup_initial_amount, setup_years, logger):
    """Testing the bank to withdraw the amount."""
    logger.info("Testing: the bank to withdraw the amount.")
    setup_bank.deposit(setup_user1, setup_initial_amount, setup_years)
    withdrawn_amount = setup_bank.withdraw(setup_user1)
    logger.debug("User %s withdrawn amount: %f", setup_user1,
                 withdrawn_amount)
    assert setup_user1 not in setup_bank.user_accounts
    assert round(withdrawn_amount, 2) == round(setup_deposit.final_amount(), 2)


def test_bank_withdraw_secondary_user(setup_bank, setup_user1, setup_years,
                                      setup_initial_amount, setup_user2,
                                      logger):
    """Testing the user2 tries to withdraw amount from the user1's account."""
    logger.info("Testing the user2 tries to withdraw amount not from his "
                "account.")
    setup_bank.deposit(setup_user1, setup_initial_amount, setup_years)
    withdrawn_amount = setup_bank.withdraw(setup_user2)
    logger.debug("User2 %s withdrawn amount: %f", setup_user2,
                 withdrawn_amount)
    assert setup_initial_amount != (withdrawn_amount, 2)


def test_bank_withdraw_nonexistent_user(setup_bank, logger):
    """Testing bank withdraw for nonexistent user."""
    logger.info("Testing bank withdraw for nonexistent user.")
    withdrawn_amount = setup_bank.withdraw("NonexistentUser")
    logger.debug("Nonexistent user withdrawn amount: %f",
                 withdrawn_amount)
    assert withdrawn_amount == 0


def test_initial_amount_less_final_amount(setup_deposit, setup_initial_amount,
                                          logger):
    """Testing the initial amount is less than the final amount."""
    logger.info("Testing that the initial amount is less than the final "
                "amount.")
    final_amount = setup_deposit.final_amount()
    logger.debug("Initial amount: %f, final amount: %f",
                 setup_initial_amount, final_amount)
    assert setup_initial_amount < final_amount


if __name__ == '__main__':
    pytest.main()