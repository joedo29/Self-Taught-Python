# Author: Joe Do
# Zip and Enumerate in Python

# zip() makes an iterator that aggregates elements from each of the iterables.
# enumerate() allows you to keep a count as you iterate through an object.

# /////////////////////Zip////////////////////
# Example, let's zip two lists together
x = [1, 2, 3]
y = [4, 5, 6]
z = zip(x, y)
print(z) # output: [(1, 4), (2, 5), (3, 6)]

# What happen when you zip two lists with uneven length?
# Answer: The iterator stops when the shortest input iterable is exhausted.
x1 = [1, 2, 3]
y1 = [4, 5, 6, 7, 8]
z1 = zip(x1, y1)
print(z) # output is still [(1, 4), (2, 5), (3, 6)]

# You can also zip two sets
set1 = set(range(1, 5))
set2 = set(range(1, 5))
set3 = zip(set1, set2)
print(set3) # output [(1, 1), (2, 2), (3, 3), (4, 4)]

# What happen when you zop two dictionaries
# A: it only zips the keys by default
# I strongly recommended to not zip unequal lists
d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}
d3 = zip(d1, d2)
print(d3) # output: [('a', 'c'), ('b', 'd')]

# zip two string
s1 = 'joe'
s2 = 'doe'
s3 = zip(s1, s2)
print(s3) # output: [('j', 'd'), ('o', 'o'), ('e', 'e')]
print(s3[0]) # ('j', 'd')

# /////////////////////Enumerate////////////////////
list = ['a', 'b', 'c']

for count, item in enumerate(list):
    print(item)
    print(count)

print("total count is: ", count + 1)

# enumerate() becomes particularly useful when you have a case where you need to have some sort of tracker.
# For example:
list1 = range(20)
for count, item in enumerate(list1):
    if count >= 20: # only print from 1 to 20
        break
    else:
        print(item)