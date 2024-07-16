"""Unittest for Homework 11: bank deposit."""

import unittest
import logging
from homework11_bank_deposit import Deposit, Bank

formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
file_handler = logging.FileHandler('test_bank.log')
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)


class TestBank(unittest.TestCase):
    """Test cases for the bank class deposit method."""

    def setUp(self):
        """Set up the test environment."""
        logger.info("Assign variables.")
        self.bank = Bank()
        self.user = "Petya"
        self.initial_amount = 100
        self.years = 2
        self.deposit = Deposit(self.initial_amount, self.years)
        self.user2 = "Katya"

    def tearDown(self):
        """Deleting variables after each test."""
        logger.info("Deleting variables.")
        del self.bank
        del self.user
        del self.initial_amount
        del self.years
        del self.deposit
        del self.user2

    def test_deposit_initialization(self):
        """Testing deposit initialization."""
        logger.info("Testing deposit initialization.")
        logger.debug("Deposit details: %s", self.deposit)
        self.assertEqual(self.deposit.get_deposit_amount(),
                         self.initial_amount)
        self.assertEqual(self.deposit.get_deposit_term(), self.years)
        self.assertEqual(self.deposit.get_annual_rate(), 10)

    def test_final_amount(self):
        """Testing actual final amount the same as expected final amount."""
        logger.info("Testing final amount.")
        actual_final_amount = self.deposit.final_amount()
        logger.debug("Final amount1: %f", actual_final_amount)
        expected_final_amount = 100 * (1 + 10 / 12 / 100) ** (2 * 12)
        self.assertAlmostEqual(actual_final_amount, expected_final_amount,
                               places=2)

    def test_bank_deposit(self):
        """Testing bank deposit."""
        logger.info("Testing bank deposit.")
        final_amount = self.bank.deposit(self.user, self.initial_amount,
                                         self.years)
        logger.debug("User %s final amount1: %f", self.user,
                     final_amount)
        self.assertIn(self.user, self.bank.user_accounts)
        self.assertAlmostEqual(self.bank.user_accounts[self.user],
                               final_amount, places=2)

    def test_bank_withdraw(self):
        """Testing the bank to withdraw the amount."""
        logger.info("Testing: the bank to withdraw the amount.")
        self.bank.deposit(self.user, self.initial_amount, self.years)
        withdrawn_amount = self.bank.withdraw(self.user)
        logger.debug("User %s withdrawn amount: %f", self.user,
                     withdrawn_amount)
        self.assertNotIn(self.user, self.bank.user_accounts)
        self.assertAlmostEqual(withdrawn_amount, self.deposit.final_amount(),
                               places=2)

    def test_bank_withdraw_secondary_user(self):
        """Testing the user2 tries to withdraw amount from the user1's
        account."""
        logger.info("Testing: the user2 tries to withdraw amount not from his"
                    " account.")
        self.bank.deposit(self.user, self.initial_amount, self.years)
        withdrawn_amount = self.bank.withdraw(self.user2)
        logger.debug("User2 %s withdrawn amount: %f", self.user2,
                     withdrawn_amount)
        self.assertNotEqual(self.initial_amount, withdrawn_amount)

    def test_bank_withdraw_nonexistent_user(self):
        """Testing bank withdraw for nonexistent user."""
        logger.info("Testing: bank withdraw for nonexistent user.")
        withdrawn_amount = self.bank.withdraw("NonexistentUser")
        logger.debug("Nonexistent user withdrawn amount: %f",
                     withdrawn_amount)
        self.assertEqual(withdrawn_amount, 0)

    def test_initial_amount_less_final_amount(self):
        """Testing the initial amount is less than the final amount."""
        logger.info("Testing that the initial amount is less than the "
                    "final amount.")
        final_amount = self.deposit.final_amount()
        logger.debug("Initial amount: %f, final amount: %f",
                     self.initial_amount, final_amount)
        self.assertLess(self.initial_amount, final_amount)


if __name__ == '__main__':
    unittest.main()
