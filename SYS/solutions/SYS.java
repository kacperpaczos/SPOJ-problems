import java.util.Scanner;

public class SYS {
    public static boolean isPowerOf(int base1, int base2) {
        if (base1 == 1 || base2 == 1) return false;
        if (base1 == base2) return true;

        // Check if base1 is power of base2
        long temp = base2;
        while (temp < base1) {
            temp *= base2;
            if (temp == base1) return true;
        }

        // Check if base2 is power of base1
        temp = base1;
        while (temp < base2) {
            temp *= base1;
            if (temp == base2) return true;
        }

        return false;
    }

    public static class PowerRelation {
        public boolean isPower;
        public int exponent;
        public int direction; // 0: same, 1: toBase = fromBase^exp, -1: fromBase = toBase^exp

        public PowerRelation(boolean isPower, int exponent, int direction) {
            this.isPower = isPower;
            this.exponent = exponent;
            this.direction = direction;
        }
    }

    public static PowerRelation getPowerRelationship(int fromBase, int toBase) {
        if (fromBase == toBase) {
            return new PowerRelation(true, 1, 0);
        }

        // Check if toBase is power of fromBase
        int exponent = 1;
        long temp = fromBase;
        while (temp < toBase) {
            temp *= fromBase;
            exponent++;
            if (temp == toBase) {
                return new PowerRelation(true, exponent, 1);
            }
        }

        // Check if fromBase is power of toBase
        exponent = 1;
        temp = toBase;
        while (temp < fromBase) {
            temp *= toBase;
            exponent++;
            if (temp == fromBase) {
                return new PowerRelation(true, exponent, -1);
            }
        }

        return new PowerRelation(false, 0, 0);
    }

    public static String convertBaseDirect(String numberStr, int fromBase, int toBase) {
        PowerRelation rel = getPowerRelationship(fromBase, toBase);
        if (!rel.isPower) {
            throw new IllegalArgumentException("Bases are not compatible for direct conversion");
        }

        // Convert to decimal first
        long decimal = 0;
        for (int i = numberStr.length() - 1, power = 0; i >= 0; i--, power++) {
            char digit = numberStr.charAt(i);
            int val;
            if (Character.isDigit(digit)) {
                val = Character.getNumericValue(digit);
            } else {
                val = 10 + (Character.toUpperCase(digit) - 'A');
            }
            decimal += val * (long)Math.pow(fromBase, power);
        }

        // Convert decimal to target base using direct method
        return toBaseN(decimal, toBase);
    }

    public static String toBaseN(long num, int base) {
        if (num == 0) {
            return "0";
        }

        // For bases 2, 4, 8, 16 - we can optimize using binary grouping
        if (base == 2 || base == 4 || base == 8 || base == 16) {
            // Convert to binary first, then group bits
            StringBuilder binary = new StringBuilder();
            long temp = num;
            if (temp == 0) {
                binary.append('0');
            } else {
                while (temp > 0) {
                    binary.insert(0, (temp % 2));
                    temp /= 2;
                }
            }
            String binaryStr = binary.toString();

            if (base == 2) {
                return binaryStr;
            } else if (base == 4) {
                // Group by 2 bits
                int padding = (2 - binaryStr.length() % 2) % 2;
                String paddedBinary = "0".repeat(padding) + binaryStr;
                StringBuilder result = new StringBuilder();
                for (int i = 0; i < paddedBinary.length(); i += 2) {
                    String group = paddedBinary.substring(i, i + 2);
                    int groupVal = Integer.parseInt(group, 2);
                    result.append(groupVal);
                }
                return result.toString();
            } else if (base == 8) {
                // Group by 3 bits
                int padding = (3 - binaryStr.length() % 3) % 3;
                String paddedBinary = "0".repeat(padding) + binaryStr;
                StringBuilder result = new StringBuilder();
                for (int i = 0; i < paddedBinary.length(); i += 3) {
                    String group = paddedBinary.substring(i, i + 3);
                    int groupVal = Integer.parseInt(group, 2);
                    result.append(groupVal);
                }
                return result.toString();
            } else if (base == 16) {
                // Group by 4 bits
                int padding = (4 - binaryStr.length() % 4) % 4;
                String paddedBinary = "0".repeat(padding) + binaryStr;
                StringBuilder result = new StringBuilder();
                for (int i = 0; i < paddedBinary.length(); i += 4) {
                    String group = paddedBinary.substring(i, i + 4);
                    int groupVal = Integer.parseInt(group, 2);
                    if (groupVal < 10) {
                        result.append(groupVal);
                    } else {
                        result.append((char)('A' + groupVal - 10));
                    }
                }
                return result.toString();
            }
        }

        // For other bases, use standard conversion
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
