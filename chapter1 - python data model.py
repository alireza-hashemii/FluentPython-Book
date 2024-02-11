"""
A simple class to learn deeply 
the concept of special methods
in Python - taken from the first
chapter of the fluent python book 
"""


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.x},{self.y}"

    def __repr__(self) -> str:
        return f"Point{self.x,self.y}"

    def __mul__(self, scalar: int):
        return Point(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: int):
        return Point(self.x * scalar, self.y * scalar)

    def __bool__(self):
        return bool(self.x or self.y)

    def __add__(self, number: int):
        x = self.x + number
        y = self.y + number
        return Point(x, y)

    def __radd__(self, number: int):
        x = self.x + number
        y = self.y + number
        return Point(x, y)

    def __sub__(self, number: int):
        x = self.x - number
        y = self.y - number
        return Point(x, y)

    def __rsub__(self, number: int):
        x = number - self.x
        y = number - self.y
        return Point(x, y)

    def __gt__(self, point):
        return self.x + self. y > point.x + point.y

    def __ge__(self, point):
        return self.x + self. y >= point.x + point.y

    def __pow__(self, number: int):
        self.x = self.x ** number
        self.y = self.y ** number
        return repr(self)

    def __truediv__(self, number: int):
        self.x = self.x / number
        self.y = self.y / number
        return repr(self)

    def __floordiv__(self, number: int):
        self.x = self.x // number
        self.y = self.y // number
        return repr(self)

    def __reversed__(self):
        temp_x = self.x
        self.x = self.y
        self.y = temp_x
        return repr(self)
