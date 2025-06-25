"""
Mechaniki biznesu, giełdy, inwestycji
"""

class BusinessSystem:
    def __init__(self, businesses):
        self.businesses = businesses
    
    def start_business(self, name, city, type_):
        new = {"name": name, "city": city, "type": type_, "legal": True, "revenue": 0, "employees": 1, "branches": []}
        self.businesses.append(new)
        print(f"Rozpoczęto biznes: {name} w mieście {city}")

    def invest(self, business_name, amount):
        for b in self.businesses:
            if b["name"] == business_name:
                b["revenue"] += amount
                print(f"Zainwestowano {amount} w firmę {business_name}.")
                return
        print("Nie znaleziono firmy.")

    def illegal_action(self, business_name, action="money_laundering"):
        for b in self.businesses:
            if b["name"] == business_name:
                print(f"Firma {business_name} wykonuje nielegalną akcję: {action}!")
                return

    def show_businesses(self):
        for b in self.businesses:
            print(f"{b['name']} ({b['city']}): {b['revenue']} PLN")