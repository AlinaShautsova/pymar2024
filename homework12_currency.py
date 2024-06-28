"""Module contains a solution to the task: Currency Converter."""
from decimal import Decimal, ROUND_HALF_UP


class Currency:
    """A dictionary of currencies with exchange rates has been added to
    the class ."""
    exchange_rates = {
            'USD': 3.2,
            'EUR': 3.5,
            'PLN': 7.8,
            'BYN': 1.0
    }


class Person:
    """Enables initialization function."""
    def __init__(self, name, currency, amount):
        """Function initializes name of person, currency and amount
        of Person class."""
        self.name = name
        self.currency = currency
        self.amount = amount


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
        self.exchange_rates = Currency.exchange_rates

    def deposit(self, user1, sum_of_deposit, deposit_term):
        """Function takes the deposit amount and term and returns the total
         amount in the user's account."""
        deposit = Deposit(sum_of_deposit, deposit_term)
        final_amount1 = deposit.final_amount()
        self.user_accounts[user1] = final_amount1
        return final_amount1

    def exchange_currency(self, amount, from_currency, to_currency='BYN'):
        """Function converts money from one currency to another."""
        if from_currency == to_currency:
            answer = amount
        else:
            amount_in_byn = amount * self.exchange_rates[from_currency]
            answer = amount_in_byn / self.exchange_rates[to_currency]
            answer = float(Decimal(str(answer)).
                           quantize(Decimal('1.' + '0' * 2),
                                    rounding=ROUND_HALF_UP))
        return answer, to_currency

    def withdraw(self, user1):
        """Function withdraws the deposit amount for the user."""
        if user1 in self.user_accounts:
            amount = self.user_accounts.pop(user1)
            return amount
        return 0


bank = Bank()
person1 = Person("Vasya", 'USD', 10.0)
person2 = Person("Petya", 'EUR', 5.0)

assert (bank.exchange_currency(person1.amount, person1.currency) ==
        (32.0, "BYN"))
assert (bank.exchange_currency(person2.amount, person2.currency) ==
        (17.5, "BYN"))
assert bank.exchange_currency(person1.amount, person1.currency,
                              'EUR') == (9.14, "EUR")
assert bank.exchange_currency(person2.amount, person2.currency,
                              'USD') == (5.47, "USD")
