# SYS - Systemy pozycyjne

## Opis problemu

Zadanie polega na zamianie podanej liczby n, która jest w systemie dziesiątkowym, na liczbę w systemie szesnastkowym (cyfry: 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F) i jedenastkowym (cyfry: 0,1,2,3,4,5,6,7,8,9,A).

## Wejście

W pierwszym wierszu wejścia znajduje się dokładnie jedna t (1 <= t <= 10000) oznaczająca liczbę zestawów danych. W każdym wierszu od 2 do t+1 znajduje się dokładnie jedna liczba całkowita n (1 <= n <= 10^6).

## Wyjście

W każdym wierszu wyjścia powinny znaleźć się dokładnie dwie liczby, pierwsza - oznaczająca podana liczbę w systemie szesnastkowym, druga - oznaczająca podana liczbę w systemie jedenastkowym.

## Przykład

### Wejście:
```
2
1263
10
```

### Wyjście:
```
4EF A49
A A
```

## Rozwiązania

Rozwiązania zostały zaimplementowane w trzech językach programowania:

- **Python**: `solutions/sys.py`
- **C++**: `solutions/sys.cpp`
- **Java**: `solutions/SYS.java`

Wszystkie rozwiązania czytają dane ze standardowego wejścia i wypisują wyniki na standardowe wyjście.

### 🔁 Optymalizacje konwersji

Rozwiązania zawierają inteligentne optymalizacje dla konwersji między kompatybilnymi systemami pozycyjnymi:

**Konwersje bezpośrednie (bez pośrednictwa systemu dziesiętnego):**

Możliwe między podstawami będącymi potęgami tej samej liczby:
- **Potęgi 2**: 2 ↔ 4 ↔ 8 ↔ 16 ↔ 32 ↔ ...
- **Potęgi 3**: 3 ↔ 9 ↔ 27 ↔ 81 ↔ ...
- **Potęgi 5**: 5 ↔ 25 ↔ 125 ↔ ...
- **Ogólnie**: jeśli base₁ = r^n i base₂ = r^m, można konwertować bezpośrednio

**Metoda wykrywania:**
```python
def get_base_root(base):
    # Znajduje najmniejszą liczbę r taką, że base = r^n
    # Np: 16 → (2, 4), 9 → (3, 2), 25 → (5, 2)
    
def can_convert_directly(base1, base2):
    # Sprawdza czy obie podstawy mają ten sam root
    # Np: 8 i 16 → TAK (oba są potęgami 2)
    #     8 i 9  → NIE (2^3 vs 3^2)
```

**Konwersje standardowe (przez system dziesiętny):**
- Wszystkie inne podstawy (np. base 11, 13, 7)

**Przykład optymalizacji:**
```
Konwersja 100₁₀:
  → Base 16 (2^4): 64  ✓ optymalizacja (grupowanie po 4 bity)
  → Base 9  (3^2): 121 ✓ optymalizacja (grupowanie po 2 "trity")
  → Base 11:       91  ✗ standardowa konwersja
```

**Demonstracje:**
- `python3 demo_optimizations.py` - optymalizacje dla potęg 2
- `python3 demo_general_conversion.py` - ogólne konwersje (2,3,5,...)
