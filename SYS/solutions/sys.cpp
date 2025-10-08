#include <iostream>
#include <string>
#include <algorithm>

bool is_power_of_two_base(int base) {
    // Sprawdź czy podstawa jest potęgą dwójki (2, 4, 8, 16, 32, ...)
    return base > 1 && (base & (base - 1)) == 0;
}

int count_bits_per_digit(int base) {
    // Oblicz ile bitów reprezentuje jedna cyfra w danej podstawie
    // base = 2^bits → bits = log2(base)
    int bits = 0;
    int temp = base;
    while (temp > 1) {
        temp >>= 1;
        bits++;
    }
    return bits;
}


std::string to_base_n(long long num, int base) {
    if (num == 0) {
        return "0";
    }

    // Optymalizacja: dla potęg dwójki używamy grupowania bitów
    if (is_power_of_two_base(base)) {
        // Oblicz ile bitów reprezentuje jedna cyfra
        int bits_per_digit = count_bits_per_digit(base);
        
        // Konwertuj do binarnego
        std::string binary = "";
        long long temp = num;
        while (temp > 0) {
            binary = char('0' + (temp % 2)) + binary;
            temp /= 2;
        }
        
        // Dopełnij zerami do wielokrotności bits_per_digit
        int padding = (bits_per_digit - binary.length() % bits_per_digit) % bits_per_digit;
        binary = std::string(padding, '0') + binary;
        
        // Grupuj bity i konwertuj każdą grupę na cyfrę
        std::string result = "";
        for (size_t i = 0; i < binary.length(); i += bits_per_digit) {
            std::string group = binary.substr(i, bits_per_digit);
            int group_val = std::stoi(group, nullptr, 2);
            if (group_val < 10) {
                result += char('0' + group_val);
            } else {
                result += char('A' + group_val - 10);
            }
        }
        return result;
    }

    // Standardowa konwersja dla innych podstaw
    std::string result = "";
    while (num > 0) {
        int remainder = num % base;
        if (remainder < 10) {
            result += char('0' + remainder);
        } else {
            result += char('A' + remainder - 10);
        }
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
