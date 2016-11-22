"""Tests for 'random' filters."""

import re

from flask_extras.filters import random


class TestRandomChoice:
    """All tests for random choice function."""

    def test_choice_returns_str(self):
        """Test the return value for a valid type."""
        assert isinstance(random.rand_choice([0, 1, 2, 3]), int)


class TestRandomNameTitle:
    """All tests for random title function."""

    def test_name_returns_str(self):
        """Test the return value for a valid type."""
        assert isinstance(random.rand_name_title('Chris'), str)

    def test_name_returns_spaced_name(self):
        """Test the return value for a valid value length."""
        assert len(random.rand_name_title('Chris').split()) == 2


class TestRandomColor:
    """All tests for random color function."""

    def test_returns_str(self):
        """Test the return value for a valid type."""
        assert isinstance(random.rand_color(), str)

    def test_returns_rgba_format(self):
        """Test the return value for a valid string format."""
        re_rgba = r'rgba\([0-9{0,3}]+, [0-9{0,3}]+, [0-9{0,3}]+, [0-9{0,3}]+\)'
        assert re.match(re_rgba, random.rand_color(alpha=10)) is not None
