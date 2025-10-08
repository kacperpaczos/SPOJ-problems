#!/usr/bin/env python3
"""
Test suite for TABLICA problem solutions in Python, Java, and C++.

This script tests all three implementations with various input cases
to ensure they produce correct output and handle errors properly.
"""

import subprocess
import sys
import os
from typing import List, Tuple, Optional


class SolutionTester:
    """Test class for running and validating TABLICA solutions."""

    def __init__(self, solutions_dir: str = "solutions"):
        """Initialize tester with solutions directory path."""
        self.solutions_dir = solutions_dir
        self.solutions = {
            'python': os.path.join(solutions_dir, 'tablica.py'),
            'java': os.path.join(solutions_dir, 'Tablica.java'),
            'cpp': os.path.join(solutions_dir, 'tablica.cpp')
        }

    def run_solution(self, language: str, input_data: str) -> Tuple[str, str, int]:
        """
        Run a solution with given input data.

        Args:
            language: One of 'python', 'java', 'cpp'
            input_data: Input string to feed to the program

        Returns:
            Tuple of (stdout, stderr, return_code)
        """
        if language not in self.solutions:
            raise ValueError(f"Unknown language: {language}")

        file_path = self.solutions[language]

        if language == 'python':
            cmd = [sys.executable, file_path]
        elif language == 'java':
            # Compile and run Java
            class_name = os.path.splitext(os.path.basename(file_path))[0]
            compile_cmd = ['javac', file_path]
            run_cmd = ['java', '-cp', self.solutions_dir, class_name]

            # Compile first
            compile_result = subprocess.run(
                compile_cmd,
                input=input_data,
                text=True,
                capture_output=True
            )
            if compile_result.returncode != 0:
                return "", compile_result.stderr, compile_result.returncode

            # Run compiled class
            cmd = run_cmd
        elif language == 'cpp':
            # Compile and run C++
            exe_path = os.path.join(self.solutions_dir, 'tablica_exe')
            compile_cmd = ['g++', '-std=c++17', '-o', exe_path, file_path]

            # Compile first
            compile_result = subprocess.run(
                compile_cmd,
                input=input_data,
                text=True,
                capture_output=True
            )
            if compile_result.returncode != 0:
                return "", compile_result.stderr, compile_result.returncode

            # Run executable
            cmd = [exe_path]

        # Run the solution
        result = subprocess.run(
            cmd,
            input=input_data,
            text=True,
            capture_output=True
        )

        return result.stdout.strip(), result.stderr.strip(), result.returncode

    def test_case(self, language: str, input_data: str, expected_output: str,
                  expected_return_code: int = 0, description: str = "") -> bool:
        """
        Test a single case for a solution.

        Args:
            language: Language to test ('python', 'java', 'cpp')
            input_data: Input to provide to the program
            expected_output: Expected stdout output
            expected_return_code: Expected return code (default 0)
            description: Test description for logging

        Returns:
            True if test passes, False otherwise
        """
        stdout, stderr, return_code = self.run_solution(language, input_data)

        success = (stdout == expected_output and return_code == expected_return_code)

        status = "PASS" if success else "FAIL"
        print(f"{language.upper():>6} | {description:<20} | {status}")

        if not success:
            print(f"        Input: {repr(input_data)}")
            print(f"        Expected: {repr(expected_output)} (return code: {expected_return_code})")
            print(f"        Got: {repr(stdout)} (return code: {return_code})")
            if stderr:
                print(f"        Stderr: {repr(stderr)}")

        return success


def run_all_tests():
    """Run comprehensive tests for all solutions."""
    tester = SolutionTester()

    test_cases = [
        # (input_data, expected_output, expected_return_code, description)
        ("1 2 3", "3 2 1", 0, "Basic reverse"),
        ("5 4 3 2 1", "1 2 3 4 5", 0, "Reverse sequence"),
        ("42", "42", 0, "Single number"),
        ("", "", 0, "Empty input"),
        ("1 2 3 4 5 6 7 8 9 10", "10 9 8 7 6 5 4 3 2 1", 0, "Long sequence"),
        ("1 a 3", "", 1, "Invalid input (Python)"),
    ]

    print("Testing TABLICA solutions")
    print("=" * 60)
    print(f"{'LANG':<6} | {'TEST':<20} | {'RESULT'}")
    print("-" * 60)

    total_tests = 0
    passed_tests = 0

    for language in ['python', 'java', 'cpp']:
        print(f"\nTesting {language.upper()} solution:")
        print("-" * 40)

        for input_data, expected_output, expected_return_code, description in test_cases:
            # Skip invalid input test for Java and C++ (they don't handle it the same way)
            if language in ['java', 'cpp'] and 'Invalid' in description:
                continue

            success = tester.test_case(
                language, input_data, expected_output,
                expected_return_code, description
            )
            total_tests += 1
            if success:
                passed_tests += 1

    print("\n" + "=" * 60)
    print(f"Test Results: {passed_tests}/{total_tests} tests passed")

    if passed_tests == total_tests:
        print("🎉 All tests passed!")
        return True
    else:
        print("❌ Some tests failed!")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
