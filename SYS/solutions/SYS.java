import java.util.Scanner;

public class SYS {
    public static boolean isPowerOfTwoBase(int base) {
        // Sprawdź czy podstawa jest potęgą dwójki (2, 4, 8, 16, 32, ...)
        return base > 1 && (base & (base - 1)) == 0;
    }

    public static int countBitsPerDigit(int base) {
        // Oblicz ile bitów reprezentuje jedna cyfra w danej podstawie
        // base = 2^bits → bits = log2(base)
        int bits = 0;
        int temp = base;
        while (temp > 1) {
            temp >>= 1;
            bits++;
        }
        return bits;
    }

    public static String toBaseN(long num, int base) {
        if (num == 0) {
            return "0";
        }

        // Optymalizacja: dla potęg dwójki używamy grupowania bitów
        if (isPowerOfTwoBase(base)) {
            // Oblicz ile bitów reprezentuje jedna cyfra
            int bitsPerDigit = countBitsPerDigit(base);
            
            // Konwertuj do binarnego
            StringBuilder binary = new StringBuilder();
            long temp = num;
            while (temp > 0) {
                binary.insert(0, (temp % 2));
                temp /= 2;
            }
            String binaryStr = binary.toString();
            
            // Dopełnij zerami do wielokrotności bitsPerDigit
            int padding = (bitsPerDigit - binaryStr.length() % bitsPerDigit) % bitsPerDigit;
            String paddedBinary = "0".repeat(padding) + binaryStr;
            
            // Grupuj bity i konwertuj każdą grupę na cyfrę
            StringBuilder result = new StringBuilder();
            for (int i = 0; i < paddedBinary.length(); i += bitsPerDigit) {
                String group = paddedBinary.substring(i, i + bitsPerDigit);
                int groupVal = Integer.parseInt(group, 2);
                if (groupVal < 10) {
                    result.append(groupVal);
                } else {
                    result.append((char)('A' + groupVal - 10));
                }
            }
            return result.toString();
        }

        // Standardowa konwersja dla innych podstaw
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
