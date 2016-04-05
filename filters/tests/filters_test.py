"""Test jinja filters."""


from __future__ import absolute_import

import unittest

from .. import filters


class MockClass:
    """Empty class for testing."""


class TitleTest(unittest.TestCase):
    """All tests for title function."""

    def test_title_returns_str(self):
        """Test the return value for a valid type."""
        self.assertIsInstance(filters.title('foo bar'), str)

    def test_title_word(self):
        """Test the `word` argument."""
        self.assertEqual(filters.title('foo bar'), 'Foo bar')

    def test_title_capitalize(self):
        """Test the `capitalize` argument."""
        self.assertEqual(
            filters.title('foo bar', capitalize=True), 'Foo Bar')

    def test_title_capitalize_sentence(self):
        """Test the `capitalize` argument."""
        self.assertEqual(filters.title(
            'the quick brown fox... ah forget it', capitalize=True),
            'The Quick Brown Fox... Ah Forget It')

    def test_title_none(self):
        """Test the function with None argument."""
        self.assertEqual(filters.questionize_label(None), '')


class QuestionizeLabelTest(unittest.TestCase):
    """All tests for questionize label function."""

    def test_questionize_label_returns_str(self):
        """Test the return value for a valid type."""
        self.assertIsInstance(filters.questionize_label('foo bar'), str)

    def test_questionize_label_word_is(self):
        """Test the `word` argument."""
        self.assertEqual(filters.questionize_label('is_cool'), 'cool?')

    def test_questionize_label_word_has(self):
        """Test the `word` argument."""
        self.assertEqual(filters.questionize_label('has_stuff'), 'stuff?')

    def test_questionize_label_none(self):
        """Test the function with None argument."""
        self.assertEqual(filters.questionize_label(None), '')


class FirstOfTest(unittest.TestCase):
    """All tests for first of function."""

    def test_firstof_all_false(self):
        """Test what is returned when all values are falsy."""
        self.assertEqual(filters.firstof([None, False, 0]), '')

    def test_firstof_last_true(self):
        """Test what is returned when last value is true."""
        self.assertEqual(filters.firstof([None, False, 0, 'yay']), 'yay')

    def test_firstof_first_true(self):
        """Test what is returned when first value is true."""
        self.assertEqual(filters.firstof(['yay', False, 0, 'yay']), 'yay')


class AddTest(unittest.TestCase):
    """All tests for add function."""

    def test_returns_updated_list(self):
        """Test return value."""
        self.assertEqual(filters.add([1, 2], 3), [1, 2, 3])


class CutTest(unittest.TestCase):
    """All tests for cut function."""

    def test_returns_updated_string(self):
        """Test return value."""
        self.assertEqual(filters.cut('Hello world', ['world']), 'Hello ')

    def test_returns_updated_multi(self):
        """Test return value."""
        self.assertEqual(filters.cut(
            'Well hello world', ['hello', 'world']), 'Well  ')

    def test_returns_updated_multispace(self):
        """Test return value."""
        self.assertEqual(filters.cut(
            'String with spaces', [' ']), 'Stringwithspaces')


class AddSlashesTest(unittest.TestCase):
    """All tests for add slashes function."""

    def test_returns_updated_basic(self):
        """Test return value."""
        res = filters.addslashes("I'm using Flask!")
        self.assertEqual(res, "I\\'m using Flask!")

    def test_returns_updated_empty(self):
        """Test return value."""
        res = filters.addslashes("Using Flask!")
        self.assertEqual(res, "Using Flask!")

    def test_returns_updated_complex(self):
        """Test return value."""
        res = filters.addslashes("I'm u's'i'n'g Flask!")
        self.assertEqual(res, "I\\'m u\\'s\\'i\\'n\\'g Flask!")


class DefaultValTest(unittest.TestCase):
    """All tests for default val function."""

    def test_returns_default(self):
        """Test return value."""
        self.assertEqual(filters.default(False, 'default'), 'default')

    def test_returns_original(self):
        """Test return value."""
        self.assertEqual(filters.default(1, 'default'), 1)


class DefaultIfNoneValTest(unittest.TestCase):
    """All tests for default if none function."""

    def test_returns_default(self):
        """Test return value."""
        self.assertEqual(filters.default_if_none(
            None, 'default'), 'default')

    def test_returns_original(self):
        """Test return value."""
        self.assertEqual(filters.default_if_none(1, 'default'), 1)


class GetDigitTest(unittest.TestCase):
    """All tests for get digit function."""

    def test_returns_index_empty(self):
        """Test return value."""
        self.assertEqual(filters.get_digit(123456789, 0), 123456789)

    def test_returns_index_end(self):
        """Test return value."""
        self.assertEqual(filters.get_digit(123456789, 1), 9)

    def test_returns_index_mid(self):
        """Test return value."""
        self.assertEqual(filters.get_digit(123456789, 5), 5)

    def test_returns_index_beg(self):
        """Test return value."""
        self.assertEqual(filters.get_digit(123456789, 9), 1)


class LengthIsTest(unittest.TestCase):
    """All tests for length is function."""

    def test_returns_false(self):
        """Test return value."""
        self.assertFalse(filters.length_is('three', 4))

    def test_returns_true(self):
        """Test return value."""
        self.assertTrue(filters.length_is('one', 3))


class IsUrlTest(unittest.TestCase):
    """All tests for is url function."""

    def test_returns_urls_true(self):
        """Test return value."""
        self.assertTrue(filters.is_url('http://foo.bar'))
        self.assertTrue(filters.is_url('https://foo.bar'))

    def test_returns_urls_false(self):
        """Test return value."""
        self.assertFalse(filters.is_url('//foo.bar'))


class LJustTest(unittest.TestCase):
    """All tests for ljust function."""

    def test_returns_lpadding(self):
        """Test return value."""
        self.assertEqual(filters.ljust('Flask', 10), 'Flask     ')


class RJustTest(unittest.TestCase):
    """All tests for rjust function."""

    def test_returns_rpadding(self):
        """Test return value."""
        self.assertEqual(filters.rjust('Flask', 10), '     Flask')


class MakeListTest(unittest.TestCase):
    """All tests for make list function."""

    def test_list2list(self):
        """Test return value."""
        self.assertEqual(filters.make_list([1, 2]), [1, 2])

    def test_ints_not_coerced(self):
        """Test return value."""
        self.assertEqual(filters.make_list(
            '12', coerce_numbers=False), ['1', '2'])

    def test_ints_coerced(self):
        """Test return value."""
        self.assertEqual(filters.make_list('12'), [1, 2])

    def test_dict(self):
        """Test return value."""
        self.assertEqual(filters.make_list({'foo': 'bar'}), [('foo', 'bar')])

    def test_list(self):
        """Test return value."""
        self.assertEqual(filters.make_list([1, 2]), [1, 2])

    def test_str(self):
        """Test return value."""
        self.assertEqual(filters.make_list('abc'), ['a', 'b', 'c'])


class Phone2NumericTest(unittest.TestCase):
    """All tests for phone2numeric function."""

    def test_basic(self):
        """Test return value."""
        self.assertEqual(
            filters.phone2numeric('1800-COLLeCT'), '1800-2655328')

    def test_1_thru_9(self):
        """Test return value."""
        self.assertEqual(
            filters.phone2numeric('1800-ADGJMPTX'), '1800-23456789')


class SlugifyTest(unittest.TestCase):
    """All tests for slugify function."""

    def test_slugify_plain(self):
        """Test return value."""
        self.assertEqual(filters.slugify('My news title!'), 'my-news-title')

    def test_slugify_complex(self):
        """Test return value."""
        self.assertEqual(
            filters.slugify('I am an OBFUsc@@Ted URL!!! Foo bar'),
            'i-am-an-obfusc--ted-url----foo-bar')


class PagetitleTest(unittest.TestCase):
    """All tests for pagetitle function."""

    def test_title_plain(self):
        """Test return value."""
        self.assertEqual(
            filters.pagetitle('/foo/bar/bam'), ' > foo > bar > bam')

    def test_title_removefirst(self):
        """Test return value."""
        self.assertEqual(
            filters.pagetitle('/foo/bar/bam', divider=' | '),
            ' | foo | bar | bam')

    def test_title_divider(self):
        """Test return value."""
        self.assertEqual(
            filters.pagetitle('/foo/bar/bam', remove_first=True),
            'foo > bar > bam')


class GreetTest(unittest.TestCase):
    """All tests for greet function."""

    def test_greet(self):
        """Test return value."""
        self.assertEqual(filters.greet('Chris'), 'Hello, Chris!')

    def test_greet_override(self):
        """Test return value."""
        self.assertEqual(filters.greet(
            'Chris', greeting='Bonjour'), 'Bonjour, Chris!')


class IsListTest(unittest.TestCase):
    """All tests for islist function."""

    def test_islist(self):
        """Test return value."""
        self.assertTrue(filters.islist([1, 2, 3]))

    def test_notislist(self):
        """Test return value."""
        self.assertFalse(filters.islist('Foo'))
        self.assertFalse(filters.islist({'foo': 'bar'}))
        self.assertFalse(filters.islist(1))
        self.assertFalse(filters.islist(1.0))


class Sql2dictTest(unittest.TestCase):
    """All tests for sql2dict function."""

    def setUp(self):
        """Setup fake sql class."""
        self.mm = MockClass()
        self.mm.__dict__ = {'foo': 'bar'}

    def test_none(self):
        """Test return value."""
        self.assertEqual(filters.sql2dict(None), [])

    def test_set(self):
        """Test return value."""
        self.assertEqual(filters.sql2dict([self.mm]), [{'foo': 'bar'}])
