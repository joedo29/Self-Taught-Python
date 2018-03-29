# main.py
# Author: Joe Do
# Date: March 28, 2018

from bank_account import BankAccount

# class inheritance
class SavingsAccount(BankAccount):
    """
    A class representing a saving account
    """
    def __init__(self, customer, account_number, interest_rate, balance=0):
        """
        Initialize the saving account
        """
        self.interest_rate = interest_rate
        super().__init__(customer, account_number, balance)
    def add_interest(self):
        self.balance *= (1. + self.interest_rate / 100)

# List of test cases for SavingsAccount class
# my_savings = SavingsAccount('Joe Do', 123454321, 6.0, 1000)
# my_savings.check_balance()
# my_savings.add_interest()
# my_savings.check_balance()
