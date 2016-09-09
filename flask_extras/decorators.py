"""App view decorators."""

from functools import wraps

from flask import request


def require_headers(headers=[]):
    """Check for required headers in a view.

    @require_headers(['X-Foo'])
    @def view():
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

    @require_cookies(['csrftoken', 'session'])
    @def view():
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
                        'Missing required cookie(s): {}'.format(diff))
            return func(*args, **kwargs)
        return inner
    return outer


def require_args(args={}, use_values=True):
    """Check for required args (and values) in a view.

    @require_args({'paginate': True})
    @def view():
        pass
    """
    def outer(func, *args, **kwargs):
        @wraps(func)
        def inner(*args, **kwargs):
            if args:
                s1 = set(args.values())
                s2 = set([k for k, v in request.args.items()])
                matches = s1.intersection(s2)
                diff = s1.difference(s2)
                if len(s1) != len(matches):
                    raise ValueError(
                        'Missing required arg(s): {}'.format(diff))
            return func(*args, **kwargs)
        return inner
    return outer
