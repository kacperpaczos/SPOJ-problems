#include <iostream>
#include <string>
#include <algorithm>
#include <utility>

// Zwraca (root, exponent) dla base = root^exponent lub (base, 1) gdy base nie jest potęgą jednej liczby pierwszej
static std::pair<int,int> get_base_root(int base) {
    if (base <= 1) {
        return {base, 1};
    }

    int first_factor = 0;
    int exponent = 0;
    int n = base;

    // Sprawdź 2
    if ((n % 2) == 0) {
        first_factor = 2;
        while ((n % 2) == 0) {
            exponent++;
            n /= 2;
        }
    }

    // Jeśli zostało coś więcej niż 1, to nie jest czysta potęga 2
    if (first_factor != 0 && n > 1) {
        return {base, 1};
    }

    // Szukaj nieparzystych czynników
    if (first_factor == 0) {
        int d = 3;
        while (1LL * d * d <= n) {
            if ((n % d) == 0) {
                first_factor = d;
                while ((n % d) == 0) {
                    exponent++;
                    n /= d;
                }
                break;
            }
            d += 2;
        }
    }

    // Jeśli została reszta > 1
    if (n > 1) {
        if (first_factor != 0) {
            // różne czynniki → nie jest potęgą jednej liczby pierwszej
            return {base, 1};
        }
        // base było liczbą pierwszą
        return {n, 1};
    }

    return { first_factor != 0 ? first_factor : base, exponent > 0 ? exponent : 1 };
}

static inline char digit_to_char(int digit) {
    return digit < 10 ? static_cast<char>('0' + digit) : static_cast<char>('A' + digit - 10);
}


std::string to_base_n(long long num, int base) {
    if (num == 0) {
        return "0";
    }

    // Detekcja potęgi liczby pierwszej i optymalizacja dla potęg 2
    auto root_exp = get_base_root(base);
    int root = root_exp.first;
    int exp = root_exp.second;

    if (root == 2 && exp > 1) {
        int bits_per_digit = exp; // base = 2^exp
        int mask = (1 << bits_per_digit) - 1;
        std::string result;
        while (num > 0) {
            int group_val = static_cast<int>(num & mask);
            result.push_back(digit_to_char(group_val));
            num >>= bits_per_digit;
        }
        std::reverse(result.begin(), result.end());
        return result;
    }

    // Standardowa konwersja dla innych podstaw
    std::string result = "";
    while (num > 0) {
        int remainder = num % base;
        result += digit_to_char(remainder);
        num /= base;
    }

    std::reverse(result.begin(), result.end());
    return result;
}

int main() {
    int t;
    std::cin >> t;

    for (int i = 0; i < t; i++) {
        long long n;
        std::cin >> n;

        std::string hex_result = to_base_n(n, 16);
        std::string undecimal_result = to_base_n(n, 11);

        std::cout << hex_result << " " << undecimal_result << std::endl;
    }

    return 0;
}
