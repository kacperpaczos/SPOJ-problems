# Notatki techniczne - SYS (Systemy pozycyjne)

## Optymalizacja konwersji między systemami

### Kluczowa obserwacja

Konwersje bezpośrednie są możliwe między podstawami będącymi **potęgami tej samej liczby**!

### Dlaczego to działa?

**Dla potęg 2** (2, 4, 8, 16, 32, ...):
- Każda cyfra w takiej podstawie reprezentuje stałą liczbę bitów
- Base 2 = 1 bit na cyfrę
- Base 4 = 2 bity na cyfrę (4 = 2²)
- Base 8 = 3 bity na cyfrę (8 = 2³)
- Base 16 = 4 bity na cyfrę (16 = 2⁴)

**Dla potęg 3** (3, 9, 27, 81, ...):
- Każda cyfra reprezentuje stałą liczbę "tritów" (cyfr w base 3)
- Base 3 = 1 trit na cyfrę
- Base 9 = 2 trity na cyfrę (9 = 3²)
- Base 27 = 3 trity na cyfrę (27 = 3³)

**Ogólnie**: Jeśli base = r^n, każda cyfra = n cyfr w systemie o podstawie r

### Implementacja

#### 1. Znajdowanie "root" podstawy (get_base_root)

```python
def get_base_root(base):
    """Znajdź najmniejszą podstawę r, której potęgą jest base.
    Zwraca (root, exponent) gdzie base = root^exponent
    """
    for root in range(2, int(base ** 0.5) + 2):
        exp = 1
        power = root
        while power < base:
            power *= root
            exp += 1
            if power == base:
                return root, exp
    return base, 1  # base jest liczbą pierwszą
```

**Przykłady:**
- 16 → (2, 4) bo 16 = 2⁴
- 9 → (3, 2) bo 9 = 3²
- 27 → (3, 3) bo 27 = 3³
- 25 → (5, 2) bo 25 = 5²
- 11 → (11, 1) bo 11 jest liczbą pierwszą

#### 2. Sprawdzanie kompatybilności (can_convert_directly)

```python
def can_convert_directly(base1, base2):
    root1, exp1 = get_base_root(base1)
    root2, exp2 = get_base_root(base2)
    return root1 == root2  # Ten sam root = kompatybilne!
```

**Przykłady:**
- can_convert_directly(8, 16) → True (oba: root=2)
- can_convert_directly(9, 27) → True (oba: root=3)
- can_convert_directly(8, 9) → False (root=2 vs root=3)

#### 3. Optymalizacja dla potęg dwójki (szybka ścieżka)

```python
def is_power_of_two_base(base):
    return base > 1 and (base & (base - 1)) == 0
```

**Trick bitowy:**
- Potęgi dwójki: 2=10, 4=100, 8=1000, 16=10000
- Minus 1: 1=01, 3=011, 7=0111, 15=01111
- AND = 0 tylko dla potęg dwójki!

```
16 = 10000        12 = 01100
15 = 01111        11 = 01011
& --------        & --------
     00000 = 0 ✓       01000 ≠ 0 ✗
```

#### 4. Obliczanie cyfr na jednostkę

```python
# Dla potęg 2 (szybka ścieżka):
bits_per_digit = (base - 1).bit_length()

# Ogólnie:
digits_per_unit = exponent  # gdzie base = root^exponent
```

### Porównanie podejść

#### Podejście 1: Tylko potęgi dwójki (najprostsze)
```python
def is_power_of_two_base(base):
    return base > 1 and (base & (base - 1)) == 0
```
✓ Bardzo szybkie (O(1))  
✓ Proste  
✗ Działa tylko dla potęg 2

#### Podejście 2: Dowolne potęgi (uniwersalne)
```python
def get_base_root(base):
    for root in range(2, int(base ** 0.5) + 2):
        # ... sprawdź czy base = root^n
    return base, 1

def can_convert_directly(base1, base2):
    return get_base_root(base1)[0] == get_base_root(base2)[0]
```
✓ Działa dla wszystkich potęg (2,3,5,...)  
✓ Nadal proste (~20 linii)  
✗ Wolniejsze (O(√n))

### Korzyści nad starym kodem

**Stary kod**: 70+ linii sprawdzających relacje w obie strony  
**Nowy kod**: ~20 linii znajdowania wspólnego root

1. **Czytelność**: Jasna logika "znajdź root, porównaj"
2. **Uniwersalność**: Działa dla 2,3,5,7... nie tylko 2
3. **Prostota**: Jedna koncepcja zamiast wielu przypadków
4. **Łatwość rozbudowy**: Łatwo dodać cache dla często używanych podstaw

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
