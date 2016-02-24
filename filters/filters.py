"""Standard bonus filters."""


def title(word, capitalize=False):
    """Convert a string to a title format, where the words are capitalized.

    Args:
        word (string): The string to format.

    Returns:
        word (string): The formatted word.
    """
    def _capitalize(w):
        return '{}{}'.format(w[0].upper(), w[1:])

    if word is None:
        return ''
    words = word.split(' ')
    for i, word in enumerate(words):
        if i == 0 or capitalize:
            words[i] = _capitalize(word)
    return ' '.join(words)


def firstof(seq):
    """Return the first item that is truthy in a sequence.

    Equivalent to Djangos' firstof.

    Args:
        seq (list): A list of values.

    Returns:
        value (mixed): The output, depending on the truthiness of the input.
    """
    if not any(seq):
        return ''
    if all(seq):
        return seq[0]
    while len(seq) > 0:
        item = seq.pop(0)
        if item:
            return item
    return ''


def questionize_label(word):
    """Convert a word to a true/false style question format.

    If a user follows the convention of using `is_something`, or
    `has_something`, for a boolean value, the *property* text will
    automatically be converted into a more human-readable
    format, e.g. 'Something?' for is_ and Has Something? for has_.

    Args:
        word (string): The string to format.

    Returns:
        word (string): The formatted word.
    """
    if word is None:
        return ''
    if word.startswith('is_'):
        return '{}?'.format(word[3:])
    elif word.startswith('has_'):
        return '{}?'.format(word[4:])
    return word


def add(lst, arg):
    """Add an item to a list.

    Equivalent to Djangos' add.

    Args:
        lst (list): A list.
        arg (mixed): Any value to append to the list.

    Returns:
        list: The updated list.
    """
    lst.append(arg)
    return lst


def cut(val, removals):
    """Remove some value from a string.

    Similar to Djangos' cut, but accepts N arguments to remove, in turn.

    Args:
        val (str): A string.
        removals (list): Alist of values to remove in turn, from the value.

    Returns:
        str: The updated string.
    """
    def _cut(val, tocut):
        return val.replace(tocut, '')
    for r in removals:
        val = _cut(val, r)
    return val


def addslashes(val):
    """Add slashes before all single quotes in a given string.

    Equivalent to Djangos' addslashes.

    Args:
        val (str): A string.

    Returns:
        str: The updated string.
    """
    return val.replace("'", "\\'")


def default(val, default):
    """Default to a given value if another given value is falsy.

    Equivalent to Djangos' default.

    Args:
        val (mixed): A mixed value that is truthy or falsy.
        default (mixed): A default replacement value.

    Returns:
        mixed: The default given value, or the original value.
    """
    return default if not val else val


def default_if_none(val, default):
    """Default to a given value if another given value is None.

    Equivalent to Djangos' default_if_none.

    Args:
        val (mixed): A mixed value that may or may not be None.
        default (mixed): A default replacement value.

    Returns:
        mixed: The default given value, or the original value.
    """
    return default if val is None else val


def get_digit(val, index):
    """Return the digit of a value specified by an index.

    Args
        val (int): An integer.
        index (int): The index to check against.

    Returns:
        int: The original integer if index is invalid, otherwise the digit
        at the specified index.
    """
    digits = reversed(list(str(val)))
    for k, digit in enumerate(digits):
        if k + 1 == int(index):
            return int(digit)
    return val


def length_is(val, length):
    """Return True if the length of a given value matches a given length.

    Args:
        val (mixed): A value to check the length of.
        length (int): The length to check.

    Returns:
        bool: The value of checking the length against length.
    """
    return len(val) == length
