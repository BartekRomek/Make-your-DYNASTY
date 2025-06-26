"""
Mechaniki rodziny i dziedziczenia
"""

class FamilySystem:
    def __init__(self, player_data):
        self.family = player_data.get("family", {})
        self.morality = player_data.get("morality", 50)
    
    def add_child(self, name):
        self.family.setdefault("children", []).append(name)
    
    def conflict(self, type="inheritance"):
        if type == "inheritance":
            print("Konflikt o majątek! Musisz podjąć decyzję jak rozwiązać spór w rodzinie.")
        # Rozbuduj o inne typy konfliktów rodzinnych

    def show_family(self):
        print("Rodzina gracza:")
        for role, members in self.family.items():
            print(f"{role}: {members}")