"""Test munging filters."""

from dateutil.parser import parse as dtparse

from flask_extras.filters import datetimes

import pytest


class TestStr2Dt:
    """All tests for str2dt function."""

    def test_title_returns_valid(self):
        """Test function."""
        timestr = '01-05-1900 00:00:00'
        res = datetimes.str2dt(timestr)
        assert res == dtparse(timestr) == res

    def test_title_returns_invalid(self):
        """Test function."""
        with pytest.raises(TypeError):
            datetimes.str2dt(None)
