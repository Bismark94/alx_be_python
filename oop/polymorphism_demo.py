# polymorphism_demo.py

'''
    from math import pi

class Shape:
    def area(self):
        """
        Calculate area of the shape.
        Must be overridden by derived classes.
        """
        raise NotImplementedError("Derived classes must override area()")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """
        Return the area of the rectangle (length * width).
        """
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Return the area of the circle (π * radius^2).
        """
        return 3.14 * (self.radius ** 2)
'''



    # polymorphism_demo.py

import math

class Shape:
    def area(self):
        """
        Calculate the area of the shape. Must be overridden by derived classes.
        """
        raise NotImplementedError("Derived classes must override area()")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """
        Return the area of the rectangle (length * width).
        """
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Return the area of the circle (π * radius^2).
        """
        return math.pi * (self.radius ** 2)

if __name__ == "__main__":
    # Demonstrate polymorphism
    shapes = [
        Rectangle(10, 5),  # area = 50
        Circle(7)           # area ≈ 153.938...
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

