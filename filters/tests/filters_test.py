from __future__ import absolute_import

import unittest
from .. import filters


class TitleTest(unittest.TestCase):
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

    def test_returns_updated_list(self):
        """Test return value."""
        self.assertEqual(filters.add([1, 2], 3), [1, 2, 3])


class CutTest(unittest.TestCase):

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

    def test_returns_default(self):
        """Test return value."""
        self.assertEqual(filters.default(False, 'default'), 'default')

    def test_returns_original(self):
        """Test return value."""
        self.assertEqual(filters.default(1, 'default'), 1)


class DefaultIfNoneValTest(unittest.TestCase):

    def test_returns_default(self):
        """Test return value."""
        self.assertEqual(filters.default_if_none(
            None, 'default'), 'default')

    def test_returns_original(self):
        """Test return value."""
        self.assertEqual(filters.default_if_none(1, 'default'), 1)


class GetDigitTest(unittest.TestCase):

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

    def test_returns_false(self):
        """Test return value."""
        self.assertFalse(filters.length_is('three', 4))

    def test_returns_true(self):
        """Test return value."""
        self.assertTrue(filters.length_is('one', 3))


class IsUrlTest(unittest.TestCase):

    def test_returns_urls_true(self):
        """Test return value."""
        self.assertTrue(filters.is_url('http://foo.bar'))
        self.assertTrue(filters.is_url('https://foo.bar'))

    def test_returns_urls_false(self):
        """Test return value."""
        self.assertFalse(filters.is_url('//foo.bar'))
