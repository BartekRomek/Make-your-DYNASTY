"""
Główny plik prototypu gry "Symulator Dynastii"
"""

import yaml
import os
from systems.family import FamilySystem
from systems.business import BusinessSystem
from systems.crime import CrimeSystem
from systems.football import FootballSystem
from systems.education import EducationSystem
from systems.events import EventsSystem
from systems.property import PropertySystem

def load_sample_data():
    """Ładuje dane przykładowe z pliku YAML"""
    try:
        with open('sample_data.yaml', 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print("Nie znaleziono pliku sample_data.yaml!")
        return None
    except yaml.YAMLError as e:
        print(f"Błąd podczas wczytywania pliku YAML: {e}")
        return None

def main():
    print("=" * 50)
    print("Witaj w prototypie gry Symulator Dynastii!")
    print("=" * 50)
    
    # Załaduj dane przykładowe
    data = load_sample_data()
    if not data:
        print("Nie można załadować danych. Kończę program.")
        return
    
    # Inicjalizuj systemy gry
    family_system = FamilySystem(data.get('player', {}))
    business_system = BusinessSystem(data.get('businesses', []))
    crime_system = CrimeSystem(data.get('underworld_contacts', []))
    football_system = FootballSystem(data.get('clubs', []))
    education_system = EducationSystem(data.get('player', {}))
    events_system = EventsSystem(data.get('events', []))
    property_system = PropertySystem(data.get('properties', []))
    
    # Wyświetl podstawowe informacje o graczu
    player = data.get('player', {})
    print(f"\nGracz: {player.get('name', 'Nieznany')}")
    print(f"Wiek: {player.get('age', 'Nieznany')}")
    print(f"Wykształcenie: {player.get('education', 'Brak')}")
    print(f"Moralność: {player.get('morality', 50)}/100")
    
    # Testuj systemy
    print("\n" + "=" * 30)
    print("TESTOWANIE SYSTEMÓW")
    print("=" * 30)
    
    # Test systemu rodziny
    print("\n1. System Rodziny:")
    family_system.show_family()
    
    # Test systemu biznesu
    print("\n2. System Biznesu:")
    business_system.show_businesses()
    
    # Test systemu nieruchomości
    print("\n3. System Nieruchomości:")
    property_system.show_properties()
    
    # Test systemu piłkarskiego
    print("\n4. System Piłkarski:")
    football_system.show_clubs()
    
    print("\n" + "=" * 50)
    print("Prototyp załadowany pomyślnie!")
    print("Możesz teraz rozbudowywać poszczególne systemy.")
    print("=" * 50)

if __name__ == "__main__":
    main()