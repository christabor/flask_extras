from flask import Flask
import pytest


app = Flask('__config_test')


@pytest.fixture()
def client():
    return app, app.test_client()
