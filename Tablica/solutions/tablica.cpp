#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <sstream>
#include <string>

/// SPOJ: TABLICA – Reverse array problem in C++17/20.
/// Reads a sequence of integers from stdin and outputs them in reverse order.
/// Uses modern C++ features: ranges, iterators, and STL algorithms.

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::vector<int> numbers;
    std::string line;

    // Read all integers from stdin (line by line)
    while (std::getline(std::cin, line)) {
        std::istringstream iss(line);
        numbers.insert(numbers.end(),
                       std::istream_iterator<int>(iss),
                       std::istream_iterator<int>());
    }

    if (numbers.empty())
        return 0;  // No input → nothing to print

    std::reverse(numbers.begin(), numbers.end());

    // Print all numbers separated by spaces
    for (size_t i = 0; i < numbers.size(); ++i) {
        if (i) std::cout << ' ';
        std::cout << numbers[i];
    }
    std::cout << '\n';

    return 0;
}
