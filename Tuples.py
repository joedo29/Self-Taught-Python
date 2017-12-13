# Joe Do
# Tuples
# In Python tuples are very similar to lists, however, unlike lists they are immutable meaning they can not be changed.
# You would use tuples to present things that shouldn't be changed, such as days of the week, or dates on a calendar.
#
# In this section, we will get a brief overview of the following:
#
# 1.) Constructing Tuples
# 2.) Basic Tuple Methods
# 3.) Immutability
# 4.) When to Use Tuples.
# You'll have an intuition of how to use tuples based on what you've learned about lists.
# We can treat them very similarly with the major distinction being that tuples are immutable.
#
# Constructing Tuples
# The construction of a tuples use () with elements separated by commas.

# You can create a tuple with mix type
t = (1, 2, 3, 3, 'Joe', [1, 2, 3])
print(t)

# check length of tuple just like list
print(len(t))

# use indexing similar to list
print(t[-1])

# use .index to enter a value and return the index
print("Index of value 'Joe' is {p}".format(p=t.index('Joe')))

# use count to get the number of times value appear
print('3 appears {p} times in tuple t'.format(p=t.count(3)))


# When to use tuple?
# If in your program you are passing around an object and need to make sure it does not get changed,
# then tuple become your solution. It provides a convenient source of data integrity
