#!/usr/bin/env python3
"""
Advanced edge case tests for TABLICA solutions.

Tests advanced scenarios including resource limits, signal handling,
and extreme edge cases that production code should handle.
"""

import unittest
import signal
from tests.test_runner import SolutionRunner


class TestAdvancedCases(unittest.TestCase):
    """Test advanced edge cases and production scenarios."""

    @classmethod
    def setUpClass(cls):
        """Set up test runner for all test methods."""
        cls.runner = SolutionRunner()

    def test_very_long_line(self):
        """Test handling of very long input line (stress test)."""
        # Create a line with 50,000 numbers
        numbers = list(range(50000))
        input_data = " ".join(map(str, numbers))
        expected = " ".join(map(str, reversed(numbers)))
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data, timeout=30)
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code for very long line")
                self.assertEqual(stdout, expected, f"{lang}: Failed very long line")

    def test_maximum_integer_values(self):
        """Test with maximum 32-bit integer values."""
        # INT_MAX and INT_MIN for 32-bit integers
        input_data = "2147483647 -2147483648 0"
        expected = "0 -2147483648 2147483647"
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed max integer values")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_all_negative_numbers(self):
        """Test with all negative numbers."""
        input_data = "-100 -50 -25 -10 -5 -1"
        expected = "-1 -5 -10 -25 -50 -100"
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed all negative")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_repeating_pattern(self):
        """Test with repeating number pattern."""
        input_data = "1 2 3 1 2 3 1 2 3"
        expected = "3 2 1 3 2 1 3 2 1"
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed repeating pattern")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_fibonacci_sequence(self):
        """Test with Fibonacci sequence."""
        fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        input_data = " ".join(map(str, fib))
        expected = " ".join(map(str, reversed(fib)))
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed Fibonacci sequence")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_powers_of_two(self):
        """Test with powers of two."""
        powers = [2**i for i in range(20)]  # 1 to 524288
        input_data = " ".join(map(str, powers))
        expected = " ".join(map(str, reversed(powers)))
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed powers of two")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_prime_numbers(self):
        """Test with prime numbers."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        input_data = " ".join(map(str, primes))
        expected = " ".join(map(str, reversed(primes)))
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed prime numbers")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_sparse_range(self):
        """Test with sparse number range."""
        input_data = "1000000 500000 250000 125000 62500 31250"
        expected = "31250 62500 125000 250000 500000 1000000"
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed sparse range")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_mixed_magnitude_numbers(self):
        """Test with numbers of vastly different magnitudes."""
        input_data = "1000000000 1000 1 0 -1 -1000 -1000000000"
        expected = "-1000000000 -1000 -1 0 1 1000 1000000000"
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed mixed magnitude")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_newline_separated_input(self):
        """Test with numbers on separate lines."""
        input_data = "1\n2\n3\n4\n5"
        expected = "5 4 3 2 1"
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed newline separated")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_mixed_separators(self):
        """Test with mixed whitespace separators (spaces, tabs, newlines)."""
        input_data = "1\t2  3\n4    5\t\t6"
        expected = "6 5 4 3 2 1"
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed mixed separators")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")


if __name__ == '__main__':
    unittest.main()
