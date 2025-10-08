#!/usr/bin/env python3
"""
Edge case tests for TABLICA solutions.

Tests boundary conditions, empty inputs, and special cases.
"""

import unittest
from tests.test_runner import SolutionRunner


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions."""

    @classmethod
    def setUpClass(cls):
        """Set up test runner for all test methods."""
        cls.runner = SolutionRunner()

    def test_empty_input(self):
        """Test handling of empty input."""
        input_data = ""
        expected = ""
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed empty input")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code for empty input")

    def test_whitespace_only(self):
        """Test handling of whitespace-only input."""
        input_data = "   \n  \t  "
        expected = ""
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed whitespace-only input")

    def test_zero_value(self):
        """Test handling of zero as a value."""
        input_data = "0"
        expected = "0"
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed zero value")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_multiple_zeros(self):
        """Test handling of multiple zeros."""
        input_data = "0 0 0"
        expected = "0 0 0"
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed multiple zeros")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_negative_numbers(self):
        """Test handling of negative numbers."""
        input_data = "-5 -3 -1"
        expected = "-1 -3 -5"
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed negative numbers")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_mixed_positive_negative(self):
        """Test handling of mixed positive and negative numbers."""
        input_data = "-10 5 -3 8 0"
        expected = "0 8 -3 5 -10"
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed mixed pos/neg")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_extra_spaces_between_numbers(self):
        """Test handling of multiple spaces between numbers."""
        input_data = "1    2     3"
        expected = "3 2 1"
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed extra spaces")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_leading_trailing_spaces(self):
        """Test handling of leading and trailing spaces."""
        input_data = "   1 2 3   "
        expected = "3 2 1"
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed leading/trailing spaces")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")


if __name__ == '__main__':
    unittest.main()
