# Joe Do
# Python uses file objects to interact with external files on your computer.
# These file objects can be any sort of file you have on your computer,
# whether it be an audio file, a text file, emails, Excel documents, etc.
# Note: You will probably need to install certain libraries or modules to interact with those various file types,
# but they are easily available.
# Python has a built-in open function that allows us to open and play with basic file types.

# We're going to use some iPython magic to create a text file!

# Open the phonebook.txt file
my_file = open('phonebook.txt')

# Read a file using read() function
# after you read, the cursor is now at the end of the file
# meaning you can't read the file again unless you seek
print(my_file.read())

# Seek to the start of file (index 0) so you can read the file again
my_file.seek(0)
print(my_file.read())

# readlines() returns a list of the lines in the file
# readlines() avoid having to reset cursor every time
my_file.seek(0)
print()
print('The first line of the file is {p}'.format(p=my_file.readline()))

# ITERATING THROUGH A FILE
for line in open('phonebook.txt'):
    print(line)



# WRITING TO A FILE
# By default, using the open() function will only allow us to read the file,
# we need to pass the argument 'w' to write over the file. For example:
my_file = open('phonebook.txt', 'w+')

# now write to my_file
my_file.write('JOE DO 123456')
print(my_file.read())
