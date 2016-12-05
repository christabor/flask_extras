"""Test munging filters."""

from flask_extras.filters import munging


class TestFilterVals:
    """All tests for filter_vals function."""

    def test_title_returns_invalid_first(self):
        """Test function."""
        assert munging.filter_vals({}, None) == {}

    def test_title_returns_invalid_second(self):
        """Test function."""
        assert munging.filter_vals(None, []) is None

    def test_title_returns_invalid_both(self):
        """Test function."""
        assert munging.filter_vals(None, None) is None

    def test_title_returns_valid_empty(self):
        """Test function."""
        assert munging.filter_vals(dict(), []) == {}

    def test_title_returns_valid_filtered_empty(self):
        """Test function."""
        assert munging.filter_vals(dict(foo='bar'), ['bar']) == {}

    def test_title_returns_valid_filtered(self):
        """Test function."""
        assert munging.filter_vals(
            dict(foo='bar', bar='foo'), ['bar']) == dict(bar='foo')

    def test_title_returns_valid_filtered_invalid_val(self):
        """Test function."""
        d = dict(foo='bar', bar='foo')
        assert munging.filter_vals(d, ['baz']) == d


class TestFilterKeys:
    """All tests for filter_keys function."""

    def test_title_returns_invalid_first(self):
        """Test function."""
        assert munging.filter_keys({}, None) == {}

    def test_title_returns_invalid_second(self):
        """Test function."""
        assert munging.filter_keys(None, []) is None

    def test_title_returns_invalid_both(self):
        """Test function."""
        assert munging.filter_keys(None, None) is None

    def test_title_returns_valid_empty(self):
        """Test function."""
        assert munging.filter_keys(dict(), []) == {}

    def test_title_returns_valid_filtered_empty(self):
        """Test function."""
        assert munging.filter_keys(dict(foo='bar'), ['foo']) == {}

    def test_title_returns_valid_filtered(self):
        """Test function."""
        assert munging.filter_keys(
            dict(foo='bar', bar='foo'), ['bar']) == dict(foo='bar')

    def test_title_returns_valid_filtered_invalid_val(self):
        """Test function."""
        d = dict(foo='bar', bar='foo')
        assert munging.filter_keys(d, ['baz']) == d


class TestFilterList:
    """All tests for filter_list function."""

    def test_title_returns_invalid_first(self):
        """Test function."""
        assert munging.filter_list([], None) == []

    def test_title_returns_invalid_second(self):
        """Test function."""
        assert munging.filter_list(None, []) is None

    def test_title_returns_invalid_both(self):
        """Test function."""
        assert munging.filter_list(None, None) is None

    def test_title_returns_invalid_dict(self):
        """Test function."""
        assert munging.filter_list(dict(), []) == dict()

    def test_title_returns_valid_filtered_empty(self):
        """Test function."""
        assert munging.filter_list([], ['foo']) == []

    def test_title_returns_valid_filtered(self):
        """Test function."""
        assert munging.filter_list(['foo', 'bar'], ['bar']) == ['foo']

    def test_title_returns_valid_filtered_invalid_val(self):
        """Test function."""
        assert munging.filter_list(['foo', 'bar'], ['baz']) == ['foo', 'bar']
