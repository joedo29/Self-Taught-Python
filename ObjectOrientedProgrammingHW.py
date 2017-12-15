# Author: Joe Do

# Object Oriented Programming
# Homework Assignment
#
# Problem 1
# Fill in the Line class methods to accept coordinate as a pair of tuples and return the slope and distance of the line.

from __future__ import print_function
import math

class Line(object):
    def __init__(self, coor1, coor2):  # coor1 = (x1, y1)  coor2 = (x2, y2)
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return math.sqrt((self.coor2[0] - self.coor1[0]) ** 2 + (self.coor2[1] - self.coor1[1]) ** 2)

    def slope(self):
        return (float(self.coor2[1] - self.coor1[1])) / float((self.coor2[0] - self.coor1[0]))


# EXAMPLE OUTPUT
print("Calculate the length of a line and the slope from two coordinates")
x1 = float(input("Enter x1 of first coordinate: "))
y1 = float(input("Enter y1 of first coordinate: "))
x2 = float(input("Enter x2 of first coordinate: "))
y2 = float(input("Enter y2 of first coordinate: "))
coordinate1 = (x1, y1)
coordinate2 = (x2, y2)

li = Line(coordinate1, coordinate2)

print("Length of the line is: ", (li.distance()))

print("Slope is: ", li.slope())

# ####Problem 2

# Fill in the class

import math

class Cylinder(object):
    # Class Object Attributes
    pi = math.pi

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):  # V=π*r**2*h
        r = self.radius
        h = self.height
        return Cylinder.pi * r ** 2 * h

    def surface_area(self):  # A = 2πrh + 2πr**2
        r = self.radius
        h = self.height
        return (2 * Cylinder.pi * r * h) + (2 * Cylinder.pi * r ** 2)


# EXAMPLE OUTPUT
print("Calculate volume and surface area of a cylinder")
h = float(input("Enter height: "))
r = float(input("Enter radius: "))
c = Cylinder(h, r)

print("The cylinder volume is: ", c.volume())

print("The cylinder surface area is: ", c.surface_area())

