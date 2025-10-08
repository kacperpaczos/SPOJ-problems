#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <sstream>
#include <string>
#include <stdexcept>
#include <limits>

/// SPOJ: TABLICA – Reverse array problem in C++17/20.
///
/// Reads a sequence of integers from stdin and outputs them in reverse order.
///
/// Time Complexity: O(n) where n is the number of integers
/// Space Complexity: O(n) for storing the input array
///
/// Features:
/// - Modern C++ idioms (RAII, STL algorithms, iterators)
/// - Fast I/O with sync_with_stdio(false)
/// - Robust error handling
/// - Memory-efficient processing

namespace {

/// Reads all integers from stdin into a vector.
/// @return Vector containing all parsed integers
/// @throws std::bad_alloc if memory allocation fails
std::vector<int> read_integers() {
    std::vector<int> numbers;
    numbers.reserve(1024);  // Reserve space to reduce reallocations
    
    std::string line;
    while (std::getline(std::cin, line)) {
        if (line.empty()) continue;
        
        std::istringstream iss(line);
        int num;
        
        while (iss >> num) {
            numbers.push_back(num);
        }
        
        // Check for parsing errors (non-integer input)
        if (iss.fail() && !iss.eof()) {
            std::cerr << "Error: Input must contain only integers.\n";
            std::exit(1);
        }
    }
    
    return numbers;
}

/// Prints integers in reverse order, space-separated.
/// @param numbers Vector of integers to print in reverse
void print_reversed(const std::vector<int>& numbers) {
    if (numbers.empty()) return;
    
    // Print in reverse order without creating reversed copy
    for (auto it = numbers.rbegin(); it != numbers.rend(); ++it) {
        if (it != numbers.rbegin()) std::cout << ' ';
        std::cout << *it;
    }
    std::cout << '\n';
}

}  // anonymous namespace

int main() {
    try {
        // Optimize I/O performance
        std::ios::sync_with_stdio(false);
        std::cin.tie(nullptr);
        
        // Read all integers
        std::vector<int> numbers = read_integers();
        
        // Handle empty input
        if (numbers.empty()) {
            return 0;
        }
        
        // Print in reverse order
        print_reversed(numbers);
        
        return 0;
        
    } catch (const std::bad_alloc&) {
        std::cerr << "Error: Input too large to process.\n";
        return 1;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << '\n';
        return 1;
    } catch (...) {
        std::cerr << "Error: Unknown error occurred.\n";
        return 1;
    }
}
