#!/usr/bin/env python3

import sys

def to_base_n(num, base):
    """Convert decimal number to specified base (11 or 16)"""
    if num == 0:
        return '0'

    digits = []
    while num > 0:
        remainder = num % base
        if remainder < 10:
            digits.append(str(remainder))
        else:
            digits.append(chr(ord('A') + remainder - 10))
        num //= base

    return ''.join(reversed(digits))

def main():
    input_data = sys.stdin.read().splitlines()
    t = int(input_data[0])

    for i in range(1, t + 1):
        n = int(input_data[i])
        hex_result = to_base_n(n, 16).upper()
        undecimal_result = to_base_n(n, 11).upper()
        print(f"{hex_result} {undecimal_result}")

if __name__ == "__main__":
    main()
