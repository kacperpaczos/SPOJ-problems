#!/usr/bin/env python3
"""
SPOJ: TABLICA – Reverse array problem

Reads a sequence of integers from stdin and outputs them in reverse order.
"""

import sys


def main() -> None:
    """Main function to read, process, and output reversed numbers."""
    try:
        data = sys.stdin.read().strip()
        if not data:
            return  # No input data – nothing to output

        numbers = [int(x) for x in data.split()]
        reversed_numbers = map(str, reversed(numbers))
        print(' '.join(reversed_numbers))
    except ValueError:
        # If input contains non-integer values
        sys.stderr.write("Error: Input must contain only integers.\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
