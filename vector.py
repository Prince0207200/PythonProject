import math


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
            s=f"{self.x},{self.y},{self.z}"
            return s

    def __eq__(self, other):
            return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mag__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

v1=Vector(1,2,3)
v2=Vector(8,2,1)
print(v1)
print(v2)
v3=v1+ v2
print(v3)
v4=v1- v2
print(v4)
