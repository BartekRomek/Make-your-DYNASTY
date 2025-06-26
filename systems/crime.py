"""
System półświatka, kontaktów z mafią
"""

import random

class CrimeSystem:
    def __init__(self, underworld_contacts):
        self.contacts = underworld_contacts
    
    def show_contacts(self):
        """Wyświetla kontakty z półświatkiem"""
        print("\n🌑 KONTAKTY Z PÓŁŚWIATKIEM:")
        for contact in self.contacts:
            trust_bar = "█" * (contact['trust'] // 5) + "░" * (20 - contact['trust'] // 5)
            risk_bar = "█" * (contact['risk'] // 5) + "░" * (20 - contact['risk'] // 5)
            print(f"👤 {contact['name']} ({contact['role']})")
            print(f"   Zaufanie: [{trust_bar}] {contact['trust']}/100")
            print(f"   Ryzyko:   [{risk_bar}] {contact['risk']}/100")
    
    def do_crime(self, crime_type="laundering"):
        """Wykonuje przestępstwo"""
        print(f"🌑 Wykonujesz przestępstwo: {crime_type}")
        
        crimes = {
            "laundering": {"reward": 100000, "risk": 40, "description": "Pranie brudnych pieniędzy"},
            "smuggling": {"reward": 150000, "risk": 60, "description": "Przemyt towarów"},
            "extortion": {"reward": 80000, "risk": 30, "description": "Wymuszenia"},
            "fraud": {"reward": 120000, "risk": 50, "description": "Oszustwa finansowe"}
        }
        
        if crime_type in crimes:
            crime = crimes[crime_type]
            print(f"📋 {crime['description']}")
            print(f"💰 Potencjalna nagroda: {crime['reward']:,} PLN")
            print(f"⚠️ Ryzyko: {crime['risk']}/100")
            
            # Symulacja przestępstwa
            success_chance = 100 - crime['risk']
            if random.randint(1, 100) <= success_chance:
                print("✅ Przestępstwo zakończone sukcesem!")
                return crime['reward']
            else:
                print("❌ Zostałeś przyłapany! Konsekwencje...")
                if random.randint(1, 100) <= 30:
                    self.betrayal()
                return -crime['reward'] // 2  # Strata
        
        return 0

    def betrayal(self):
        """Zdrada przez kontakt"""
        if self.contacts:
            traitor = random.choice(self.contacts)
            print(f"🔪 {traitor['name']} cię zdradził!")
            print("💸 Tracisz część majątku i reputacji!")
            self.contacts.remove(traitor)
            return traitor
        return None
    
    def meet_contact(self, name):
        """Spotyka się z kontaktem"""
        for contact in self.contacts:
            if contact["name"] == name:
                print(f"🤝 Spotykasz się z: {name}")
                print(f"🎭 Rola: {contact['role']}")
                print(f"💯 Zaufanie: {contact['trust']}/100")
                print(f"⚠️ Ryzyko: {contact['risk']}/100")
                
                # Możliwość poprawy relacji
                if random.randint(1, 100) <= 50:
                    contact['trust'] = min(100, contact['trust'] + 5)
                    print("📈 Zaufanie wzrosło!")
                
                return contact
        print("❌ Nie znaleziono kontaktu.")
        return None