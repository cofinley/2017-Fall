"""
    Connor Finley
    Advanced Python
    Shape Classes Assignment
    2017/10/24
"""

from math import pi, sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        # Shift point's x and y by dx and dy, respectively
        self.x += dx
        self.y += dy

    def dist(self, other):
        # Calculate Euclidean distance from this point to the `other` point
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __repr__(self):
        # Custom string representation
        return "({},{})".format(self.x, self.y)


class Eclipse:
    def __init__(self, center_point, y_extent, x_extent):
        self.center_point = center_point
        # Eclipse's A is half the total height
        self.height = y_extent * 2
        # Eclipse's B is half the total width
        self.width = x_extent * 2

    def get_area(self):
        return pi * ((self.height / 2)**2 + (self.width / 2)**2)

    def translate(self, dx, dy):
        # Re-use translation function
        self.center_point.translate(dx, dy)

    def __repr__(self):
        return "Eclipse with center: {}; Width: {}; Height: {}".format(self.center_point, self.width, self.height)


class Circle(Eclipse):
    def __init__(self, center_point, r):
        Eclipse.__init__(self, center_point, r, r)
        self.radius = self.height / 2

    def get_area(self):
        return pi * self.radius**2

    def contains(self, other):
        # Get distance between both circles' centers
        # If radius of circle 1 is greater than the distance + radius of circle 2, circle 1 contains circle 2
        dist = self.center_point.dist(other.center_point)
        return self.radius > (other.radius + dist)

    def __repr__(self):
        return "Circle with center: {}; Radius: {}".format(self.center_point, self.radius)


def get_eclipse():
    # User prompts for generating an eclipse object
    center_x = float(input("Specify the center x coordinate: "))
    center_y = float(input("Specify the center y coordinate: "))
    p = Point(center_x, center_y)
    a = float(input("Specify the eclipse's A value (half height): "))
    b = float(input("Specify the eclipse's B value (half width): "))
    e = Eclipse(p, a, b)
    return e


def get_circle():
    # User prompts for generating an circle object
    center_x = float(input("Specify the center x coordinate: "))
    center_y = float(input("Specify the center y coordinate: "))
    p = Point(center_x, center_y)
    r = float(input("Specify the circle's radius: "))
    c = Circle(p, r)
    return c


def main():
    # Testing code
    print("Eclipse:")
    e = get_eclipse()
    print(e)
    translation_x = float(input("Translation amount (x): "))
    translation_y = float(input("Translation amount (y): "))
    e.translate(translation_x,translation_y)
    print("\nNew eclipse:", e)

    print("\nCircle 1")
    c1 = get_circle()
    print("\nCircle 2")
    c2 = get_circle()
    print("\nCircle 1 contains circle 2?", c1.contains(c2))

if __name__ == "__main__":
    main()
