# Author: Joe Do
# Everything about Dictionaries in Python

#  If you're familiar with other languages you can think of these Dictionaries as hash tables.
# This section will serve as a brief introduction to dictionaries and consist of:
# 1.) Constructing a Dictionary
# 2.) Accessing objects from a dictionary
# 3.) Nesting Dictionaries
# 4.) Basic Dictionary Methods
# So what are mappings? Mappings are a collection of objects that are stored by a key,
# unlike a sequence that stored objects by their relative position.
# This is an important distinction, since mappings won't retain order since they have objects defined by a key.
# A Python dictionary consists of a key and then an associated value. That value can be almost any Python object.

# Make a dictionary
my_dict = {1:'string', 2:['this', 'is', 'a', 'list'], 3:100}
print('Value of key 3 is {p}'.format(p = my_dict[3]))

# you can call an index on a value if it's a list value
print(my_dict[2][1])

# you can even call method on that value
print(my_dict[2][0].upper())

# or do computation on that value
print(my_dict[3] - 1)

# create a new key through assignment
my_dict[4] = [1, 2, 3]
print(my_dict)

# Nesting with dictionaries
d = {'key':{'key2':{'key3':'This is the value of three nested dictionary'}}}
print(d['key']['key2']['key3'])

# keys() method returns the list of all keys
print(my_dict.keys())

# values() method returns the list of all values
print(my_dict.values())

print(my_dict.items())

# this is tricky
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1])