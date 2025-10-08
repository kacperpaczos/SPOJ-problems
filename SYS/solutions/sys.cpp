#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>

bool is_power_of(int base1, int base2) {
    if (base1 == 1 || base2 == 1) return false;
    if (base1 == base2) return true;

    // Check if base1 is power of base2
    long long temp = base2;
    while (temp < base1) {
        temp *= base2;
        if (temp == base1) return true;
    }

    // Check if base2 is power of base1
    temp = base1;
    while (temp < base2) {
        temp *= base1;
        if (temp == base2) return true;
    }

    return false;
}

struct PowerRelation {
    bool is_power;
    int exponent;
    int direction; // 0: same, 1: to_base = from_base^exp, -1: from_base = to_base^exp
};

PowerRelation get_power_relationship(int from_base, int to_base) {
    if (from_base == to_base) {
        return {true, 1, 0};
    }

    // Check if to_base is power of from_base
    int exponent = 1;
    long long temp = from_base;
    while (temp < to_base) {
        temp *= from_base;
        exponent++;
        if (temp == to_base) {
            return {true, exponent, 1};
        }
    }

    // Check if from_base is power of to_base
    exponent = 1;
    temp = to_base;
    while (temp < from_base) {
        temp *= to_base;
        exponent++;
        if (temp == from_base) {
            return {true, exponent, -1};
        }
    }

    return {false, 0, 0};
}


std::string to_base_n(long long num, int base) {
    if (num == 0) {
        return "0";
    }

    // For bases 2, 4, 8, 16 - we can optimize using binary grouping
    if (base == 2 || base == 4 || base == 8 || base == 16) {
        // Convert to binary first, then group bits
        std::string binary = "";
        long long temp = num;
        if (temp == 0) binary = "0";
        else {
            while (temp > 0) {
                binary = char('0' + (temp % 2)) + binary;
                temp /= 2;
            }
        }

        if (base == 2) {
            return binary;
        } else if (base == 4) {
            // Group by 2 bits
            int padding = (2 - binary.length() % 2) % 2;
            binary = std::string(padding, '0') + binary;
            std::string result = "";
            for (size_t i = 0; i < binary.length(); i += 2) {
                std::string group = binary.substr(i, 2);
                int group_val = std::stoi(group, nullptr, 2);
                result += char('0' + group_val);
            }
            return result;
        } else if (base == 8) {
            // Group by 3 bits
            int padding = (3 - binary.length() % 3) % 3;
            binary = std::string(padding, '0') + binary;
            std::string result = "";
            for (size_t i = 0; i < binary.length(); i += 3) {
                std::string group = binary.substr(i, 3);
                int group_val = std::stoi(group, nullptr, 2);
                result += char('0' + group_val);
            }
            return result;
        } else if (base == 16) {
            // Group by 4 bits
            int padding = (4 - binary.length() % 4) % 4;
            binary = std::string(padding, '0') + binary;
            std::string result = "";
            for (size_t i = 0; i < binary.length(); i += 4) {
                std::string group = binary.substr(i, 4);
                int group_val = std::stoi(group, nullptr, 2);
                if (group_val < 10) {
                    result += char('0' + group_val);
                } else {
                    result += char('A' + group_val - 10);
                }
            }
            return result;
        }
    }

    // For other bases, use standard conversion
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

std::string convert_base_direct(const std::string& number_str, int from_base, int to_base) {
    PowerRelation rel = get_power_relationship(from_base, to_base);
    if (!rel.is_power) {
        throw std::invalid_argument("Bases are not compatible for direct conversion");
    }

    // Convert to decimal first
    long long decimal = 0;
    for (int i = number_str.length() - 1, power = 0; i >= 0; i--, power++) {
        char digit = number_str[i];
        int val;
        if (digit >= '0' && digit <= '9') {
            val = digit - '0';
        } else {
            val = 10 + (toupper(digit) - 'A');
        }
        decimal += val * (long long)pow(from_base, power);
    }

    // Convert decimal to target base using direct method
    return to_base_n(decimal, to_base);
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
