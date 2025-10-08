#!/usr/bin/env python3
"""SPOJ TABLICA problem solution in Python.

This program reads a sequence of integers from stdin and outputs them in reverse order.
Uses advanced Python features like list comprehensions and string slicing for minimal code.
"""

import sys

# Read all numbers from stdin, split by spaces, convert to integers, and reverse order
numbers = list(map(int, sys.stdin.read().split()))
print(' '.join(map(str, numbers[::-1])))
