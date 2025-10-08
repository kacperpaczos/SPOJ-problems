#!/usr/bin/env python3
"""
Basic functionality tests for SYS solutions.

Tests fundamental base conversion operations with simple inputs.
"""

import unittest
from tests.test_runner import SolutionRunner


class TestBasicFunctionality(unittest.TestCase):
    """Test basic base conversion functionality."""

    @classmethod
    def setUpClass(cls):
        """Set up test runner for all test methods."""
        cls.runner = SolutionRunner()

    def test_example_case(self):
        """Test the example case from problem description."""
        input_data = "2\n1263\n10"
        expected = "4EF A49\nA A"

        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed example case")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_single_test_case(self):
        """Test with single test case."""
        input_data = "1\n100"
        expected = "64 91"

        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed single test case")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_zero_value(self):
        """Test conversion of zero."""
        input_data = "1\n0"
        expected = "0 0"

        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed zero value")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_small_numbers(self):
        """Test conversion of small numbers."""
        input_data = "3\n1\n2\n9"
        expected = "1 1\n2 2\n9 9"

        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed small numbers")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_base_digits(self):
        """Test numbers that are digits in the target bases."""
        input_data = "2\n15\n10"
        expected = "F 14\nA A"

        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed base digits")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_max_value(self):
        """Test maximum allowed value."""
        input_data = "1\n1000000"
        expected = "F4240 623351"

        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed max value")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")


if __name__ == '__main__':
    unittest.main()
