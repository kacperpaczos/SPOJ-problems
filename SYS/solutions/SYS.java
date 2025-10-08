import java.util.Scanner;

public class SYS {
    public static String toBaseN(long num, int base) {
        if (num == 0) {
            return "0";
        }

        StringBuilder result = new StringBuilder();
        while (num > 0) {
            int remainder = (int)(num % base);
            if (remainder < 10) {
                result.append(remainder);
            } else {
                result.append((char)('A' + remainder - 10));
            }
            num /= base;
        }

        return result.reverse().toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        for (int i = 0; i < t; i++) {
            long n = scanner.nextLong();
            String hexResult = toBaseN(n, 16).toUpperCase();
            String undecimalResult = toBaseN(n, 11).toUpperCase();
            System.out.println(hexResult + " " + undecimalResult);
        }

        scanner.close();
    }
}
