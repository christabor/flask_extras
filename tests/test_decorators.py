"""Test jinja filters."""

import unittest

from flask import Flask

from flask_extras import FlaskExtras
from flask_extras import decorators

app = Flask('test_flask_jsondash')
app.debug = True
app.secret_key = 'Foo'
FlaskExtras(app)


@app.route('/xhr-custom')
@decorators.xhr_only(status_code=400)
def foo_xhr_custom():
    return ''


@app.route('/xhr')
@decorators.xhr_only()
def foo_xhr():
    return ''


@app.route('/args')
@decorators.require_args(params=['foo', 'bar'])
def foo_args():
    return ''


@app.route('/cookies')
@decorators.require_cookies(['foo'])
def foo_cookies():
    return ''


@app.route('/headers')
@decorators.require_headers(headers=['X-Foo'])
def foo_headers():
    return ''

client = app.test_client()


class DecoratorTest(unittest.TestCase):
    """All tests for title function."""


class XhsTest(DecoratorTest):
    """All tests for title function."""

    def test_invalid_xhr_decorator(self):
        """Test the function with None argument."""
        with app.app_context():
            res = client.get('/xhr')
            self.assertEqual(res.status_code, 415)

    def test_invalid_xhr_custom_decorator(self):
        """Test the function with None argument."""
        with app.app_context():
            res = client.get('/xhr-custom')
            self.assertEqual(res.status_code, 400)


class RequireArgsTest(DecoratorTest):
    """All tests for title function."""

    def test_invalid_require_args_decorator(self):
        """Test the function with None argument."""
        with self.assertRaises(ValueError):
            with app.app_context():
                client.get('/args')

    def test_valid_require_args_decorator(self):
        """Test the function with None argument."""
        with app.app_context():
            res = client.get('/args?foo=1&bar=1')
            self.assertEqual(res.status_code, 200)


class RequireCookiesTest(DecoratorTest):
    """All tests for title function."""

    def test_invalid_require_cookies_decorator(self):
        """Test the function with None argument."""
        with self.assertRaises(ValueError):
            with app.app_context():
                client.get('/cookies')


class RequireHeadersTest(DecoratorTest):
    """All tests for title function."""

    def test_invalid_require_headers_decorator(self):
        """Test the function with None argument."""
        with self.assertRaises(ValueError):
            with app.app_context():
                client.get('/headers')

    def test_valid_require_headers_decorator(self):
        """Test the function with None argument."""
        with app.app_context():
            res = client.get('/headers', headers={'X-Foo': 'Foo'})
            self.assertEqual(res.status_code, 200)
