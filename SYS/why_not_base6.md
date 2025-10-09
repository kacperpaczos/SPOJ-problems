# Dlaczego base 6 NIE ma optymalizacji?

## Kluczowa różnica

### ✅ Podstawy z optymalizacją (potęgi jednej liczby):
```
4  = 2²     (potęga 2)
8  = 2³     (potęga 2)
9  = 3²     (potęga 3)
16 = 2⁴     (potęga 2)
25 = 5²     (potęga 5)
27 = 3³     (potęga 3)
```

### ✗ Podstawy BEZ optymalizacji (iloczyny różnych liczb):
```
6  = 2 × 3      (iloczyn 2 i 3)
10 = 2 × 5      (iloczyn 2 i 5)
12 = 2² × 3     (iloczyn potęgi 2 i 3)
14 = 2 × 7      (iloczyn 2 i 7)
15 = 3 × 5      (iloczyn 3 i 5)
```

## Dlaczego to ma znaczenie?

### Dla base 16 (2⁴) - DZIAŁA ✓
```
Każda cyfra hex = dokładnie 4 bity:
  0 = 0000
  1 = 0001
  F = 1111
  
Konwersja 255₁₀ → FF₁₆:
  255₁₀ = 11111111₂
  Grupuj po 4: [1111][1111]
  Konwertuj:   [F]   [F]
  Wynik: FF
```

### Dla base 6 (2×3) - NIE DZIAŁA ✗
```
Każda cyfra w base 6 ≠ stała liczba bitów/tritów

Cyfra 5₆ w binarnym:  101₂   (3 bity)
Cyfra 4₆ w binarnym:  100₂   (3 bity)
Cyfra 3₆ w binarnym:   11₂   (2 bity!)
Cyfra 2₆ w binarnym:   10₂   (2 bity!)

Nie ma stałej wielkości grupy! 
Nie można używać prostego grupowania.
```

## Matematyczne wyjaśnienie

**Warunek optymalizacji**: base = r^n

- Jeśli `base = r^n`, to każda cyfra w base reprezentuje **dokładnie n cyfr** w systemie r
- Dla base 6 = 2×3, nie ma takiego r i n
- 6 nie jest potęgą 2: 2¹=2, 2²=4, 2³=8 (brak 6)
- 6 nie jest potęgą 3: 3¹=3, 3²=9 (brak 6)
- 6 nie jest potęgą żadnej innej liczby

## Przykłady w praktyce

### Base 4 (2²) - można grupować po 2 bity:
```
100₁₀ = 1100100₂
Grupuj:  1 10 01 00
Base 4:  1  2  1  0  → 1210₄ ✓
```

### Base 9 (3²) - można grupować po 2 trity:
```
100₁₀ = 10201₃
Grupuj:  1 02 01
Base 9:  1  2  1  → 121₉ ✓
```

### Base 6 (2×3) - NIE można grupować:
```
100₁₀ = 1100100₂
Nie ma stałej wielkości grupy dla base 6!
Trzeba użyć standardowej konwersji: 100 ÷ 6 = 16 r 4
                                     16 ÷ 6 = 2 r 4
                                      2 ÷ 6 = 0 r 2
Wynik: 244₆ (czytając reszty od dołu)
```

## Podsumowanie

| Podstawa | Rozkład | Optymalizacja? | Dlaczego? |
|----------|---------|----------------|-----------|
| 4 | 2² | ✓ TAK | Potęga 2 → grupuj po 2 bity |
| 6 | 2×3 | ✗ NIE | Iloczyn różnych liczb |
| 8 | 2³ | ✓ TAK | Potęga 2 → grupuj po 3 bity |
| 9 | 3² | ✓ TAK | Potęga 3 → grupuj po 2 trity |
| 10 | 2×5 | ✗ NIE | Iloczyn różnych liczb |
| 12 | 2²×3 | ✗ NIE | Iloczyn różnych liczb |
| 16 | 2⁴ | ✓ TAK | Potęga 2 → grupuj po 4 bity |
| 25 | 5² | ✓ TAK | Potęga 5 → grupuj po 2 "pentity" |
| 27 | 3³ | ✓ TAK | Potęga 3 → grupuj po 3 trity |

## Wniosek

Base 6 używa **standardowej konwersji** (dzielenie modulo), ponieważ:
1. 6 = 2 × 3 (iloczyn różnych liczb pierwszych)
2. Nie jest potęgą żadnej mniejszej liczby
3. Nie ma stałej wielkości grupy dla grupowania cyfr
4. Optymalizacja grupowania nie jest możliwa
