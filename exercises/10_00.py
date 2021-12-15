#!/usr/bin/env python3
class Point3D:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def show(self):
        return (self.x, self.y, self.z)


p1 = Point3D(1, 2, 3)
print(p1.show())
