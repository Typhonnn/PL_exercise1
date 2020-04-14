import math
import unittest

"""Author: Tal Balelty - 312270291"""


class GeometricShape:
    def __init__(self, area, perimeter):
        self.area = area
        self.perimeter = perimeter

    def __repr__(self):
        return "Area: %.5s Perimeter: %.5s" % (self.area, self.perimeter)


class Circle(GeometricShape):
    def __init__(self, radius):
        area = math.pi * radius * radius
        perimeter = 2 * math.pi * radius
        super().__init__(area, perimeter)

    def __repr__(self):
        return "Circle: %s" % (super().__repr__())


class Triangle(GeometricShape):
    def __init__(self, a, b, c):
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        perimeter = a + b + c
        super().__init__(area, perimeter)

    def __repr__(self):
        return "Triangle: %s" % (super().__repr__())


class Rectangle(GeometricShape):
    def __init__(self, a, b):
        area = a * b
        perimeter = 2 * a + 2 * b
        super().__init__(area, perimeter)

    def __repr__(self):
        return "Rectangle: %s" % (super().__repr__())


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

    def __repr__(self):
        return "Square: %s" % (GeometricShape.__repr__(self))


def main():
    user_shape = input("Choose The Shape by Typing The Number:\n1.Circle\n2.Triangle\n3.Rectangle\n4.Square\n")
    if user_shape == '1':
        print(Circle(float(input("Enter Radius: "))))
    elif user_shape == '2':
        print(Triangle(float(input("Enter Side 1: ")), float(input("Enter Side 2: ")), float(input("Enter Side 3: "))))
    elif user_shape == '3':
        print(Rectangle(float(input("Enter Long Side: ")), float(input("Enter Short Side: "))))
    elif user_shape == '4':
        print(Square(float(input("Enter Side: "))))
    else:
        print("Invalid Number Entered")


class TestGeometricShapes(unittest.TestCase):
    def test_circle(self):
        circle = Circle(5)
        self.assertEqual(circle.area, math.pi * 25)
        self.assertEqual(circle.perimeter, math.pi * 10)

    def test_triangle(self):
        tri = Triangle(3, 4, 5)
        self.assertEqual(tri.area, 6)
        self.assertEqual(tri.perimeter, 12)

    def test_rectangle(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area, 20)
        self.assertEqual(rect.perimeter, 18)

    def test_square(self):
        squ = Square(4)
        self.assertEqual(squ.area, 16)
        self.assertEqual(squ.perimeter, 16)


if __name__ == '__main__':
    unittest.main()
