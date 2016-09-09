"""App view decorators."""

from functools import wraps

from flask import request


def require_headers(headers=[]):
    """Check for required headers in a view.

    @require_headers(headers=['X-Foo'])
    def view():
        pass
    """
    def outer(func, *args, **kwargs):
        @wraps(func)
        def inner(*args, **kwargs):
            if headers:
                s1, s2 = set(headers), set([h[0] for h in request.headers])
                matches = s1.intersection(s2)
                diff = s1.difference(s2)
                if len(s1) != len(matches):
                    raise ValueError(
                        'Missing required header(s): {}'.format(list(diff)))
            return func(*args, **kwargs)
        return inner
    return outer


def require_cookies(cookies=[]):
    """Check for required cookies in a view.

    @require_cookies(cookies=['csrftoken', 'session'])
    def view():
        pass
    """
    def outer(func, *args, **kwargs):
        @wraps(func)
        def inner(*args, **kwargs):
            if cookies:
                s1 = set(cookies)
                s2 = set([k for k, v in request.cookies.items()])
                matches = s1.intersection(s2)
                diff = s1.difference(s2)
                if len(s1) != len(matches):
                    raise ValueError(
                        'Missing required cookie(s): {}'.format(list(diff)))
            return func(*args, **kwargs)
        return inner
    return outer


def require_args(params=[]):
    """Check for required args (and values) in a view.

    @require_args(params=['paginate'])
    def view():
        pass

    or, if you want to check both key and value:

    @require_args(params={'paginate': True})
    def view():
        pass
    """
    def outer(func, *args, **kwargs):
        @wraps(func)
        def inner(*args, **kwargs):
            if params:
                if isinstance(params, list):
                    s1 = set(params)
                    s2 = set([k for k, v in request.args.items()])
                    matches = s1.intersection(s2)
                    diff = s1.difference(s2)
                    if len(s1) != len(matches):
                        raise ValueError(
                            'Missing required arg(s): {}'.format(list(diff)))
                else:
                    for param, val in params.items():
                        arg = request.args.get(param, None)
                        if arg is None:
                            raise ValueError(
                                'Missing param `{}`'.format(param))
                        if arg != val:
                            raise ValueError(
                                'Invalid value `{}` '
                                'for param {}.'.format(arg, param))
            return func(*args, **kwargs)
        return inner
    return outer


def require_form(values=[]):
    """Check for required form values.

    @require_form(values=['name', 'address'])
    def view():
        pass
    """
    def outer(func, *args, **kwargs):
        @wraps(func)
        def inner(*args, **kwargs):
            if request.method == 'POST':
                if values:
                    s1 = set(values)
                    s2 = set([k for k, v in request.form.items()])
                    matches = s1.intersection(s2)
                    diff = s1.difference(s2)
                    if len(s1) != len(matches):
                        raise ValueError(
                            'Missing required form '
                            'field(s): {}'.format(list(diff)))
            return func(*args, **kwargs)
        return inner
    return outer
