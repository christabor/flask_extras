"""Hook to setup app easily."""

import os

from flask_extras import macros
from flask_extras.filters import config as filter_conf

import jinja2


def FlaskExtras(app):
    """Setup app config."""
    extra_folders = jinja2.ChoiceLoader([
        app.jinja_loader,
        jinja2.FileSystemLoader(os.path.dirname(macros.__file__)),
    ])
    app.jinja_loader = extra_folders
    # Setup template filters
    filter_conf.config_flask_filters(app)
