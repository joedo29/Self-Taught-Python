# bank_account.py
# Author: Joe Do
# Date: March 28, 2018

class BankAccount:
    """ An abstract base class representing a bank account """
    currency = '$'
    def __init__(self, customer, account_number, balance = 0):
        """
        Initialize BankAccount class with a customer, account number
        and a balance (which defaults to 0).
        """
        self.customer       = customer
        self.account_number = account_number
        self.balance        = balance
    def deposit(self, amount):
        """
        deposit some amount into bank account
        """
        if amount > 0:
            self.balance += amount
        else:
            print('Invalid deposit amount: ', amount)
    def withdraw(self, amount):
        """
        withdraw some amount from bank account. Check for Insufficient funds
        """
        if amount > 0:
            if amount > self.balance:
                print('Insufficient funds')
            else:
                self.balance -= amount
        else:
            print('Invalid withdraw amount: ', amount)
    def check_balance(self):
        """
        Print account balance statement
        """
        print('The balance of account number', self.account_number, 'is',
        self.currency,self.balance)

# List of test cases for BankAccount abstract class
# joe = BankAccount('Joe Do', 1234554321)
# print(joe.account_number)
# joe.deposit(100)
# print(joe.balance)
# joe.withdraw(20)
# print(joe.balance)
# joe.check_balance
