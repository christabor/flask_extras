"""Date and date-time related filters."""

from dateutil.parser import parse as dtparse


def str2dt(timestr):
    """Convert a string date to a real date.

    Args:
        timestr (str) - the datetime as a raw string.
    Returns:
        dateutil.parser.parse - the parsed datetime object.
    """
    try:
        return dtparse(timestr)
    except (TypeError, ValueError):
        if timestr in ['None', 'null']:
            return None
        return timestr
