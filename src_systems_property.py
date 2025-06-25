"""
Nieruchomości, rozbudowa posiadłości, wynajem
"""

class PropertySystem:
    def __init__(self, properties):
        self.properties = properties
    
    def buy_property(self, name, type_, value):
        new = {"name": name, "type": type_, "value": value, "rented": False}
        self.properties.append(new)
        print(f"Kupiono nieruchomość: {name} ({type_}) za {value} PLN.")

    def rent_property(self, name):
        for p in self.properties:
            if p["name"] == name:
                if not p["rented"]:
                    p["rented"] = True
                    print(f"Nieruchomość {name} została wynajęta.")
                else:
                    print(f"{name} już jest wynajmowana.")
                return
        print("Nie znaleziono nieruchomości.")

    def show_properties(self):
        for p in self.properties:
            print(f"{p['name']} ({p['type']}): {p['value']} PLN, wynajem: {'tak' if p['rented'] else 'nie'}")