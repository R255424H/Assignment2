# write a function that takes a list of different shapes such as CIRCLE and RECTANGLE
# calculate  the total area of all shapes using POLYMORPHISM

import math

# parent class for shape (circle, rectangle)
class Shape:
    def area(self):
        raise

#shape subclasses
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    #defining method for Circle
    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    #defining method for Rectangle
    def area(self):
        return self.length * self.width

#demonstrating polymorphism
shapes=[Circle(5), Rectangle(5,4)]
for Shape in shapes:
    print(f"area:{Shape.area()}")