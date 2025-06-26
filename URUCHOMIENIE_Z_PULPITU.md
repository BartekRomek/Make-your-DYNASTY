# 🖥️ DYNASTY SIMULATOR - Uruchomienie z Pulpitu

## 🎯 Najłatwiejszy Sposób - Podwójne Kliknięcie!

Na twoim pulpicie znajdziesz teraz:

### 🏰 Dynasty Simulator.command
**Kliknij dwukrotnie** i gra się uruchomi automatycznie!

### Dynasty Simulator.app  
Alternatywna **aplikacja macOS** - również podwójne kliknięcie.

## 🛠️ Co zrobiłem dla Ciebie:

### ✅ Skróty na Pulpicie
- **🏰 Dynasty Simulator.command** - główny skrót
- **Dynasty Simulator.app** - aplikacja macOS
- Oba otwierają Terminal i uruchamiają grę automatycznie

### ✅ Automatyczna Instalacja
- Sprawdza czy środowisko Python istnieje
- Instaluje zależności automatycznie  
- Uruchamia grę w terminalu z ładnym interfejsem

### ✅ Obsługa Błędów
- Sprawdza czy gra istnieje
- Wyświetla pomocne komunikaty
- Automatycznie naprawia problemy

## 🎮 Jak Uruchomić Grę:

### Sposób 1: Z Pulpitu (ZALECANE) 🖱️
```
1. Idź na pulpit
2. Znajdź "🏰 Dynasty Simulator.command"  
3. Kliknij dwukrotnie
4. Gra uruchomi się w Terminalu
```

### Sposób 2: Z Findera
```
1. Otwórz Finder
2. Idź do /Users/bartekromek/Desktop/code_app/Make-your-DYNASTY
3. Kliknij dwukrotnie "run.sh"
```

### Sposób 3: Z Terminala
```bash
cd /Users/bartekromek/Desktop/code_app/Make-your-DYNASTY
./run.sh
```

## 🔧 Jeśli Masz Problemy:

### ❌ "Nie można otworzyć pliku"
```bash
# W Terminalu uruchom:
chmod +x "/Users/bartekromek/Desktop/🏰 Dynasty Simulator.command"
```

### ❌ "Nie znaleziono gry"  
Sprawdź czy folder gry istnieje:
```bash
ls -la "/Users/bartekromek/Desktop/code_app/Make-your-DYNASTY"
```

### ❌ "Python not found"
Zainstaluj Python 3:
```bash
# Sprawdź czy masz Pythona:
python3 --version

# Jeśli nie, zainstaluj przez Homebrew:
brew install python3
```

## 📱 Dla Innych Systemów:

### Windows
Stwórz plik `dynasty.bat`:
```batch
@echo off
cd /d "C:\ścieżka\do\gry\Make-your-DYNASTY"
python dynasty_game.py
pause
```

### Linux
Stwórz plik `dynasty.sh`:
```bash
#!/bin/bash
cd "/ścieżka/do/gry/Make-your-DYNASTY"
./run.sh
```

## 🎯 Po Uruchomieniu:

1. **Otwiera się Terminal** z menu gry
2. **Wybierasz opcje** numerami (1-9, S, L, Q, E)
3. **Grasz** - buduj dynastię!
4. **Zapisujesz** grę (opcja S)
5. **Wczytuj** później (opcja L)

## 🏆 Teraz Możesz:

- ✅ **Kliknąć dwukrotnie** na pulpicie
- ✅ **Uruchomić z dowolnego miejsca**  
- ✅ **Nie pamiętać ścieżek**
- ✅ **Grać natychmiast**

---

**🎮 Graj w Dynasty Simulator z pulpitu jak w prawdziwą grę!** 🏰

*Podwójne kliknięcie i jesteś w grze!*
