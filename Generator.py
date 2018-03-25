# Author: Joe Do
# Generator
# The generator functions will automatically suspend and resume their execution
# and state around the last point of value generation
# The main advantage here is that instead of having to compute an entire series
# of values upfront and the generator functions can be suspended,
# this feature is known as state suspension.

import memory_profiler
import random
import time

def square_numbers(num):
    result = []
    for i in num:
        result.append(i*i)
    return result

my_num = square_numbers([1,2,3,4,5])


# same function as above but with Generator
def square_numbers_decorator(num):
    for i in num:
        yield (i*i)
my_num_generator = square_numbers_decorator([1,2,3,4,5])
# list COMPREHENSION and Generator
my_nums = (x*x for x in [1,2,3,4,5])


# Below is a test to see how decorator save up your memory space
names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print ('Memory (Before): {}Mb'.format(memory_profiler.memory_usage()))

def people_list(num_people): # this function creates a list
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people): # this function creates a decorator
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

# t1 = time.clock()
# people = people_list(1000000)
# t2 = time.clock()
# With list you should get this:
# Memory (Before): [48.234375]Mb
# Memory (After) : [311.5390625]Mb
# Took 1.853254 Seconds

t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()
# With decorator you should get this:
# Memory (Before): [48.59765625]Mb
# Memory (After) : [48.62109375]Mb
# Took 1.399999999995849e-05 Seconds

print('Memory (After) : {}Mb'.format(memory_profiler.memory_usage()))
print('Took {} Seconds'.format(t2-t1))

print(next(people))
print(next(people))
