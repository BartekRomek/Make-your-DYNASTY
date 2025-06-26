#!/bin/bash

# Dynasty Simulator 2D - Launcher dla macOS
# Uruchamia wersję 2D z dowolnego miejsca na komputerze

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
    pip install pygame pygame-gui
else
    # Aktywuj istniejące środowisko
    source .venv/bin/activate
fi

# Sprawdź czy pygame jest zainstalowane
python -c "import pygame, pygame_gui" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "🔧 Instaluję biblioteki dla wersji 2D..."
    pip install pygame pygame-gui
fi

# Wyczyść terminal
clear

# Pokaż logo
echo "🎮 ================================== 🎮"
echo "    DYNASTY SIMULATOR 2D - GRAFICZNA"
echo "🎮 ================================== 🎮"
echo ""
echo "📍 Uruchamianie z: $GAME_DIR"
echo "🎯 Sterowanie: WASD/Strzałki - ruch, E - interakcja"
echo "💡 Aby zamknąć grę, naciśnij ALT+F4 lub zamknij okno"
echo ""

# Uruchom grę 2D
python dynasty_2d.py

# Pauza po zakończeniu gry
echo ""
echo "🎮 Gra 2D zakończona!"
read -p "Naciśnij Enter aby zamknąć..."
