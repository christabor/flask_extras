import unittest
import filters


class TitleTest(unittest.TestCase):
    def test_title_returns_str(self):
        """Test the return value for a valid type"""
        self.assertIsInstance(filters.title('foo bar'), str)

    def test_title_word(self):
        """Tests the `word` argument."""
        self.assertEqual(filters.title('foo bar'), 'Foo bar')

    def test_title_capitalize(self):
        """Tests the `capitalize` argument."""
        self.assertEqual(
            filters.title('foo bar', capitalize=True), 'Foo Bar')

    def test_title_capitalize_sentence(self):
        """Tests the `capitalize` argument."""
        self.assertEqual(filters.title(
            'the quick brown fox... ah forget it', capitalize=True),
            'The Quick Brown Fox... Ah Forget It')

    def test_title_none(self):
        """Tests the function with None argument."""
        self.assertEqual(filters.questionize_label(None), '')


class QuestionizeLabelTest(unittest.TestCase):

    def test_questionize_label_returns_str(self):
        """Test the return value for a valid type"""
        self.assertIsInstance(filters.questionize_label('foo bar'), str)

    def test_questionize_label_word_is(self):
        """Tests the `word` argument."""
        self.assertEqual(filters.questionize_label('is_cool'), 'cool?')

    def test_questionize_label_word_has(self):
        """Tests the `word` argument."""
        self.assertEqual(filters.questionize_label('has_stuff'), 'stuff?')

    def test_questionize_label_none(self):
        """Tests the function with None argument."""
        self.assertEqual(filters.questionize_label(None), '')
