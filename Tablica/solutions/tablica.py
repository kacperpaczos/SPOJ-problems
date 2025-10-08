#!/usr/bin/env python3
"""
SPOJ: TABLICA – Reverse array problem

Reads a sequence of integers from stdin and outputs them in reverse order.

Time Complexity: O(n) where n is the number of integers
Space Complexity: O(n) for storing the input array
"""

import sys
from typing import List, NoReturn


def parse_integers(data: str) -> List[int]:
    """
    Parse whitespace-separated integers from input string.
    
    Args:
        data: Input string containing integers separated by whitespace
        
    Returns:
        List of parsed integers
        
    Raises:
        ValueError: If any token cannot be parsed as an integer
    """
    return [int(token) for token in data.split()]


def reverse_and_format(numbers: List[int]) -> str:
    """
    Reverse a list of integers and format as space-separated string.
    
    Args:
        numbers: List of integers to reverse
        
    Returns:
        Space-separated string of reversed integers
    """
    return ' '.join(map(str, reversed(numbers)))


def handle_error(message: str) -> NoReturn:
    """
    Write error message to stderr and exit with error code.
    
    Args:
        message: Error message to display
    """
    sys.stderr.write(f"Error: {message}\n")
    sys.exit(1)


def main() -> None:
    """
    Main function to read, process, and output reversed numbers.
    
    Reads integers from stdin, reverses their order, and prints to stdout.
    Handles edge cases: empty input, invalid integers, overflow.
    """
    try:
        data = sys.stdin.read().strip()
        
        # Handle empty input gracefully
        if not data:
            return
        
        # Parse and validate input
        numbers = parse_integers(data)
        
        # Check for empty result after parsing
        if not numbers:
            return
        
        # Reverse and output
        output = reverse_and_format(numbers)
        print(output)
        
    except ValueError as e:
        # Handle parsing errors (non-integer input)
        handle_error("Input must contain only integers")
    except MemoryError:
        # Handle extremely large inputs
        handle_error("Input too large to process")
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        sys.stderr.write("\nInterrupted by user\n")
        sys.exit(130)
    except Exception as e:
        # Catch-all for unexpected errors (shouldn't happen in production)
        handle_error(f"Unexpected error: {type(e).__name__}")


if __name__ == "__main__":
    main()
