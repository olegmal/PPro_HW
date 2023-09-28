import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(Point):
    def __init__(self, x, y, radius):
        Point.__init__(self, x, y)
        self.radius = radius

    def contains(self):
        hypotenuse = math.sqrt(self.x ** 2 + self.y ** 2)
        if hypotenuse <= self.radius:
            print(True)
        else:
            print(False)


circle = Circle(1, 4, 7)
circle.contains()

