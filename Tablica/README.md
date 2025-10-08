# TABLICA - Array Reversal Problem

Solution for SPOJ problem TABLICA - reversing an array of integers.

## Problem Description

Write a program that reads a sequence of integers from stdin and outputs them in reverse order.

**Input:** A sequence of space-separated integers  
**Output:** The same integers in reverse order, space-separated

**Example:**
```
Input:  1 2 3
Output: 3 2 1
```

## Solutions

This repository contains three implementations:

### 1. Python (`solutions/tablica.py`)
- Uses list comprehensions and `reversed()` function
- Includes comprehensive error handling with try/except
- Validates input and handles edge cases
- Type hints for better code documentation
- Follows PEP 8 standards

**Features:**
- ✅ Empty input handling
- ✅ Invalid input detection (non-integers)
- ✅ Error messages to stderr
- ✅ Proper exit codes

### 2. Java (`solutions/Tablica.java`)
- Uses Java 8+ Stream API
- `Collections.reverse()` for efficient reversal
- Try-with-resources for automatic resource management
- Follows Google Java Style Guide

**Features:**
- ✅ Functional programming with streams
- ✅ `Collectors.joining()` for output formatting
- ✅ Proper resource management

### 3. C++ (`solutions/tablica.cpp`)
- Modern C++17/20 features
- `std::vector` and `std::reverse` from STL
- Iterator-based copying with `std::copy`
- Follows Google C++ Style Guide

**Features:**
- ✅ STL algorithms for efficiency
- ✅ Range-based for loops
- ✅ Modern C++ idioms

## Project Structure

```
Tablica/
├── solutions/              # Solution implementations
│   ├── tablica.py         # Python solution
│   ├── Tablica.java       # Java solution
│   └── tablica.cpp        # C++ solution
├── tests/                 # Test suites
│   ├── __init__.py
│   ├── test_basic.py      # Basic functionality tests
│   ├── test_edge_cases.py # Edge cases and boundary conditions
│   ├── test_performance.py # Performance and stress tests
│   ├── test_error_handling.py # Error handling tests
│   └── test_runner.py     # Test execution utility
├── run_tests.py           # Main test runner
└── README.md              # This file
```

## Running Solutions

### Python
```bash
cd solutions
echo "1 2 3" | python3 tablica.py
```

### Java
```bash
cd solutions
javac Tablica.java
echo "1 2 3" | java Tablica
```

### C++
```bash
cd solutions
g++ -std=c++17 -O2 -o tablica tablica.cpp
echo "1 2 3" | ./tablica
```

## Running Tests

### Run All Tests (27 tests)
```bash
cd Tablica
python3 run_tests.py
```

### Run Specific Test Suite
```bash
python3 run_tests.py basic           # Basic functionality (5 tests)
python3 run_tests.py edge_cases      # Edge cases (8 tests)
python3 run_tests.py performance     # Performance tests (7 tests)
python3 run_tests.py error_handling  # Error handling (7 tests)
```

### Test Coverage

**Basic Functionality (5 tests)**
- Simple array reversal
- Single element
- Two elements
- Already reversed sequence
- Identical elements

**Edge Cases (8 tests)**
- Empty input
- Whitespace-only input
- Zero values
- Negative numbers
- Mixed positive/negative
- Extra spaces between numbers
- Leading/trailing spaces

**Performance (7 tests)**
- Large arrays (100, 1000, 10000 elements)
- Very large integer values (INT_MAX/INT_MIN)
- Alternating patterns
- Random values
- Palindromic arrays
- Performance benchmarks (<5s for 10k elements)

**Error Handling (7 tests - Python only)**
- Invalid input (letters, special chars)
- Mixed valid/invalid input
- Floating point numbers
- Comma-separated values
- Plus sign handling
- Proper error messages to stderr
- Non-zero exit codes for errors

## Test Results

All 27 tests pass successfully across all three implementations:
- ✅ Python: All tests pass
- ✅ Java: All applicable tests pass
- ✅ C++: All applicable tests pass

**Execution time:** ~3.3 seconds for full test suite

## Requirements

### Python
- Python 3.6+
- No external dependencies

### Java
- Java 8+
- JDK with javac compiler

### C++
- C++17 compatible compiler (g++ 7+, clang++ 5+)
- Standard library

## Code Quality

All solutions follow industry best practices:
- ✅ Google coding standards
- ✅ Comprehensive documentation
- ✅ Type hints (Python)
- ✅ Modern language features
- ✅ Minimal, readable code
- ✅ Proper error handling
- ✅ Extensive test coverage

## Performance

All solutions have O(n) time complexity and O(n) space complexity:
- Reading input: O(n)
- Reversing: O(n)
- Output: O(n)

Tested with arrays up to 10,000 elements - all complete in under 5 seconds.

## License

This is a solution for educational purposes for the SPOJ TABLICA problem.
