__doc__ = """Replace Magic Number with Symbolic Constant

You have a literal number with a particular meaning.
Create a constant, name it after the meaning, and replace the number with it.
"""


# Original code
def potential_energy(mass, height):
    return mass * 9.81 * height


# Refactored code
GRAVITY_CONSTANT = 9.81


def ref_potential_energy(mass, height):
    return mass * GRAVITY_CONSTANT * height


# Tests
if __name__ == '__main__':
    assert potential_energy(100, 1000) == ref_potential_energy(100, 1000)
