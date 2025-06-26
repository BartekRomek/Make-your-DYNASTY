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

# Pokaż logo i menu wyboru
echo "🏰 ================================== 🏰"
echo "        DYNASTY SIMULATOR"
echo "🏰 ================================== 🏰"
echo ""
echo "📍 Lokalizacja: $GAME_DIR"
echo ""
echo "🎮 Wybierz wersję gry:"
echo "   1️⃣  Wersja tekstowa (klasyczna)"
echo "   2️⃣  Wersja 2D (graficzna)"
echo "   0️⃣  Anuluj"
echo ""
read -p "Twój wybór (1/2/0): " choice

case $choice in
    1)
        echo ""
        echo "🔤 Uruchamianie wersji tekstowej..."
        python dynasty_game.py
        ;;
    2)
        echo ""
        echo "🎮 Sprawdzam biblioteki dla wersji 2D..."
        
        # Sprawdź czy pygame jest zainstalowane
        python -c "import pygame, pygame_gui" 2>/dev/null
        if [ $? -ne 0 ]; then
            echo "🔧 Instaluję biblioteki dla wersji 2D..."
            pip install pygame pygame-gui
        fi
        
        echo "🎮 Uruchamianie wersji 2D..."
        echo "🎯 Sterowanie: WASD/Strzałki - ruch, E - interakcja"
        python dynasty_2d.py
        ;;
    0)
        echo ""
        echo "👋 Anulowano uruchomienie"
        exit 0
        ;;
    *)
        echo ""
        echo "❌ Niepoprawny wybór. Uruchamiam wersję tekstową..."
        python dynasty_game.py
        ;;
esac

# Pauza po zakończeniu gry
echo ""
echo "🎮 Gra zakończona!"
echo "👋 Dziękujemy za grę w Dynasty Simulator!"
read -p "Naciśnij Enter aby zamknąć..."
