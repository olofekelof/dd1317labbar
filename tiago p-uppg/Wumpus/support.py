# Skapad av: Tiago Venhammar
"""
Modulen innehåller metoder för att ladda in filer
"""

# Importera nödvändiga moduler
from csv import reader
from os import walk
import pygame

def import_csv_layout(path):
    """
    Importerar .csv-filer

    INPUT = path, filsökväg
    OUTPU = terrain_map, lista baserad på .csv-filen
    """
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter = ',') # Kommatecken mellan varje värde
        for row in layout:
            terrain_map.append(list(row))
        print(layout)
        return terrain_map

def import_folder(path):
    """
    Importerar ett flertal bilder från en fil
    INPUT = path, filsökväg
    OUTPUT = surface_list, lista med samtliga bilder i en fil
    """
    surface_list = []

    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image # Fulländer filsökvägen
            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)
    
    return surface_list

def read_high_scores(path):
    """
    Läser in high_scores enligt "path"

    INPUT = path, filsökväg, enligt standard ska detta vara high_scores.txt när metoden används, om textfilen inte flyttas
    OUTPUT = high_scores, dictionary med spelarnamn och dess poäng
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            high_scores = {}
            for line in lines:
                parts = line.strip().split(':')
                if len(parts) ==2:
                    player_name, player_score = parts
                    high_scores[player_name] = int(player_score)
                else:
                    print(f"Skipping invalid line: {line}") # Berättar var det är fel i textfilen om något inte är i rätt format

    except FileNotFoundError:
        # Skickar ett tom dictionary om det inte finns något i textfilen
        high_scores = {}
    except Exception as e: # Felhantering för att inte krascha programmet
        print(f"Error reading high scores: {e}")
        high_scores = {}
    return high_scores

def write_high_scores(path, player_score, player_name):
    """
    Lägger till nya high-scores

    INPUT = path, filsökväg
            player_score, spelarens poäng
            player_name, spelarens användarnamn
    """
    high_scores = read_high_scores(path)

    # Om spelaren redan finns i high-scores, uppdaterar poängen om de nya är bättre
    if player_name in high_scores:
        current_score = int(high_scores[player_name])
        if player_score < current_score: # Lägre poäng är bättre
            high_scores[player_name] = str(player_score)
    else:
        # Om spelaren inte finns, lägg till denne i high-scores
        high_scores[player_name] = str(player_score)

    # Skriv in de nya high-scoresen i textfilen
    with open(path, 'w', encoding='utf-8') as file:
        for name, score in high_scores.items():
            file.write(f"{name}:{score}\n")