import unittest

from nose.tools import assert_equal
from parameterized import parameterized, parameterized_class

from src.sample.zad1 import *


class HammingParametrizedPackage1(unittest.TestCase):

    def setUp(self):
        self.hamming = Hamming()

    @parameterized.expand([
        ('A', 'A', 0),
        ('AB', 'AC', 1),
        ('', '', 0),
        ('ABCD', 'GHFJ', 4),
    ])
    def test_hamming_parametrized_method(self, str1, str2, expected):
        self.assertEqual(self.hamming.distance(str1, str2), expected)


@parameterized_class(('str1', 'str2', 'expected'), [
    ('A', 'A', 0),
    ('AB', 'AC', 1),
    ('', '', 0),
    ('ABCD', 'GHFJ', 4),
])
class HammingParametrizedPackage2(unittest.TestCase):

    def setUp(self):
        self.hamming = Hamming()

    def test_hamming_parametrized_class(self):
        self.assertEqual(self.hamming.distance(self.str1, self.str2), self.expected)


@parameterized([
    ('A', 'A', 0),
    ('AB', 'AC', 1),
    ('', '', 0),
    ('ABCD', 'GHFJ', 4),
])
def test_hamming_parametrized_dodatkowo(str1, str2, expected):
    hamming = Hamming()
    assert_equal(hamming.distance(str1, str2), expected)


if __name__ == '__main__':
    unittest.main()


