#!/bin/bash

# Skrypt do uruchomienia Dynasty Simulator - Pełnej Gry

echo "🏰 Dynasty Simulator - Zbuduj swoją dynastię!"
echo "=============================================="

# Sprawdź czy istnieje środowisko wirtualne
if [ ! -d ".venv" ]; then
    echo "🔧 Tworzenie środowiska wirtualnego..."
    python3 -m venv .venv
fi

# Aktywuj środowisko wirtualne
source .venv/bin/activate

# Zainstaluj zależności
echo "📦 Instalowanie zależności..."
pip install -r requirements.txt > /dev/null 2>&1

# Wyczyść ekran
clear

# Uruchom pełną grę
echo "🚀 Uruchamianie Dynasty Simulator..."
echo ""
python dynasty_game.py

echo ""
echo "✅ Dziękujemy za grę w Dynasty Simulator!"
