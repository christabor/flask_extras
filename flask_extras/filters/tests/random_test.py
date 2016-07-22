"""Tests for 'random' filters."""

from __future__ import absolute_import

import re
import unittest

from .. import random


class RandomChoiceTest(unittest.TestCase):
    """All tests for random choice function."""

    def test_choice_returns_str(self):
        """Test the return value for a valid type."""
        self.assertIsInstance(random.rand_choice([0, 1, 2, 3]), int)


class RandomNameTitleTest(unittest.TestCase):
    """All tests for random title function."""

    def test_name_returns_str(self):
        """Test the return value for a valid type."""
        self.assertIsInstance(random.rand_name_title('Chris'), str)

    def test_name_returns_spaced_name(self):
        """Test the return value for a valid value length."""
        self.assertEqual(len(random.rand_name_title('Chris').split()), 2)


class RandomColorTest(unittest.TestCase):
    """All tests for random color function."""

    def test_returns_str(self):
        """Test the return value for a valid type."""
        self.assertIsInstance(random.rand_color(), str)

    def test_returns_rgba_format(self):
        """Test the return value for a valid string format."""
        re_rgba = r'rgba\([0-9{0,3}]+, [0-9{0,3}]+, [0-9{0,3}]+, [0-9{0,3}]+\)'
        self.assertIsNotNone(re.match(re_rgba, random.rand_color(alpha=10)))
