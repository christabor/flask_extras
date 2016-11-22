"""Test configuration utilities."""

from flask import Flask

from flask_extras.filters import config


class TestGetFuncs:
    """All tests for get funcs function."""

    def test_get_module_funcs(self, client):
        """Test the return value."""
        assert isinstance(config._get_funcs(config), dict)

    def test_get_module_funcs_notempty(self, client):
        """Test the return value functions length."""
        assert len(config._get_funcs(config).items()) > 0


class TestInjectFilters:
    """All tests for inject filters function."""

    def test_inject_filters_inst(self, client):
        """Test the return value."""
        app, test = client
        assert isinstance(config._inject_filters(app, {}), Flask)

    def test_inject_filters_count(self, client):
        """Test the return value."""
        app, test = client
        old = len(app.jinja_env.filters)
        config._inject_filters(app, {'foo': lambda x: x})
        new = len(app.jinja_env.filters)
        assert new > old
        assert 'foo' in app.jinja_env.filters


class TestConfigFlaskFilters:
    """All tests for config flask filters function."""

    def test_config_filters_inst(self, client):
        """Test the return value."""
        app, test = client
        assert isinstance(config.config_flask_filters(app), Flask)

    def test_config_filters_count(self, client):
        """Test the return value."""
        app, test = client
        del app.jinja_env.filters
        setattr(app.jinja_env, 'filters', dict())
        old = len(app.jinja_env.filters)
        config.config_flask_filters(app)
        new = len(app.jinja_env.filters)
        assert new > old
