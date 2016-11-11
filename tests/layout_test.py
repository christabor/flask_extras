"""Tests for 'layout' filters."""

import unittest

from flask_extras.filters import layout


class Bs3ColTest(unittest.TestCase):
    """All tests for bs3 col function."""

    def test_returns_right_width(self):
        """Test the return value for a valid type."""
        self.assertEqual(layout.bs3_cols(1), 12)
        self.assertEqual(layout.bs3_cols(2), 6)
        self.assertEqual(layout.bs3_cols(3), 4)
        self.assertEqual(layout.bs3_cols(4), 3)
        self.assertEqual(layout.bs3_cols(5), 2)
        self.assertEqual(layout.bs3_cols(6), 2)

    def test_returns_right_width_bad_data(self):
        """Test the return value for an invalid type."""
        self.assertEqual(layout.bs3_cols(None), 12)
        self.assertEqual(layout.bs3_cols('foo'), 12)
        self.assertEqual(layout.bs3_cols(dict()), 12)
