"""Filters for working with data structures, munging, etc..."""


def filter_vals(obj, vals):
    """Filter a dictionary by values.

    Args:
        string (dict): The dictionary to filter.

    Returns:
        string (dict): The filtered dict.
    """
    if obj is None or not isinstance(vals, list):
        return obj
    newdict = {}
    for k, v in obj.items():
        if v in vals:
            continue
        newdict[k] = v
    return newdict


def filter_keys(obj, keys):
    """Filter a dictionary by keys.

    Args:
        string (dict): The dictionary to filter.

    Returns:
        string (dict): The filtered dict.
    """
    if obj is None or not isinstance(keys, list):
        return obj
    newdict = {}
    for k, v in obj.items():
        if k in keys:
            continue
        newdict[k] = v
    return newdict
