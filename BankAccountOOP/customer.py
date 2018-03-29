# customer.py
# Author: Joe Do
# Date: March 28, 2018

from datetime import datetime
class Customer:
    """
    A class representing a bank customer
    """
    def __init__(self, name, address, date_of_birth):
        self.name = name
        self.address = address
        self.date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')

    def get_age(self):
        """
        Calculate and return customer birthday
        """
        today = datetime.today()
        try:
            birthday = self.date_of_birth.replace(year=today.year)
        except ValueError:
            # in case someone birthday is Feb 29 and this year is not leap year
            birthday = self.date_of_birth.replace(year=today.year,
                                                day=self.date_of_birth.day - 1)
        if birthday > today:
            return today.year - self.date_of_birth.year - 1
        return today.year - self.date_of_birth.year

# List of test cases for Customer class
# customer = Customer('Joe Do', '12345 1st Ave NE, Seattle, WA 98079', '1987-09-20')
# print(customer.name)
# print(customer.date_of_birth)
# print(customer.get_age())
