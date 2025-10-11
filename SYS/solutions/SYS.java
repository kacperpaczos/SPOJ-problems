import java.util.Scanner;

public class SYS {
    // Zwraca (root, exponent) dla base = root^exponent; jeśli nie jest potęgą jednej liczby pierwszej: (base, 1)
    public static int[] getBaseRoot(int base) {
        if (base <= 1) return new int[]{base, 1};

        int firstFactor = 0;
        int exponent = 0;
        int n = base;

        if ((n % 2) == 0) {
            firstFactor = 2;
            while ((n % 2) == 0) {
                exponent++;
                n /= 2;
            }
        }

        if (firstFactor != 0 && n > 1) return new int[]{base, 1};

        if (firstFactor == 0) {
            int d = 3;
            while ((long)d * d <= n) {
                if ((n % d) == 0) {
                    firstFactor = d;
                    while ((n % d) == 0) {
                        exponent++;
                        n /= d;
                    }
                    break;
                }
                d += 2;
            }
        }

        if (n > 1) {
            if (firstFactor != 0) return new int[]{base, 1};
            return new int[]{n, 1};
        }

        return new int[]{ firstFactor != 0 ? firstFactor : base, exponent > 0 ? exponent : 1 };
    }

    private static char digitToChar(int digit) {
        return (char)(digit < 10 ? ('0' + digit) : ('A' + digit - 10));
    }

    public static String toBaseN(long num, int base) {
        if (num == 0) return "0";

        int[] rootExp = getBaseRoot(base);
        int root = rootExp[0];
        int exp = rootExp[1];

        // Optymalizacja: potęgi 2 → operacje bitowe
        if (root == 2 && exp > 1) {
            int bitsPerDigit = exp;
            int mask = (1 << bitsPerDigit) - 1;
            StringBuilder result = new StringBuilder();
            long n = num;
            while (n > 0) {
                int groupVal = (int)(n & mask);
                result.append(digitToChar(groupVal));
                n >>= bitsPerDigit;
            }
            return result.reverse().toString();
        }

        // Standardowa konwersja
        StringBuilder result = new StringBuilder();
        long n = num;
        while (n > 0) {
            int remainder = (int)(n % base);
            result.append(digitToChar(remainder));
            n /= base;
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
