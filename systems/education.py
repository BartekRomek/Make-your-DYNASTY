"""
System edukacji i rozwoju umiejętności
"""

import random

class EducationSystem:
    def __init__(self, player_data):
        self.education = player_data.get("education", "")
        self.skills = player_data.get("skills", {})
    
    def study(self, skill, amount=5):
        """Rozwija umiejętność"""
        cost = amount * 1000  # Koszt za punkt umiejętności
        current_level = self.skills.get(skill, 0)
        
        if current_level >= 100:
            print(f"❌ Umiejętność {skill} jest już na maksymalnym poziomie!")
            return False
        
        print(f"📚 Rozwijasz umiejętność: {skill}")
        print(f"💰 Koszt: {cost:,} PLN")
        print(f"📈 Obecny poziom: {current_level}/100")
        
        # Zwiększ umiejętność
        new_level = min(100, current_level + amount)
        self.skills[skill] = new_level
        
        print(f"✅ Umiejętność rozwinięta! Nowy poziom: {new_level}/100")
        
        # Bonus za osiągnięcie pełnego poziomu
        if new_level == 100:
            print(f"🏆 Osiągnąłeś mistrzostwo w {skill}!")
        
        return True
    
    def show_skills(self):
        """Wyświetla umiejętności gracza"""
        print("\n🎯 UMIEJĘTNOŚCI GRACZA:")
        print("=" * 40)
        
        for skill, value in self.skills.items():
            # Pasek postępu
            bar_length = 20
            filled = int((value / 100) * bar_length)
            bar = "█" * filled + "░" * (bar_length - filled)
            
            # Określ poziom
            if value >= 90:
                level = "Mistrz"
            elif value >= 75:
                level = "Ekspert"
            elif value >= 50:
                level = "Zaawansowany"
            elif value >= 25:
                level = "Średnio-zaawansowany"
            else:
                level = "Początkujący"
            
            print(f"🎯 {skill.capitalize():<15} [{bar}] {value:3d}/100 ({level})")
    
    def take_course(self, course_type):
        """Bierze udział w kursie"""
        courses = {
            "MBA": {
                "cost": 100000,
                "duration": 6,  # miesięcy
                "skills": {"management": 20, "negotiation": 15},
                "description": "Master of Business Administration"
            },
            "Programming": {
                "cost": 25000,
                "duration": 3,
                "skills": {"technology": 25},
                "description": "Kurs programowania i technologii"
            },
            "Psychology": {
                "cost": 30000,
                "duration": 4,
                "skills": {"manipulation": 20, "negotiation": 10},
                "description": "Psychologia w biznesie"
            },
            "Finance": {
                "cost": 50000,
                "duration": 4,
                "skills": {"management": 15, "negotiation": 10},
                "description": "Zarządzanie finansami"
            }
        }
        
        if course_type not in courses:
            print("❌ Nieznany typ kursu!")
            return False
        
        course = courses[course_type]
        print(f"\n📚 KURS: {course_type}")
        print(f"📖 {course['description']}")
        print(f"💰 Koszt: {course['cost']:,} PLN")
        print(f"⏰ Czas trwania: {course['duration']} miesięcy")
        print("📈 Rozwój umiejętności:")
        
        for skill, bonus in course['skills'].items():
            current = self.skills.get(skill, 0)
            new_level = min(100, current + bonus)
            print(f"   {skill.capitalize()}: {current} → {new_level}")
        
        choice = input("\nCzy chcesz zapisać się na kurs? (t/n): ").strip().lower()
        
        if choice == 't':
            # Zastosuj bonusy
            for skill, bonus in course['skills'].items():
                self.skills[skill] = min(100, self.skills.get(skill, 0) + bonus)
            
            print(f"✅ Zapisałeś się na kurs {course_type}!")
            print("📚 Umiejętności zostały rozwinięte!")
            return True
        
        return False
    
    def get_certification(self, field):
        """Zdobywa certyfikat w danej dziedzinie"""
        certifications = {
            "Project Management": {"cost": 15000, "skill": "management", "bonus": 10},
            "Digital Marketing": {"cost": 12000, "skill": "negotiation", "bonus": 8},
            "Data Analysis": {"cost": 18000, "skill": "technology", "bonus": 12},
            "Leadership": {"cost": 20000, "skill": "management", "bonus": 15}
        }
        
        if field not in certifications:
            print("❌ Nieznany certyfikat!")
            return False
        
        cert = certifications[field]
        skill = cert['skill']
        current_level = self.skills.get(skill, 0)
        
        if current_level >= 90:
            print(f"📜 Zdobywasz certyfikat: {field}")
            print(f"🎯 Bonus do {skill}: +{cert['bonus']}")
            print(f"💰 Koszt: {cert['cost']:,} PLN")
            
            self.skills[skill] = min(100, current_level + cert['bonus'])
            print("✅ Certyfikat zdobyty!")
            return True
        else:
            print(f"❌ Potrzebujesz minimum 90 punktów w {skill} aby zdobyć ten certyfikat!")
            print(f"📊 Obecny poziom: {current_level}/100")
            return False
    
    def mentor_training(self):
        """Trening z mentorem"""
        mentors = [
            {"name": "Prof. Anna Kowalska", "speciality": "management", "cost": 50000},
            {"name": "Dr. Piotr Nowak", "speciality": "technology", "cost": 40000},
            {"name": "Mgr. Maria Zielińska", "speciality": "negotiation", "cost": 45000},
            {"name": "Ekspert Jan Wiśniewski", "speciality": "manipulation", "cost": 60000}
        ]
        
        print("\n👨‍🏫 DOSTĘPNI MENTORZY:")
        for i, mentor in enumerate(mentors, 1):
            print(f"{i}. {mentor['name']} - {mentor['speciality']} ({mentor['cost']:,} PLN)")
        
        try:
            choice = int(input("Wybierz mentora (0 = anuluj): "))
            if choice == 0:
                return False
            
            if 1 <= choice <= len(mentors):
                mentor = mentors[choice - 1]
                skill = mentor['speciality']
                
                print(f"\n👨‍🏫 Trening z: {mentor['name']}")
                print(f"🎯 Specjalizacja: {skill}")
                print(f"💰 Koszt: {mentor['cost']:,} PLN")
                
                current = self.skills.get(skill, 0)
                bonus = random.randint(15, 25)  # Losowy bonus
                new_level = min(100, current + bonus)
                
                print(f"📈 {skill.capitalize()}: {current} → {new_level}")
                
                if input("Kontynuować? (t/n): ").strip().lower() == 't':
                    self.skills[skill] = new_level
                    print("✅ Trening zakończony sukcesem!")
                    
                    if new_level == 100:
                        print(f"🏆 Osiągnąłeś mistrzostwo w {skill} dzięki mentorowi!")
                    
                    return True
            else:
                print("❌ Nieprawidłowy wybór!")
        except ValueError:
            print("❌ Podaj prawidłowy numer!")
        
        return False