# Author: Joe Do
# Everything about List in Python

x = [1, 2, 3, 4, 5]
print('X is {p}'.format(p=x))
y = [6, 7, 8, 9, 10]
print('Y is {p}'.format(p=y))
z = x + y
print('Z is the combination of x and y {p}'.format(p=z))
print('The inverse of z is {p}'.format(p=z[::-1]))
print('Length of z is {p}'.format(p=len(z)))

# check to see if an item is exist in a list
check = 200
if check in z:
    print('{p} is in z'.format(p=check))
else:
    print('{p} is not in z'.format(p=check))

# append method to add an element to the end of a list
x.append(200)
print('X is {p}'.format(p=x))

# insert element to a specified index
x.insert(2, 300) # insert 300 to index 2 of list x
print('X after insert is {p}'.format(p=x))

# pop method to take off the last index (you can choose what index to pop too)
print(x.pop())
print('X after pop is {p}'.format(p=x))

# reverse a list
x.reverse()
print('X after reverse is {p}'.format(p=x))

# sort a lit
x.sort()
print('X after sort is {p}'.format(p=x))

# List comprehension
# List comprehensions allow us to build out lists using a different notation.
# You can think of it as essentially a one line for loop built inside of brackets.
# For a simple example:

l = [x for x in 'Hello'] # grab every letter in string 'Hello'
print(l)
print(len(l))

l1 = [x**2 for x in range(11, 21)] # square number in a range and turn into a list
print(l1)

l3 = [x for x in range(11) if x % 2 == 0] # check for even numbers
print(l3)

# you can also do complicated arithmetic
# Convert Celsius to Fahrenheit
celsius = [-5, 0, 10, 20.1, 34.5]
fahrenheit = [((float(9) / 5) * temp + 32) for temp in celsius]
print(fahrenheit)


