#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Multiple Tests For max_integer function using unittest Module
    Args:
        unittest (_type_): Inheriting Various Methods From TestCase Class
    """
    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_negative(self):
        self.assertEqual(max_integer([-3, -4, -7, -1]), -1)
        self.assertEqual(max_integer([-3, 29, 100, 30, 15]), 100)

    def test_one_element(self):
        self.assertEqual(max_integer([100]), 100)

    def test_at_the_beginning(self):
        self.assertEqual(max_integer([100, 84, 29, 0]), 100)

    def test_at_the_middle(self):
        self.assertEqual(max_integer([84, 100, 0]), 100)

    def test_at_the_end(self):
        self.assertEqual(max_integer([0, 39, 93, 130]), 130)
