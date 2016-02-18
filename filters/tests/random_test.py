from __future__ import absolute_import

import unittest
from .. import random


class RandomChoiceTest(unittest.TestCase):
    def test_choice_returns_str(self):
        """Test the return value for a valid type"""
        self.assertIsInstance(random.rand_choice([0, 1, 2, 3]), int)


class RandomNameTitleTest(unittest.TestCase):
    def test_name_returns_str(self):
        """Test the return value for a valid type"""
        self.assertIsInstance(random.rand_name_title('Chris'), str)

    def test_name_returns_spaced_name(self):
        """Test the return value for a valid type"""
        self.assertEqual(len(random.rand_name_title('Chris').split()), 2)
