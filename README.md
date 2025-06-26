„Make your Dynasty"

## 🚀 Jak uruchomić aplikację

### Wymagania
- Python 3.8+ 
- pip (menedżer pakietów Python)

### Instalacja i uruchomienie

#### Metoda 1: Użyj skryptu (zalecane)
```bash
./run.sh
```

#### Metoda 2: Ręcznie
```bash
# 1. Stwórz środowisko wirtualne
python3 -m venv .venv

# 2. Aktywuj środowisko wirtualne
source .venv/bin/activate  # macOS/Linux
# lub
.venv\Scripts\activate     # Windows

# 3. Zainstaluj zależności
pip install -r requirements.txt

# 4. Uruchom aplikację
python src_main.py
```

#### Metoda 3: Bezpośrednio z interpreterem Python
```bash
python3 src_main.py
```

### Co się dzieje po uruchomieniu?
- Aplikacja ładuje dane przykładowe z pliku `sample_data.yaml`
- Inicjalizuje wszystkie systemy gry (rodzina, biznes, nieruchomości, piłka nożna, etc.)
- Wyświetla podstawowe informacje o graczu
- Pokazuje testowe dane z każdego systemu

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
