#!/usr/bin/env python3
"""
Dynasty Simulator - Pełna Gra
Zbuduj swoją dynastię od zera!
"""

from game_engine_full import DynastyGame

def main():
    """Funkcja główna - uruchamia grę"""
    print("🎮 Uruchamianie Dynasty Simulator...")
    
    try:
        game = DynastyGame()
        game.run()
    except KeyboardInterrupt:
        print("\n\n👋 Dziękujemy za grę!")
    except Exception as e:
        print(f"\n❌ Wystąpił błąd: {e}")
        print("📧 Zgłoś problem deweloperom!")

if __name__ == "__main__":
    main()
