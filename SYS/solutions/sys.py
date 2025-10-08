#!/usr/bin/env python3

import sys

def is_power_of_two_base(base):
    """Sprawdź czy podstawa jest potęgą dwójki (2, 4, 8, 16, 32, ...)"""
    return base > 1 and (base & (base - 1)) == 0

def to_base_n(num, base):
    """Convert decimal number to specified base with optimization for power-of-2 bases"""
    if num == 0:
        return '0'

    # Optymalizacja: dla potęg dwójki używamy grupowania bitów
    if is_power_of_two_base(base):
        # Oblicz ile bitów reprezentuje jedna cyfra w docelowej podstawie
        # base = 2^bits_per_digit → bits_per_digit = log2(base)
        bits_per_digit = (base - 1).bit_length()
        
        # Konwertuj do binarnego
        binary = bin(num)[2:]  # Usuń prefix '0b'
        
        # Dopełnij zerami do wielokrotności bits_per_digit
        padding = (bits_per_digit - len(binary) % bits_per_digit) % bits_per_digit
        binary = '0' * padding + binary
        
        # Grupuj bity i konwertuj każdą grupę na cyfrę
        result = []
        for i in range(0, len(binary), bits_per_digit):
            group = binary[i:i+bits_per_digit]
            group_val = int(group, 2)
            if group_val < 10:
                result.append(str(group_val))
            else:
                result.append(chr(ord('A') + group_val - 10))
        return ''.join(result)

    # Standardowa konwersja dla innych podstaw
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
