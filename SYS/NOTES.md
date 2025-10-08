# Notatki techniczne - SYS (Systemy pozycyjne)

## Optymalizacja konwersji między systemami

### Kluczowa obserwacja

Zamiast skomplikowanych funkcji sprawdzających relacje potęg między dowolnymi podstawami, wystarczy:

**Sprawdzić czy podstawa jest potęgą dwójki!**

### Dlaczego to działa?

Dla podstaw będących potęgami 2 (2, 4, 8, 16, 32, ...):
- Każda cyfra w takiej podstawie reprezentuje stałą liczbę bitów
- Base 2 = 1 bit na cyfrę
- Base 4 = 2 bity na cyfrę (4 = 2²)
- Base 8 = 3 bity na cyfrę (8 = 2³)
- Base 16 = 4 bity na cyfrę (16 = 2⁴)

### Implementacja

#### 1. Sprawdzanie czy podstawa jest potęgą dwójki

```python
def is_power_of_two_base(base):
    return base > 1 and (base & (base - 1)) == 0
```

**Jak to działa?**
- Potęgi dwójki w binarnym: 2=10, 4=100, 8=1000, 16=10000
- Potęga dwójki minus 1: 1=01, 3=011, 7=0111, 15=01111
- AND tych dwóch liczb zawsze daje 0 dla potęg dwójki!

Przykład:
```
16 = 10000
15 = 01111
& --------
     00000 = 0  ✓ (16 jest potęgą 2)

12 = 01100
11 = 01011
& --------
     01000 ≠ 0  ✗ (12 nie jest potęgą 2)
```

#### 2. Obliczanie liczby bitów na cyfrę

```python
bits_per_digit = (base - 1).bit_length()
```

Przykłady:
- base=2: (2-1).bit_length() = 1.bit_length() = 1 bit
- base=4: (4-1).bit_length() = 3.bit_length() = 2 bity
- base=8: (8-1).bit_length() = 7.bit_length() = 3 bity
- base=16: (16-1).bit_length() = 15.bit_length() = 4 bity

### Porównanie: stary vs nowy kod

#### STARY KOD (skomplikowany):
```python
def get_power_relationship(from_base, to_base):
    # 50+ linii kodu sprawdzającego relacje między podstawami
    # Pętle, warunki, sprawdzanie w obie strony...
    ...

def is_power_of(base1, base2):
    # Kolejne 20+ linii...
    ...
```

#### NOWY KOD (prosty):
```python
def is_power_of_two_base(base):
    return base > 1 and (base & (base - 1)) == 0
```

### Korzyści uproszczenia

1. **Czytelność**: 1 linia zamiast 70+ linii
2. **Wydajność**: O(1) zamiast O(log n) pętli
3. **Prostota**: Jeden warunek zamiast złożonej logiki
4. **Uniwersalność**: Działa dla wszystkich potęg dwójki, nie tylko 2,4,8,16

### Algorytm konwersji

```
Dla podstawy będącej potęgą 2:
1. Oblicz bits_per_digit = log2(base)
2. Konwertuj liczbę do binarnego
3. Dopełnij zerami do wielokrotności bits_per_digit
4. Grupuj bity po bits_per_digit
5. Każdą grupę konwertuj na cyfrę w docelowej podstawie

Dla innych podstaw:
- Użyj standardowej metody dzielenia modulo
```

### Przykład działania

```
255₁₀ → 16₁₆:

1. is_power_of_two_base(16) = True ✓
2. bits_per_digit = 4
3. binary = "11111111"
4. padding = 0 (już jest wielokrotnością 4)
5. Grupowanie: "1111" "1111"
6. Konwersja: 15₁₀=F, 15₁₀=F
7. Wynik: "FF"
```

### Wnioski

Czasami najprostsze rozwiązanie jest najlepsze. Zamiast budować skomplikowany system sprawdzania relacji między podstawami, wystarczy jedna elegancka obserwacja: **jeśli podstawa jest potęgą dwójki, możemy użyć optymalizacji**.

To znacznie upraszcza kod i czyni go bardziej zrozumiałym, bez utraty funkcjonalności!
