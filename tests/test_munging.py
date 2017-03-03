"""Test munging filters."""

from flask_extras.filters import munging

import pytest


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


class TestGroupBy:
    """All tests for group_by function."""

    def _get_obj(self, name):
        """Data for tests."""
        class ObjClass(object):
            def __init__(self, name=None):
                if name is not None:
                    self.name = name
        return ObjClass(name=name)

    def test_returns_no_objs_noname(self):
        """Test function."""
        objs = [None for _ in range(4)]
        res = munging.group_by(objs, attr=None)
        assert res.keys() == ['__unlabeled']
        assert len(res['__unlabeled']) == 4

    def test_returns_no_objs_with_name(self):
        """Test function."""
        objs = [None for _ in range(4)]
        res = munging.group_by(objs, attr='invalid-attr')
        assert res.keys() == ['__unlabeled']
        assert len(res['__unlabeled']) == 4

    def test_returns_objs_nogroup_noname(self):
        """Test function."""
        objs = [self._get_obj(name) for name in ['foo1']]
        res = munging.group_by(objs, attr=None)
        assert res.keys() == ['__unlabeled']
        assert len(res['__unlabeled']) == 1

    def test_returns_objs_nogroup_fallback(self):
        """Test function."""
        objs = [self._get_obj(name) for name in ['foo1']]
        res = munging.group_by(objs, attr=None, fallback='somegroup')
        assert res.keys() == ['somegroup']
        assert len(res['somegroup']) == 1

    def test_returns_objs_nogroup(self):
        """Test function."""
        objs = [self._get_obj(None)]
        res = munging.group_by(objs, attr='name')
        assert res.keys() == ['__unlabeled']
        assert len(res['__unlabeled']) == 1

    def test_returns_objs_group_custom_group(self):
        """Test function."""
        objs = [self._get_obj(name) for name in ['foo1', 'foo2']]
        groups = [('group1', ('foo1', 'foo2'))]
        res = munging.group_by(objs, groups=groups, attr='name')
        assert res.keys() == ['group1', '__unlabeled']
        assert len(res['group1']) == 2

    def test_returns_objs_group_custom_group_with_one_unlabeled(self):
        """Test function."""
        objs = [self._get_obj(name) for name in ['foo1', 'foo2', 'foo3']]
        groups = [('group1', ('foo1', 'foo2'))]
        res = munging.group_by(objs, groups=groups, attr='name')
        assert res.keys() == ['group1', '__unlabeled']
        assert len(res['group1']) == 2
        assert len(res['__unlabeled']) == 1

    def test_returns_objs_group_custom_group_with_one_unlabeled_complex(self):
        """Test function."""
        names = ['foo{}'.format(i) for i in range(1, 11)]
        objs = [self._get_obj(name) for name in names]
        groups = [
            ('group1', ('foo1', 'foo2', 'foo3')),
            ('group2', ('foo4', 'foo5', 'foo6')),
            ('group3', ('foo7', 'foo8', 'foo9')),
        ]
        res = munging.group_by(objs, groups=groups, attr='name')
        for key in res.keys():
            assert key in ['group1', 'group2', 'group3', '__unlabeled']
        assert len(res.keys()) == 4
        assert len(res['group1']) == 3
        assert len(res['group2']) == 3
        assert len(res['group3']) == 3
        assert len(res['__unlabeled']) == 1

    def test_returns_objs_group_custom_group_with_order_preserved(self):
        """Test function."""
        names = ['foo{}'.format(i) for i in range(1, 10)]
        objs = [self._get_obj(name) for name in names]
        groups = [
            ('group1', ('foo2', 'foo1', 'foo3')),
            ('group2', ('foo5', 'foo4', 'foo6')),
            ('group3', ('foo7', 'foo9', 'foo8')),
        ]
        res = munging.group_by(objs, groups=groups, attr='name')
        for key in res.keys():
            assert key in ['group1', 'group2', 'group3', '__unlabeled']
        for group in groups:
            label, items = group
            for i, item in enumerate(items):
                obj_label = getattr(res[label][i], 'name')
                assert item == obj_label


class TestSortDictKeysFromReflist:
    """All tests for sort_dict_keys_from_reflist function."""

    def test_sort_dict_keys_from_reflist(self):
        """Test function."""
        data = dict(foo=1, bar=2, baz=3, quux=4)
        ref = ['quux', 'baz', 'foo', 'bar']
        expected = [('quux', 4), ('baz', 3), ('foo', 1), ('bar', 2)]
        assert munging.sort_dict_keys_from_reflist(data, ref) == expected

    def test_sort_dict_keys_from_reflist_nested(self):
        """Test function."""
        data = dict(foo=dict(inner1=1, inner2=2), bar=2, baz=3, quux=4)
        ref = ['quux', 'baz', 'foo', 'bar']
        expected = [
            ('quux', 4), ('baz', 3),
            ('foo', {'inner1': 1, 'inner2': 2}), ('bar', 2)]
        assert munging.sort_dict_keys_from_reflist(data, ref) == expected

    def test_sort_dict_keys_from_reflist_none(self):
        """Test function."""
        data = dict(foo=None, bar=2, baz=3, quux=4)
        ref = ['quux', 'baz', 'foo', 'bar']
        expected = [('quux', 4), ('baz', 3), ('foo', None), ('bar', 2)]
        assert munging.sort_dict_keys_from_reflist(data, ref) == expected

    def test_sort_dict_keys_from_reflist_missing_val(self):
        """Test function."""
        data = dict(foo=1, bar=2, baz=3, quux=4)
        ref = ['quux', 'baz', 'foo']
        expected = [('quux', 4), ('baz', 3), ('foo', 1)]
        assert munging.sort_dict_keys_from_reflist(data, ref) == expected


class TestSortDictValsFromReflist:
    """All tests for sort_dict_vals_from_reflist function."""

    def test_sort_dict_vals_from_reflist(self):
        """Test function."""
        data = dict(foo=1, bar=2, baz=3, quux=4)
        ref = [4, 3, 1, 2]
        expected = [('quux', 4), ('baz', 3), ('foo', 1), ('bar', 2)]
        assert munging.sort_dict_vals_from_reflist(data, ref) == expected

    def test_sort_dict_vals_from_reflist_nested(self):
        """Test function."""
        data = dict(foo=dict(inner1=1, inner2=2), bar=2, baz=3, quux=4)
        ref = [4, 3, {'inner1': 1, 'inner2': 2}, 2]
        expected = [
            ('quux', 4), ('baz', 3),
            ('foo', {'inner1': 1, 'inner2': 2}), ('bar', 2)]
        assert munging.sort_dict_vals_from_reflist(data, ref) == expected

    def test_sort_dict_vals_from_reflist_none(self):
        """Test function."""
        data = dict(foo=None, bar=2, baz=3, quux=4)
        ref = [4, 3, None, 2]
        expected = [('quux', 4), ('baz', 3), ('foo', None), ('bar', 2)]
        assert munging.sort_dict_vals_from_reflist(data, ref) == expected

    def test_sort_dict_vals_from_reflist_missing_val(self):
        """Test function."""
        data = dict(foo=1, bar=2, baz=3, quux=4)
        ref = [4, 3, 1]
        expected = [('quux', 4), ('baz', 3), ('foo', 1)]
        assert munging.sort_dict_vals_from_reflist(data, ref) == expected
