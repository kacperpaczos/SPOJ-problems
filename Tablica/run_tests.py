#!/usr/bin/env python3
"""
Main test runner for TABLICA problem solutions.

This script runs all test suites (basic, edge cases, performance, error handling)
for Python, Java, and C++ implementations and provides a comprehensive report.
"""

import sys
import unittest
import time
from io import StringIO


def run_all_tests():
    """
    Discover and run all tests in the tests directory.
    
    Returns:
        bool: True if all tests passed, False otherwise
    """
    print("=" * 70)
    print("TABLICA Problem - Comprehensive Test Suite")
    print("=" * 70)
    print()
    
    # Discover all tests in the tests directory
    loader = unittest.TestLoader()
    start_dir = 'tests'
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    # Count total tests
    def count_tests(test_suite):
        count = 0
        for test in test_suite:
            if isinstance(test, unittest.TestSuite):
                count += count_tests(test)
            else:
                count += 1
        return count
    
    total_tests = count_tests(suite)
    print(f"Discovered {total_tests} tests across multiple test suites")
    print()
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    
    start_time = time.time()
    result = runner.run(suite)
    elapsed_time = time.time() - start_time
    
    # Print summary
    print()
    print("=" * 70)
    print("Test Summary")
    print("=" * 70)
    print(f"Total tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Skipped: {len(result.skipped)}")
    print(f"Time elapsed: {elapsed_time:.2f} seconds")
    print()
    
    # Print detailed failure information
    if result.failures:
        print("=" * 70)
        print("Failed Tests Details")
        print("=" * 70)
        for test, traceback in result.failures:
            print(f"\n{test}:")
            print(traceback)
    
    if result.errors:
        print("=" * 70)
        print("Error Details")
        print("=" * 70)
        for test, traceback in result.errors:
            print(f"\n{test}:")
            print(traceback)
    
    # Final result
    print("=" * 70)
    if result.wasSuccessful():
        print("✓ All tests passed!")
        print("=" * 70)
        return True
    else:
        print("✗ Some tests failed!")
        print("=" * 70)
        return False


def run_specific_suite(suite_name: str):
    """
    Run a specific test suite.
    
    Args:
        suite_name: Name of the test suite (e.g., 'basic', 'edge_cases', 'performance', 'error_handling')
    
    Returns:
        bool: True if all tests passed, False otherwise
    """
    print(f"Running {suite_name} test suite...")
    print()
    
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromName(f'tests.test_{suite_name}')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


def print_usage():
    """Print usage information."""
    print("Usage:")
    print("  python3 run_tests.py              # Run all tests")
    print("  python3 run_tests.py basic        # Run basic functionality tests")
    print("  python3 run_tests.py edge_cases   # Run edge case tests")
    print("  python3 run_tests.py performance  # Run performance tests")
    print("  python3 run_tests.py error_handling # Run error handling tests")
    print()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] in ['--help', '-h', 'help']:
            print_usage()
            sys.exit(0)
        
        suite_name = sys.argv[1]
        valid_suites = ['basic', 'edge_cases', 'performance', 'error_handling']
        
        if suite_name not in valid_suites:
            print(f"Error: Unknown test suite '{suite_name}'")
            print(f"Valid suites: {', '.join(valid_suites)}")
            print()
            print_usage()
            sys.exit(1)
        
        success = run_specific_suite(suite_name)
    else:
        success = run_all_tests()
    
    sys.exit(0 if success else 1)
