# Author: Joe Do
# Object Oriented Programming in Python

# Create a new object type called Sample
class Sample(object): # By convention we give classes a name that starts with a capital letter.
    pass
# Instances of Sample
x = Sample()
print(type(x))

# The syntax of creting an attribute is:
# self.attribute = something
# use __init__() method to initialize the attributes of an object. For example:
class Dog(object):
    def __init__(self, breed): # Each attribute in a class definition begins with a reference to the instance object.
        # It is by convention named self. The breed is the argument. The value is passed during the class instantiation.
        self.breed = breed

sam = Dog(breed='Lab') # here we pass the attribute 'Lab' to a dog named 'sam'
print(sam.breed) # calling breed of sam will return its attribute 'Lab'

frank = Dog(breed='Huskie') # or we can say frank = Dog('Huskie')
print(frank.breed)

# In Python there are also 'Class Object Attributes'. These Class Object Attributes are the same for any instance of the class.
class Person(object):
    # Class Object Attributes. Also by convention, we place them first before the init.
    species = 'Homo Sapiens'

    def __init__(self, first, last, phone):
        self.first = first
        self.last = last
        self.phone = phone
personA = Person('Joe', 'Do', '425-449-3635')
print(personA.first + ' ' + personA.last + ' ' + personA.species + ' ' + personA.phone)

personB = Person('Sang', 'Do', '0909-20-0987')
print(personB.first + ' ' + personB.last + ' ' + personB.species + ' ' + personB.phone)


# METHODS
# Methods are functions defined inside the body of a class. They are used to perform operations with the attributes of our objects.
# Methods are essential in encapsulation concept of the OOP paradigm. This is essential in dividing responsibilities in programming,
# especially in large applications.

class Circle(object):
    # Class Object Attribute
    pi = 3.14

    # Circle get instantiated with a radius (default is 1)
    def __init__(self, radius = 1):
        self.radius = radius

    # Area method calculates the area of the circle. Note the use of self
    def area(self):
        return self.radius * self.radius * Circle.pi

    # Perimeter method
    def perimeter(self):
        return 2 * Circle.pi * self.radius

    # Method for resetting (called setter in Java or C++) radius
    def setRadius(self, radius):
        self.radius = radius

    # Method for getting (called getter in Java or C++) radius (same as just calling .radius
    def getRadius(self):
        return self.radius

# Create a new Circle object
c = Circle()
c.setRadius(3) # set radius = 3
print('Radius is: ', c.getRadius())
print('Area is: ', c.area())
print("Perimeter is: ", c.perimeter())


#INHERITANCE
# Inheritance is a way to form new classes using classes that have already been defined.
# The newly formed classes are called derived classes, the classes that we derive from are called base classes.
# Important benefits of inheritance are code reuse and reduction of complexity of a program.
# The derived classes (descendants) override or extend the functionality of base classes (ancestors).
# For example, let's create an ancestor class called 'Animal' and a derived class call 'Cat'

class Animal(object):
    def __init__(self):
        print("A new animal  is created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")
class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("A new cat is created")
    def whoAmI(self):
        print("Cat")
    def bark(self):
        print("Meooo!")
ca = Cat()
ca.whoAmI()
ca.eat()
ca.bark()

# SPECIAL METHODS
# Classes in Python can implement certain operations with special method names.
# These methods are not actually called directly but by Python specific language syntax.
# For example Lets create a Book class:


class Book(object):
    def __init__(self, title, author, page):
        print("A book is created")
        self.title = title
        self.author = author
        self.page = page

    def __str__(self):
        return "Title: %s, Author: %s, Pages: %s" %(self.title, self.author, self.page)

    def __len__(self):
        return self.page

    def __del__(self):
        print("A book is destroyed")

b = Book("Intro to Python", "Joe Do", 199)

# Special methods
print(b)
print(len(b))
del b

# OOP HOMEWORKS