#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <sstream>

/// SPOJ TABLICA problem solution in C++17/20.
/// Reads a sequence of integers from stdin and outputs them in reverse order.
/// Uses modern C++ features like std::vector, std::reverse, and iterator-based copying.
int main() {
    std::vector<int> numbers;
    std::string line;

    // Read all input data from stdin line by line
    while (std::getline(std::cin, line)) {
        std::istringstream iss(line);
        std::copy(std::istream_iterator<int>(iss),
                  std::istream_iterator<int>(),
                  std::back_inserter(numbers));
    }

    // Reverse the order using std::reverse algorithm
    std::reverse(numbers.begin(), numbers.end());

    // Output numbers with space separation using range-based for loop
    for (size_t i = 0; i < numbers.size(); ++i) {
        if (i > 0) std::cout << " ";
        std::cout << numbers[i];
    }
    std::cout << std::endl;

    return 0;
}
