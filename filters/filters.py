"""Standard filters."""

from string import ascii_lowercase


def title(word, capitalize=False):
    """Convert a string to a title format, where the words are capitalized.

    Args:
        word (string): The string to format.

    Returns:
        word (string): The formatted word.
    """
    def _capitalize(w):
        return '{0}{1}'.format(w[0].upper(), w[1:])

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
    while seq:
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
        return '{0}?'.format(word[3:])
    elif word.startswith('has_'):
        return '{0}?'.format(word[4:])
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

    Equivalent to Djangos' get_digit.

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

    Equivalent to Djangos' length_is.

    Args:
        val (mixed): A value to check the length of.
        length (int): The length to check.

    Returns:
        bool: The value of checking the length against length.
    """
    return len(val) == length


def is_url(val):
    """Return true if a value is a url string, otherwise false.

    Args:
        val (mixed): The value to check.

    Returns:
        bool: True if the value is an http string, False if not.
    """
    if isinstance(val, (str, unicode)):
        return val.startswith('http://') or val.startswith('https://')
    return False


def ljust(string, amt):
    """Left-align the value by the amount specified.

    Equivalent to Djangos' ljust.

    Args:
        string (str): The string to adjust.
        amt (int): The amount of space to adjust by.

    Returns:
        str: The padded string.
    """
    return string.ljust(amt)


def rjust(string, amt):
    """Right-align the value by the amount specified.

    Equivalent to Djangos' rjust.

    Args:
        string (str): The string to adjust.
        amt (int): The amount of space to adjust by.

    Returns:
        str: The padded string.
    """
    return string.rjust(amt)


def make_list(val, coerce_numbers=True):
    """Make a list from a given value.

    Roughly equivalent to Djangos' make_list, with some enhancements.

    Args:
        val (mixed): The value to convert.
        coerce_numbers (bool, optional): Whether or not string number
            should be coerced back to their original values.

    Returns:
        mixed: If dict is given, return d.items(). If list is given, return it.
            If integers given, return a list of digits.
            Otherwise, return a list of characters.
    """
    if isinstance(val, dict):
        return val.items()
    if isinstance(val, list):
        return val
    vals = list(str(val))
    if coerce_numbers and isinstance(val, str):
        lst = []
        for v in vals:
            try:
                lst.append(int(v))
            except ValueError:
                lst.append(v)
        return lst
    return vals


def phone2numeric(phoneword):
    """Convert a phoneword string into the translated number equivalent.

    Roughly equivalent to Djangos' phone2numeric.

    Args:
        phoneword (str): The phoneword string.

    Returns:
        str: The converted string digits.
    """
    two, three = ['a', 'b', 'c'], ['d', 'e', 'f']
    four, five = ['g', 'h', 'i'], ['j', 'k', 'l']
    six, seven = ['m', 'n', 'o'], ['p', 'q', 'r', 's']
    eight, nine = ['t', 'u', 'v'], ['w', 'x', 'y', 'z']
    newdigits = ''
    for digit in list(phoneword.lower()):
        if digit in two:
            newdigits += '2'
        elif digit in three:
            newdigits += '3'
        elif digit in four:
            newdigits += '4'
        elif digit in five:
            newdigits += '5'
        elif digit in six:
            newdigits += '6'
        elif digit in seven:
            newdigits += '7'
        elif digit in eight:
            newdigits += '8'
        elif digit in nine:
            newdigits += '9'
        else:
            newdigits += digit
    return newdigits


def pagetitle(string, remove_first=False, divider=' > '):
    """Convert a string of characters to page-title format.

    Args:
        string (str): The string to conert.
        remove_first (bool, optional): Remove the first instance of the
            delimiter of the newly formed title.

    Returns:
        str: The converted string.
    """
    _title = divider.join(string.split('/'))
    if remove_first:
        _title = _title.replace(divider, '', 1)
    return _title


def slugify(string):
    """Convert a string of characters to URL slug format.

    All characters replacing all characters with hyphens if invalid.
    Roughly equivalent to Djangos' slugify.

    Args:
        string (str): The string to slugify.

    Returns:
        str: The slugified string.
    """
    slug = ''
    accepted = ['-', '_'] + list(ascii_lowercase) + list('01234567890')
    end = len(string) - 1
    for k, char in enumerate(string.lower().strip()):
        if char not in accepted:
            # Forget about the last char if it would get replaced.
            if k < end:
                slug += '-'
        else:
            slug += char
    return slug


def greet(name, greeting='Hello'):
    """Add a greeting to a given name.

    Args:
        name (str): The name to greet.
        greeting (str, optional): An optional greeting override.

    Returns:
        str: The updated greeting string.
    """
    return '{0}, {1}!'.format(greeting, name)


def islist(item):
    """Check if an is item is a list - not just a sequence.

    Args:
        item (mixed): The item to check as a list.

    Returns:
        result (bool): True if the item is a list, False if not.

    """
    return isinstance(item, list)


def sql2dict(queryset):
    """Return a SQL alchemy style query result into a list of dicts.

    Args:
        queryset (object): The SQL alchemy result.

    Returns:
        result (list): The converted query set.

    """
    if queryset is None:
        return []
    return [record.__dict__ for record in queryset]
