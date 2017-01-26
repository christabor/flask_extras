"""Filters for working with data structures, munging, etc..."""

from collections import OrderedDict


def filter_list(lst, vals):
    """Filter a list by vals.

    Args:
        lst (dict): The dictionary to filter.

    Returns:
        string (dict): The filtered dict.
    """
    if any([not lst, not isinstance(lst, list), not isinstance(vals, list)]):
        return lst
    return list(set(lst).difference(set(vals)))


def filter_vals(obj, vals):
    """Filter a dictionary by values.

    Args:
        obj (dict): The dictionary to filter.

    Returns:
        obj (dict): The filtered dict.
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
        obj (dict): The dictionary to filter.

    Returns:
        obj (dict): The filtered dict.
    """
    if obj is None or not isinstance(keys, list):
        return obj
    newdict = {}
    for k, v in obj.items():
        if k in keys:
            continue
        newdict[k] = v
    return newdict


def group_by(objs, groups=[], attr='name'):
    """Group a list of objects into an ordered dict grouped by specified keys.

    Args:
        objs: A list of objects
        keys: A list of 2-tuples where the first index is the group name,
            and the second key is a tuple of all matches.
        attr: The attr to use to get fields for matching (default: 'name')

    Returns:
        An OrderedDict of grouped items.

    >>> group_by([obj1, obj2],
                 groups=[('g1', ('name1', 'name2'))], attr='name')
    """
    grouped = OrderedDict()
    if not groups or attr is None:
        return {'__unlabeled': objs}
    # Initial population since it's not a defaultdict.
    for ordered_group in groups:
        label, _ = ordered_group
        grouped[label] = []
    seen = []
    for ordered_group in groups:
        label, matches = ordered_group
        for curr in objs:
            attr_label = getattr(curr, attr) if hasattr(curr, attr) else ''
            if attr_label in seen:
                continue
            if attr_label in matches:
                idx = matches.index(attr_label)
                grouped[label].insert(idx, curr)
                seen.append(attr_label)
    # Add unlabeled extras last so order is preserved.
    grouped['__unlabeled'] = [
        curr for curr in objs if getattr(curr, attr) not in seen
    ]
    return grouped
