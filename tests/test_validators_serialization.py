"""Test WTForm validators."""

from collections import namedtuple

import pytest

from flask_extras.forms.validators import serialization


class FakeCls(object):
    pass


Field = namedtuple('Field', 'data')


def test_valid_json_valid():
    # Just ensuring it doesn't raise a ValueError
    serialization.valid_json(FakeCls(), Field(data='{"foo": "bar"}'))


def test_valid_json_invalid():
    with pytest.raises(ValueError):
        serialization.valid_json(FakeCls(), Field(data='asdASDp'))


def test_valid_json_invalid_dict_ish():
    with pytest.raises(ValueError):
        serialization.valid_json(FakeCls(), Field(data='{foo: bar}'))


def test_valid_json_invalid_none():
    with pytest.raises(TypeError):
        serialization.valid_json(FakeCls(), Field(data=None))
