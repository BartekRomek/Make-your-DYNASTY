"""
System dynamicznych wydarzeń
"""

class EventsSystem:
    def __init__(self, events):
        self.events = events

    def trigger_event(self, type_):
        for event in self.events:
            if event["type"] == type_:
                print(f"Wydarzenie: {event['description']}. Efekt: {event['effect']}")
                return
        print("Brak takiego wydarzenia.")

    def list_events(self):
        for event in self.events:
            print(f"{event['type']}: {event['description']}")