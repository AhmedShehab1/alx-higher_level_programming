import unittest
from models.base import Base
"""
Module To Test For base.py Class
"""

class TestsForBaseClass(unittest.TestCase):
    """
    Class Inheriting From TestCase
    Args:
        unittest (): _description_
    """
    def test_base_class(self):
        """
        Should Provide Correct Id For Each Instance
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(15)
        self.assertEqual(b2.id, 15)
        b3 = Base()
        self.assertEqual(b3.id, 2)
