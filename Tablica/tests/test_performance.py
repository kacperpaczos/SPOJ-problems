#!/usr/bin/env python3
"""
Performance and stress tests for TABLICA solutions.

Tests with large inputs, extreme values, and performance benchmarks.
"""

import unittest
import time
from tests.test_runner import SolutionRunner


class TestPerformance(unittest.TestCase):
    """Test performance with large inputs and extreme values."""

    @classmethod
    def setUpClass(cls):
        """Set up test runner for all test methods."""
        cls.runner = SolutionRunner()

    def test_large_array_100(self):
        """Test reversing 100 elements."""
        numbers = list(range(1, 101))
        input_data = " ".join(map(str, numbers))
        expected = " ".join(map(str, reversed(numbers)))
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed 100 elements")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_large_array_1000(self):
        """Test reversing 1000 elements."""
        numbers = list(range(1, 1001))
        input_data = " ".join(map(str, numbers))
        expected = " ".join(map(str, reversed(numbers)))
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed 1000 elements")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_large_array_10000(self):
        """Test reversing 10000 elements."""
        numbers = list(range(1, 10001))
        input_data = " ".join(map(str, numbers))
        expected = " ".join(map(str, reversed(numbers)))
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                start_time = time.time()
                stdout, stderr, code = self.runner.run(lang, input_data)
                elapsed = time.time() - start_time
                
                self.assertEqual(stdout, expected, f"{lang}: Failed 10000 elements")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")
                self.assertLess(elapsed, 5.0, f"{lang}: Too slow (>{elapsed:.2f}s)")

    def test_very_large_numbers(self):
        """Test with very large integer values."""
        input_data = "2147483647 -2147483648 1000000000"
        expected = "1000000000 -2147483648 2147483647"
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed large numbers")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_alternating_pattern(self):
        """Test with alternating positive/negative pattern."""
        numbers = []
        for i in range(1, 51):
            numbers.append(i if i % 2 == 0 else -i)
        
        input_data = " ".join(map(str, numbers))
        expected = " ".join(map(str, reversed(numbers)))
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed alternating pattern")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_random_large_values(self):
        """Test with random large values."""
        import random
        random.seed(42)  # For reproducibility
        numbers = [random.randint(-1000000, 1000000) for _ in range(100)]
        
        input_data = " ".join(map(str, numbers))
        expected = " ".join(map(str, reversed(numbers)))
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed random values")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")

    def test_palindrome_array(self):
        """Test with palindromic array (same forwards and backwards)."""
        input_data = "1 2 3 4 5 4 3 2 1"
        expected = "1 2 3 4 5 4 3 2 1"
        
        for lang in ['python', 'java', 'cpp']:
            with self.subTest(language=lang):
                stdout, stderr, code = self.runner.run(lang, input_data)
                self.assertEqual(stdout, expected, f"{lang}: Failed palindrome")
                self.assertEqual(code, 0, f"{lang}: Non-zero exit code")


if __name__ == '__main__':
    unittest.main()
