"""Test jinja filters."""

from flask_extras.filters import filters


class MockClass:
    """Empty class for testing."""


class TestCssSelector:
    """All tests for css_selector function."""

    def test_title_returns_invalid(self):
        """Test the return value for a valid type."""
        assert filters.css_selector(123) == 123

    def test_title_returns_str(self):
        """Test the return value for a valid type."""
        assert isinstance(filters.css_selector('foo bar'), str)

    def test_basic(self):
        """Test the argument."""
        assert filters.css_selector('Hello World') == 'hello_world'

    def test_no_lowercase(self):
        """Test the argument."""
        expected = 'Hello_World'
        assert filters.css_selector('Hello World', lowercase=False) == expected


class TestTitle:
    """All tests for title function."""

    def test_title_returns_str(self):
        """Test the return value for a valid type."""
        assert isinstance(filters.title('foo bar'), str)

    def test_title_word(self):
        """Test the `word` argument."""
        assert filters.title('foo bar') == 'Foo bar'

    def test_title_capitalize(self):
        """Test the `capitalize` argument."""
        assert filters.title('foo bar', capitalize=True) == 'Foo Bar'

    def test_title_capitalize_sentence(self):
        """Test the `capitalize` argument."""
        res = filters.title('the quick brown fox... ah forget it',
                            capitalize=True)
        expected = 'The Quick Brown Fox... Ah Forget It'
        assert res == expected

    def test_title_none(self):
        """Test the function with None argument."""
        assert filters.questionize_label(None) == ''


class TestQuestionizeLabel:
    """All tests for questionize label function."""

    def test_questionize_label_returns_str(self):
        """Test the return value for a valid type."""
        assert isinstance(filters.questionize_label('foo bar'), str)

    def test_questionize_label_word_is(self):
        """Test the `word` argument."""
        assert filters.questionize_label('is_cool') == 'cool?'

    def test_questionize_label_word_has(self):
        """Test the `word` argument."""
        assert filters.questionize_label('has_stuff') == 'stuff?'

    def test_questionize_label_none(self):
        """Test the function with None argument."""
        assert filters.questionize_label(None) == ''


class TestFirstOf:
    """All tests for first of function."""

    def test_firstof_all_false(self):
        """Test what is returned when all values are falsy."""
        assert filters.firstof([None, False, 0]) == ''

    def test_firstof_last_true(self):
        """Test what is returned when last value is true."""
        assert filters.firstof([None, False, 0, 'yay']) == 'yay'

    def test_firstof_first_true(self):
        """Test what is returned when first value is true."""
        assert filters.firstof(['yay', False, 0, 'yay']) == 'yay'


class TestAdd:
    """All tests for add function."""

    def test_returns_updated_list(self):
        """Test return value."""
        assert filters.add([1, 2], 3) == [1, 2, 3]


class TestCut:
    """All tests for cut function."""

    def test_returns_updated_string(self):
        """Test return value."""
        assert filters.cut('Hello world', ['world']) == 'Hello '

    def test_returns_updated_multi(self):
        """Test return value."""
        assert filters.cut(
            'Well hello world', ['hello', 'world']) == 'Well  '

    def test_returns_updated_multispace(self):
        """Test return value."""
        assert filters.cut(
            'String with spaces', [' ']) == 'Stringwithspaces'


class TestAddSlashes:
    """All tests for add slashes function."""

    def test_returns_updated_basic(self):
        """Test return value."""
        res = filters.addslashes("I'm using Flask!")
        assert res == "I\\'m using Flask!"

    def test_returns_updated_empty(self):
        """Test return value."""
        res = filters.addslashes("Using Flask!")
        assert res == "Using Flask!"

    def test_returns_updated_complex(self):
        """Test return value."""
        res = filters.addslashes("I'm u's'i'n'g Flask!")
        assert res == "I\\'m u\\'s\\'i\\'n\\'g Flask!"


class TestDefaultVal:
    """All tests for default val function."""

    def test_returns_default(self):
        """Test return value."""
        assert filters.default(False, 'default') == 'default'

    def test_returns_original(self):
        """Test return value."""
        assert filters.default(1, 'default') == 1


class TestDefaultIfNoneVal:
    """All tests for default if none function."""

    def test_returns_default(self):
        """Test return value."""
        assert filters.default_if_none(None, 'default') == 'default'

    def test_returns_original(self):
        """Test return value."""
        assert filters.default_if_none(1, 'default') == 1


class TestGetDigit:
    """All tests for get digit function."""

    def test_returns_index_empty(self):
        """Test return value."""
        assert filters.get_digit(123456789, 0) == 123456789

    def test_returns_index_end(self):
        """Test return value."""
        assert filters.get_digit(123456789, 1) == 9

    def test_returns_index_mid(self):
        """Test return value."""
        assert filters.get_digit(123456789, 5) == 5

    def test_returns_index_beg(self):
        """Test return value."""
        assert filters.get_digit(123456789, 9) == 1


class TestLengthIs:
    """All tests for length is function."""

    def test_returns_false(self):
        """Test return value."""
        assert not filters.length_is('three', 4)

    def test_returns_true(self):
        """Test return value."""
        assert filters.length_is('one', 3)


class TestIsUrl:
    """All tests for is url function."""

    def test_returns_urls_true(self):
        """Test return value."""
        assert filters.is_url('http://foo.bar')
        assert filters.is_url('https://foo.bar')

    def test_returns_urls_false(self):
        """Test return value."""
        assert not filters.is_url('//foo.bar')


class TestLJust:
    """All tests for ljust function."""

    def test_returns_lpadding(self):
        """Test return value."""
        assert filters.ljust('Flask', 10) == 'Flask     '


class TestRJust:
    """All tests for rjust function."""

    def test_returns_rpadding(self):
        """Test return value."""
        assert filters.rjust('Flask', 10) == '     Flask'


class TestMakeList:
    """All tests for make list function."""

    def test_list2list(self):
        """Test return value."""
        assert filters.make_list([1, 2]) == [1, 2]

    def test_ints_not_coerced(self):
        """Test return value."""
        assert filters.make_list(
            '12', coerce_numbers=False) == ['1', '2']

    def test_ints_coerced(self):
        """Test return value."""
        assert filters.make_list('12') == [1, 2]

    def test_dict(self):
        """Test return value."""
        assert filters.make_list({'foo': 'bar'}) == [('foo', 'bar')]

    def test_list(self):
        """Test return value."""
        assert filters.make_list([1, 2]) == [1, 2]

    def test_str(self):
        """Test return value."""
        assert filters.make_list('abc') == ['a', 'b', 'c']


class TestPhone2Numeric:
    """All tests for phone2numeric function."""

    def test_basic(self):
        """Test return value."""
        assert filters.phone2numeric('1800-COLLeCT') == '1800-2655328'

    def test_1_thru_9(self):
        """Test return value."""
        assert filters.phone2numeric('1800-ADGJMPTX') == '1800-23456789'


class TestSlugify:
    """All tests for slugify function."""

    def test_slugify_plain(self):
        """Test return value."""
        assert filters.slugify('My news title!') == 'my-news-title'

    def test_slugify_complex(self):
        """Test return value."""
        res = filters.slugify('I am an OBFUsc@@Ted URL!!! Foo bar')
        expected = 'i-am-an-obfusc--ted-url----foo-bar'
        assert res == expected


class TestPagetitle:
    """All tests for pagetitle function."""

    def test_title_plain(self):
        """Test return value."""
        assert filters.pagetitle('/foo/bar/bam') == ' > foo > bar > bam'

    def test_title_removefirst(self):
        """Test return value."""
        res = filters.pagetitle('/foo/bar/bam', divider=' | ')
        expected = ' | foo | bar | bam'
        assert res == expected

    def test_title_divider(self):
        """Test return value."""
        res = filters.pagetitle('/foo/bar/bam', remove_first=True)
        assert res == 'foo > bar > bam'


class TestGreet:
    """All tests for greet function."""

    def test_greet(self):
        """Test return value."""
        assert filters.greet('Chris') == 'Hello, Chris!'

    def test_greet_override(self):
        """Test return value."""
        assert filters.greet(
            'Chris', greeting='Bonjour' == 'Bonjour, Chris!')


class TestIsList:
    """All tests for islist function."""

    def test_islist(self):
        """Test return value."""
        assert filters.islist([1, 2, 3])

    def test_notislist(self):
        """Test return value."""
        assert not filters.islist('Foo')
        assert not filters.islist({'foo': 'bar'})
        assert not filters.islist(1)
        assert not filters.islist(1.0)


class TestSql2dict:
    """All tests for sql2dict function."""

    def test_none(self):
        """Test return value."""
        assert filters.sql2dict(None) == []

    def test_set(self):
        """Test return value."""
        mm = MockClass()
        mm.__dict__ = {'foo': 'bar'}
        assert filters.sql2dict([mm]) == [{'foo': 'bar'}]
