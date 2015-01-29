__doc__ = """Replace Method with Method Object

You have a long method that uses local variables in such a way that you cannot
apply Extract Method.
Turn the method into its own object so that all the local variables become
fields on that object. You can then decompose the method into other methods
on the same object.
"""


# Original code
class Employee(object):
    def __init__(self, salary, seniority, courses_passed, projects_completed):
        self.salary = salary
        self.seniority = seniority
        self.courses_passed = courses_passed
        self.projects_completed = projects_completed

    def benefits(self, rate1, rate2, rate3):
        avg_rate = (rate1 + rate2 + rate3) / 3
        progress = self.courses_passed + 2 * self.projects_completed
        efficiency = self.salary / self.seniority
        total_benefits = avg_rate * progress * efficiency / 100
        return total_benefits


# Refactored code
class Benefits(object):
    def calculate(self, employee, rate1, rate2, rate3):
        avg_rate = (rate1 + rate2 + rate3) / 3
        progress = employee.courses_passed + 2 * employee.projects_completed
        efficiency = employee.salary / employee.seniority
        total_benefits = avg_rate * progress * efficiency / 100
        return total_benefits


# Tests
if __name__ == '__main__':
    employee = Employee(100000, 5, 10, 7)
    benefits = employee.benefits(2, 3, 5)

    ref_employee = Employee(100000, 5, 10, 7)
    ref_benefits = Benefits().calculate(ref_employee, 2, 3, 5)

    assert benefits == ref_benefits
