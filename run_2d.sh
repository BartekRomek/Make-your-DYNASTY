#!/bin/bash

# Dynasty Simulator 2D - Skrypt uruchomieniowy
echo "🎮 Dynasty Simulator 2D"
echo "========================="

# Sprawdź czy jesteśmy w odpowiednim folderze
if [ ! -f "dynasty_2d.py" ]; then
    echo "❌ Błąd: Nie znaleziono dynasty_2d.py"
    echo "   Uruchom skrypt z folderu gry!"
    exit 1
fi

# Sprawdź czy istnieje środowisko wirtualne
if [ -d ".venv" ]; then
    echo "🔧 Używam środowiska wirtualnego..."
    PYTHON_CMD=".venv/bin/python"
else
    echo "🔧 Używam systemowego Python..."
    PYTHON_CMD="python3"
fi

# Sprawdź czy pygame jest zainstalowane
echo "🔍 Sprawdzam biblioteki..."
$PYTHON_CMD -c "import pygame, pygame_gui; print('✅ Wszystkie biblioteki gotowe!')" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ Brakuje bibliotek! Instaluję..."
    $PYTHON_CMD -m pip install pygame pygame-gui PyYAML
fi

echo ""
echo "🚀 Uruchamiam Dynasty Simulator 2D..."
echo "🎯 Sterowanie: WASD/Strzałki - ruch, E - interakcja, I - inwentarz"
echo "💡 Aby zamknąć grę, naciśnij ALT+F4 lub zamknij okno"
echo ""

# Uruchom grę
$PYTHON_CMD dynasty_2d.py

echo ""
echo "👋 Dziękujemy za grę!"
