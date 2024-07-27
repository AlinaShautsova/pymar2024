"""Pytest for Homework 11: bank deposit."""
from logging_module import setup_logging

logger = setup_logging()


def test_deposit_initialization(setup_deposit):
    """Testing deposit initialization."""
    logger.info("Testing deposit initialization.")
    logger.debug("Deposit details: %s", setup_deposit)
    deposit = setup_deposit
    assert deposit.get_deposit_amount() == 100
    assert deposit.get_deposit_term() == 2
    assert deposit.get_annual_rate() == 10


def test_final_amount(setup_deposit):
    """Testing actual final amount the same as expected final amount."""
    logger.info("Testing final amount.")
    actual_final_amount = setup_deposit.final_amount()
    logger.debug("Final amount1: %f", actual_final_amount)
    expected_final_amount = 100 * (1 + 10 / 12 / 100) ** (2 * 12)
    assert round(actual_final_amount, 2) == round(expected_final_amount, 2)


def test_bank_deposit(setup_bank, setup_user1_bank, setup_initial_amount,
                      setup_years):
    """Testing bank deposit."""
    logger.info("Testing bank deposit.")
    final_amount = setup_bank.deposit(setup_user1_bank, setup_initial_amount,
                                      setup_years)
    logger.debug("User %s final amount1: %f", setup_user1_bank,
                 final_amount)
    assert setup_user1_bank in setup_bank.user_accounts
    assert (round(setup_bank.user_accounts[setup_user1_bank], 2) ==
            round(final_amount, 2))


def test_bank_withdraw(setup_deposit, setup_bank, setup_user1_bank,
                       setup_initial_amount, setup_years):
    """Testing the bank to withdraw the amount."""
    logger.info("Testing: the bank to withdraw the amount.")
    setup_bank.deposit(setup_user1_bank, setup_initial_amount, setup_years)
    withdrawn_amount = setup_bank.withdraw(setup_user1_bank)
    logger.debug("User %s withdrawn amount: %f", setup_user1_bank,
                 withdrawn_amount)
    assert setup_user1_bank not in setup_bank.user_accounts
    assert round(withdrawn_amount, 2) == round(setup_deposit.final_amount(), 2)


def test_bank_withdraw_secondary_user(setup_bank, setup_user1_bank,
                                      setup_years, setup_initial_amount,
                                      setup_user2_bank):
    """Testing the user2 tries to withdraw amount from the user1's account."""
    logger.info("Testing the user2 tries to withdraw amount not from his "
                "account.")
    setup_bank.deposit(setup_user1_bank, setup_initial_amount, setup_years)
    withdrawn_amount = setup_bank.withdraw(setup_user2_bank)
    logger.debug("User2 %s withdrawn amount: %f", setup_user2_bank,
                 withdrawn_amount)
    assert setup_initial_amount != (withdrawn_amount, 2)


def test_bank_withdraw_nonexistent_user(setup_bank):
    """Testing bank withdraw for nonexistent user."""
    logger.info("Testing bank withdraw for nonexistent user.")
    withdrawn_amount = setup_bank.withdraw("NonexistentUser")
    logger.debug("Nonexistent user withdrawn amount: %f",
                 withdrawn_amount)
    assert withdrawn_amount == 0


def test_initial_amount_less_final_amount(setup_deposit, setup_initial_amount):
    """Testing the initial amount is less than the final amount."""
    logger.info("Testing that the initial amount is less than the final "
                "amount.")
    final_amount = setup_deposit.final_amount()
    logger.debug("Initial amount: %f, final amount: %f",
                 setup_initial_amount, final_amount)
    assert setup_initial_amount < final_amount
