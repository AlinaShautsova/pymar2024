"""Module contains a solution to the task: bank deposit."""


class Deposit:

    def __init__(self, sum_of_deposit_N, deposit_term_R, annual_rate=10):
        """Function initializes a new instance of the Deposit class."""
        self.sum_of_deposit_N = sum_of_deposit_N
        self.deposit_term_R = deposit_term_R
        self.annual_rate = annual_rate

    def final_amount(self):
        """Function calculate the total deposit amount taking into account
        the monthly capitalization."""
        months = self.deposit_term_R * 12
        monthly_rate = self.annual_rate / 12 / 100
        final_amount1 = self.sum_of_deposit_N

        for i in range(months):
            final_amount1 += final_amount1 * monthly_rate
        return final_amount1


class Bank:
    def __init__(self):
        """Function initializes a new instance of the Bank class."""
        self.user_accounts = {}

    def deposit(self, user1, sum_of_deposit_N, deposit_term_R):
        """Function takes the deposit amount and term and returns the total
         amount in the user's account."""
        deposit = Deposit(sum_of_deposit_N, deposit_term_R)
        final_amount1 = deposit.final_amount()
        self.user_accounts[user1] = final_amount1
        return final_amount1

    def refund_of_amount(self, user1):
        if user1 in self.user_accounts:
            return self.user_accounts[user1]
        else:
            return f"User {user1} don't have deposit."

    def withdraw(self, user1):
        """Function withdraws the deposit amount for the user."""
        if user1 in self.user_accounts:
            amount = self.user_accounts.pop(user1)
            return amount
        else:
            return f"The user {user} doesn't have deposit."


bank = Bank()
user = "Petya"
initial_amount = 100
years = 2

final_amount = bank.deposit(user, initial_amount, years)
print(f"Total invoice amount {user} after {years} years: {final_amount:.2f} "
      f"euro.")

refund_amount = bank.refund_of_amount(user)
print(f"User deposit amount {user}: {refund_amount:.2f} euro.")

withdrawn_amount = bank.withdraw(user)
if isinstance(withdrawn_amount, float):
    print(f"User {user} withdrawn {withdrawn_amount:.2f} euro.")
else:
    print(withdrawn_amount)
