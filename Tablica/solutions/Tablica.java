import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

/**
 * SPOJ: TABLICA – Reverse array problem (Java 8+)
 *
 * <p>Reads a sequence of integers from stdin and outputs them in reverse order.
 * 
 * <p>Time Complexity: O(n) where n is the number of integers
 * <p>Space Complexity: O(n) for storing the input array
 * 
 * <p>Features:
 * <ul>
 *   <li>Functional programming with Stream API</li>
 *   <li>Efficient I/O with BufferedReader</li>
 *   <li>Comprehensive error handling</li>
 *   <li>Graceful handling of edge cases</li>
 * </ul>
 */
public final class Tablica {

    private Tablica() {
        // Prevent instantiation of utility class
        throw new AssertionError("Utility class should not be instantiated");
    }

    /**
     * Main entry point that reads input, reverses numbers, and outputs result.
     *
     * @param args command line arguments (unused)
     */
    public static void main(String[] args) {
        try {
            String input = readAllInput();
            
            if (input == null || input.trim().isEmpty()) {
                return; // No data to process
            }

            List<Integer> numbers = parseIntegers(input.trim());
            
            if (numbers.isEmpty()) {
                return; // Empty result after parsing
            }

            String output = reverseAndFormat(numbers);
            System.out.println(output);

        } catch (NumberFormatException e) {
            System.err.println("Error: Input must contain only integers.");
            System.exit(1);
        } catch (OutOfMemoryError e) {
            System.err.println("Error: Input too large to process.");
            System.exit(1);
        } catch (IOException e) {
            System.err.println("Error: Failed to read input.");
            System.exit(1);
        } catch (Exception e) {
            System.err.println("Error: Unexpected error - " + e.getClass().getSimpleName());
            System.exit(1);
        }
    }

    /**
     * Reads all input from stdin using BufferedReader for efficiency.
     * 
     * @return All input as a single string
     * @throws IOException if reading fails
     */
    private static String readAllInput() throws IOException {
        StringBuilder sb = new StringBuilder();
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(System.in))) {
            String line;
            while ((line = reader.readLine()) != null) {
                sb.append(line).append(' ');
            }
        }
        return sb.toString();
    }

    /**
     * Parses whitespace-separated integers from input string.
     * 
     * @param input Input string containing integers
     * @return List of parsed integers
     * @throws NumberFormatException if any token cannot be parsed
     */
    private static List<Integer> parseIntegers(String input) {
        return Stream.of(input.split("\\s+"))
                .filter(s -> !s.isEmpty())
                .map(Integer::parseInt)
                .collect(Collectors.toList());
    }

    /**
     * Reverses a list of integers and formats as space-separated string.
     * 
     * @param numbers List of integers to reverse
     * @return Space-separated string of reversed integers
     */
    private static String reverseAndFormat(List<Integer> numbers) {
        Collections.reverse(numbers);
        return numbers.stream()
                .map(String::valueOf)
                .collect(Collectors.joining(" "));
    }
}
