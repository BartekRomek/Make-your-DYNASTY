"""
Mechaniki nielegalne, półświatek, ryzyko
"""

class CrimeSystem:
    def __init__(self, underworld_contacts):
        self.contacts = underworld_contacts
    
    def do_crime(self, crime_type="laundering"):
        print(f"Wykonujesz przestępstwo: {crime_type}.")
        # Losuj ryzyko, efekty, zdrady, itp.
    
    def betrayal(self):
        print("Twój kontakt z półświatka zdradził cię! Tracisz majątek lub trafiasz do więzienia.")

    def show_contacts(self):
        for c in self.contacts:
            print(f"{c['name']} ({c['role']}) – zaufanie: {c['trust']}, ryzyko zdrady: {c['risk']}")