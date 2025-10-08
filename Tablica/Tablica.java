import java.util.*;
import java.util.stream.Collectors;

/**
 * SPOJ TABLICA problem solution in Java 8+.
 *
 * <p>Reads a sequence of integers from stdin and outputs them in reverse order.
 * Uses Java 8+ Stream API and Collections utilities for maximum efficiency.
 */
public class Tablica {
    /**
     * Main entry point that reads input, reverses numbers, and outputs result.
     *
     * @param args command line arguments (unused)
     */
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            // Read all numbers using Stream API and split by whitespace
            List<Integer> numbers = Arrays.stream(scanner.nextLine().split("\\s+"))
                    .map(Integer::valueOf)
                    .collect(Collectors.toList());

            // Reverse the order using Collections.reverse
            Collections.reverse(numbers);

            // Output using Stream API with space separation
            System.out.println(numbers.stream()
                    .map(Object::toString)
                    .collect(Collectors.joining(" ")));
        }
    }
}
