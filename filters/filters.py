"""Standard bonus filters."""


def title(word, capitalize=False):
    """Convert a string to a title format, where the words are capitalized

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
    """If a user follows the convention of using `is_something`, or
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
