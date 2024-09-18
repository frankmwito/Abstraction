# Abstract shape class

from abc import ABC, abstractmethod
import math

# Abstract class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Rectangle class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * math.pow(self.radius, 2)

# Triangle class
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# Creating instances of each shape and printing their areas
shape1 = Rectangle(int(input("Enter length of the rectangle: ")), int(input("Enter width of the rectangle: ")))
print(f"Area of Rectangle: {shape1.area()}")

shape2 = Circle(int(input("Enter radius of the circle: ")))
print(f"Area of Circle: {shape2.area()}")

shape3 = Triangle(int(input("Enter base of the triangle: ")), int(input("Enter height of the triangle: ")))
print(f"Area of Triangle: {shape3.area()}")
