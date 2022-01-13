from turtle import *


class Square:
    def __init__(self, sidelength=50):
        self.sidelength = sidelength

    def draw(self, bigger=0):
        for _ in range(4):
            forward(self.sidelength)
            right(90)
        self.sidelength += bigger


class Triangle:
    def __init__(self, sidelength=50):
        self.sidelength = sidelength

    def draw(self, bigger=0):
        for _ in range(3):
            forward(self.sidelength)
            right(120)
        self.sidelength += bigger


class Star:
    def __init__(self, sidelength=50):
        self.sidelength = sidelength

    def draw(self, bigger=0):
        for _ in range(5):
            forward(self.sidelength)
            right(144)
        self.sidelength += bigger


class Polygon:
    def __init__(self, sides=6, sidelength=50):
        self.sidelength = sidelength
        self.sides = sides

    def draw(self, bigger=0):
        for _ in range(self.sides):
            forward(self.sidelength)
            right(360/self.sides)
        self.sidelength += bigger


class Rotation:
    def __init__(self, figure, angle=0, amount=10, bigger=0):
        self.base = figure
        self.bigger = bigger
        self.amount = amount
        if angle == 0:
            self.angle = 360 / self.amount
        else:
            self.angle = angle

    def draw(self):
        for _ in range(self.amount):
            self.base.draw(self.bigger)
            right(self.angle)


speed(0)
# Rotation(Square(5), angle=5, amount=60, bigger=5).draw()

# Rotation(Triangle(100), 20).draw()

Rotation(Star(5), angle=5, amount=60, bigger=5).draw()

# Rotation(Polygon(10, 50), 20).draw()

done()
