__doc__ = """Remove Assignments to Parameters

The code assigns to a parameter.
Use a temporary variable instead.
"""


# Original code
def degree_2(x):
    x = x * x
    return x


# Refactored code
def ref_degree_2(x):
    result = x * x
    return result


# Tests
if __name__ == '__main__':
    assert degree_2(20) == ref_degree_2(20)
