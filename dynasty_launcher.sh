#!/bin/bash

# Dynasty Simulator - Launcher dla macOS
# Uruchamia grę z dowolnego miejsca na komputerze

# Ustaw ścieżkę do gry (zmień na właściwą ścieżkę)
GAME_DIR="/Users/bartekromek/Desktop/code_app/Make-your-DYNASTY"

# Sprawdź czy katalog istnieje
if [ ! -d "$GAME_DIR" ]; then
    echo "❌ Nie znaleziono katalogu gry: $GAME_DIR"
    echo "📝 Edytuj ten plik i zmień ścieżkę GAME_DIR na właściwą"
    echo "💡 Obecna lokalizacja: $(pwd)"
    read -p "Naciśnij Enter aby zamknąć..."
    exit 1
fi

# Przejdź do katalogu gry
cd "$GAME_DIR"

# Sprawdź czy środowisko wirtualne istnieje
if [ ! -d ".venv" ]; then
    echo "🔧 Tworzenie środowiska wirtualnego..."
    python3 -m venv .venv
    
    # Aktywuj i zainstaluj zależności
    source .venv/bin/activate
    pip install -r requirements.txt
else
    # Aktywuj istniejące środowisko
    source .venv/bin/activate
fi

# Wyczyść terminal
clear

# Pokaż logo
echo "🏰 ================================== 🏰"
echo "    DYNASTY SIMULATOR - PEŁNA GRA"
echo "🏰 ================================== 🏰"
echo ""
echo "📍 Uruchamianie z: $GAME_DIR"
echo ""

# Uruchom grę
python dynasty_game.py

# Pauza po zakończeniu gry
echo ""
echo "🎮 Gra zakończona!"
echo "👋 Dziękujemy za grę w Dynasty Simulator!"
read -p "Naciśnij Enter aby zamknąć..."
