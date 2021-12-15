#!/usr/bin/env python3


class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def rect_area(self) -> int:
        return self.width * self.height


rect1 = Rectangle(10, 5)
print(rect1.rect_area())
