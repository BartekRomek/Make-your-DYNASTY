"""
Silnik gry Dynasty Simulator - pełna wersja gry
"""

import yaml
import os
import time
import random
from systems.family import FamilySystem
from systems.business import BusinessSystem
from systems.crime import CrimeSystem
from systems.football import FootballSystem
from systems.education import EducationSystem
from systems.events import EventsSystem
from systems.property import PropertySystem
from save_system import SaveSystem

class DynastyGame:
    def __init__(self):
        self.running = True
        self.player_data = None
        self.game_data = None
        self.systems = {}
        self.turn = 1
        self.month = 1
        self.year = 2025
        self.save_system = SaveSystem(self)
        
    def load_game_data(self):
        """Ładuje dane gry z pliku YAML"""
        try:
            with open('sample_data.yaml', 'r', encoding='utf-8') as file:
                self.game_data = yaml.safe_load(file)
                self.player_data = self.game_data.get('player', {})
                return True
        except FileNotFoundError:
            print("❌ Nie znaleziono pliku sample_data.yaml!")
            return False
        except yaml.YAMLError as e:
            print(f"❌ Błąd podczas wczytywania pliku YAML: {e}")
            return False
    
    def initialize_systems(self):
        """Inicjalizuje wszystkie systemy gry"""
        self.systems = {
            'family': FamilySystem(self.player_data),
            'business': BusinessSystem(self.game_data.get('businesses', [])),
            'crime': CrimeSystem(self.game_data.get('underworld_contacts', [])),
            'football': FootballSystem(self.game_data.get('clubs', [])),
            'education': EducationSystem(self.player_data),
            'events': EventsSystem(self.game_data.get('events', [])),
            'property': PropertySystem(self.game_data.get('properties', []))
        }
    
    def clear_screen(self):
        """Czyści ekran"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def print_header(self):
        """Wyświetla nagłówek gry"""
        print("=" * 60)
        print("🏰 DYNASTY SIMULATOR - ZBUDUJ SWOJĄ DYNASTIĘ 🏰")
        print("=" * 60)
        print(f"📅 {self.month:02d}/{self.year} | Tura: {self.turn}")
        print(f"👤 {self.player_data.get('name', 'Gracz')} | Wiek: {self.player_data.get('age', 0)}")
        print(f"💰 Gotówka: {self.get_total_money():,} PLN | Moralność: {self.player_data.get('morality', 50)}/100")
        print("=" * 60)
    
    def get_total_money(self):
        """Oblicza całkowitą gotówkę gracza"""
        total = 0
        # Przychody z biznesów
        for business in self.game_data.get('businesses', []):
            total += business.get('revenue', 0)
        
        # Wartość nieruchomości (część dostępna)
        for prop in self.game_data.get('properties', []):
            if prop.get('rented', False):
                total += prop.get('value', 0) * 0.05  # 5% miesięcznego zysku z wynajmu
        
        return int(total)
    
    def show_main_menu(self):
        """Wyświetla główne menu gry"""
        print("\n🎮 GŁÓWNE MENU")
        print("-" * 30)
        print("1. 👨‍👩‍👧‍👦 Rodzina")
        print("2. 🏢 Biznes")
        print("3. 🏠 Nieruchomości")
        print("4. ⚽ Piłka nożna")
        print("5. 🎓 Edukacja")
        print("6. 🌑 Półświatek")
        print("7. 📰 Wydarzenia")
        print("8. 📊 Status gracza")
        print("9. ⏭️  Następna tura")
        print("=" * 30)
        print("💾 ZAPIS I WCZYTYWANIE")
        print("S. 💾 Zapisz grę")
        print("L. 📂 Wczytaj grę")
        print("Q. ⚡ Szybki zapis")
        print("E. 📊 Eksportuj statystyki")
        print("=" * 30)
        print("0. 🚪 Wyjście")
        print("-" * 30)
    
    def handle_save_load_menu(self, choice):
        """Obsługuje opcje zapisu i wczytywania"""
        if choice.upper() == 'S':
            save_name = input("Podaj nazwę zapisu (Enter = automatyczna): ").strip()
            if save_name:
                self.save_system.save_game(save_name)
            else:
                self.save_system.save_game()
            input("Naciśnij Enter...")
            
        elif choice.upper() == 'L':
            saves = self.save_system.list_saves()
            if saves:
                try:
                    choice = int(input("Wybierz zapis do wczytania (0 = anuluj): "))
                    if choice > 0 and choice <= len(saves):
                        save_info = saves[choice - 1]
                        if 'error' not in save_info:
                            self.save_system.load_game(save_info['name'])
                        else:
                            print("❌ Nie można wczytać uszkodzonego zapisu!")
                except ValueError:
                    print("❌ Podaj prawidłowy numer!")
            input("Naciśnij Enter...")
            
        elif choice.upper() == 'Q':
            self.save_system.quick_save()
            input("Naciśnij Enter...")
            
        elif choice.upper() == 'E':
            self.save_system.export_stats()
            input("Naciśnij Enter...")
    
    def next_turn(self):
        """Przechodzi do następnej tur - autoSave"""
        print("\n⏭️  NASTĘPNA TURA")
        print("⏳ Przetwarzanie...")
        
        # Automatyczny zapis co 5 tur
        if self.turn % 5 == 0:
            print("💾 Wykonuję automatyczny zapis...")
            self.save_system.auto_save()
        
        time.sleep(1)
        
        # Zwiększ wiek co 12 tur (miesięcy)
        if self.turn % 12 == 0:
            self.player_data['age'] += 1
            print(f"🎂 Masz urodziny! Teraz masz {self.player_data['age']} lat!")
        
        # Pasywne przychody
        total_income = 0
        for business in self.game_data.get('businesses', []):
            monthly_income = int(business['revenue'] * 0.1)  # 10% miesięcznego przychodu
            total_income += monthly_income
        
        for prop in self.game_data.get('properties', []):
            if prop.get('rented', False):
                rental_income = int(prop['value'] * 0.05)  # 5% wartości miesięcznie
                total_income += rental_income
        
        if total_income > 0:
            print(f"💰 Pasywne przychody tego miesiąca: {total_income:,} PLN")
        
        # Losowe wydarzenie (30% szansy)
        if random.randint(1, 100) <= 30:
            self.handle_events()
        
        # Aktualizuj datę
        self.month += 1
        if self.month > 12:
            self.month = 1
            self.year += 1
        
        self.turn += 1
        
        print("✅ Tura zakończona!")
        input("Naciśnij Enter aby kontynuować...")
    
    def run(self):
        """Główna pętla gry"""
        self.clear_screen()
        
        # Sprawdź czy wczytać grę
        print("🎮 Dynasty Simulator")
        print("1. 🆕 Nowa gra")
        print("2. 📂 Wczytaj grę")
        
        start_choice = input("Wybierz opcję: ").strip()
        
        if start_choice == "2":
            saves = self.save_system.list_saves()
            if saves:
                try:
                    choice = int(input("Wybierz zapis (0 = nowa gra): "))
                    if choice > 0 and choice <= len(saves):
                        save_info = saves[choice - 1]
                        if 'error' not in save_info:
                            if self.save_system.load_game(save_info['name']):
                                print("✅ Gra wczytana pomyślnie!")
                            else:
                                print("❌ Nie udało się wczytać gry. Rozpoczynam nową grę.")
                                if not self.load_game_data():
                                    return
                                self.initialize_systems()
                        else:
                            print("❌ Uszkodzony zapis. Rozpoczynam nową grę.")
                            if not self.load_game_data():
                                return
                            self.initialize_systems()
                    else:
                        if not self.load_game_data():
                            return
                        self.initialize_systems()
                except ValueError:
                    if not self.load_game_data():
                        return
                    self.initialize_systems()
            else:
                if not self.load_game_data():
                    return
                self.initialize_systems()
        else:
            if not self.load_game_data():
                return
            self.initialize_systems()
        
        print("🎮 Ładowanie gry...")
        time.sleep(2)
        
        while self.running:
            self.clear_screen()
            self.print_header()
            self.show_main_menu()
            
            choice = input("\n🎯 Wybierz opcję: ").strip()
            
            if choice == "1":
                self.handle_family_menu()
            elif choice == "2":
                self.handle_business_menu()
            elif choice == "3":
                self.handle_property_menu()
            elif choice == "4":
                self.handle_football_menu()
            elif choice == "5":
                self.handle_education_menu()
            elif choice == "6":
                self.handle_crime_menu()
            elif choice == "7":
                self.handle_events()
                input("Naciśnij Enter...")
            elif choice == "8":
                self.show_player_status()
                input("Naciśnij Enter...")
            elif choice == "9":
                self.next_turn()
            elif choice.upper() in ['S', 'L', 'Q', 'E']:
                self.handle_save_load_menu(choice)
            elif choice == "0":
                print("💾 Zapisać grę przed wyjściem? (t/n)")
                if input().strip().lower() == 't':
                    self.save_system.save_game()
                print("👋 Dziękujemy za grę w Dynasty Simulator!")
                self.running = False
            else:
                print("❌ Nieprawidłowy wybór!")
                time.sleep(1)

    # Tu będą wszystkie pozostałe metody z poprzedniego pliku...
    # Dodaję je teraz:

    def show_player_status(self):
        """Wyświetla szczegółowy status gracza"""
        print("\n📊 STATUS GRACZA")
        print("=" * 40)
        
        player = self.player_data
        print(f"👤 Imię: {player.get('name', 'Nieznane')}")
        print(f"🎂 Wiek: {player.get('age', 0)} lat")
        print(f"🎓 Wykształcenie: {player.get('education', 'Brak')}")
        print(f"😇 Moralność: {player.get('morality', 50)}/100")
        
        print("\n🎯 UMIEJĘTNOŚCI:")
        skills = player.get('skills', {})
        for skill, value in skills.items():
            bar = "█" * (value // 5) + "░" * (20 - value // 5)
            print(f"  {skill.capitalize()}: [{bar}] {value}/100")
        
        print("\n📈 REPUTACJA:")
        reputation = player.get('reputation', {})
        for rep_type, value in reputation.items():
            bar = "█" * (value // 5) + "░" * (20 - value // 5)
            print(f"  {rep_type.capitalize()}: [{bar}] {value}/100")
        
        print("\n💰 FINANSE:")
        print(f"  Całkowita wartość: {self.get_total_money():,} PLN")
        print(f"  Liczba biznesów: {len(self.game_data.get('businesses', []))}")
        print(f"  Liczba nieruchomości: {len(self.game_data.get('properties', []))}")

    def handle_family_menu(self):
        """Obsługuje menu rodziny"""
        while True:
            print("\n👨‍👩‍👧‍👦 MENU RODZINY")
            print("-" * 25)
            print("1. 👥 Pokaż rodzinę")
            print("2. 💒 Małżeństwo/Związek")
            print("3. 👶 Dzieci")
            print("4. ⚡ Konflikty rodzinne")
            print("0. ⬅️  Powrót")
            
            choice = input("\nWybierz opcję: ").strip()
            
            if choice == "1":
                self.systems['family'].show_family()
            elif choice == "2":
                self.handle_marriage()
            elif choice == "3":
                self.handle_children()
            elif choice == "4":
                self.systems['family'].conflict()
            elif choice == "0":
                break
            else:
                print("❌ Nieprawidłowy wybór!")
            
            input("\nNaciśnij Enter aby kontynuować...")

    def handle_marriage(self):
        """Obsługuje małżeństwo"""
        family = self.player_data.get('family', {})
        if family.get('spouse'):
            print(f"💍 Jesteś już w związku z: {family['spouse']}")
            print("1. 💔 Rozwód")
            print("2. 💝 Poprawa relacji")
            choice = input("Wybierz opcję: ").strip()
            
            if choice == "1":
                self.player_data['family']['spouse'] = None
                print("💔 Rozwód zakończony. Jesteś teraz singlem.")
                self.player_data['morality'] -= 5
            elif choice == "2":
                print("💝 Spędzasz czas z partnerem/partnerką. Relacja się poprawia!")
                self.player_data['morality'] += 2
        else:
            print("💕 Szukasz miłości...")
            names = ["Anna Nowak", "Katarzyna Wiśniewska", "Magdalena Kowalczyk", 
                    "Piotr Zieliński", "Michał Lewandowski", "Tomasz Wójcik"]
            partner = random.choice(names)
            print(f"💘 Poznałeś/aś {partner}!")
            
            choice = input("Czy chcesz rozpocząć związek? (t/n): ").strip().lower()
            if choice == 't':
                self.player_data.setdefault('family', {})['spouse'] = partner
                print(f"💍 Gratulacje! Jesteś teraz w związku z {partner}!")
                self.player_data['morality'] += 5

    def handle_children(self):
        """Obsługuje dzieci"""
        family = self.player_data.get('family', {})
        children = family.get('children', [])
        
        print(f"👶 Masz {len(children)} dzieci:")
        for i, child in enumerate(children, 1):
            print(f"  {i}. {child}")
        
        if len(children) < 5:  # Limit dzieci
            choice = input("\nCzy chcesz mieć dziecko? (t/n): ").strip().lower()
            if choice == 't':
                names = ["Aleksander", "Zofia", "Jan", "Maria", "Piotr", "Anna", "Michał", "Katarzyna"]
                child_name = random.choice(names)
                self.player_data.setdefault('family', {}).setdefault('children', []).append(child_name)
                print(f"🎉 Gratulacje! Urodziło się dziecko: {child_name}!")
                self.player_data['morality'] += 3

    def handle_business_menu(self):
        """Obsługuje menu biznesu"""
        while True:
            print("\n🏢 MENU BIZNESU")
            print("-" * 25)
            print("1. 📋 Pokaż biznesy")
            print("2. 🚀 Rozpocznij nowy biznes")
            print("3. 💰 Inwestuj w biznes")
            print("4. 🌑 Nielegalne działania")
            print("0. ⬅️  Powrót")
            
            choice = input("\nWybierz opcję: ").strip()
            
            if choice == "1":
                self.systems['business'].show_businesses()
            elif choice == "2":
                self.start_new_business()
            elif choice == "3":
                self.invest_in_business()
            elif choice == "4":
                self.illegal_business_actions()
            elif choice == "0":
                break
            else:
                print("❌ Nieprawidłowy wybór!")
            
            input("\nNaciśnij Enter aby kontynuować...")

    def start_new_business(self):
        """Rozpoczyna nowy biznes"""
        print("\n🚀 NOWY BIZNES")
        print("Dostępne typy biznesów:")
        business_types = [
            ("Restauracja", 50000, "restaurant"),
            ("Sklep internetowy", 30000, "ecommerce"),
            ("Firma IT", 100000, "tech"),
            ("Firma budowlana", 200000, "construction"),
            ("Hotel", 500000, "hotel")
        ]
        
        for i, (name, cost, _) in enumerate(business_types, 1):
            print(f"{i}. {name} (Koszt: {cost:,} PLN)")
        
        try:
            choice = int(input("\nWybierz typ biznesu: ")) - 1
            if 0 <= choice < len(business_types):
                name, cost, biz_type = business_types[choice]
                
                if self.get_total_money() >= cost:
                    business_name = input("Podaj nazwę firmy: ").strip()
                    city = input("Podaj miasto: ").strip() or "Warszawa"
                    
                    self.systems['business'].start_business(business_name, city, biz_type)
                    print(f"✅ Biznes {business_name} został założony!")
                    self.player_data['skills']['management'] += 5
                else:
                    print("❌ Nie masz wystarczających środków!")
            else:
                print("❌ Nieprawidłowy wybór!")
        except ValueError:
            print("❌ Podaj prawidłowy numer!")

    def invest_in_business(self):
        """Inwestuje w biznes"""
        businesses = self.game_data.get('businesses', [])
        if not businesses:
            print("❌ Nie masz żadnych biznesów!")
            return
        
        print("\n💰 INWESTYCJE")
        for i, business in enumerate(businesses, 1):
            print(f"{i}. {business['name']} - obecny przychód: {business['revenue']:,} PLN")
        
        try:
            choice = int(input("Wybierz biznes do inwestycji: ")) - 1
            if 0 <= choice < len(businesses):
                amount = int(input("Podaj kwotę inwestycji: "))
                if amount > 0 and self.get_total_money() >= amount:
                    self.systems['business'].invest(businesses[choice]['name'], amount)
                    self.player_data['skills']['management'] += 2
                else:
                    print("❌ Nieprawidłowa kwota lub brak środków!")
            else:
                print("❌ Nieprawidłowy wybór!")
        except ValueError:
            print("❌ Podaj prawidłowe liczby!")

    def illegal_business_actions(self):
        """Nielegalne działania biznesowe"""
        if self.player_data.get('morality', 50) > 70:
            print("😇 Twoja moralność jest zbyt wysoka dla nielegalnych działań!")
            return
        
        print("\n🌑 NIELEGALNE DZIAŁANIA")
        print("⚠️  UWAGA: Te działania są bardzo ryzykowne!")
        print("1. 💸 Pranie pieniędzy")
        print("2. 🤝 Łapówki")
        print("3. 📈 Manipulacja giełdowa")
        print("0. ⬅️  Powrót")
        
        choice = input("Wybierz akcję: ").strip()
        
        if choice == "1":
            risk = random.randint(1, 100)
            if risk < 30:
                print("🚨 Zostałeś przyłapany! Reputacja spada!")
                self.player_data['reputation']['personal'] -= 20
                self.player_data['morality'] -= 10
            else:
                money_gained = random.randint(50000, 200000)
                print(f"💰 Udało się! Zyskujesz {money_gained:,} PLN")
                self.player_data['morality'] -= 5
                self.player_data['skills']['manipulation'] += 3

    def handle_property_menu(self):
        """Obsługuje menu nieruchomości"""
        while True:
            print("\n🏠 MENU NIERUCHOMOŚCI")
            print("-" * 30)
            print("1. 🏘️  Pokaż nieruchomości")
            print("2. 🏪 Kup nieruchomość")
            print("3. 🏠 Wynajmij nieruchomość")
            print("0. ⬅️  Powrót")
            
            choice = input("\nWybierz opcję: ").strip()
            
            if choice == "1":
                self.systems['property'].show_properties()
            elif choice == "2":
                self.buy_property()
            elif choice == "3":
                self.rent_property()
            elif choice == "0":
                break
            else:
                print("❌ Nieprawidłowy wybór!")
            
            input("\nNaciśnij Enter aby kontynuować...")

    def buy_property(self):
        """Kupuje nieruchomość"""
        print("\n🏪 DOSTĘPNE NIERUCHOMOŚCI")
        properties = [
            ("Mieszkanie w bloku", 300000, "apartment"),
            ("Dom jednorodzinny", 800000, "house"),
            ("Luksusowa willa", 2000000, "villa"),
            ("Działka budowlana", 500000, "land"),
            ("Biurowiec", 5000000, "office")
        ]
        
        for i, (name, price, prop_type) in enumerate(properties, 1):
            print(f"{i}. {name} - {price:,} PLN")
        
        try:
            choice = int(input("Wybierz nieruchomość: ")) - 1
            if 0 <= choice < len(properties):
                name, price, prop_type = properties[choice]
                if self.get_total_money() >= price:
                    city = input("W jakim mieście? (domyślnie Warszawa): ").strip() or "Warszawa"
                    full_name = f"{name} w {city}"
                    self.systems['property'].buy_property(full_name, prop_type, price)
                    print("✅ Nieruchomość kupiona!")
                else:
                    print("❌ Nie masz wystarczających środków!")
            else:
                print("❌ Nieprawidłowy wybór!")
        except ValueError:
            print("❌ Podaj prawidłowy numer!")

    def rent_property(self):
        """Wynajmuje nieruchomość"""
        properties = self.game_data.get('properties', [])
        available = [p for p in properties if not p.get('rented', False)]
        
        if not available:
            print("❌ Nie masz dostępnych nieruchomości do wynajmu!")
            return
        
        print("\n🏠 DOSTĘPNE DO WYNAJMU:")
        for i, prop in enumerate(available, 1):
            monthly_income = int(prop['value'] * 0.05)
            print(f"{i}. {prop['name']} - potencjalny zysk: {monthly_income:,} PLN/miesiąc")
        
        try:
            choice = int(input("Wybierz nieruchomość: ")) - 1
            if 0 <= choice < len(available):
                prop_name = available[choice]['name']
                self.systems['property'].rent_property(prop_name)
                print("✅ Nieruchomość wynajęta!")
            else:
                print("❌ Nieprawidłowy wybór!")
        except ValueError:
            print("❌ Podaj prawidłowy numer!")

    def handle_football_menu(self):
        """Obsługuje menu piłkarskie"""
        while True:
            print("\n⚽ MENU PIŁKARSKIE")
            print("-" * 25)
            print("1. 🏟️  Pokaż kluby")
            print("2. 💰 Zarządzaj klubem")
            print("3. 🏆 Rozegraj mecz")
            print("0. ⬅️  Powrót")
            
            choice = input("\nWybierz opcję: ").strip()
            
            if choice == "1":
                self.systems['football'].show_clubs()
            elif choice == "2":
                self.manage_football_club()
            elif choice == "3":
                self.play_football_match()
            elif choice == "0":
                break
            else:
                print("❌ Nieprawidłowy wybór!")
            
            input("\nNaciśnij Enter aby kontynuować...")

    def manage_football_club(self):
        """Zarządza klubem piłkarskim"""
        clubs = self.game_data.get('clubs', [])
        if not clubs:
            print("❌ Nie masz żadnych klubów!")
            return
        
        print("\n🏟️ ZARZĄDZANIE KLUBEM")
        for i, club in enumerate(clubs, 1):
            print(f"{i}. {club['name']}")
        
        try:
            choice = int(input("Wybierz klub: ")) - 1
            if 0 <= choice < len(clubs):
                club = clubs[choice]
                print(f"\n⚽ Zarządzasz klubem: {club['name']}")
                print(f"💰 Budżet: {club['budget']:,} PLN")
                print(f"🏟️ Stadion: {club['stadium']}")
                print(f"👥 Fani: {club['fans']:,}")
                print(f"📊 Liga: {club['league']}")
                
                print("\n1. 💰 Zwiększ budżet")
                print("2. 🏟️ Rozbuduj stadion")
                print("3. 👥 Kampania marketingowa")
                
                action = input("Wybierz akcję: ").strip()
                
                if action == "1":
                    investment = int(input("Podaj kwotę inwestycji: "))
                    if self.get_total_money() >= investment:
                        club['budget'] += investment
                        print(f"✅ Budżet klubu zwiększony o {investment:,} PLN!")
                    else:
                        print("❌ Nie masz wystarczających środków!")
                
        except ValueError:
            print("❌ Podaj prawidłowy numer!")

    def play_football_match(self):
        """Rozgrywa mecz piłkarski"""
        clubs = self.game_data.get('clubs', [])
        if not clubs:
            print("❌ Nie masz żadnych klubów!")
            return
        
        print("\n🏆 MECZ PIŁKARSKI")
        for i, club in enumerate(clubs, 1):
            print(f"{i}. {club['name']}")
        
        try:
            choice = int(input("Wybierz swój klub: ")) - 1
            if 0 <= choice < len(clubs):
                my_club = clubs[choice]
                opponent = f"{random.choice(['Legia', 'Wisła', 'Lech', 'Cracovia'])} {random.choice(['Warszawa', 'Kraków', 'Poznań'])}"
                
                print(f"\n⚽ {my_club['name']} vs {opponent}")
                print("🎮 Rozgrywamy mecz...")
                time.sleep(2)
                
                my_goals = random.randint(0, 4)
                opp_goals = random.randint(0, 4)
                
                print(f"🥅 Wynik: {my_club['name']} {my_goals} - {opp_goals} {opponent}")
                
                if my_goals > opp_goals:
                    print("🎉 ZWYCIĘSTWO!")
                    my_club['fans'] = int(my_club['fans'] * 1.05)
                    my_club['budget'] += 50000
                    print("👥 Liczba fanów wzrosła!")
                    print("💰 Budżet wzrósł o 50,000 PLN!")
                elif my_goals == opp_goals:
                    print("🤝 REMIS!")
                    my_club['budget'] += 20000
                else:
                    print("😞 PORAŻKA!")
                    my_club['fans'] = int(my_club['fans'] * 0.98)
                    print("👥 Niektórzy fani są rozczarowani...")
        except ValueError:
            print("❌ Podaj prawidłowy numer!")

    def handle_education_menu(self):
        """Obsługuje menu edukacji"""
        while True:
            print("\n🎓 MENU EDUKACJI")
            print("-" * 25)
            print("1. 🎯 Pokaż umiejętności")
            print("2. 📚 Rozwijaj umiejętności")
            print("3. 🎓 Weź udział w kursie")
            print("0. ⬅️  Powrót")
            
            choice = input("\nWybierz opcję: ").strip()
            
            if choice == "1":
                self.systems['education'].show_skills()
            elif choice == "2":
                self.develop_skills()
            elif choice == "3":
                self.take_course()
            elif choice == "0":
                break
            else:
                print("❌ Nieprawidłowy wybór!")
            
            input("\nNaciśnij Enter aby kontynuować...")

    def develop_skills(self):
        """Rozwija umiejętności"""
        skills = self.player_data.get('skills', {})
        print("\n🎯 ROZWÓJ UMIEJĘTNOŚCI")
        
        skill_list = list(skills.keys())
        for i, skill in enumerate(skill_list, 1):
            print(f"{i}. {skill.capitalize()} ({skills[skill]}/100)")
        
        try:
            choice = int(input("Wybierz umiejętność do rozwoju: ")) - 1
            if 0 <= choice < len(skill_list):
                skill = skill_list[choice]
                amount = int(input("O ile punktów rozwinąć? (1-10): "))
                if 1 <= amount <= 10:
                    self.systems['education'].study(skill, amount)
                else:
                    print("❌ Nieprawidłowa wartość!")
            else:
                print("❌ Nieprawidłowy wybór!")
        except ValueError:
            print("❌ Podaj prawidłowe liczby!")

    def take_course(self):
        """Bierze udział w kursie"""
        print("\n📚 DOSTĘPNE KURSY")
        courses = ["MBA", "Programming", "Psychology", "Finance"]
        
        for i, course in enumerate(courses, 1):
            print(f"{i}. {course}")
        
        try:
            choice = int(input("Wybierz kurs: ")) - 1
            if 0 <= choice < len(courses):
                course = courses[choice]
                self.systems['education'].take_course(course)
            else:
                print("❌ Nieprawidłowy wybór!")
        except ValueError:
            print("❌ Podaj prawidłowy numer!")

    def handle_crime_menu(self):
        """Obsługuje menu półświatka"""
        while True:
            print("\n🌑 MENU PÓŁŚWIATKA")
            print("-" * 25)
            print("1. 👥 Pokaż kontakty")
            print("2. 💰 Wykonaj przestępstwo")
            print("3. 🤝 Spotkaj się z kontaktem")
            print("0. ⬅️  Powrót")
            
            choice = input("\nWybierz opcję: ").strip()
            
            if choice == "1":
                self.systems['crime'].show_contacts()
            elif choice == "2":
                self.commit_crime()
            elif choice == "3":
                self.meet_crime_contact()
            elif choice == "0":
                break
            else:
                print("❌ Nieprawidłowy wybór!")
            
            input("\nNaciśnij Enter aby kontynuować...")

    def commit_crime(self):
        """Wykonuje przestępstwo"""
        if self.player_data.get('morality', 50) > 70:
            print("😇 Twoja moralność jest zbyt wysoka dla takich działań!")
            return
        
        crimes = ["laundering", "smuggling", "extortion", "fraud"]
        print("\n💰 DOSTĘPNE PRZESTĘPSTWA")
        
        for i, crime in enumerate(crimes, 1):
            print(f"{i}. {crime.capitalize()}")
        
        try:
            choice = int(input("Wybierz rodzaj przestępstwa: ")) - 1
            if 0 <= choice < len(crimes):
                crime = crimes[choice]
                reward = self.systems['crime'].do_crime(crime)
                if reward > 0:
                    print(f"💰 Zyskujesz {reward:,} PLN!")
                elif reward < 0:
                    print(f"💸 Tracisz {abs(reward):,} PLN!")
            else:
                print("❌ Nieprawidłowy wybór!")
        except ValueError:
            print("❌ Podaj prawidłowy numer!")

    def meet_crime_contact(self):
        """Spotyka się z kontaktem z półświatka"""
        contacts = self.game_data.get('underworld_contacts', [])
        if not contacts:
            print("❌ Nie masz żadnych kontaktów w półświatku!")
            return
        
        print("\n🤝 KONTAKTY")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} ({contact['role']})")
        
        try:
            choice = int(input("Z kim chcesz się spotkać: ")) - 1
            if 0 <= choice < len(contacts):
                contact = contacts[choice]
                self.systems['crime'].meet_contact(contact['name'])
            else:
                print("❌ Nieprawidłowy wybór!")
        except ValueError:
            print("❌ Podaj prawidłowy numer!")

    def handle_events(self):
        """Obsługuje wydarzenia"""
        events = self.game_data.get('events', [])
        if not events:
            print("❌ Brak aktualnych wydarzeń!")
            return
        
        event = random.choice(events)
        print(f"\n📰 WYDARZENIE: {event['type'].upper()}")
        print(f"📝 {event['description']}")
        print(f"⚠️  Ryzyko: {event['risk']}/100")
        print(f"💥 Efekt: {event['effect']}")
        
        if event['type'] == 'scandal':
            self.player_data['reputation']['business'] -= event['risk'] // 2
            print(f"📉 Reputacja biznesowa spadła o {event['risk'] // 2}!")
        elif event['type'] == 'crisis':
            for business in self.game_data.get('businesses', []):
                business['revenue'] = int(business['revenue'] * 0.9)
            print("📉 Przychody wszystkich biznesów spadły o 10%!")

if __name__ == "__main__":
    game = DynastyGame()
    game.run()
