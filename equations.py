"""algebraic equations"""


from math import sqrt


def g(x):
    return 6*x**3 + 31*x**2 + 3*x - 10


def plug():
    x = -100
    while x < 100:
        if g(x) == 0:
            return x
        x += 1


def equation(a, b, c, d):
    """solves 'ax + b = cx + d' equations"""
    return (d - b) / (a - c)


def quad(a, b, c):
    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x1, x2


print(plug())
print(equation(2, 5, 0, 13))
print(quad(2, 7, -15))
print(plug())
