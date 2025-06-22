# main.py

from polymorphism_demo import Shape, Rectangle, Circle


def main():
    shapes = [
        Rectangle(10, 5),  # area = 50
        Circle(5)           # area ≈ 78.5
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")


if __name__ == "__main__":
    main()
