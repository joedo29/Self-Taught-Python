# Author: Joe Do
# Functions in Python

# function's syntax in Python. It has the following form:
'''
def name_of_function(arg1,arg2):
    This is where the function's Document String (doc-string) goes

    Do stuff here
    return desired result
'''

# A simple print hello function
def say_hello(name):
    '''
    This function will print out hello plus your input name
    '''
    print("Hello %s" %name)

say_hello("Joe")

# Using return
def add_num():
    print("Enter two numbers that you wanna add")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1 + num2

print(add_num())

# Find factorial of a number
def factorial():
    num = int(input("Enter a number to find its factorial: "))
    if num == 0 or num == 1:
        return 1
    else:
        result = 1
        for n in range(2, num + 1):
            result *= n

        return result

print(factorial())

# Find factorial using recursive

def rFactorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * rFactorial(n - 1)
n = int(input("Enter a number to find its factorial recursively: "))
print(rFactorial(n))