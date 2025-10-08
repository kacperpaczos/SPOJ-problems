#!/usr/bin/env python3
"""
Demonstracja konwersji bezpośredniej między dowolnymi kompatybilnymi podstawami.

Pokazuje jak wykrywać i konwertować między podstawami będącymi potęgami tej samej liczby:
- 2, 4, 8, 16 (potęgi 2)
- 3, 9, 27 (potęgi 3)
- 5, 25, 125 (potęgi 5)
"""

import importlib.util

# Załaduj moduł
spec = importlib.util.spec_from_file_location("sys_solution", "solutions/sys.py")
sys_solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sys_solution)

def demo():
    print("🔄 Demonstracja konwersji między kompatybilnymi podstawami\n")
    print("=" * 70)
    
    # Przykład 1: Potęgi dwójki
    print("\n📘 Przykład 1: Konwersje między potęgami 2 (2, 4, 8, 16)")
    print("-" * 70)
    bases_2 = [2, 4, 8, 16]
    for base in bases_2:
        root, exp = sys_solution.get_base_root(base)
        print(f"  Base {base:2d} = {root}^{exp}")
    
    print("\n  Możliwe konwersje bezpośrednie:")
    print("  • 2 ↔ 4 ↔ 8 ↔ 16")
    print("  • Każda cyfra w base 16 = 4 cyfry w base 2")
    print("  • Każda cyfra w base 8 = 3 cyfry w base 2")
    print("  • Każda cyfra w base 4 = 2 cyfry w base 2")
    
    # Przykład 2: Potęgi trójki
    print("\n📗 Przykład 2: Konwersje między potęgami 3 (3, 9, 27)")
    print("-" * 70)
    bases_3 = [3, 9, 27]
    for base in bases_3:
        root, exp = sys_solution.get_base_root(base)
        print(f"  Base {base:2d} = {root}^{exp}")
    
    print("\n  Możliwe konwersje bezpośrednie:")
    print("  • 3 ↔ 9 ↔ 27")
    print("  • Każda cyfra w base 9 = 2 cyfry w base 3")
    print("  • Każda cyfra w base 27 = 3 cyfry w base 3")
    
    # Przykład 3: Potęgi piątki
    print("\n📙 Przykład 3: Konwersje między potęgami 5 (5, 25, 125)")
    print("-" * 70)
    bases_5 = [5, 25, 125]
    for base in bases_5:
        root, exp = sys_solution.get_base_root(base)
        print(f"  Base {base:3d} = {root}^{exp}")
    
    print("\n  Możliwe konwersje bezpośrednie:")
    print("  • 5 ↔ 25 ↔ 125")
    print("  • Każda cyfra w base 25 = 2 cyfry w base 5")
    print("  • Każda cyfra w base 125 = 3 cyfry w base 5")
    
    # Przykład 4: Niekompatybilne podstawy
    print("\n📕 Przykład 4: Niekompatybilne podstawy")
    print("-" * 70)
    incompatible = [(2, 3), (8, 9), (16, 25), (11, 13)]
    for b1, b2 in incompatible:
        can, root, e1, e2 = sys_solution.can_convert_directly(b1, b2)
        r1, exp1 = sys_solution.get_base_root(b1)
        r2, exp2 = sys_solution.get_base_root(b2)
        print(f"  {b1} ({r1}^{exp1}) ↔ {b2} ({r2}^{exp2}): {'TAK' if can else 'NIE - różne rooty'}")
    
    # Praktyczny przykład konwersji
    print("\n" + "=" * 70)
    print("\n💡 Praktyczny przykład: 100₁₀ w różnych systemach")
    print("-" * 70)
    
    test_bases = [2, 3, 4, 5, 8, 9, 16, 25, 27]
    for base in test_bases:
        result = sys_solution.to_base_n(100, base)
        root, exp = sys_solution.get_base_root(base)
        is_power = "✓" if root != base else " "
        print(f"  100₁₀ = {result:>10s} (base {base:2d}) {is_power} [{root}^{exp}]")
    
    print("\n" + "=" * 70)
    print("\n✅ Wnioski:")
    print("  1. Funkcja get_base_root() znajduje wspólny 'root' dla podstaw")
    print("  2. Jeśli dwie podstawy mają ten sam root, można konwertować bezpośrednio")
    print("  3. Działa dla dowolnych potęg, nie tylko potęg 2!")
    print("  4. Przykłady: 3↔9↔27, 5↔25↔125, 2↔4↔8↔16")

if __name__ == "__main__":
    demo()
