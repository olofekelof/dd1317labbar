# Skapad av: Tiago Venhammar
"""
Denna modul hanterar skapandet av entitet-klassen
"""


# Importera nödvändiga moduler
import pygame
from settings import *


class Entity(pygame.sprite.Sprite):
    """
    Det finns fyra typer av entiteter som skapas i level-modulen med hjälp av den här klassen
    """
    def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((TILESIZE,TILESIZE))):
        """
        Skapar grundvärden för klassen
        """
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,0)