"""Filters for generating random data."""

from __future__ import absolute_import


def bs3_cols(num_entries):
    """Return the appropriate bootstrap framework column width.

    Args:
        num_entries (int): The number of entries to determine column width for.

    Returns:
        int: The integer value for column width.
    """
    if not isinstance(num_entries, int):
        return 12
    mappings = {
        1: 12,
        2: 6,
        3: 4,
        4: 3,
        5: 2,
        6: 2,
    }
    try:
        return mappings[num_entries]
    except KeyError:
        return 12
