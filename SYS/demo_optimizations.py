#!/usr/bin/env python3
"""
Demonstracja optymalizacji konwersji między kompatybilnymi systemami pozycyjnymi.

Pokazuje jak funkcja to_base_n() automatycznie wykrywa kompatybilne podstawy
i używa bezpośredniej konwersji przez grupowanie bitów zamiast pośredniego
przeliczania przez system dziesiętny.
"""

import importlib.util

# Załaduj moduł sys.py
spec = importlib.util.spec_from_file_location("sys_solution", "solutions/sys.py")
sys_solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sys_solution)

def demo_conversion_optimization():
    """Demonstruje optymalizacje konwersji."""

    print("🔁 Demonstracja optymalizacji konwersji między kompatybilnymi systemami\n")

    test_cases = [
        # (liczba dziesiętna, podstawa docelowa, opis)
        (255, 2, "255₁₀ → binarny (grupowanie po 1 bicie)"),
        (255, 16, "255₁₀ → szesnastkowy (grupowanie po 4 bity)"),
        (63, 8, "63₁₀ → ósemkowy (grupowanie po 3 bity)"),
        (15, 4, "15₁₀ → czwórkowy (grupowanie po 2 bity)"),
        (100, 11, "100₁₀ → jedenastkowy (standardowa konwersja)"),
        (1263, 16, "1263₁₀ → szesnastkowy (grupowanie po 4 bity)"),
        (1263, 11, "1263₁₀ → jedenastkowy (standardowa konwersja)"),
    ]

    for num, base, description in test_cases:
        result = sys_solution.to_base_n(num, base)
        print(f"  {description}")
        print(f"  Wynik: {result}")
        print()

    print("📊 Wyjaśnienie optymalizacji:\n")

    print("Dla podstaw będących potęgami 2 (2, 4, 8, 16), funkcja używa:")
    print("1. Konwersji liczby dziesiętnej na postać binarną")
    print("2. Grupowania bitów w grupy odpowiedniej wielkości")
    print("3. Konwersji każdej grupy na cyfrę w docelowej podstawie\n")

    print("Przykład dla 255₁₀ → 16₁₆ (szesnastkowy):")
    print("  255₁₀ = 11111111₂ (binarnie)")
    print("  Grupowanie po 4 bity: 1111 1111")
    print("  1111₂ = F₁₆, 1111₂ = F₁₆")
    print("  Wynik: FF₁₆\n")

    print("Dla innych podstaw (np. 11), używa standardowej konwersji:")
    print("1. Dzielenie przez podstawę")
    print("2. Zbieranie reszt")
    print("3. Odwracanie kolejności cyfr\n")

    print("✅ Optymalizacja pozwala uniknąć kosztownych operacji mnożenia")
    print("   i potęgowania przy konwersjach między kompatybilnymi systemami!")

if __name__ == "__main__":
    demo_conversion_optimization()
