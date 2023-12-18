# Skapad av: Tiago Venhammar
"""
Denna modul hanterar skapandet av tiles, t.ex väggarna i spelet
"""


# Importera nödvändiga moduler
import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((TILESIZE,TILESIZE))):
        """
        Grundvärden för objekt av Tile-klassen
        """
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,0)
