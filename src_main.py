"""
Główny plik prototypu gry "Symulator Dynastii"
"""

from systems.family import FamilySystem
from systems.business import BusinessSystem
from systems.crime import CrimeSystem
from systems.football import FootballSystem
from systems.education import EducationSystem
from systems.events import EventsSystem
from systems.property import PropertySystem

def main():
    print("Witaj w prototypie gry Symulator Dynastii!")
    # Tu można załadować sample_data.yaml i zainicjować główne systemy.
    # Przykład (do rozbudowy):
    # family = FamilySystem(...)
    # business = BusinessSystem(...)
    # crime = CrimeSystem(...)
    # football = FootballSystem(...)
    # education = EducationSystem(...)
    # events = EventsSystem(...)
    # property = PropertySystem(...)
    # Główna pętla gry/prototypu
    
    print("Załaduj sample_data.yaml i rozpocznij testowanie systemów!")

if __name__ == "__main__":
    main()