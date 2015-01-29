__doc__ = """Substitute Algorithm

You want to replace an algorithm with one that is clearer.
Replace the body of the method with the new algorithm.
"""


# Original code
def evens(n):
    numbers = range(n)
    size = len(numbers)
    result = []
    i = 0
    while i < size:
        if i % 2 == 0:
            result.append(i)
        i += 1
    return result


# Refactored code
def ref_evens(n):
    return [i for i in range(n) if i % 2 == 0]


# Tests
if __name__ == '__main__':
    assert evens(20) == ref_evens(20)
