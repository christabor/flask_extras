"""App view decorators."""

from functools import wraps

from flask import request


def require_headers(headers=[]):
    """Check for required headers in a view."""
    def outer(func, *args, **kwargs):
        @wraps(func)
        def inner(*args, **kwargs):
            if headers:
                s1, s2 = set(headers), set([h[0] for h in request.headers])
                matches = s1.intersection(s2)
                if not matches:
                    raise ValueError(
                        'Missing required header(s): {}'.format(headers))
            return func(*args, **kwargs)
        return inner
    return outer
