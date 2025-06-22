# polymorphism_demo.py

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
