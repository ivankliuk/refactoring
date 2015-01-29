__doc__ = """Encapsulate Field

There is a public field.
Make it private and provide accessors.
"""
import unittest


# Original
class Person(object):
    def __init__(self, name):
        self._name = name


# Refactored code
class RefPerson(Person):
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def del_name(self):
        del self._name


# Refactored code to property
class RefPersonToProperty(Person):
    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def del_name(self):
        del self._name

    name = property(get_name, set_name, del_name, "Name property")


# Refactored code to property decorators
class RefPersonToPropertyDecorator(Person):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter
    def name(self):
        del self._name


# Tests
class EncapsulationTests(unittest.TestCase):
    def setUp(self):
        self.p = Person('John')
        self.p1 = RefPerson('John')
        self.p2 = RefPersonToProperty('John')
        self.p3 = RefPersonToPropertyDecorator('John')

    def test_get(self):
        self.assertEqual(self.p._name, 'John')
        self.assertEqual(self.p1.get_name(), 'John')
        self.assertEqual(self.p2.name, 'John')
        self.assertEqual(self.p3.name, 'John')

    def test_set(self):
        self.p._name = 'Mike'
        self.p1.set_name('Mike')
        self.p2.name = 'Mike'
        self.p3.name = 'Mike'

        self.assertEqual(self.p._name, 'Mike')
        self.assertEqual(self.p1.get_name(), 'Mike')
        self.assertEqual(self.p2.name, 'Mike')
        self.assertEqual(self.p3.name, 'Mike')

    def test_delete(self):
        del self.p._name
        self.p1.del_name()
        del self.p2.name
        del self.p3.name

        with self.assertRaises(AttributeError):
            self.p._name

        with self.assertRaises(AttributeError):
            self.p1.get_name()

        with self.assertRaises(AttributeError):
            self.p2.name

        with self.assertRaises(AttributeError):
            self.p3.name


if __name__ == '__main__':
    unittest.main()
