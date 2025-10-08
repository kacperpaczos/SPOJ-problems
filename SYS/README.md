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
- **Binarny (2)** ↔ **Czwórkowy (4)** ↔ **Ósemkowy (8)** ↔ **Szesnastkowy (16)**
- Metoda: Grupowanie bitów (1→2→3→4 bity odpowiednio)

**Konwersje standardowe (przez system dziesiętny):**
- Wszystkie inne podstawy (np. base 11)

**Przykład optymalizacji:**
```
255₁₀ → FF₁₆:
  255₁₀ = 11111111₂ (binarnie)
  Grupowanie po 4 bity: 1111 1111
  1111₂ = F₁₆, 1111₂ = F₁₆
  Wynik: FF₁₆
```

Uruchom `python3 demo_optimizations.py` aby zobaczyć demonstrację optymalizacji.
