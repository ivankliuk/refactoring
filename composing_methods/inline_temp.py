__doc__ = """Inline Temp

You have a temp that is assigned to once with a simple expression, and the temp
is getting in the way of other refactorings.
Replace all references to that temp with the expression.
"""
from math import pi as PI


# Original code
def calc_disc_area(radius):
    area = PI * radius ** 2
    return area


# Refactored code
def ref_calc_disc_area(radius):
    return PI * radius ** 2


# Tests
if __name__ == '__main__':
    assert calc_disc_area(50) == ref_calc_disc_area(50)
