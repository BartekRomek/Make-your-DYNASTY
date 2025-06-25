"""
System edukacji i rozwoju umiejętności
"""

class EducationSystem:
    def __init__(self, player_data):
        self.education = player_data.get("education", "")
        self.skills = player_data.get("skills", {})
    
    def study(self, skill, amount=5):
        self.skills[skill] = self.skills.get(skill, 0) + amount
        print(f"Rozwijasz umiejętność {skill}. Aktualny poziom: {self.skills[skill]}")

    def show_skills(self):
        print("Umiejętności gracza:")
        for s, v in self.skills.items():
            print(f"{s}: {v}")