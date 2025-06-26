# 🚀 SZYBKI PRZEWODNIK URUCHAMIANIA

## 🎮 Jak uruchomić Dynasty Simulator?

### 1. **Z pulpitu (najłatwiej)** 🖱️

Na pulpicie znajdziesz:

**🏰 Dynasty Simulator.command**
- Podwójne kliknięcie → MENU WYBORU
- Możesz wybrać wersję tekstową lub 2D

**🎮 Dynasty Simulator 2D.command**  
- Podwójne kliknięcie → bezpośrednio wersja 2D

### 2. **Z folderu gry** 📁

Otwórz terminal w folderze gry:

```bash
./run.sh        # Wersja tekstowa
./run_2d.sh     # Wersja 2D
```

### 3. **Bezpośrednio** 🔧

```bash
python dynasty_game.py    # Wersja tekstowa
python dynasty_2d.py      # Wersja 2D
```

## 🤔 Którą wersję wybrać?

### 🔤 **Wersja tekstowa** (`dynasty_game.py`)
**✅ Wybierz jeśli:**
- Lubisz klasyczne gry RPG
- Chcesz pełną funkcjonalność (zapis/wczytaj)
- Preferujesz szybką nawigację
- Grasz na słabszym komputerze

**🎯 Funkcje:**
- Kompleksne systemy ekonomiczne
- Pełne zarządzanie dynastią  
- System zapisywania gier
- Wszystkie mechaniki zaimplementowane

### 🎮 **Wersja 2D** (`dynasty_2d.py`)
**✅ Wybierz jeśli:**
- Lubisz graficzne gry
- Chcesz kontrolować postać
- Preferujesz wizualne doświadczenie
- Masz komputer z kartą graficzną

**🎯 Funkcje:**
- Graficzny świat 2D
- Kontrola postaci (WASD)
- Interakcje z budynkami i NPCs
- Immersyjne dialogi

## ❓ Problemy?

### 🚫 Gra się nie uruchamia
```bash
# Sprawdź Python
python --version

# Zainstaluj zależności
pip install -r requirements.txt
pip install pygame pygame-gui  # Dla wersji 2D
```

### 🖥️ Wersja 2D nie działa
- Upewnij się że masz środowisko graficzne
- Nie działa przez SSH/terminal zdalny
- Wymagana karta graficzna

### 📱 Skrót na pulpicie
- Jeśli nie ma skrótów, uruchom grę raz z terminala
- Skróty utworzą się automatycznie

## 💡 Wskazówki

1. **Pierwszy raz?** Uruchom `🏰 Dynasty Simulator.command` - dostaniesz menu wyboru
2. **Lubisz 2D?** Użyj `🎮 Dynasty Simulator 2D.command` 
3. **Zaawansowany użytkownik?** Uruchamiaj bezpośrednio z terminala
4. **Problemy?** Sprawdź `INSTRUKCJA_2D.md` dla wersji graficznej

---

**Miłej zabawy z Dynasty Simulator!** 🏰✨
