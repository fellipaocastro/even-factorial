#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import
import unittest
import math
import random

from even_factorial import factorial, is_even


class EvenFactorialTestCase(unittest.TestCase):
    def test_factorial_of_0_should_return_1(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_3_should_return_6(self):
        self.assertEqual(factorial(3), 6)

    def test_factorial_should_return_the_same_value_as_math_factorial(self):
        n = random.randint(0, 100)

        self.assertEqual(factorial(n), math.factorial(n))

    def test_is_even_should_return_true_with_8(self):
        self.assertTrue(is_even(8))

    def test_is_even_should_return_false_with_9(self):
        self.assertFalse(is_even(9))


if __name__ == '__main__':
    unittest.main()
