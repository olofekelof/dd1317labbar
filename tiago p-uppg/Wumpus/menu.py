# Skapad av: Tiago Venhammar

"""
Denna modul hanterar:

- Huvudmenyn
- Svårighetsgrad
- Hantering av high-scores
- Intro-texten till spelet

Innehåller 12 metoder i en klass

"""

# Importera nödvändiga moduler
import pygame, sys
from support import import_folder
from settings import *
from support import read_high_scores
from support import write_high_scores

class Menu:
    """
    Skapar objektet Menu
    """
    def __init__(self):
        """
        Initialiseringsvärden för klassen

        """

        # Värden som justeras av svårighetsgraden nedan satt till "Mellan" som standard
        self.bat_spawn_rate = 0.3 # Sannolikhet att en fladdermus skapas i ett rum
        self.pit_spawn_rate = 0.2 # Sannolikhet att ett bottenlöst hål skapas i ett rum
        self.empty_room_spawn_rate = 0.5 # Sannolikhet att ett rum är tomt
        self.wumpus_follow = False # Avgör om Wumpus förföljer spelaren

        # Skapar en instans av skärmen
        self.screen = pygame.display.get_surface()

        # Värden för olika typsnitt, "UI_FONT" är ett globalt typsnitt som definieras i settings.py
        self.title_font = pygame.font.Font(UI_FONT, 54)
        self.author_font = pygame.font.Font(UI_FONT, 30)
        self.menu_font = pygame.font.Font(UI_FONT, 24)

        # Skapar en lista för valen i menyn, samt startindex för menyn
        self.menu_options = ["Starta spelet", "High Scores", "Inställningar", "Avsluta"]
        self.selected_option = 0

        # Animerar Bosk, som är en liten markör bredvid nuvarande val i menyn
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = import_folder('graphics/player_animation/down') # "import_folder" är en funktion i support.py som skapar en lista av alla bilder i filen
        self.image = self.frames[0]
        
        # Ljudfiler
        self.menu_click = pygame.mixer.Sound('audio/click.wav') # Klickljud för navigation i menyn

        # Filsökvägen för .txt filen som innehåller high-scores, ändra ifall den flyttas
        self.high_scores_path = "high_scores.txt"

        # Variabelinitialisering
        self.player_name = None
        self.high_score_added = False
        self.timer_activated = False
        self.timer_done = False
        self.high_scores = None
        self.running = True
        self.settings_running = True

    def draw_menu(self):
        """
        Hanterar det grafiska upplägget för huvudmenyn

        """
        # Skapar en bakgrundsfärg
        self.screen.fill(('black'))

        # Animerar boskmarkören
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

        # Ritar titeltexten
        title_text = self.title_font.render("Wumpus", True, (255, 255, 255))
        self.screen.blit(title_text, (100, 50))

        # Ritar texten under titeltexten
        author_text = self.author_font.render("Bosks äventyr", True, (255, 255, 255))
        self.screen.blit(author_text, (100, 110))

        # Ritar de olika menyvalen
        for i, option in enumerate(self.menu_options):
            color = (255, 255, 255) if i == self.selected_option else (150, 150, 150) # Om användaren har ett val markerat visas det i vitt, övriga val är gråa
            option_text = self.menu_font.render(option, True, color)
            self.screen.blit(option_text, (100, 200 + i * 40))
            if i == self.selected_option:
                self.rect = self.image.get_rect(topleft = (70, 195 + i * 40))
                self.screen.blit(self.image, self.rect)

        pygame.display.flip() # Uppdaterar skärmen

    def run(self):
        """
        Skapar en loop för menyn och hanterar användarens knapptryckningar
        """
        while self.running: # self.running är en variabel som används för att programmet ska veta när spelaren är färdig i menyn
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.menu_click.play() # Spelar knapptryckningsljud
                    if event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.menu_options) # Hoppar mellan val i menyn
                    elif event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.menu_options)
                    elif event.key == pygame.K_RETURN:
                        self.handle_selection()

            self.draw_menu()

    def timer_delay(self, delay):
        """
        Skapar en timer för att hantera när loopen ska vänta innan den påbörjar något
        INPUT = "delay" hur många millisekunder timern ska vara
        """
        if not self.timer_activated:
            self.timer = pygame.time.get_ticks()
            self.timer_activated = True
        if pygame.time.get_ticks() - self.timer > delay:
            self.timer_done = True
        
    def draw_settings(self):
        """
        Ritar undermenyn settings
        """
        # Bakgrundsfärg samt ritar över tidigare ritade objekt
        self.screen.fill(('black'))

        # Ritar titeln för menyn
        title_text = self.title_font.render("Inställningar", True, (255, 255, 255))
        self.screen.blit(title_text, (100, 50))
        sub_menu_text = self.author_font.render("Svårighetssgrad", True, (255, 255, 255))
        self.screen.blit(sub_menu_text, (100, 130))

        # Ritar menyns val
        self.settings_options = ["Lätt", "Mellan", "Svår", "Tillbaka"]
        for i, option in enumerate(self.settings_options):
            color = (255, 255, 255) if i == self.selected_option else (150, 150, 150)
            option_text = self.menu_font.render(option, True, color)
            self.screen.blit(option_text, (100, 200 + i * 40))

        pygame.display.flip()

    def handle_settings(self):
        """
        Skapar en ny loop för undermenyn och hanterar användarens knapptryckningar
        """

        # Startval
        self.selected_option = 0

        while self.settings_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.menu_click.play()
                    if event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.settings_options)
                    elif event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.settings_options)
                    elif event.key == pygame.K_RETURN:
                        self.handle_settings_selection(self.settings_options[self.selected_option])

            self.draw_settings()
    
    def handle_settings_selection(self, selected_option):
        """
        Hanterar användarens val av svårighetsgrad
        - Modifierar värden för spawnrates
        - Anger om Wumpus ska förfölja spelaren eller inte
        """
        if selected_option == "Lätt":
            self.bat_spawn_rate = 0.2
            self.pit_spawn_rate = 0.1
            self.empty_room_spawn_rate = 0.7
            self.wumpus_follow = False
            print("Svårighetsgrad = Lätt")
            print(self.wumpus_follow)
            self.settings_running = False # Avslutar loopen när ett val har gjorts och återgår till huvudmenyloopen

        elif selected_option == "Mellan":
            self.bat_spawn_rate = 0.3
            self.pit_spawn_rate = 0.2
            self.empty_room_spawn_rate = 0.5
            self.wumpus_follow = False
            print("Svårighetsgrad = Mellan")
            print(self.wumpus_follow)
            self.settings_running = False

        elif selected_option == "Svår":
            self.bat_spawn_rate = 0.4
            self.pit_spawn_rate = 0.3
            self.empty_room_spawn_rate = 0.3
            self.wumpus_follow = True
            print("Svårighetsgrad = Svår")
            print(self.wumpus_follow)
            self.settings_running = False

        elif selected_option == "Tillbaka":
            print("Going back to main menu")
            self.settings_running = False

    def wumpus_moving(self):
        """
        Möjliggör export av om self.wumpus_follow är True eller False, används i level.py
        OUTPUT = self.wumpus_follow True eller False
        """
        self.wumpus_follow = False
        return self.wumpus_follow

    def display_high_scores(self):
        """
        Hanterar visandet av high-scores
        - Visar en rullande lista med upp till 10 tidigare high-scores
        - High-scores hämtas från high_scores.txt som är satt i en variabel self.high_scores_path
        - Fryser skärmen tillfälligt när high-scores visas
        """
        self.high_scores = read_high_scores(self.high_scores_path)
        print("Reading highscores...")
        if not self.high_scores: # Hanterar ifall high_scores.txt är tom
            info_text = self.menu_font.render("Inga sparade high scores", True, (255, 255, 255))
            self.screen.blit(info_text, (200, 240))
            pygame.display.flip()
            pygame.time.wait(1000)
            return

        # Sorterar high-scores som laddats in så att lägsta värden är först
        sorted_high_scores = sorted(self.high_scores.items(), key=lambda x: int(x[1]), reverse=False)
        y_position = 200 # Variabel för att bestämma radavstånd
        title_text = self.author_font.render("High Scores:", True, (255, 255, 255))
        self.screen.blit(title_text, (500, y_position))
        y_position += title_text.get_height() + 5
        
        # Hur många high_scores som ska visas
        max_items_to_show = 10

        # Ritar top scores, med användarnamn på den som satt scoret
        for rank, (player, score) in enumerate(sorted_high_scores[:max_items_to_show], start=1):
            score_text = self.menu_font.render(f"{rank}. {player}: {score}", True, (255, 255, 255))
            self.screen.blit(score_text, (500, y_position))
            y_position += score_text.get_height() + 2
            pygame.display.flip()
            pygame.time.wait(100) # Delay mellan varje ritning för att skapa en "skrollande" effekt
        pygame.time.wait(4000) # Fryser skärmen i 4 sekunder så att användaren kan läsa high-scores

    def add_high_score(self, score):
        """
        Låter användaren mata in sitt användarnamn
        INPUT = Score, hämtas från level.py där metoden används
        OUTPUT = Användarnamn och Score som sparas i high_scores.txt
        """
        self.timer_delay(3000) # Timer för att inte avbryta annan kod
        if self.timer_done and not self.high_score_added:
            self.show_input_screen()
            if not self.high_score_added:
                write_high_scores(self.high_scores_path, score, self.player_name) # Använder metoden write_high_scores för att föra in data i high_scores.txt
                self.high_score_added = True
                self.display_high_scores() # Visar tidigare high-scores

    def show_input_screen(self):
        """
        Metod för att låta användaren mata in ett namn som kommer visas i high-scores
        INPUT = Användaren skriver in på spelskärmen
        OUTPUT = self.player_name som används i add_high_score metoden
        """
        input_font = pygame.font.Font(UI_FONT, 36)
        input_text = ""
        input_active = True

        # Skapar en loop för användarinmatning
        while input_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        input_active = False # Flaggar om spelaren är färdig och avbryter loopen
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

            self.screen.fill(('black'))
            text_surface = input_font.render(f"Skriv ditt användarnamn: {input_text}", True, (TEXT_COLOR))
            self.screen.blit(text_surface, (30, 40))
            pygame.display.flip()

        self.player_name = input_text

    def handle_selection(self):
        """
        Metod för att hantera användarens val i huvudmenyn
        - "Starta spelet" visar en introtext och avslutar menyns loop så att spelloopen kan ta över
        - "High scores" visar high-scores
        - "Inställningar" öppnar undermenyn för svårighetsgrad
        - "Avsluta" gör precis vad det låter som
        """
        selected_option_text = self.menu_options[self.selected_option]
        if selected_option_text == "Starta spelet":
            intro_text = [
            "Du befinner dig i kulvertarna under D-huset, där den glupske Wumpus",
            "bor. För att undvika att bli uppäten måste du skjuta Wumpus med din",
            "pil och båge. Kulvertarna har 20 rum som är förenade med smala gångar.",
            "",
            "Här finns faror som lurar. I vissa rum finns bottenlösa hål. Kliver",
            "du ner i ett sådant dör du omedelbart. I andra rum finns fladdermöss",
            "som lyfter upp dig, flyger en bit och släpper dig i ett godtyckligt",
            "rum. I ett av rummen finns Wumpus, och om du vågar dig in i det rummet",
            "blir du genast uppäten. Som tur är kan du från rummen bredvid känna",
            "vinddraget från ett avgrundshål eller lukten av Wumpus. Du kan också",
            "i varje rum reda se i vilka nya riktningar du kan gå.",
            "För att vinna spelet måste du skjuta Wumpus.",
            "När du skjuter iväg en pil kan du styra pilens bana genom luften",
            "i 4 sekunder.",
            "Du kan skjuta iväg din pil för att utforska rum, men tänk på att du",
            "bara har fem pilar, tar de slut så dör du. Lycka till!",
            "",
            "Tryck 'ENTER' för att starta spelet!"
            ]

            self.screen.fill(('black'))

            # Radavstånd
            y_position = 20

            for line in intro_text:
                info_text = self.menu_font.render(line, True, (255, 255, 255))
                self.screen.blit(info_text, (50, y_position))
                y_position += info_text.get_height() + 2

            pygame.display.flip()

            waiting_for_start = True
            while waiting_for_start:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: # Hanterar ifall användaren vill stänga rutan
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        waiting_for_start = False # Avslutar loopen
                        
            self.screen.fill(('black'))  # Fill the screen with black color
            pygame.display.flip()  # Update the display to clear the information text
            self.running = False

        elif selected_option_text == "High Scores":
            self.display_high_scores()

        elif selected_option_text == "Inställningar":
            print("Displaying settings")
            self.settings_running = True
            self.handle_settings()

        elif selected_option_text == "Avsluta":
            pygame.quit()
            sys.exit()