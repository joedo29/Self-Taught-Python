# Author: Joe Do
# for Loops in Python

# A for loop acts as an iterator in Python, it goes through items that are in a sequence or any other iterable item.
# Objects that we've learned about that we can iterate over include strings,lists,tuples,
# and even built in iterables for dictionaries, such as the keys or values

# Here's the general format for a for loop in Python:
'''
for item in object:
    statements to do stuff
'''
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in l:
    if num % 2 != 0:
        print(num)
    else:
        print("Even number")

sum = 0
for num in l:
    sum += num
print('Sum of all values in list l is {p}'.format(p = sum))

#  Remember strings are a sequence so when we iterate through them we will be accessing each item in that string.
a = 'String'
for letter in a:
    print(letter)

# for loop can be used for 'unpacking' a tuple
list = [(1, 2), (3, 4), (5, 6)]
for tuple in list: # not yet unpacking
    print(tuple)

for (t1, t2) in list: # Unpacking
    print(t1)

for (t1, t2) in list: # Unpacking
    print('{t1} {t2}'.format(t1=t1, t2=t2))

# for loops for dictionary
d = {1: 'Joe', 2: 'Do', 3: 4254493635}
for i1 in d.keys(): # print all keys of dictionary d
    print(i1)

for i2 in d.values(): # print all values of dictionary d
    print(i2)

for i1, i2 in d.items():
    print('{i1} : {i2}'.format(i1=i1, i2=i2))
