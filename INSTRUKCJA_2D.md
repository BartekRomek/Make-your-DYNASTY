# 🎮 Dynasty Simulator 2D - Instrukcja

## 🚀 Jak uruchomić wersję 2D

### Opcja 1: Automatyczny skrypt
```bash
./run_2d.sh
```

### Opcja 2: Bezpośrednio
```bash
python dynasty_2d.py
```

## 🎯 Sterowanie

### 🚶‍♂️ Ruch postaci
- **WASD** lub **Strzałki** - poruszanie się po mapie
- Postać automatycznie omija przeszkody

### 🎮 Interakcje
- **E** - interakcja z budynkami i NPCs
- **I** - otwórz inwentarz/statystyki
- **ESC** - menu pauzy
- **Spacja** - kontynuuj dialog
- **ESC** (w dialogu) - zamknij dialog

## 🗺️ Mapa świata

### 🏢 Budynki
- **🏢 Biuro** (zielony) - zarządzanie biznesami
- **🏠 Agencja Nieruchomości** (brązowy) - kupno/sprzedaż nieruchomości  
- **⚽ Stadion** (pomarańczowy) - zarządzanie klubem piłkarskim
- **🎓 Uniwersytet** (fioletowy) - kursy i edukacja
- **🌑 Ciemna Uliczka** (czerwony) - półświatek (wymaga niskiej moralności)
- **👨‍👩‍👧‍👦 Dom Rodzinny** (żółty) - relacje rodzinne
- **🏦 Bank** (złoty) - kredyty i inwestycje
- **🛒 Sklep** (szary) - zakupy

### 👥 NPCs (Postacie)
- **Anna** (Dom) - żona/partnerka
- **Viktor** (Półświatek) - kontakty z półświatkiem
- **Prof. Kowalski** (Edukacja) - kursy i szkolenia
- **Broker** (Biznes) - doradca biznesowy

## 📊 Interfejs użytkownika (HUD)

### 📈 Panel gracza (lewy górny róg)
- **👤 Imię** - nazwa postaci
- **🎂 Wiek** - aktualny wiek
- **💰 Pieniądze** - stan konta w PLN
- **😇 Moralność** - poziom moralności (0-100)

### 🎯 Umiejętności (lewy panel)
- **Paski postępu** dla każdej umiejętności:
  - 🟢 Zielony (70-100) - ekspert
  - 🟡 Żółty (40-69) - średniozaawansowany  
  - 🔴 Czerwony (0-39) - początkujący

### 🎮 Sterowanie (prawy górny róg)
- Podpowiedzi sterowania
- Aktualne klawisze

## 💬 System dialogów

### 🗨️ Rozmowy z NPCs
- Kliknij **E** obok NPC
- **Spacja** - następna wiadomość
- **ESC** - zamknij dialog

### 🏢 Interakcje z budynkami
- Wejdź w budynek i naciśnij **E**
- Każdy budynek ma unikalne menu
- Różne opcje w zależności od typu budynku

## 📦 Inwentarz (I)

### 📊 Przegląd majątku
- Wszystkie biznesy gracza
- Posiadane nieruchomości
- Informacje o rodzinie
- Statistyki postaci

## ⚙️ Menu (ESC)

### 🔧 Opcje pauzy
- **ESC** - powrót do gry
- **S** - zapisz grę (planowane)
- **L** - wczytaj grę (planowane)
- **Q** - wyjście z gry

## 🎯 Cele gry w wersji 2D

### 💰 Ekonomiczne
- Zbuduj imperium biznesowe
- Osiągnij majątek 100 mln PLN
- Kup luksusowe nieruchomości

### 👨‍👩‍👧‍👦 Społeczne
- Zbuduj szczęśliwą rodzinę
- Nawiąż kontakty biznesowe
- Wybierz ścieżkę moralną

### ⚖️ Moralne wybory
- **Uczciwe biznesy** - wolny, ale bezpieczny rozwój
- **Półświatek** - szybkie zyski, wysokie ryzyko
- Każdy wybór ma konsekwencje!

## 🔧 Rozwiązywanie problemów

### ❌ Gra się nie uruchamia
```bash
# Sprawdź biblioteki
python -c "import pygame, pygame_gui; print('OK')"

# Zainstaluj brakujące
pip install pygame pygame-gui PyYAML
```

### 🖥️ Problemy z grafiką
- Upewnij się, że masz środowisko graficzne
- Nie działa przez SSH/terminal
- Wymagany jest dostęp do ekranu

### 🐛 Błędy w grze
- Sprawdź terminal - tam wyświetlają się komunikaty błędów
- Uruchom ponownie grę
- Sprawdź wersję Python (wymagane 3.8+)

## 🚧 Planowane funkcje

### 🔄 W rozwoju
- **Animacje postaci** - płynniejszy ruch
- **Więcej budynków** - rozszerzona mapa
- **System zadań** - konkretne cele do wykonania
- **Efekty dźwiękowe** - muzyka i efekty
- **Lepsze grafiki** - ładniejsze tekstury

### 📅 Przyszłość
- **Multiplayer** - gra z przyjaciółmi
- **Większe mapy** - różne miasta
- **Więcej NPCs** - bogatsza fabuła
- **System czasu** - dzień/noc, pory roku

---

## 🎮 Miłej zabawy!

Wersja 2D oferuje immersyjne doświadczenie wizualne, zachowując całą głębię mechanik z wersji tekstowej. Eksploruj świat, podejmuj decyzje i buduj swoją dynastię!
