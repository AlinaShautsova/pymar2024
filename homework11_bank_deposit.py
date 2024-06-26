"""Module contains a solution to the task: bank deposit."""


class Deposit:
    """This class include functions for initializes, for calculation
    total amount. """
    def __init__(self, sum_of_deposit, deposit_term, annual_rate=10):
        """Function initializes a new instance of the Deposit class."""
        self.sum_of_deposit = sum_of_deposit
        self.deposit_term = deposit_term
        self.annual_rate = annual_rate

    def final_amount(self):
        """Function calculate the total deposit amount taking into account
        the monthly capitalization. And functions for returns: deposit amount,
        the deposit term in years, the annual interest rate."""
        months = self.deposit_term * 12
        monthly_rate = self.annual_rate / 12 / 100
        final_amount1 = self.sum_of_deposit

        for _ in range(months):
            final_amount1 += final_amount1 * monthly_rate
        return final_amount1

    def get_deposit_amount(self):
        """Returns the initial deposit amount."""
        return self.sum_of_deposit

    def get_deposit_term(self):
        """Returns the deposit term in years."""
        return self.deposit_term

    def get_annual_rate(self):
        """Returns the annual interest rate."""
        return self.annual_rate


class Bank:
    """This class include 3 functions for initializes, for takes deposit and
    withdraw the deposit amount."""
    def __init__(self):
        """Function initializes a new instance of the Bank class."""
        self.user_accounts = {}

    def deposit(self, user1, sum_of_deposit, deposit_term):
        """Function takes the deposit amount and term and returns the total
         amount in the user's account."""
        deposit = Deposit(sum_of_deposit, deposit_term)
        final_amount1 = deposit.final_amount()
        self.user_accounts[user1] = final_amount1
        return final_amount1

    def withdraw(self, user1):
        """Function withdraws the deposit amount for the user."""
        if user1 in self.user_accounts:
            amount = self.user_accounts.pop(user1)
            return amount
        return 0


bank = Bank()
USER = "Petya"
INITIAL_AMOUNT = 100
YEARS = 2

final_amount = bank.deposit(USER, INITIAL_AMOUNT, YEARS)
print(f"Total invoice amount {USER} after {YEARS} years: {final_amount:.2f} "
      f"euro.")

withdrawn_amount = bank.withdraw(USER)
if isinstance(withdrawn_amount, float):
    print(f"User {USER} withdrawn {withdrawn_amount:.2f} euro.")
else:
    print(withdrawn_amount)
