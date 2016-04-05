"""Filters for generating random data."""

from __future__ import absolute_import

from random import choice, randrange


def rand_choice(options):
    """Pick a random value from a range of numbers, like pythons' stdlib.

    Equivalent to Djangos' random.

    Args:
        options (list): A list of values.

    Returns:
        randchoice (mixed): The random choice, selected from the given list.
    """
    return choice(options)


def rand_name_title(name):
    """Pick a random title for a given name (e.g. ESQ. MD, etc...).

    Source: https://www.lehigh.edu/lewis/suffix.htm

    Args:
        options (str): A name, or other string.

    Returns:
        name (str): The name, with a random suffixed appended.
    """
    titles = [
        'B.V.M.', 'CFRE', 'CLU', 'CPA', 'C.S.C.', 'C.S.J.', 'D.C.', 'D.D.',
        'D.D.S.', 'D.M.D.', 'D.O.', 'D.V.M.', 'Ed.D.', 'Esq.', 'II', 'III',
        'IV', 'Inc.', 'J.D.', 'Jr.', 'LL.D.', 'Ltd.', 'M.D.', 'O.D.',
        'O.S.B.', 'P.C.', 'P.E.', 'Ph.D.', 'Ret.', 'R.G.S', 'R.N.', 'R.N.C.',
        'S.H.C.J.', 'S.J.', 'S.N.J.M.', 'Sr.', 'S.S.M.O.', 'USA', 'USAF',
        'USAFR', 'USAR', 'USCG', 'USMC', 'USMCR', 'USN', 'USNR',
    ]
    return '{0} {1}'.format(name, choice(titles))


def rand_color(alpha=100):
    """Return a random CSS friendly RGB color value.

    Args:
        alpha (int): The optional alpha value for the RGBA string.

    Returns:
        str: The RGB triplet for use with inline css.
            (e.g. rgba(10, 20, 30, 100))
    """
    return 'rgba({0}, {1}, {2}, {3})'.format(
        randrange(0, 255), randrange(0, 255), randrange(0, 255), alpha)
