"""
System klubów piłkarskich
"""

class FootballSystem:
    def __init__(self, clubs):
        self.clubs = clubs
    
    def manage_club(self, club_name):
        for club in self.clubs:
            if club["name"] == club_name:
                print(f"Zarządzasz klubem {club_name} w lidze {club['league']}. Budżet: {club['budget']} PLN")
                return
        print("Nie znaleziono klubu.")

    def transfer_player(self, club_name, player_name, amount):
        print(f"Transferujesz {player_name} do klubu {club_name} za {amount} PLN.")

    def show_clubs(self):
        for c in self.clubs:
            print(f"{c['name']} – liga: {c['league']}, budżet: {c['budget']} PLN, fani: {c['fans']}")