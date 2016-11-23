from flask import Flask
import pytest

from flask_extras import FlaskExtras

app = Flask('__config_test')
app.secret_key = '123'
app.debug = True
FlaskExtras(app)


@pytest.fixture()
def client():
    return app, app.test_client()
