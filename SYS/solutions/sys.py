#!/usr/bin/env python3

import sys

def get_base_root(base):
    """Znajdź najmniejszą podstawę, której potęgą jest dana liczba.
    Np: 16→2, 9→3, 27→3, 8→2, 25→5
    Zwraca (root, exponent) lub (base, 1) jeśli base nie jest potęgą liczby pierwszej
    
    Metoda: Faktoryzacja na czynniki pierwsze z early return.
    Zlicza wykładnik podczas faktoryzacji bez budowania listy.
    """
    if base <= 1:
        return base, 1
    
    first_factor = None
    exponent = 0
    n = base
    
    # Sprawdź dzielenie przez 2
    if n % 2 == 0:
        first_factor = 2
        while n % 2 == 0:
            exponent += 1
            n //= 2
    
    # Jeśli pozostało coś więcej, nie jest potęgą 2
    if first_factor and n > 1:
        return base, 1
    
    # Sprawdź nieparzyste czynniki pierwsze
    if not first_factor:
        divisor = 3
        while divisor * divisor <= n:
            if n % divisor == 0:
                first_factor = divisor
                while n % divisor == 0:
                    exponent += 1
                    n //= divisor
                break
            divisor += 2
    
    # Sprawdź pozostałość
    if n > 1:
        if first_factor:
            return base, 1  # Różne czynniki pierwsze
        return n, 1  # base jest liczbą pierwszą
    
    return first_factor if first_factor else base, exponent if exponent > 0 else 1

def digit_to_char(digit):
    """Helper: konwertuj cyfrę (0-35) na znak (0-9, A-Z)"""
    return str(digit) if digit < 10 else chr(ord('A') + digit - 10)

def to_base_n(num, base):
    """Konwertuj liczbę dziesiętną na string w podanej podstawie z optymalizacjami"""
    if num == 0:
        return '0'
    
    root, exp = get_base_root(base)
    
    # Optymalizacja dla potęg dwójki - operacje bitowe
    if root == 2 and exp > 1:
        bits_per_digit = exp
        mask = (1 << bits_per_digit) - 1
        result = []
        while num > 0:
            result.append(digit_to_char(num & mask))
            num >>= bits_per_digit
        return ''.join(reversed(result))
    
    # Standardowa konwersja dla pozostałych przypadków
    result = []
    while num > 0:
        result.append(digit_to_char(num % base))
        num //= base
    return ''.join(reversed(result))

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
