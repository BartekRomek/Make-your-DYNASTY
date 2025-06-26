"""
Dynasty Simulator 2D - Graficzna wersja gry z kontrolą nad postacią
"""

import pygame
import pygame_gui
import sys
import math
import yaml
import json
from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional

# Inicjalizacja Pygame
pygame.init()

# Kolory
class Colors:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    PURPLE = (128, 0, 128)
    ORANGE = (255, 165, 0)
    BROWN = (139, 69, 19)
    GRAY = (128, 128, 128)
    LIGHT_GRAY = (200, 200, 200)
    DARK_GREEN = (0, 100, 0)
    GOLD = (255, 215, 0)

# Ustawienia gry
class Settings:
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800
    FPS = 60
    TILE_SIZE = 32
    PLAYER_SPEED = 3
    
class GameState(Enum):
    MENU = "menu"
    PLAYING = "playing"
    INVENTORY = "inventory"
    DIALOG = "dialog"
    BUSINESS_MENU = "business"
    FAMILY_MENU = "family"
    PROPERTY_MENU = "property"

@dataclass
class Position:
    x: int
    y: int
    
    def distance_to(self, other: 'Position') -> float:
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Player:
    def __init__(self, x: int, y: int):
        self.position = Position(x, y)
        self.speed = Settings.PLAYER_SPEED
        self.rect = pygame.Rect(x, y, Settings.TILE_SIZE, Settings.TILE_SIZE)
        self.color = Colors.BLUE
        self.name = "Jan Kowalski"
        self.age = 28
        self.money = 100000
        self.morality = 50
        self.skills = {
            "management": 55,
            "negotiation": 60,
            "technology": 35,
            "manipulation": 40
        }
        self.businesses = []
        self.properties = []
        self.family = {"spouse": None, "children": []}
        
    def move(self, dx: int, dy: int, obstacles: List[pygame.Rect]):
        """Porusza postać z kolizjami"""
        new_x = self.position.x + dx * self.speed
        new_y = self.position.y + dy * self.speed
        
        # Sprawdź kolizje z przeszkodami
        new_rect = pygame.Rect(new_x, new_y, Settings.TILE_SIZE, Settings.TILE_SIZE)
        
        # Sprawdź granice ekranu
        if new_x < 0 or new_x > Settings.SCREEN_WIDTH - Settings.TILE_SIZE:
            dx = 0
        if new_y < 0 or new_y > Settings.SCREEN_HEIGHT - Settings.TILE_SIZE:
            dy = 0
            
        # Sprawdź kolizje z przeszkodami
        collision = False
        for obstacle in obstacles:
            if new_rect.colliderect(obstacle):
                collision = True
                break
                
        if not collision:
            self.position.x = new_x
            self.position.y = new_y
            self.rect.x = new_x
            self.rect.y = new_y
    
    def draw(self, screen: pygame.Surface):
        """Rysuje gracza"""
        # Ciało
        pygame.draw.rect(screen, self.color, self.rect)
        # Głowa
        head_rect = pygame.Rect(self.rect.x + 8, self.rect.y - 8, 16, 16)
        pygame.draw.ellipse(screen, Colors.YELLOW, head_rect)
        # Oczy
        pygame.draw.circle(screen, Colors.BLACK, (self.rect.x + 12, self.rect.y - 4), 2)
        pygame.draw.circle(screen, Colors.BLACK, (self.rect.x + 20, self.rect.y - 4), 2)

class Building:
    def __init__(self, x: int, y: int, width: int, height: int, building_type: str, name: str):
        self.rect = pygame.Rect(x, y, width, height)
        self.type = building_type
        self.name = name
        self.interactable = True
        self.visited = False
        
    def draw(self, screen: pygame.Surface):
        """Rysuje budynek"""
        color_map = {
            "business": Colors.GREEN,
            "property": Colors.BROWN,
            "football": Colors.ORANGE,
            "education": Colors.PURPLE,
            "crime": Colors.RED,
            "family": Colors.YELLOW,
            "bank": Colors.GOLD,
            "shop": Colors.LIGHT_GRAY
        }
        
        color = color_map.get(self.type, Colors.GRAY)
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, Colors.BLACK, self.rect, 3)
        
        # Tekst nazwy
        font = pygame.font.Font(None, 20)
        text = font.render(self.name[:10], True, Colors.BLACK)
        text_rect = text.get_rect(center=(self.rect.centerx, self.rect.bottom + 10))
        screen.blit(text, text_rect)

class NPC:
    def __init__(self, x: int, y: int, name: str, npc_type: str, dialog: List[str]):
        self.position = Position(x, y)
        self.rect = pygame.Rect(x, y, Settings.TILE_SIZE, Settings.TILE_SIZE)
        self.name = name
        self.type = npc_type
        self.dialog = dialog
        self.color = Colors.RED if npc_type == "crime" else Colors.GREEN
        
    def draw(self, screen: pygame.Surface):
        """Rysuje NPC"""
        pygame.draw.ellipse(screen, self.color, self.rect)
        pygame.draw.ellipse(screen, Colors.BLACK, self.rect, 2)
        
        # Nazwa nad NPC
        font = pygame.font.Font(None, 16)
        text = font.render(self.name, True, Colors.BLACK)
        text_rect = text.get_rect(center=(self.rect.centerx, self.rect.y - 10))
        screen.blit(text, text_rect)

class GameWorld:
    def __init__(self):
        self.buildings = []
        self.npcs = []
        self.obstacles = []
        self.setup_world()
        
    def setup_world(self):
        """Ustawia świat gry - budynki, NPCs, przeszkody"""
        
        # Budynki biznesowe
        self.buildings.append(Building(100, 100, 80, 60, "business", "Biuro"))
        self.buildings.append(Building(250, 150, 100, 80, "property", "Agencja Nieruchomości"))
        self.buildings.append(Building(400, 100, 120, 90, "football", "Stadion"))
        self.buildings.append(Building(600, 200, 90, 70, "education", "Uniwersytet"))
        self.buildings.append(Building(800, 300, 80, 60, "crime", "Ciemna Uliczka"))
        self.buildings.append(Building(150, 350, 100, 80, "family", "Dom Rodzinny"))
        self.buildings.append(Building(500, 400, 90, 60, "bank", "Bank"))
        self.buildings.append(Building(700, 150, 80, 70, "shop", "Sklep"))
        
        # NPCs
        self.npcs.append(NPC(200, 300, "Anna", "family", ["Cześć kochanie!", "Jak minął dzień?"]))
        self.npcs.append(NPC(850, 350, "Viktor", "crime", ["Mam dla ciebie propozycję...", "Ryzykowna, ale dochodowa."]))
        self.npcs.append(NPC(450, 250, "Prof. Kowalski", "education", ["Chcesz rozwijać umiejętności?", "Mam świetny kurs dla ciebie!"]))
        self.npcs.append(NPC(320, 180, "Broker", "business", ["Inwestycje to przyszłość!", "Mogę ci pomóc zarobić."]))
        
        # Przeszkody (drzewa, kamienie, etc.)
        for i in range(10):
            x = (i * 120 + 50) % (Settings.SCREEN_WIDTH - 40)
            y = (i * 80 + 500) % (Settings.SCREEN_HEIGHT - 40)
            self.obstacles.append(pygame.Rect(x, y, 40, 40))
            
    def draw(self, screen: pygame.Surface):
        """Rysuje cały świat"""
        # Tło
        screen.fill(Colors.DARK_GREEN)
        
        # Rysuj drogi
        for i in range(0, Settings.SCREEN_WIDTH, 100):
            pygame.draw.line(screen, Colors.GRAY, (i, 0), (i, Settings.SCREEN_HEIGHT), 5)
        for i in range(0, Settings.SCREEN_HEIGHT, 100):
            pygame.draw.line(screen, Colors.GRAY, (0, i), (Settings.SCREEN_WIDTH, i), 5)
        
        # Przeszkody
        for obstacle in self.obstacles:
            pygame.draw.rect(screen, Colors.BROWN, obstacle)
            
        # Budynki
        for building in self.buildings:
            building.draw(screen)
            
        # NPCs
        for npc in self.npcs:
            npc.draw(screen)

class Dialog:
    def __init__(self, npc_name: str, messages: List[str]):
        self.npc_name = npc_name
        self.messages = messages
        self.current_message = 0
        self.font = pygame.font.Font(None, 24)
        
    def draw(self, screen: pygame.Surface):
        """Rysuje okno dialogu"""
        # Tło dialogu
        dialog_rect = pygame.Rect(50, Settings.SCREEN_HEIGHT - 150, Settings.SCREEN_WIDTH - 100, 120)
        pygame.draw.rect(screen, Colors.WHITE, dialog_rect)
        pygame.draw.rect(screen, Colors.BLACK, dialog_rect, 3)
        
        # Nazwa NPC
        name_text = self.font.render(f"{self.npc_name}:", True, Colors.BLACK)
        screen.blit(name_text, (dialog_rect.x + 10, dialog_rect.y + 10))
        
        # Wiadomość
        if self.current_message < len(self.messages):
            message = self.messages[self.current_message]
            message_text = self.font.render(message, True, Colors.BLACK)
            screen.blit(message_text, (dialog_rect.x + 10, dialog_rect.y + 40))
            
        # Instrukcja
        instruction = self.font.render("Naciśnij SPACJĘ aby kontynuować, ESC aby zamknąć", True, Colors.GRAY)
        screen.blit(instruction, (dialog_rect.x + 10, dialog_rect.y + 90))
        
    def next_message(self) -> bool:
        """Przechodzi do następnej wiadomości. Zwraca False jeśli koniec"""
        self.current_message += 1
        return self.current_message < len(self.messages)

class UI:
    def __init__(self, player: Player):
        self.player = player
        self.font = pygame.font.Font(None, 24)
        self.small_font = pygame.font.Font(None, 18)
        
    def draw_hud(self, screen: pygame.Surface):
        """Rysuje interfejs użytkownika (HUD)"""
        # Panel informacji gracza
        info_rect = pygame.Rect(10, 10, 300, 120)
        pygame.draw.rect(screen, Colors.WHITE, info_rect)
        pygame.draw.rect(screen, Colors.BLACK, info_rect, 2)
        
        # Informacje gracza
        y_offset = 20
        info_lines = [
            f"👤 {self.player.name}",
            f"🎂 Wiek: {self.player.age}",
            f"💰 Pieniądze: {self.player.money:,} PLN",
            f"😇 Moralność: {self.player.morality}/100"
        ]
        
        for line in info_lines:
            text = self.small_font.render(line, True, Colors.BLACK)
            screen.blit(text, (20, y_offset))
            y_offset += 20
            
        # Umiejętności (paski)
        skills_rect = pygame.Rect(10, 140, 300, 100)
        pygame.draw.rect(screen, Colors.WHITE, skills_rect)
        pygame.draw.rect(screen, Colors.BLACK, skills_rect, 2)
        
        y_offset = 150
        for skill, value in self.player.skills.items():
            # Nazwa umiejętności
            skill_text = self.small_font.render(f"{skill}:", True, Colors.BLACK)
            screen.blit(skill_text, (20, y_offset))
            
            # Pasek postępu
            bar_rect = pygame.Rect(120, y_offset + 3, 150, 12)
            pygame.draw.rect(screen, Colors.LIGHT_GRAY, bar_rect)
            
            # Wypełnienie paska
            fill_width = int((value / 100) * 150)
            fill_rect = pygame.Rect(120, y_offset + 3, fill_width, 12)
            color = Colors.GREEN if value >= 70 else Colors.YELLOW if value >= 40 else Colors.RED
            pygame.draw.rect(screen, color, fill_rect)
            
            pygame.draw.rect(screen, Colors.BLACK, bar_rect, 1)
            
            y_offset += 18
            
        # Instrukcje sterowania
        controls_rect = pygame.Rect(Settings.SCREEN_WIDTH - 250, 10, 240, 100)
        pygame.draw.rect(screen, Colors.WHITE, controls_rect)
        pygame.draw.rect(screen, Colors.BLACK, controls_rect, 2)
        
        controls = [
            "🎮 STEROWANIE:",
            "WASD/Strzałki - Ruch",
            "E - Interakcja",
            "I - Inwentarz",
            "ESC - Menu"
        ]
        
        y_offset = 20
        for control in controls:
            text = self.small_font.render(control, True, Colors.BLACK)
            screen.blit(text, (Settings.SCREEN_WIDTH - 240, y_offset))
            y_offset += 16

class Dynasty2DGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
        pygame.display.set_caption("Dynasty Simulator 2D")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Inicjalizacja komponentów gry
        self.player = Player(400, 300)
        self.world = GameWorld()
        self.ui = UI(self.player)
        self.current_dialog = None
        self.game_state = GameState.PLAYING
        
        # Manager UI dla okien dialogowych
        self.ui_manager = pygame_gui.UIManager((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
        
    def handle_events(self):
        """Obsługuje wydarzenia"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
            elif event.type == pygame.KEYDOWN:
                if self.game_state == GameState.PLAYING:
                    if event.key == pygame.K_e:
                        self.interact()
                    elif event.key == pygame.K_i:
                        self.game_state = GameState.INVENTORY
                    elif event.key == pygame.K_ESCAPE:
                        self.game_state = GameState.MENU
                        
                elif self.game_state == GameState.DIALOG:
                    if event.key == pygame.K_SPACE:
                        if not self.current_dialog.next_message():
                            self.current_dialog = None
                            self.game_state = GameState.PLAYING
                    elif event.key == pygame.K_ESCAPE:
                        self.current_dialog = None
                        self.game_state = GameState.PLAYING
                        
                elif self.game_state == GameState.INVENTORY:
                    if event.key == pygame.K_i or event.key == pygame.K_ESCAPE:
                        self.game_state = GameState.PLAYING
                        
                elif self.game_state == GameState.MENU:
                    if event.key == pygame.K_ESCAPE:
                        self.game_state = GameState.PLAYING
            
            # Przekaż wydarzenia do UI managera
            self.ui_manager.process_events(event)
    
    def handle_movement(self):
        """Obsługuje ruch gracza"""
        if self.game_state != GameState.PLAYING:
            return
            
        keys = pygame.key.get_pressed()
        dx = dy = 0
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy = -1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = 1
            
        if dx != 0 or dy != 0:
            obstacles = self.world.obstacles + [building.rect for building in self.world.buildings]
            self.player.move(dx, dy, obstacles)
    
    def interact(self):
        """Obsługuje interakcje z obiektami"""
        # Sprawdź interakcje z NPCs
        for npc in self.world.npcs:
            if self.player.position.distance_to(npc.position) < 50:
                self.current_dialog = Dialog(npc.name, npc.dialog)
                self.game_state = GameState.DIALOG
                return
                
        # Sprawdź interakcje z budynkami
        for building in self.world.buildings:
            if self.player.rect.colliderect(building.rect):
                self.enter_building(building)
                return
    
    def enter_building(self, building: Building):
        """Wchodzi do budynku"""
        building.visited = True
        
        if building.type == "business":
            self.open_business_menu()
        elif building.type == "property":
            self.open_property_menu()
        elif building.type == "family":
            self.open_family_menu()
        elif building.type == "bank":
            self.open_bank_menu()
        elif building.type == "education":
            self.open_education_menu()
        elif building.type == "football":
            self.open_football_menu()
        elif building.type == "crime":
            self.open_crime_menu()
        else:
            # Domyślny dialog
            self.current_dialog = Dialog(building.name, [f"Witaj w {building.name}!", "Dziękujemy za wizytę!"])
            self.game_state = GameState.DIALOG
    
    def open_business_menu(self):
        """Otwiera menu biznesu"""
        dialog_messages = [
            "💼 MENU BIZNESU",
            "1. Załóż nową firmę",
            "2. Zarządzaj istniejącymi",
            "3. Inwestuj w rozwój",
            "Wybierz opcję..."
        ]
        self.current_dialog = Dialog("Biuro Biznesowe", dialog_messages)
        self.game_state = GameState.DIALOG
    
    def open_property_menu(self):
        """Otwiera menu nieruchomości"""
        dialog_messages = [
            "🏠 AGENCJA NIERUCHOMOŚCI",
            "Dostępne nieruchomości:",
            "• Mieszkanie - 300,000 PLN",
            "• Dom - 800,000 PLN", 
            "• Willa - 2,000,000 PLN"
        ]
        self.current_dialog = Dialog("Agent Nieruchomości", dialog_messages)
        self.game_state = GameState.DIALOG
    
    def open_family_menu(self):
        """Otwiera menu rodziny"""
        spouse = self.player.family.get("spouse", "Brak")
        children_count = len(self.player.family.get("children", []))
        
        dialog_messages = [
            "👨‍👩‍👧‍👦 DOM RODZINNY",
            f"Partner/ka: {spouse}",
            f"Dzieci: {children_count}",
            "Tu możesz budować relacje rodzinne"
        ]
        self.current_dialog = Dialog("Dom", dialog_messages)
        self.game_state = GameState.DIALOG
    
    def open_bank_menu(self):
        """Otwiera menu banku"""
        dialog_messages = [
            "🏦 BANK",
            f"Twoje konto: {self.player.money:,} PLN",
            "Dostępne usługi:",
            "• Kredyty",
            "• Inwestycje",
            "• Oszczędności"
        ]
        self.current_dialog = Dialog("Bankier", dialog_messages)
        self.game_state = GameState.DIALOG
    
    def open_education_menu(self):
        """Otwiera menu edukacji"""
        dialog_messages = [
            "🎓 UNIWERSYTET",
            "Dostępne kursy:",
            "• MBA - 100,000 PLN",
            "• Technologie - 50,000 PLN",
            "• Psychologia - 75,000 PLN"
        ]
        self.current_dialog = Dialog("Profesor", dialog_messages)
        self.game_state = GameState.DIALOG
    
    def open_football_menu(self):
        """Otwiera menu piłkarskie"""
        dialog_messages = [
            "⚽ STADION",
            "Zarządzanie klubem piłkarskim:",
            "• Transfery zawodników",
            "• Rozbudowa stadionu",
            "• Organizacja meczów"
        ]
        self.current_dialog = Dialog("Manager", dialog_messages)
        self.game_state = GameState.DIALOG
    
    def open_crime_menu(self):
        """Otwiera menu półświatka"""
        if self.player.morality > 70:
            dialog_messages = [
                "🌑 CIEMNA ULICZKA",
                "Hmm... jesteś zbyt uczciwy",
                "Wróć gdy będziesz gotowy na mroczną stronę...",
                "Morlaność musi być <70"
            ]
        else:
            dialog_messages = [
                "🌑 PÓŁŚWIATEK", 
                "Mam dla ciebie propozycję...",
                "Ryzykowne, ale bardzo dochodowe",
                "Pranie pieniędzy - 100,000 PLN",
                "Przemyt - 150,000 PLN"
            ]
        self.current_dialog = Dialog("Szemrany Typ", dialog_messages)
        self.game_state = GameState.DIALOG
    
    def draw_inventory(self):
        """Rysuje ekran inwentarza"""
        self.screen.fill(Colors.BLACK)
        
        # Tytuł
        title_font = pygame.font.Font(None, 48)
        title = title_font.render("📦 INWENTARZ", True, Colors.WHITE)
        title_rect = title.get_rect(center=(Settings.SCREEN_WIDTH // 2, 50))
        self.screen.blit(title, title_rect)
        
        # Informacje o graczku
        info_font = pygame.font.Font(None, 24)
        y_offset = 120
        
        info_items = [
            f"👤 {self.player.name}",
            f"🎂 Wiek: {self.player.age} lat",
            f"💰 Pieniądze: {self.player.money:,} PLN",
            f"😇 Moralność: {self.player.morality}/100",
            "",
            "🏢 BIZNESY:",
        ]
        
        # Dodaj biznesy
        if self.player.businesses:
            for business in self.player.businesses:
                info_items.append(f"  • {business}")
        else:
            info_items.append("  Brak biznesów")
        
        info_items.append("")
        info_items.append("🏠 NIERUCHOMOŚCI:")
        
        # Dodaj nieruchomości
        if self.player.properties:
            for prop in self.player.properties:
                info_items.append(f"  • {prop}")
        else:
            info_items.append("  Brak nieruchomości")
        
        # Rodzina
        info_items.append("")
        info_items.append("👨‍👩‍👧‍👦 RODZINA:")
        spouse = self.player.family.get("spouse")
        if spouse:
            info_items.append(f"  💑 Partner/ka: {spouse}")
        children = self.player.family.get("children", [])
        info_items.append(f"  👶 Dzieci: {len(children)}")
        
        for item in info_items:
            text = info_font.render(item, True, Colors.WHITE)
            self.screen.blit(text, (50, y_offset))
            y_offset += 30
        
        # Instrukcja
        instruction = info_font.render("Naciśnij I lub ESC aby zamknąć", True, Colors.YELLOW)
        self.screen.blit(instruction, (50, Settings.SCREEN_HEIGHT - 50))
    
    def draw_menu(self):
        """Rysuje menu pauzy"""
        # Półprzezroczyste tło
        overlay = pygame.Surface((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(Colors.BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Menu
        menu_rect = pygame.Rect(
            Settings.SCREEN_WIDTH // 4, 
            Settings.SCREEN_HEIGHT // 4,
            Settings.SCREEN_WIDTH // 2,
            Settings.SCREEN_HEIGHT // 2
        )
        pygame.draw.rect(self.screen, Colors.WHITE, menu_rect)
        pygame.draw.rect(self.screen, Colors.BLACK, menu_rect, 3)
        
        # Tytuł
        title_font = pygame.font.Font(None, 48)
        title = title_font.render("🏰 MENU", True, Colors.BLACK)
        title_rect = title.get_rect(center=(Settings.SCREEN_WIDTH // 2, menu_rect.y + 50))
        self.screen.blit(title, title_rect)
        
        # Opcje menu
        menu_font = pygame.font.Font(None, 32)
        menu_items = [
            "ESC - Wróć do gry",
            "S - Zapisz grę", 
            "L - Wczytaj grę",
            "Q - Wyjście z gry"
        ]
        
        y_offset = menu_rect.y + 120
        for item in menu_items:
            text = menu_font.render(item, True, Colors.BLACK)
            text_rect = text.get_rect(center=(Settings.SCREEN_WIDTH // 2, y_offset))
            self.screen.blit(text, text_rect)
            y_offset += 50
    
    def update(self, dt: float):
        """Aktualizuje stan gry"""
        if self.game_state == GameState.PLAYING:
            self.handle_movement()
        
        self.ui_manager.update(dt)
    
    def draw(self):
        """Rysuje całą grę"""
        if self.game_state == GameState.PLAYING:
            # Rysuj świat
            self.world.draw(self.screen)
            
            # Rysuj gracza
            self.player.draw(self.screen)
            
            # Rysuj UI
            self.ui.draw_hud(self.screen)
            
            # Rysuj dialog jeśli aktywny
            if self.current_dialog:
                self.current_dialog.draw(self.screen)
                
        elif self.game_state == GameState.DIALOG:
            # Rysuj świat w tle
            self.world.draw(self.screen)
            self.player.draw(self.screen)
            self.ui.draw_hud(self.screen)
            
            # Rysuj dialog
            if self.current_dialog:
                self.current_dialog.draw(self.screen)
                
        elif self.game_state == GameState.INVENTORY:
            self.draw_inventory()
            
        elif self.game_state == GameState.MENU:
            # Rysuj grę w tle
            self.world.draw(self.screen)
            self.player.draw(self.screen)
            self.ui.draw_hud(self.screen)
            
            # Rysuj menu na wierzchu
            self.draw_menu()
        
        # Rysuj UI manager
        self.ui_manager.draw_ui(self.screen)
    
    def run(self):
        """Główna pętla gry"""
        print("🎮 Uruchamianie Dynasty Simulator 2D...")
        print("🎯 Sterowanie: WASD/Strzałki - ruch, E - interakcja, I - inwentarz")
        
        while self.running:
            dt = self.clock.tick(Settings.FPS) / 1000.0
            
            self.handle_events()
            self.update(dt)
            self.draw()
            
            pygame.display.flip()
        
        pygame.quit()
        sys.exit()

def main():
    """Funkcja główna"""
    try:
        game = Dynasty2DGame()
        game.run()
    except Exception as e:
        print(f"❌ Błąd gry: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
