__doc__ = """Inline Method

A method's body is just as clear as its name.
Put the method's body into the body of its callers and remove the method.
"""
from math import pi as PI


# Original code
class Circle(object):
    def __init__(self, radius):
        self._radius = radius

    def calc_area(self):
        area = PI * self._radius ** 2
        return area

    def print_area(self):
        area = self.calc_area()

        message = (u'Area of a disk with radius {0} is '
                   u'{1}\n'.format(self._radius, area))
        print message


# Refactored code
class RefCircle(object):
    def __init__(self, radius):
        self._radius = radius

    def print_area(self):
        area = PI * self._radius ** 2

        message = (u'Area of a disk with radius {0}'
                   u' is {1}\n'.format(self._radius, area))
        print message


# Tests
if __name__ == '__main__':
    circle = Circle(50)
    ref_circle = RefCircle(50)
    assert circle.print_area() == ref_circle.print_area()
