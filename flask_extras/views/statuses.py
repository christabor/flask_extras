"""Static pages for various HTTP codes.

Format must be `page_XXX` where XXX is the code in question. This allows
proper dynamic injection into the Flask app error handling mechanism.
"""

from inspect import isfunction

from flask import render_template


def page_400(error):
    """400 page."""
    return render_template(
        'status_codes/400.html',
        code=400, desc='bad request', error=error)


def page_401(error):
    """401 page."""
    return render_template(
        'status_codes/401.html',
        code=401, desc='unauthorized access', error=error)


def page_403(error):
    """403 page."""
    return render_template(
        'status_codes/403.html',
        code=403, desc='forbidden', error=error)


def page_404(error):
    """404 page."""
    return render_template(
        'status_codes/404.html',
        code=404, desc='not found', error=error)


def page_500(error):
    """500 page."""
    return render_template(
        'status_codes/500.html',
        code=500, desc='internal server error', error=error)


def page_503(error):
    """503 page."""
    return render_template(
        'status_codes/500.html',
        code=503, desc='service unavailable', error=error)


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
        app.register_error_handler(int(code), func)
    return app
