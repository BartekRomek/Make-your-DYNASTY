#!/bin/bash

# Skrypt do uruchomienia aplikacji Dynasty Simulator

echo "🏰 Uruchamianie Dynasty Simulator..."

# Sprawdź czy istnieje środowisko wirtualne
if [ ! -d ".venv" ]; then
    echo "🔧 Tworzenie środowiska wirtualnego..."
    python3 -m venv .venv
fi

# Aktywuj środowisko wirtualne
source .venv/bin/activate

# Zainstaluj zależności
echo "📦 Instalowanie zależności..."
pip install -r requirements.txt

# Uruchom aplikację
echo "🚀 Uruchamianie aplikacji..."
python src_main.py

echo "✅ Aplikacja zakończona."
