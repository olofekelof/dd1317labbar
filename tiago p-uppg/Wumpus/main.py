# Skapad av: Tiago Venhammar
# 2023-12-18


"""
Det här är mitt spel "Wumpus".

Spelet är helt grafiskt och är till stor del skapat med hjälp av pygame,
pygame är en modul till python som behöver installeras för att köra programmet

Spelet är 2D och går ut på att spelaren navigerar 20 olika rum med slumpartade objekt,
- Fladdermöss
    Stöter spelaren på dessa så placeras denne i ett slumpartat tomt rum

- Bottenlösa hål
    Stöter spelaren på dessa så förlorar denne spelet

- Wumpus
    Stöter spelaren på Wumpus så förlorar spelaren, om inte spelaren skjuter Wumpus
    från ett intilligande rum först.

Spelet är uppdelat i 11 moduler, som alla har olika funktioner. Merparten av spelets
kod körs i Level - modulen.

Spelet använder sig av både bilder- och ljud-filer

Positionerna på alla objekt i spelet placeras med hjälp av matriser i .csv filer,
dessa matriser har skapats i programmet "Tiled" av mig.

Spelet sparar även ett High-score för varje spelare som lyckas döda Wumpus,
poängen baseras på hur många rum spelaren utforskat innan denne lyckas skjuta Wumpus

Mer information om vad respektive modul gör finns i modulerna.

"""

# Importera nödvändiga moduler
import os
import pygame, sys
from level import Level
from settings import *

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Change the current working directory to the script directory
os.chdir(script_directory)

print("Current working directory:", os.getcwd())

class Game:
    """
    Skapar objektet "Game" dvs. speletobjektet

    """
    def __init__(self):
        """
        Grundläggande setup

        """
        pygame.init() # Initialiserar pygame
        pygame.mixer.init() # Initialiserar pygames ljudhantering
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Skapar spelrutan, WIDTH och HEIGHT är globala värden från settings-modulen
        pygame.display.set_caption('Hunt the Wumpus') # Titeln på spelrutan
        self.clock = pygame.time.Clock() # Skapar en klocka för spelet för att kunna hantera olika datorers FPS
        self.level = Level() # Skapar en instans av Level

    def reset_game(self):
        """
        Metod för att kunna starta en ny spelinstans
        """
        self.level.channel0.stop() # Avbryter pågående ljuduppspelningar
        self.level = Game() # Skapar en ny instans av Game

    def run(self):
        """
        Spelets huvudloop
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Hanterar pygame och programmets nedstängning ifall användaren vill stänga ner spelrutan
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN: # Pygames hantering av knapptryckningar
                    if event.key == pygame.K_ESCAPE: # Startar om spelet ifall spelaren trycker "esc"
                        self.reset_game()

                    elif event.key == pygame.K_m: # Stänger av pågående ljud i instansen av Level
                        self.level.mute() # "mute" är en metod i Level-klassen

            self.level.run() # Kör spelet
            pygame.display.update() # Uppdaterar det grafiska gränssnittet efter varje iteration i huvudloopen
            self.clock.tick(FPS) # Spelets uppdateringsfrekvens, "FPS" är ett globalt värde i settings-modulen

if __name__ == '__main__': # Kontrollerar att det är main.py som explicit startats och att den inte kallas på i en modul
    game = Game()
    game.run() # Startar huvudloopen