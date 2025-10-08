#!/usr/bin/env python3
"""
Error handling tests for TABLICA solutions.

Tests invalid inputs and error conditions (primarily for Python solution).
"""

import unittest
from tests.test_runner import SolutionRunner


class TestErrorHandling(unittest.TestCase):
    """Test error handling and invalid input scenarios."""

    @classmethod
    def setUpClass(cls):
        """Set up test runner for all test methods."""
        cls.runner = SolutionRunner()

    def test_invalid_input_letters_python(self):
        """Test Python solution with letters in input."""
        input_data = "1 a 3"
        
        stdout, stderr, code = self.runner.run('python', input_data)
        self.assertNotEqual(code, 0, "Python: Should return non-zero exit code for invalid input")
        self.assertIn("Error", stderr, "Python: Should output error message to stderr")

    def test_invalid_input_mixed_python(self):
        """Test Python solution with mixed valid/invalid input."""
        input_data = "1 2 abc 4"
        
        stdout, stderr, code = self.runner.run('python', input_data)
        self.assertNotEqual(code, 0, "Python: Should return non-zero exit code for invalid input")
        self.assertIn("Error", stderr, "Python: Should output error message to stderr")

    def test_invalid_input_special_chars_python(self):
        """Test Python solution with special characters."""
        input_data = "1 @ 3"
        
        stdout, stderr, code = self.runner.run('python', input_data)
        self.assertNotEqual(code, 0, "Python: Should return non-zero exit code for invalid input")
        self.assertIn("Error", stderr, "Python: Should output error message to stderr")

    def test_invalid_input_float_python(self):
        """Test Python solution with floating point numbers."""
        input_data = "1.5 2.7 3.9"
        
        stdout, stderr, code = self.runner.run('python', input_data)
        self.assertNotEqual(code, 0, "Python: Should return non-zero exit code for float input")

    def test_invalid_input_comma_separated_python(self):
        """Test Python solution with comma-separated values."""
        input_data = "1,2,3"
        
        stdout, stderr, code = self.runner.run('python', input_data)
        self.assertNotEqual(code, 0, "Python: Should return non-zero exit code for comma-separated")

    def test_valid_negative_sign_python(self):
        """Test that negative numbers are handled correctly (not as invalid)."""
        input_data = "-1 -2 -3"
        expected = "-3 -2 -1"
        
        stdout, stderr, code = self.runner.run('python', input_data)
        self.assertEqual(code, 0, "Python: Should accept negative numbers")
        self.assertEqual(stdout, expected, "Python: Should correctly reverse negative numbers")

    def test_number_with_plus_sign_python(self):
        """Test numbers with explicit plus sign."""
        input_data = "+1 +2 +3"
        # Python's int() converts +1 to 1, so output won't have + signs
        expected = "3 2 1"
        
        stdout, stderr, code = self.runner.run('python', input_data)
        self.assertEqual(code, 0, "Python: Should accept numbers with + sign")
        self.assertEqual(stdout, expected, "Python: Should correctly reverse numbers (+ signs removed)")


if __name__ == '__main__':
    unittest.main()
