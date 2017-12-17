# Author: Joe Do
# Errors and Exceptions in Python
# Everything about Errors and Exceptions in Python here:
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response

try:
    2 + 's'
except:
    print("There was an error")

finally: # always execute this line of code
    print("Finally this was printed")

try:
    f = open('phonebook1.txt', 'r')
    f.write('Test write this')
except:
    print("Error in writing to the file")
else:
    print("File write was a success")

# Ask for user input until user enters input correctly
def askInt():
    while True:
        try:
            val = int(input("Please enter an integer again: "))
        except:
            print("Looks like you did not enter an integer")
            continue
        else:
            print("Correct, that is an integer")
            break

        print(val)

askInt()

# Errors and Exceptions Homework -

# Problem 1
# Handle the exception thrown by the code below by using try and except blocks.

try:
    for i in [1, 2, 'c']:
        print
        i ** 2
except:
    print("You've got an error in your data. Please try again!")

# Problem 2
# Handle the exception thrown by the code below by using **try** and **except** blocks. Then use a **finally** block to print 'All Done.'

x = 5
y = 0
try:
    z = x / y
except:
    print("There is an error in your data. Please try again!")
finally:
    print("You got it!")


# Problem 3
# Write a function that asks for an integer and prints the square of it.
# Use a while loop with a try,except, else block to account for incorrect inputs.

def ask():
    while True:
        try:
            x = int(input("Please enter an integer: "))

        except:
            print("Looks like you did not enter an integer. Please try again!")
            continue

        else:
            print("You got it!")
            print("The square root of ", x, " is: ", x ** 2)
            break

ask()
