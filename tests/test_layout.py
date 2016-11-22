"""Tests for 'layout' filters."""

from flask_extras.filters import layout


class TestBs3Col:
    """All tests for bs3 col function."""

    def test_returns_right_width(self):
        """Test the return value for a valid type."""
        assert layout.bs3_cols(1) == 12
        assert layout.bs3_cols(2) == 6
        assert layout.bs3_cols(3) == 4
        assert layout.bs3_cols(4) == 3
        assert layout.bs3_cols(5) == 2
        assert layout.bs3_cols(6) == 2

    def test_returns_right_width_bad_data(self):
        """Test the return value for an invalid type."""
        assert layout.bs3_cols(None) == 12
        assert layout.bs3_cols('foo') == 12
        assert layout.bs3_cols(dict()) == 12
