„Make your Dynasty"

## 🎮 PEŁNA GRA - Dynasty Simulator

### 🚀 Jak uruchomić grę

#### Metoda 1: Z pulpitu (najłatwiejsza) 🖱️
```
🏰 Podwójne kliknięcie na "Dynasty Simulator" na pulpicie
```

#### Metoda 2: Użyj skryptu w folderze gry
**Wersja tekstowa:**
```bash
./run.sh
```

**Wersja 2D:**
```bash
./run_2d.sh
```

#### Metoda 3: Bezpośrednio
```bash
python dynasty_game.py
```

#### Metoda 4: Wersja 2D (graficzna) 🎮
```bash
python dynasty_2d.py
```

#### Metoda 5: Prototyp (tylko demo)
```bash
python src_main.py
```

### 💻 Instalacja na pulpicie

Po pierwszym uruchomieniu gry znajdziesz na pulpicie:

**Skróty .command:**
- **🏰 Dynasty Simulator.command** - MENU WYBORU wersji (tekstowa/2D)
- **🎮 Dynasty Simulator 2D.command** - bezpośrednio wersja 2D

**Aplikacje macOS:**
- **Dynasty Simulator.app** - wersja tekstowa
- **Dynasty Simulator 2D.app** - wersja graficzna 2D

**Wystarczy podwójne kliknięcie!** 🖱️

### 🎯 Która wersja dla mnie?

**🔤 Wersja tekstowa** - jeśli lubisz:
- Klasyczne gry RPG w terminalu
- Szybkie menu i nawigację klawiaturą
- Kompleksowe systemy ekonomiczne
- Pełny system zapisywania gier

**🎮 Wersja 2D** - jeśli lubisz:
- Graficzny interfejs i kontrolę postaci
- Eksplorację świata gry
- Interakcje z NPCs i budynkami
- Immersyjne doświadczenie wizualne

### 🎯 Co to za gra?

**Dynasty Simulator** to pełnoprawna gra symulacyjna dostępna w **dwóch wersjach**:

🔤 **Wersja tekstowa** (`dynasty_game.py`) - klasyczna gra konsolowa
🎮 **Wersja 2D** (`dynasty_2d.py`) - graficzna gra z kontrolą postaci

W obu wersjach budujesz swoją dynastię od zera! 

#### 🎮 Główne mechaniki gry:
- **👨‍👩‍👧‍👦 Zarządzanie rodziną** - małżeństwo, dzieci, relacje
- **🏢 Imperium biznesowe** - zakładaj firmy, inwestuj, rozwijaj
- **🏠 Nieruchomości** - kupuj, wynajmuj, rozbudowuj
- **⚽ Kluby piłkarskie** - zarządzaj drużyną, kupuj zawodników
- **🎓 Edukacja** - rozwijaj umiejętności, zdobywaj certyfikaty
- **🌑 Półświatek** - ryzykowne, ale lukratywne działania
- **📰 Wydarzenia** - reaguj na losowe sytuacje

#### 💰 System ekonomiczny:
- **Pasywne przychody** z biznesów i wynajmu
- **Miesięczne tury** z automatycznymi zyskami
- **Inwestycje** w rozwój firm i nieruchomości
- **Koszty utrzymania** - każda decyzja ma swoją cenę

#### 🎯 Cele gry:
- Osiągnij majątek 100 milionów PLN
- Zostań właścicielem 5 firm w różnych branżach  
- Wykształć następcę i przekaż mu dynastię
- Zbuduj rodzinne imperium na pokolenia

#### ⚖️ System moralności:
- **Legalne działania** - powolny, ale bezpieczny rozwój
- **Nielegalne metody** - szybkie zyski, ale wysokie ryzyko
- **Konsekwencje wyborów** wpływają na reputację i relacje

### 🎮 Jak grać?

1. **Start** - Rozpoczynasz z 100,000 PLN i podstawowymi umiejętnościami
2. **Menu główne** - Wybierz co chcesz robić (rodzina, biznes, nieruchomości, etc.)
3. **Rozwijaj się** - Inwestuj, ucz się, buduj relacje
4. **Podejmuj decyzje** - Każdy wybór ma konsekwencje
5. **Następna tura** - Czas płynie, otrzymujesz pasywne przychody
6. **Reaguj na wydarzenia** - Losowe sytuacje wymagają reakcji

### 🔧 Wymagania techniczne:
**Wersja tekstowa:**
- Python 3.8+
- PyYAML (automatycznie instalowane)
- Terminal/Konsola

**Wersja 2D:**
- Python 3.8+
- PyYAML, pygame, pygame-gui (automatycznie instalowane)
- Środowisko graficzne (nie działa przez SSH)

### 📊 Status rozwoju:
**Wersja tekstowa:**
- ✅ **Kompletne systemy**: Rodzina, Biznes, Nieruchomości, Piłka nożna
- ✅ **Działająca ekonomia**: Pasywne przychody, koszty, inwestycje  
- ✅ **Interaktywne menu**: Pełna nawigacja po grze
- ✅ **System wydarzeń**: Losowe sytuacje i wyzwania
- ✅ **Zapis/wczytywanie**: Pełny system save/load
- 🔄 **W rozwoju**: System edukacji, półświatek (częściowo)

**Wersja 2D:**
- ✅ **Graficzny interfejs**: Pełne 2D z pygame
- ✅ **Kontrola postaci**: Ruch WASD/strzałkami
- ✅ **Interaktywny świat**: Budynki, NPCs, dialogi
- ✅ **System HUD**: Statystyki gracza, umiejętności
- ✅ **Menu i inwentarz**: Pełna nawigacja
- 🔄 **W rozwoju**: Rozszerzone mechaniki, animacje

**Planowane dla obu wersji:**
- 🔄 **Multiplayer**, **Zaawansowany AI**, **Więcej lokacji**

---

### 1. **Podstawowe założenia gry**
- **Cel gry**:
  - Budowa dynastii od zera lub jako dziedzic rodzinnego imperium.
  - Rozwój kariery, majątku, relacji rodzinnych oraz wpływów globalnych.
- **Gatunek gry**:
  - Symulator życia + strategia biznesowa + RPG moralnych wyborów.

---

### 2. **Rozgrywka i mechaniki**
#### A. **Relacje rodzinne**
- Budowanie relacji z rodziną (romanse, dzieci, konflikty).
- Dziedziczenie majątku i rozwój dynastii przez pokolenia.
- Konflikty rodzinne i ich wpływ na rozwój postaci.

#### B. **Kariera biznesowa**
- Start od małych biznesów, rozwój do globalnych korporacji.
- Lokacje biznesowe:
  - Główne biuro jako najwyższy poziom.
  - Filie w różnych miastach na świecie (np. Londyn, Nowy Jork, Tokio).
- Zarządzanie przez komputer:
  - Ikony firm, giełda, inwestycje.
  - Ukryte wejście do nielegalnych działań.
- System wrogich przejęć, manipulacji giełdowej i zdrad.

#### C. **Nielegalne działania**
- Mechaniki:
  - Pranie pieniędzy, łapówki, manipulacje kursami akcji.
  - Ukryte lokacje do działań nielegalnych (np. magazyny, bunkry).
- Ryzyko:
  - Śledzenie przez służby, medialne skandale.
  - Możliwość unikania konsekwencji przez wpływy i łapówki.

#### D. **Kluby piłkarskie**
- System zarządzania klubem:
  - Budżet, transfery, treningi.
  - Rozbudowa stadionu, akademii młodzieżowej.
- Rozgrywki:
  - Lokalne i międzynarodowe ligi, organizacja turniejów.
- Relacje z miastem i fanami:
  - Wsparcie lokalnej społeczności i budowanie popularności.

#### E. **Mapa świata**
- Kupowanie działek i posiadłości na całym globie.
- Rozwój globalny biznesów:
  - Nieruchomości, fabryki, hotele.
- Eksploracja kulturowa:
  - Wydarzenia lokalne i globalne.

---

### 3. **Wybory moralne**
- Legalne vs nielegalne działania:
  - Budowanie dynastii przez uczciwość lub manipulacje.
- Konsekwencje wyborów:
  - Reputacja, relacje z rodziną, ryzyko śledztwa.

---

### 4. **Rozbudowa posiadłości**
- Typy nieruchomości:
  - Apartamenty, wille, zamki, stadiony, wyspy.
- Personalizacja:
  - Dekoracja wnętrz, dodawanie luksusowych elementów.
- System wynajmu:
  - Generowanie pasywnego dochodu.

---

### 5. **Dynamiczne wydarzenia**
- Losowe kryzysy:
  - Epidemie, kryzysy finansowe, klęski żywiołowe.
- Skandale:
  - Konflikty w biznesie, afery medialne, zdrady wspólników.

---

### 6. **System edukacji**
- Rozwój umiejętności:
  - Negocjacje, zarządzanie, manipulacja, technologia.
- Wpływ edukacji na sukces:
  - Wyższe wykształcenie otwiera nowe możliwości.

---

### 7. **Multiplayer (w przyszłości)
- Rywalizacja online:
  - Ligowe rankingi biznesowe, turnieje piłkarskie.
- Współpraca:
  - Tworzenie globalnych partnerstw biznesowych.

---

### 8. **Technologia i przyszłość**
- Rozwój technologii w grze:
  - Automatyzacja biznesów, AI, kolonizacja kosmosu.
- Możliwość eksploracji przyszłości:
  - Nowe rynki, nowe technologie.

---

### 9. **Personalizacja gracza**
- Kreator postaci:
  - Wygląd, cechy charakteru, umiejętności.
- Wybór początkowego scenariusza:
  - Dziedziczenie rodzinnego majątku vs start od zera.

---

### 10. **System rywalizacji i wpływów**
- Wrogowie:
  - Sabotaż, zdrady, rywalizacja w biznesie.
- Budowanie sieci wpływów:
  - Politycy, biznesmeni, media.

---

### 11. **Kontakty z półświatkiem**
#### A. **Postać z półświata**
- **Mentor**:
  - Charyzmatyczna postać wprowadzająca gracza w ciemne interesy.
- **Relacja**:
  - Początkowa pomoc, która prowadzi do współpracy w półświatku.

#### B. **Mechaniki związane z półświatkiem**
- Misje:
  - Sabotaż konkurencji, pranie pieniędzy, zdobywanie informacji.
- Nowe możliwości:
  - Manipulacje giełdowe, handel wpływami, „czarne operacje”.
- System ryzyka:
  - Śledzenie przez służby, zdrady przez wspólników.

#### C. **Zdrady i konflikty**
- Zdrada przez półświatka:
  - Możliwość utraty majątku, wolności lub życia.
- Rywalizacja w półświatku:
  - Konflikty z innymi grupami ciemnych interesów.

#### D. **System ochrony**
- Zabezpieczenia:
  - Prywatni ochroniarze, fałszowanie dokumentów, niszczenie dowodów.
- Ukrywanie działań:
  - Mechanizmy pozwalające unikać wykrycia.

---

### 12. **Realizm ryzyka**
- Delikatność relacji:
  - Każda decyzja może prowadzić do utraty zaufania lub zdrady.
- Konsekwencje:
  - Strata majątku, wolności lub życia w wyniku złych decyzji.

---

### Podsumowanie
Gra „Make your Dynasty” nabiera jeszcze większej głębi dzięki dodaniu kontaktów z półświatkiem. Balansowanie między legalnymi i nielegalnymi działaniami, moralnymi wyborami oraz kruchymi relacjami z ciemnym światem tworzy unikalną mieszankę emocji, strategii i ryzyka. Jeśli masz więcej pomysłów na rozwinięcie tego, chętnie je uwzględnię!
