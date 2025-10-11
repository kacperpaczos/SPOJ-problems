# Teoria Konwersji Systemów Pozycyjnych

## Podstawa Teoretyczna

### Systemy Pozycyjne
System pozycyjny o podstawie `b` reprezentuje liczby jako sumę cyfr przemnożonych przez potęgi podstawy:

```
n = ∑(dᵢ × bⁱ)
```

gdzie `dᵢ ∈ [0, b-1]` są cyframi, a `b` jest podstawą systemu.

## Optymalizacje Konwersji

### Warunek Optymalizacji
Konwersja między dwoma podstawami może być zoptymalizowana gdy:

**Warunek konieczny:** Obie podstawy są potęgami tej samej liczby pierwszej.

Jeśli `base₁ = rᵃ` i `base₂ = rᵇ`, gdzie `r` jest liczbą pierwszą, to istnieje bezpośrednia konwersja przez grupowanie.

### Mechanizm Grupowania

**Zasada:** Każda cyfra w podstawie wyższej odpowiada stałej liczbie cyfr w podstawie niższej.

Dla `B₁ = rᵃ` i `B₂ = rᵇ`, gdzie `a > b`:
- Każda cyfra w `B₁` odpowiada dokładnie `a/b` cyfrom w `B₂`
- Konwersja sprowadza się do grupowania i bezpośredniej transformacji grup

## Złożoność Algorytmiczna

### Metoda Standardowa
- **Złożoność:** O(log₇ n) dla konwersji do podstawy 7
- **Operacje:** Dzielenie modulo, rekurencyjne dzielenie
- **Zalety:** Uniwersalna, działa dla wszystkich podstaw

### Metoda Zoptymalizowana
- **Złożoność:** O(logᵣ n) gdzie r jest wspólną podstawą
- **Operacje:** Grupowanie bitów/digitów, bezpośrednia konwersja grup
- **Zalety:** Efektywniejsza dla kompatybilnych podstaw

## Klasyfikacja Podstaw

### Podstawy z Optymalizacją
| Podstawa | Rozkład | Wspólna podstawa | Optymalizacja |
|----------|---------|------------------|---------------|
| 2 | 2¹ | 2 | Grupowanie po 1 bicie |
| 3 | 3¹ | 3 | Grupowanie po 1 trycie |
| 4 | 2² | 2 | Grupowanie po 2 bity |
| 5 | 5¹ | 5 | Grupowanie po 1 pencie |
| 8 | 2³ | 2 | Grupowanie po 3 bity |
| 9 | 3² | 3 | Grupowanie po 2 tryty |
| 16 | 2⁴ | 2 | Grupowanie po 4 bity |
| 25 | 5² | 5 | Grupowanie po 2 penty |
| 27 | 3³ | 3 | Grupowanie po 3 tryty |

### Podstawy bez Optymalizacji
Podstawy będące iloczynami różnych liczb pierwszych wymagają standardowej konwersji:
- 6 = 2 × 3
- 10 = 2 × 5
- 12 = 4 × 3
- 14 = 2 × 7
- 15 = 3 × 5

## Algorytm detekcji potęgi liczby pierwszej (użyty w implementacji)

### Idea
Zamiast generować potęgi lub budować listę czynników, wykonujemy faktoryzację z wczesnym wyjściem:
- Znajdź pierwszy czynnik pierwszy `p`
- Zlicz, ile razy dzieli `base` → to jest wykładnik `k`
- Jeśli po wyciągnięciu wszystkich `p` zostaje `> 1`, to są różne czynniki → nie jest potęgą jednej liczby pierwszej
- Jeśli nie, `base = p^k`

### Kroki (pseudokod)
```
get_base_root(base):
  if base <= 1: return (base, 1)
  first_factor = 0; exponent = 0; n = base
  if n % 2 == 0:
    first_factor = 2
    while n % 2 == 0: exponent += 1; n //= 2
  if first_factor and n > 1: return (base, 1)
  if not first_factor:
    d = 3
    while d*d <= n:
      if n % d == 0:
        first_factor = d
        while n % d == 0: exponent += 1; n //= d
        break
      d += 2
  if n > 1: return (base, 1) if first_factor else (n, 1)
  return (first_factor or base, exponent or 1)
```

## Implementacyjne Aspekty (co, jak, po co)

### Reprezentacja Wewnętrzna
- Liczby są przetwarzane w systemie dziesiętnym jako wejście
- Wyniki są zwracane jako string cyfr w docelowej podstawie
- Dla potęg 2 stosujemy operacje bitowe (wydajniej niż dzielenie)

### Obsługa Cyfr
- Cyfry 0-9: reprezentowane jako znaki '0'-'9'
- Cyfry 10+: reprezentowane jako litery 'A'-'Z'
- Wielkość liter jest normalizowana do wielkich

### Ścieżki wykonania (kroki algorytmu konwersji)
1. Wejście: liczba całkowita `n` i podstawa `b`
2. Wyznacz `root, exp = get_base_root(b)`
3. Jeśli `root == 2` i `exp > 1`:
   - Ustaw `bits_per_digit = exp`, `mask = (1 << bits_per_digit) - 1`
   - Iteruj: `digit = n & mask`; `n >>= bits_per_digit`; zapisuj digit jako znak
   - Odwróć kolejność cyfr i zwróć
4. W przeciwnym razie (dowolna inna podstawa):
   - Standardowo: `digit = n % b`; `n //= b`; zapisuj digit jako znak
   - Odwróć kolejność cyfr i zwróć

### Graniczne Przypadki
- Liczba 0: zawsze reprezentowana jako "0"
- Jednocyfrowe wyniki: zwracane bez wiodących zer
- Ujemne liczby: nieobsługiwane (zakładamy liczby naturalne)

## Wnioski Teoretyczne

1. **Efektywność:** Operacje bitowe przy potęgach 2 ograniczają koszt dzielenia/modulo
2. **Uniwersalność:** Algorytm działa dla wszystkich podstaw w zakresie 2-16
3. **Czytelność i prostota:** Brak pośrednich struktur, mało gałęzi, DRY
4. **Matematyczna poprawność:** Faktoryzacja gwarantuje poprawną detekcję potęg

Optymalizacja przez grupowanie jest możliwa wyłącznie dla podstaw będących potęgami tej samej liczby pierwszej, co wynika z fundamentalnych właściwości systemów pozycyjnych.

---

# Faktoryzacja liczb — wyjaśnienie i przykłady

## 1. Wprowadzenie

Faktoryzacja (rozłożenie na czynniki pierwsze) to proces rozbicia liczby naturalnej na iloczyn liczb pierwszych.  
Liczby pierwsze to te, które mają dokładnie dwa dzielniki: 1 oraz samą siebie.

Przykład liczb pierwszych:  
2, 3, 5, 7, 11, 13, 17, 19, …

Przykład liczby złożonej (czyli niepierwszej):  
12 = 2 × 2 × 3

---

## 2. Idea faktoryzacji

Dla każdej liczby naturalnej `N > 1`, możemy znaleźć takie liczby pierwsze `p₁, p₂, ..., pₖ`, że:

```
N = p₁ × p₂ × ... × pₖ
```

Ten zapis to rozłożenie liczby na czynniki pierwsze.

---

## 3. Przykład 1: faktoryzacja liczby 12

Rozłóżmy `N = 12`:

1. Dzielimy przez najmniejszą możliwą liczbę pierwszą, czyli 2.  
   12 ÷ 2 = 6  
   ⇒ zapisujemy 2 jako pierwszy czynnik.

2. Ponownie dzielimy 6 przez 2:  
   6 ÷ 2 = 3  
   ⇒ zapisujemy kolejną 2.

3. Liczba 3 też jest liczbą pierwszą, więc zapisujemy ją jako ostatni czynnik.

Ostatecznie:
```
12 = 2 × 2 × 3
```

lub zapisując wykładniczo:
```
12 = 2² × 3¹
```

---

## 4. Przykład 2: faktoryzacja liczby 60

1. Dzielimy przez 2:  
   60 ÷ 2 = 30  
   ⇒ 2

2. Dzielimy 30 przez 2:  
   30 ÷ 2 = 15  
   ⇒ kolejne 2

3. Dzielimy 15 przez 3:  
   15 ÷ 3 = 5  
   ⇒ 3

4. Liczba 5 jest pierwsza, więc kończymy.

Ostatecznie:
```
60 = 2 × 2 × 3 × 5
```
lub
```
60 = 2² × 3 × 5
```

---

## 5. Przykład 3: faktoryzacja liczby 100

1. 100 ÷ 2 = 50  
   ⇒ 2

2. 50 ÷ 2 = 25  
   ⇒ kolejne 2

3. 25 ÷ 5 = 5  
   ⇒ 5

4. 5 ÷ 5 = 1  
   ⇒ kolejne 5

Ostatecznie:
```
100 = 2 × 2 × 5 × 5
```
czyli:
```
100 = 2² × 5²
```

---

## 6. Wyjaśnienie pojęcia „n > 1"

W wielu algorytmach faktoryzacji występuje warunek:

```python
while n > 1:
```

Oznacza on, że dopóki liczba `n` nie została całkowicie rozłożona na czynniki, kontynuujemy proces dzielenia.

- Gdy `n > 1`, wciąż można ją podzielić.
- Gdy `n == 1`, oznacza to, że już wszystkie czynniki pierwsze zostały wyciągnięte.

Przykład:

Weźmy `n = 12`.

Kroki:
1. 12 ÷ 2 → n = 6
2. 6 ÷ 2 → n = 3
3. 3 ÷ 3 → n = 1

W tym momencie `n = 1`, więc kończymy — cała faktoryzacja wykonana.

---

## 7. Przykład implementacji w Pythonie

```python
def factorize(number: int):
    factors = []
    divisor = 2

    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    return factors


print(factorize(12))   # [2, 2, 3]
print(factorize(60))   # [2, 2, 3, 5]
print(factorize(100))  # [2, 2, 5, 5]
```

---

## 8. Ulepszony zapis i optymalizacja

Możemy skrócić zapis używając słownika (dictionary), aby zapisać potęgi czynników:

```python
from collections import Counter

def factorize(number: int):
    factors = []
    divisor = 2

    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1

    return dict(Counter(factors))


print(factorize(60))  # {2: 2, 3: 1, 5: 1}
```

Ten wynik oznacza:
```
60 = 2² × 3¹ × 5¹
```

---

## 9. Dodatkowy przykład z dużą liczbą

Faktoryzacja `n = 84`:

1. 84 ÷ 2 = 42 → 2  
2. 42 ÷ 2 = 21 → 2  
3. 21 ÷ 3 = 7 → 3  
4. 7 jest liczbą pierwszą → 7  

Wynik:
```
84 = 2 × 2 × 3 × 7
```
czyli
```
84 = 2² × 3 × 7
```

---

## 10. Podsumowanie

| Liczba | Rozkład na czynniki | Zapis wykładniczy |
|--------|----------------------|-------------------|
| 12     | 2 × 2 × 3            | 2² × 3¹           |
| 60     | 2 × 2 × 3 × 5        | 2² × 3 × 5        |
| 100    | 2 × 2 × 5 × 5        | 2² × 5²           |
| 84     | 2 × 2 × 3 × 7        | 2² × 3 × 7        |

---

📘 Najważniejsze punkty do zapamiętania:
- Faktoryzacja to rozkład liczby na czynniki pierwsze.  
- Proces trwa, dopóki liczba `n > 1`.  
- Wynik można zapisać w postaci iloczynu liczb pierwszych lub w formie wykładniczej.  
- W programowaniu, faktoryzacja jest podstawą wielu algorytmów kryptograficznych (np. RSA).

