"""Test configuration utilities."""

from __future__ import absolute_import

import unittest

from flask import Flask

from .. import config

app = Flask('__config_test')


class GetFuncsTest(unittest.TestCase):
    """All tests for get funcs function."""

    def test_get_module_funcs(self):
        """Test the return value."""
        self.assertIsInstance(config._get_funcs(config), dict)

    def test_get_module_funcs_notempty(self):
        """Test the return value functions length."""
        self.assertGreater(len(config._get_funcs(config).items()), 0)


class InjectFiltersTest(unittest.TestCase):
    """All tests for inject filters function."""

    def test_inject_filters_inst(self):
        """Test the return value."""
        self.assertIsInstance(config._inject_filters(app, {}), Flask)

    def test_inject_filters_count(self):
        """Test the return value."""
        old = len(app.jinja_env.filters)
        config._inject_filters(app, {'foo': lambda x: x})
        new = len(app.jinja_env.filters)
        self.assertGreater(new, old)
        assert 'foo' in app.jinja_env.filters


class ConfigFlaskFiltersTest(unittest.TestCase):
    """All tests for config flask filters function."""

    def test_config_filters_inst(self):
        """Test the return value."""
        self.assertIsInstance(config.config_flask_filters(app), Flask)

    def test_config_filters_count(self):
        """Test the return value."""
        old = len(app.jinja_env.filters)
        config.config_flask_filters(app)
        new = len(app.jinja_env.filters)
        self.assertGreater(new, old)
