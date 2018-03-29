# main.py
# Author: Joe Do
# Date: March 28, 2018

import random
from bank_account import BankAccount
from customer import Customer

inputName    = input('What is your name? ')
inputAddress = input('What is your address? ')
inputDOB     = input('What is your DOB? yyyy-mm-dd ')
inputDeposit = int(input('How much would you like to deposit today? '))

customer1    = Customer(inputName, inputAddress, inputDOB)
bankCustomer = BankAccount(customer1, str(random.randint(1, 1000) * 1000000 + 123), inputDeposit)

print('Hi ', inputName, '! Welcome to Bank Of X. Your acc # is: ', bankCustomer.account_number,
        ' Your current balance is: $', bankCustomer.balance)

print('And by the way. I know that you are ', bankCustomer.customer.get_age(), ' years old.')

bankCustomer.withdraw(int(input('How much would you like to withdraw today? ')))
print('Your current balance is: $', bankCustomer.balance)
