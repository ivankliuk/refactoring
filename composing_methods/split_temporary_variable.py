__doc__ = """Split Temporary Variable

You have a temporary variable assigned to more than once, but is not a loop
variable nor a collecting temporary variable.
Make a separate temporary variable for each assignment.
"""
from math import pi as PI


# Original code
def ball_geometry(r):
    """Returns geometrical parameters of the ball"""
    params = dict()
    temp = 4 * PI * r ** 2
    params['surface_area'] = temp
    temp = 4 * PI * r ** 3 / 3
    params['volume'] = temp
    return params


# Refactored code
def ref_ball_geometry(r):
    """Returns geometrical parameters of the ball"""
    params = dict()
    area = 4 * PI * r ** 2
    params['surface_area'] = area
    volume = 4 * PI * r ** 3 / 3
    params['volume'] = volume
    return params


# Tests
if __name__ == '__main__':
    assert ball_geometry(5) == ref_ball_geometry(5)
