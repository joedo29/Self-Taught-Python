# Author: Joe Do
# Lambda Expressions in Python
# lambda's body is a single expression, not a block of statements.

# We will begin to breakdown this function which will be our lambda
def square(num):
    return num**2
print(square(2))

square1 = lambda num: num**2 # here we break it down to lambda and assign it to square1
print(square1(2))

# Another example
# Check if a number is even
isEven = lambda num: num % 2 == 0
print(isEven(10))

# Now let's write a lambda to wrap first character of a string
first = lambda s: s[0]
print(first("Hello"))

# Now let's print a string in reverse
reverseString = lambda r: r[::-1]
print(reverseString("Hello"))

# Lambda can accept more than one function
addNumbers = lambda a, b: a ** b
print(addNumbers(2, 2))
