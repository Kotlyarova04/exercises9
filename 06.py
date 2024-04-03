import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance(self, other):
        lenght_x = self.x - other.get_x()
        lenght_y = self.y - other.get_y()
        return math.sqrt(lenght_x**2 + lenght_y**2)

    def sum(self, other):
        new_x = self.x + other.get_x()
        new_y = self.y + other.get_y()
        return Point(new_x, new_y)

    def __str__(self):
        return f'Point:({self.x}, {self.y})'


point1 = Point(3,4)
point2 = Point(7,6)
print(point1.get_y())
print(point2.get_y())
print(point1.distance(point2))
print(point1.sum(point2))
