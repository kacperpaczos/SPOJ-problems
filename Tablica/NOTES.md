# TABLICA - Notatki Techniczne

## Python Implementation

### Techniki Programistyczne
- **Modular design** - funkcje: `parse_integers()`, `reverse_and_format()`, `handle_error()`, `main()`
- **Type hints** - `List[int]`, `NoReturn`, `-> None`, `-> str`
- **List comprehension** - `[int(token) for token in data.split()]`
- **Built-in functions** - `reversed()`, `map()`, `str.join()`
- **Functional programming** - `map(str, reversed(numbers))`
- **Exception hierarchy** - `ValueError`, `MemoryError`, `KeyboardInterrupt`, `Exception`
- **Error handling** - try/except/multiple handlers
- **Exit codes** - 0 (success), 1 (error), 130 (SIGINT)
- **Stream separation** - stdout vs stderr
- **Google-style docstrings** - Args, Returns, Raises
- **String methods** - `strip()`, `split()`
- **Early return pattern** - guard clauses dla empty input

### Koncepcje Teoretyczne
- Single Responsibility Principle (SRP)
- Separation of Concerns
- Defensive programming
- Fail-fast principle
- DRY (Don't Repeat Yourself)
- KISS (Keep It Simple, Stupid)
- Graceful degradation

---

## Java Implementation

### Techniki Programistyczne
- **Utility class pattern** - `final class`, private constructor, `AssertionError`
- **BufferedReader** - wydajne I/O zamiast Scanner
- **Try-with-resources** - automatic resource management
- **Stream API** - `Stream.of()`, `map()`, `collect()`, `filter()`
- **Method references** - `Integer::parseInt`, `String::valueOf`
- **Collectors** - `Collectors.toList()`, `Collectors.joining()`
- **Collections.reverse()** - in-place reversal
- **StringBuilder** - efficient string concatenation
- **Exception handling** - `NumberFormatException`, `OutOfMemoryError`, `IOException`
- **Javadoc** - `@param`, `@return`, `@throws`, HTML tags (`<p>`, `<ul>`, `<li>`)
- **Method extraction** - `readAllInput()`, `parseIntegers()`, `reverseAndFormat()`
- **Null safety** - `input == null` checks
- **String operations** - `trim()`, `isEmpty()`, `split("\\s+")`
- **Regex** - `\\s+` dla whitespace

### Koncepcje Teoretyczne
- Immutability (final class)
- Encapsulation
- Information hiding
- Functional programming paradigm
- Lazy evaluation (streams)
- Resource management (RAII-like)
- Exception safety

---

## C++ Implementation

### Techniki Programistyczne
- **Anonymous namespace** - `namespace { }` dla internal linkage
- **Fast I/O** - `sync_with_stdio(false)`, `cin.tie(nullptr)`
- **Memory optimization** - `vector.reserve(1024)`
- **Reverse iterators** - `rbegin()`, `rend()` - zero-copy
- **STL algorithms** - `std::getline()`, `std::istringstream`
- **RAII** - automatic resource management
- **Exception handling** - `std::bad_alloc`, `std::exception`, catch-all `(...)`
- **Move semantics** - implicit w return
- **Const correctness** - `const std::vector<int>&`
- **Range-based for** - `for (auto it = ...)`
- **Stream operators** - `>>` dla parsing
- **Stream state checking** - `iss.fail()`, `iss.eof()`
- **Doxygen comments** - `///`, `@param`, `@return`, `@throws`
- **Error codes** - return 0/1
- **Namespace usage** - anonymous namespace dla enkapsulacji

### Koncepcje Teoretyczne
- Zero-overhead abstraction
- RAII (Resource Acquisition Is Initialization)
- Exception safety guarantees
- Memory locality
- Cache-friendly operations
- Move semantics
- Copy elision
- Internal linkage

---

## Optymalizacje Wydajnościowe

### Python
- `sys.stdin.read()` - jednorazowe czytanie
- `reversed()` - iterator, nie kopia
- `map()` - lazy evaluation
- `str.join()` - wydajniejsze niż konkatenacja

### Java
- `BufferedReader` - buforowane I/O
- `StringBuilder` - mutable string building
- Stream pipeline - lazy evaluation
- `Collections.reverse()` - in-place O(n)

### C++
- `sync_with_stdio(false)` - 2-3x szybsze I/O
- `cin.tie(nullptr)` - no flush overhead
- `reserve()` - avoid reallocations
- Reverse iterators - no copy, no reverse
- Move semantics - avoid copies

---

## Zakresy Testów

### 1. Basic Functionality (5 tests)
- Simple reversal
- Single element
- Two elements
- Already reversed
- Identical elements

**Teoria:** Podstawowe przypadki użycia, happy path

### 2. Edge Cases (8 tests)
- Empty input
- Whitespace-only
- Zero value
- Multiple zeros
- Negative numbers
- Mixed positive/negative
- Extra spaces
- Leading/trailing spaces

**Teoria:** Boundary conditions, input validation, whitespace handling

### 3. Performance (7 tests)
- 100 elements
- 1,000 elements
- 10,000 elements
- INT_MAX/INT_MIN (2^31-1, -2^31)
- Alternating patterns
- Random values
- Palindromes

**Teoria:** Scalability, stress testing, boundary values, time complexity O(n)

### 4. Error Handling (7 tests - Python)
- Letters in input
- Mixed valid/invalid
- Special characters
- Float numbers
- Comma-separated
- Plus sign
- Negative sign

**Teoria:** Input validation, error reporting, exit codes, stderr usage

### 5. Advanced Edge Cases (11 tests)
- 50,000 elements (stress)
- Maximum 32-bit integers
- All negative numbers
- Repeating patterns
- Fibonacci sequence
- Powers of two
- Prime numbers
- Sparse ranges
- Mixed magnitudes
- Newline-separated
- Mixed separators (space/tab/newline)

**Teoria:** Extreme inputs, mathematical sequences, separator handling, production scenarios

---

## Wzorce Projektowe

### Python
- **Strategy Pattern** - różne handlery błędów
- **Template Method** - main() jako szablon
- **Guard Clause** - early returns

### Java
- **Utility Class Pattern** - static methods, no instantiation
- **Builder Pattern** - StringBuilder
- **Factory Method** - Stream.of()

### C++
- **RAII Pattern** - automatic cleanup
- **Namespace Pattern** - anonymous namespace
- **Iterator Pattern** - reverse iterators

---

## Koncepcje Algorytmiczne

### Złożoność
- **Time:** O(n) - linear
- **Space:** O(n) - input storage
- **I/O:** O(n) - read once, write once

### Operacje
- **Reading:** O(n) - scan input
- **Parsing:** O(n) - split/tokenize
- **Reversing:** O(n) - in-place or iterator
- **Output:** O(n) - format and print

### Optymalizacje
- **Single pass** - read all at once
- **Lazy evaluation** - iterators, streams
- **Memory reservation** - avoid reallocations
- **Fast I/O** - buffering, sync disable

---

## Best Practices

### Code Quality
- DRY - no duplication
- KISS - simple solutions
- YAGNI - no over-engineering
- SOLID principles
- Clean Code principles

### Documentation
- Google style guides
- Comprehensive docstrings/Javadoc/Doxygen
- Complexity analysis
- Usage examples

### Error Handling
- Fail-fast
- Meaningful error messages
- Proper exit codes
- stderr for errors

### Testing
- Unit tests
- Edge case coverage
- Stress tests
- Error path testing
- 38 comprehensive tests

---

## Kluczowe Słowa

**Python:** type hints, list comprehension, reversed(), map(), exception hierarchy, docstrings, exit codes, modular design, functional programming

**Java:** Stream API, BufferedReader, utility class, try-with-resources, method references, Collectors, Javadoc, exception handling, functional paradigm

**C++:** anonymous namespace, fast I/O, reverse iterators, RAII, STL algorithms, exception safety, Doxygen, const correctness, move semantics, zero-copy

**Testing:** basic functionality, edge cases, performance, error handling, advanced scenarios, 38 tests, stress testing, boundary values

**Patterns:** SOLID, DRY, KISS, YAGNI, strategy, template method, utility class, RAII, iterator

**Complexity:** O(n) time, O(n) space, single pass, lazy evaluation, memory optimization

**Quality:** Google standards, comprehensive docs, defensive programming, graceful degradation, proper error reporting
