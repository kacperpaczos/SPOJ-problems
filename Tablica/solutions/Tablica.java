import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * SPOJ: TABLICA – Reverse array problem (Java 8+)
 *
 * Reads a sequence of integers from stdin and outputs them in reverse order.
 */
public class Tablica {

    /**
     * Main entry point that reads input, reverses numbers, and outputs result.
     *
     * @param args command line arguments (unused)
     */
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            // Read all input (can handle multiple lines)
            String input = readAllInput(scanner).trim();

            if (input.isEmpty()) {
                return; // no data to process
            }

            // Parse numbers and reverse
            List<Integer> numbers = Stream.of(input.split("\\s+"))
                    .map(Integer::parseInt)
                    .collect(Collectors.toList());

            Collections.reverse(numbers);

            // Output reversed list
            String output = numbers.stream()
                    .map(String::valueOf)
                    .collect(Collectors.joining(" "));
            System.out.println(output);

        } catch (NumberFormatException e) {
            System.err.println("Error: Input must contain only integers.");
        }
    }

    /**
     * Reads all input from scanner until EOF.
     */
    private static String readAllInput(Scanner scanner) {
        StringBuilder sb = new StringBuilder();
        while (scanner.hasNextLine()) {
            sb.append(scanner.nextLine()).append(' ');
        }
        return sb.toString();
    }
}
