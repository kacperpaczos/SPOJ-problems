#!/usr/bin/env python3

import sys
import math

def is_power_of(base1, base2):
    """Check if base1 is a power of base2"""
    if base1 == 1 or base2 == 1:
        return False
    if base1 == base2:
        return True

    # Check if base1 is power of base2
    temp = base2
    while temp < base1:
        temp *= base2
        if temp == base1:
            return True

    # Check if base2 is power of base1
    temp = base1
    while temp < base2:
        temp *= base1
        if temp == base2:
            return True

    return False

def get_power_relationship(from_base, to_base):
    """Get the power relationship between bases. Returns (is_power, exponent, direction)"""
    if from_base == to_base:
        return True, 1, 0  # same base

    # Check if to_base is power of from_base
    exponent = 1
    temp = from_base
    while temp < to_base:
        temp *= from_base
        exponent += 1
        if temp == to_base:
            return True, exponent, 1  # to_base = from_base^exponent

    # Check if from_base is power of to_base
    exponent = 1
    temp = to_base
    while temp < from_base:
        temp *= to_base
        exponent += 1
        if temp == from_base:
            return True, exponent, -1  # from_base = to_base^exponent

    return False, 0, 0

def convert_base_direct(number_str, from_base, to_base):
    """Convert directly between compatible bases (one is power of another)"""
    is_power, exponent, direction = get_power_relationship(from_base, to_base)

    if not is_power:
        raise ValueError("Bases are not compatible for direct conversion")

    # Convert to binary first
    decimal = 0
    for i, digit in enumerate(reversed(number_str)):
        if digit.isdigit():
            val = int(digit)
        else:
            val = ord(digit.upper()) - ord('A') + 10
        decimal += val * (from_base ** i)

    # Convert decimal to target base using direct method
    if decimal == 0:
        return '0'

    # Get binary representation
    binary = bin(decimal)[2:]  # Remove '0b' prefix

    # Pad with zeros to make length divisible by exponent
    if direction == 1:  # from_base -> to_base^exponent
        group_size = exponent
    else:  # to_base -> from_base^exponent
        group_size = exponent

    # Pad binary to make it divisible by group_size
    padding = (group_size - len(binary) % group_size) % group_size
    binary = '0' * padding + binary

    # Group bits and convert to target base digits
    result = []
    for i in range(0, len(binary), group_size):
        group = binary[i:i+group_size]
        group_val = int(group, 2)
        if group_val < 10:
            result.append(str(group_val))
        else:
            result.append(chr(ord('A') + group_val - 10))

    return ''.join(result)

def to_base_n(num, base):
    """Convert decimal number to specified base with optimization for compatible bases"""
    if num == 0:
        return '0'

    # For bases 2, 4, 8, 16 - we can optimize using binary grouping
    if base in [2, 4, 8, 16]:
        # Convert to binary first, then group bits
        binary = bin(num)[2:]  # Remove '0b'

        if base == 2:
            return binary
        elif base == 4:
            # Group by 2 bits
            padding = (2 - len(binary) % 2) % 2
            binary = '0' * padding + binary
            result = []
            for i in range(0, len(binary), 2):
                group = binary[i:i+2]
                result.append(str(int(group, 2)))
            return ''.join(result)
        elif base == 8:
            # Group by 3 bits
            padding = (3 - len(binary) % 3) % 3
            binary = '0' * padding + binary
            result = []
            for i in range(0, len(binary), 3):
                group = binary[i:i+3]
                result.append(str(int(group, 2)))
            return ''.join(result)
        elif base == 16:
            # Group by 4 bits
            padding = (4 - len(binary) % 4) % 4
            binary = '0' * padding + binary
            result = []
            for i in range(0, len(binary), 4):
                group = binary[i:i+4]
                group_val = int(group, 2)
                if group_val < 10:
                    result.append(str(group_val))
                else:
                    result.append(chr(ord('A') + group_val - 10))
            return ''.join(result)

    # For other bases, use standard conversion
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
