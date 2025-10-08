#!/usr/bin/env python3
"""
Basic functionality tests for TABLICA solutions.

Tests fundamental array reversal operations with simple inputs.
"""

import unittest
from tests.test_runner import SolutionRunner


class TestBasicFunctionality(unittest.TestCase):
    """Test basic array reversal functionality."""

    @classmethod
    def setUpClass(cls):
        """Set up test runner for all test methods."""
        cls.runner = SolutionRunner()

    def test_simple_reverse(self):
        """Test reversing a simple 3-element array."""
        input_data = "1 2 3"
        expected = "3 2 1"
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed simple reverse")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_single_element(self):
        """Test reversing a single element."""
        input_data = "42"
        expected = "42"
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed single element")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_two_elements(self):
        """Test reversing two elements."""
        input_data = "10 20"
        expected = "20 10"
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed two elements")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_already_reversed(self):
        """Test reversing an already reversed sequence."""
        input_data = "5 4 3 2 1"
        expected = "1 2 3 4 5"
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed already reversed")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_identical_elements(self):
        """Test reversing array with identical elements."""
        input_data = "7 7 7 7"
        expected = "7 7 7 7"
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed identical elements")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")


if __name__ == '__main__':
    unittest.main()
