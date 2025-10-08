#include <iostream>
#include <string>
#include <algorithm>

std::string to_base_n(long long num, int base) {
    if (num == 0) {
        return "0";
    }

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
