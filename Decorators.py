# Author: Joe Do
# Decorators in Python
# Decorators can be thought of as functions which modify the functionality of another function.
# They help to make your code shorter and more "Pythonic".

def new_decorator(func):
    def wrap_func():
        print('Code would be here, before executing the func')

        func()

        print('Code here will execute after the func()')

    return wrap_func

@new_decorator
def func_needs_decorator():
    print('\t Execute this function using a Decorator')

func_needs_decorator()

# Build decorator manually
# func_needs_decorator = new_decorator(func_needs_decorator)
