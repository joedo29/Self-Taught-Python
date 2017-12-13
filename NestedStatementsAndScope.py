# Author Joe Do
# Nested Statement and Scope in Python

'''
It is important to understand how Python deals with the variable names you assign.
When you create a variable name in Python the name is stored in a *name-space*.
Variable names also have a *scope*, the scope determines the visibility of that variable name to other parts of your code.
'''

#  Example:
x = 25

def printer():
    x = 50
    return x

print(x) # print 25
print(printer()) # print 50

#Enclosing function locals.
# This occurs when we have a function inside a function (nested functions)
name = 'This is a global name'


def greet():
    # Enclosing function
    name = 'Sammy'
    def hello():
        print ('Hello ' + name)
    hello()
greet()

# #Local Variables When you declare variables inside a function definition,
# they are not related in any way to other variables with the same names used outside the function
x = 50
def func(x):
    print ('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)

# Global statement is used to declare that y if global var
y = 50

def func():
    global y
    print('This function is now using the global y!')
    print('Because of global y is: ', y)
    y = 2
    print('Ran func(), changed global y to', y)

print('Before calling func(), y is: ', y)
print(func())
print('Value of y (outside of func()) is: ', y)