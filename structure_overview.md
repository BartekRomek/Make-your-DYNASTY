# Przykładowa Struktura Plików Projektu

```
/dynasty-sim
│
├── README.md                  # Opis projektu, założenia
├── game_design.md             # Szczegółowy opis mechanik, systemów
├── structure_overview.md      # Struktura projektu (ten plik)
├── sample_data.yaml           # Przykładowe dane startowe do prototypowania
│
├── /src
│   ├── main.py                # Główny plik uruchamiający prototyp
│   ├── /systems
│   │    ├── family.py         # Mechaniki rodziny i dziedziczenia
│   │    ├── business.py       # Mechaniki biznesu, giełdy
│   │    ├── crime.py          # Mechaniki nielegalne
│   │    ├── football.py       # System klubów piłkarskich
│   │    ├── education.py      # System edukacji i umiejętności
│   │    ├── events.py         # Dynamiczne wydarzenia
│   │    └── property.py       # Nieruchomości, rozbudowa posiadłości
│   └── /ui
│        ├── menu.py           # Prosty interfejs tekstowy/prototypowy
│        └── ...               # Inne moduły UI
│
└── /tests
    ├── test_family.py
    ├── test_business.py
    └── ...
```