"""
System zapisu i wczytywania gry Dynasty Simulator
"""

import yaml
import json
import os
from datetime import datetime

class SaveSystem:
    def __init__(self, game_instance):
        self.game = game_instance
        self.saves_dir = "saves"
        self.ensure_saves_directory()
    
    def ensure_saves_directory(self):
        """Tworzy katalog saves jeśli nie istnieje"""
        if not os.path.exists(self.saves_dir):
            os.makedirs(self.saves_dir)
    
    def save_game(self, save_name=None):
        """Zapisuje stan gry"""
        if not save_name:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            save_name = f"dynastia_{self.game.player_data.get('name', 'gracz')}_{timestamp}"
        
        save_data = {
            'game_info': {
                'version': '1.0',
                'save_date': datetime.now().isoformat(),
                'turn': self.game.turn,
                'month': self.game.month,
                'year': self.game.year
            },
            'player_data': self.game.player_data,
            'game_data': self.game.game_data
        }
        
        save_path = os.path.join(self.saves_dir, f"{save_name}.json")
        
        try:
            with open(save_path, 'w', encoding='utf-8') as file:
                json.dump(save_data, file, ensure_ascii=False, indent=2)
            
            print(f"✅ Gra zapisana: {save_name}")
            print(f"📁 Lokalizacja: {save_path}")
            return True
            
        except Exception as e:
            print(f"❌ Błąd podczas zapisywania: {e}")
            return False
    
    def load_game(self, save_name):
        """Wczytuje stan gry"""
        save_path = os.path.join(self.saves_dir, f"{save_name}.json")
        
        if not os.path.exists(save_path):
            print(f"❌ Nie znaleziono zapisu: {save_name}")
            return False
        
        try:
            with open(save_path, 'r', encoding='utf-8') as file:
                save_data = json.load(file)
            
            # Przywróć stan gry
            self.game.turn = save_data['game_info']['turn']
            self.game.month = save_data['game_info']['month']
            self.game.year = save_data['game_info']['year']
            self.game.player_data = save_data['player_data']
            self.game.game_data = save_data['game_data']
            
            # Reinicjalizuj systemy
            self.game.initialize_systems()
            
            save_date = save_data['game_info']['save_date']
            print(f"✅ Gra wczytana: {save_name}")
            print(f"📅 Data zapisu: {save_date}")
            print(f"🎮 Tura: {self.game.turn}, Data w grze: {self.game.month:02d}/{self.game.year}")
            return True
            
        except Exception as e:
            print(f"❌ Błąd podczas wczytywania: {e}")
            return False
    
    def list_saves(self):
        """Wyświetla dostępne zapisy"""
        if not os.path.exists(self.saves_dir):
            print("❌ Brak zapisanych gier.")
            return []
        
        save_files = [f for f in os.listdir(self.saves_dir) if f.endswith('.json')]
        
        if not save_files:
            print("❌ Brak zapisanych gier.")
            return []
        
        saves_info = []
        print("\n💾 DOSTĘPNE ZAPISY:")
        print("-" * 60)
        
        for i, filename in enumerate(save_files, 1):
            save_name = filename[:-5]  # Remove .json
            save_path = os.path.join(self.saves_dir, filename)
            
            try:
                with open(save_path, 'r', encoding='utf-8') as file:
                    save_data = json.load(file)
                
                game_info = save_data.get('game_info', {})
                player_data = save_data.get('player_data', {})
                
                save_date = game_info.get('save_date', 'Nieznana')
                turn = game_info.get('turn', 0)
                player_name = player_data.get('name', 'Nieznany')
                player_age = player_data.get('age', 0)
                
                print(f"{i:2d}. {save_name}")
                print(f"    👤 Gracz: {player_name} (wiek: {player_age})")
                print(f"    🎮 Tura: {turn}")
                print(f"    📅 Zapisano: {save_date[:19].replace('T', ' ')}")
                print()
                
                saves_info.append({
                    'index': i,
                    'name': save_name,
                    'filename': filename,
                    'player_name': player_name,
                    'turn': turn,
                    'save_date': save_date
                })
                
            except Exception as e:
                print(f"{i}. {save_name} (❌ Błąd odczytu)")
                saves_info.append({
                    'index': i,
                    'name': save_name,
                    'filename': filename,
                    'error': str(e)
                })
        
        return saves_info
    
    def delete_save(self, save_name):
        """Usuwa zapis gry"""
        save_path = os.path.join(self.saves_dir, f"{save_name}.json")
        
        if not os.path.exists(save_path):
            print(f"❌ Nie znaleziono zapisu: {save_name}")
            return False
        
        try:
            os.remove(save_path)
            print(f"🗑️ Usunięto zapis: {save_name}")
            return True
        except Exception as e:
            print(f"❌ Błąd podczas usuwania: {e}")
            return False
    
    def auto_save(self):
        """Automatyczny zapis gry"""
        auto_save_name = f"auto_save_{self.game.player_data.get('name', 'gracz')}"
        return self.save_game(auto_save_name)
    
    def quick_save(self):
        """Szybki zapis"""
        quick_save_name = f"quick_save_{self.game.player_data.get('name', 'gracz')}"
        return self.save_game(quick_save_name)
    
    def export_stats(self):
        """Eksportuje statystyki gry do pliku tekstowego"""
        stats_filename = f"stats_{self.game.player_data.get('name', 'gracz')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        stats_path = os.path.join(self.saves_dir, stats_filename)
        
        try:
            with open(stats_path, 'w', encoding='utf-8') as file:
                file.write("🏰 DYNASTY SIMULATOR - STATYSTYKI GRY\n")
                file.write("=" * 50 + "\n\n")
                
                # Informacje podstawowe
                file.write(f"👤 Gracz: {self.game.player_data.get('name', 'Nieznany')}\n")
                file.write(f"🎂 Wiek: {self.game.player_data.get('age', 0)} lat\n")
                file.write(f"🎮 Tura: {self.game.turn}\n")
                file.write(f"📅 Data w grze: {self.game.month:02d}/{self.game.year}\n")
                file.write(f"💰 Całkowity majątek: {self.game.get_total_money():,} PLN\n")
                file.write(f"😇 Moralność: {self.game.player_data.get('morality', 50)}/100\n\n")
                
                # Umiejętności
                file.write("🎯 UMIEJĘTNOŚCI:\n")
                skills = self.game.player_data.get('skills', {})
                for skill, value in skills.items():
                    file.write(f"  {skill.capitalize()}: {value}/100\n")
                file.write("\n")
                
                # Biznesy
                file.write("🏢 BIZNESY:\n")
                businesses = self.game.game_data.get('businesses', [])
                for business in businesses:
                    file.write(f"  {business['name']} ({business['city']}): {business['revenue']:,} PLN\n")
                file.write(f"  Łącznie: {len(businesses)} firm\n\n")
                
                # Nieruchomości
                file.write("🏠 NIERUCHOMOŚCI:\n")
                properties = self.game.game_data.get('properties', [])
                total_property_value = sum(prop['value'] for prop in properties)
                file.write(f"  Łączna wartość: {total_property_value:,} PLN\n")
                file.write(f"  Liczba nieruchomości: {len(properties)}\n\n")
                
                # Rodzina
                file.write("👨‍👩‍👧‍👦 RODZINA:\n")
                family = self.game.player_data.get('family', {})
                spouse = family.get('spouse')
                children = family.get('children', [])
                if spouse:
                    file.write(f"  💑 Partner/ka: {spouse}\n")
                file.write(f"  👶 Dzieci: {len(children)}\n")
                for child in children:
                    file.write(f"    - {child}\n")
                file.write("\n")
                
                file.write(f"📊 Raport wygenerowany: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            
            print(f"📊 Statystyki wyeksportowane: {stats_filename}")
            return True
            
        except Exception as e:
            print(f"❌ Błąd podczas eksportu: {e}")
            return False
