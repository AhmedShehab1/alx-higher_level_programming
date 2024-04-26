import unittest
from models.rectangle import Rectangle
"""
Module To Test For Rectangle Class
"""

class RectanlgeTests(unittest.TestCase):

    def setUp(self) -> None:
        self.r1 = Rectangle(10, 20, 3, 2, 12)
        self.r2 = Rectangle(1, 2, 0, 1)

    def test_attribute_initialization(self):
        self.assertEqual(self.r1.id, 12)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 20)
        self.assertEqual(self.r1.x, 3)
        self.assertEqual(self.r1.y, 2)

    def test_attribute_validation(self):
        """Should raise TypeError If height/width is not
        of Type int OR ValueError If width/height <= 0"""
        self.assertRaises(TypeError, self.r1.height, "1")
        self.assertRaises(ValueError, self.r1.width, 0)
        self.assertRaises(ValueError, self.r2.width, -4)

        """Should raise ValueError If x or y is < 0
        OR TypeError if x, y is not of type int"""
        self.assertRaises(ValueError, self.r1.y, -1)
        self.assertRaises(TypeError, self.r2.x, "0")
