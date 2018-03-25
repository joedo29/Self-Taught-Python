# Author: Joe Do
# map() and reduce() in Python

# map() is a function that takes in two arguments: a function and a sequence iterable. In the form: map(function, sequence)
# The first argument is the name of a function and the second a sequence (e.g. a list).
# map() applies the function to all the elements of the sequence. It returns a new list with the elements changed by function.

# Let's make our own map function
def map(aFunc, aSeq):
	result = []
	for x in aSeq: result.append(aFunc(x))
	return result

# Let's start with an example to convert Fahrenheit to Celsius using map():

def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9) * (T-32)

print(fahrenheit(0))

tempC = [0, 22.5, 40, 100] # now let's convert a whole list using map()

tempF = map(fahrenheit, tempC) # convert to F
print("Convert C to F: ", tempF)

backToC = map(celsius, tempF) # convert back to C
print("Convert F to C: ", backToC)

# map and lambda
print("map and lambda: ", map(lambda T: (9.0/5)*T + 32, tempC))

# Recall that lambda can takes in more than 2 variables?
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
# print(map(lambda x, y: x+y, a, b))

# /////////////////////////

# Let's make our own reduce function
def reduce(fnc, seq):
    tally = seq[0]
    for next in seq[1:]:
            tally = fnc(tally, next)
    return tally


def digits_to_num(digits):
    return reduce(lambda x, y: x * 10 + y, digits)
print(digits_to_num([3, 4, 3, 2, 1]))

# reduce() is another built-in function in python along with map and filter
list = [10, 20, 30, 40]
print('reduce: ')
print(reduce(lambda x, y: x+y, list))

# Now let's find the maximum value of a sequence
# you can use max() which was already exist
print(max(list))

# or use reduce()
max_find = lambda a, b: a if (a > b) else b
print(reduce(max_find, list))

# /////////////////////////
# Filter
# The function filter(function, list) offers a convenient way to filter out all the elements of an iterable,
# for which the function returns True.

# First let's make a function
def checkEven(number):
    if number % 2 == 0:
        return True
list = range(20)
print(filter(checkEven, list))

# Filter is more commonly used with lambda functions
# this because we usually use filter for a quick job where we don't want to write an entire function.
v = filter(lambda x: x%2==0, range(10))
print(v)

# Example: find numbers that are greater than 3 and less than zero
l = [1, 3, 4, 2, -1, 10] # 4, 10 are greater than 3, -1 is negative
l1 = filter(lambda x: x > 3 or x < 0, l)
print(l1)