
"""Static pages for various HTTP codes."""

from flask import render_template
from inspect import isfunction


def page_404(error):
    """404 page."""
    return render_template(
        'status_codes/404.html',
        code=404, desc='not found', error=error)


def page_500(error):
    """500 page."""
    return render_template(
        'status_codes/500.html',
        code=500, desc='server error', error=error)


def _isview(name, func):
    """Check if arguments represent a valid Flask view.

    Args:
        name (str): String name of function.
        func (function): A function.

    Returns:
        bool: Whether the given args are valid.
    """
    return isfunction(func) and name.startswith('page_')


def _get_viewfuncs():
    """Return all functions in this module that are relevant views.

    Returns:
        dict: The view functions, keyed by name.
    """
    return {name: func for name, func
            in globals().iteritems() if _isview(name, func)}


def inject_error_views(app):
    """Inject all relevant error (status code) views into an app.

    Args:
        app (object): The Flask instance.
        funcs (dict): A dict of functions by name.

    Returns:
        object: The modified Flask instance.
    """
    # See flask.pocoo.org/docs/0.10/api/#flask.Flask.errorhandler
    for name, func in _get_viewfuncs().iteritems():
        code = name.replace('page_', '')
        app.error_handler_spec[None][int(code)] = func
    return app
