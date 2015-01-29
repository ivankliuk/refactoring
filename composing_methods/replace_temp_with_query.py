__doc__ = """Replace Temp with Query

You are using a temporary variable to hold the result of an expression.
Extract the expression into a method. Replace all references to the temp
with the expression. The new method can then be used in other methods.
"""
from math import pi as PI


# Original code
class Circle(object):
    def __init__(self, radius):
        self._radius = radius

    def calc_area(self):
        area = PI * self._radius ** 2
        return area

    def calc_circumference(self):
        circ = 2 * PI * self._radius
        return circ


# Refactored code
class RefCircle(object):
    def __init__(self, radius):
        self._radius = radius

    def _base(self):
        return PI * self._radius

    def calc_area(self):
        return self._base() * self._radius

    def calc_circumference(self):
        return self._base() * 2


# Tests
if __name__ == '__main__':
    circle = Circle(50)
    ref_circle = RefCircle(50)
    assert circle.calc_area() == ref_circle.calc_area()
    assert circle.calc_circumference() == ref_circle.calc_circumference()
