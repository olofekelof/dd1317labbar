# Skapad av: Tiago Venhammar
"""
Denna modul hanterar skapandet av dimma
"""


# Importera nödvändiga moduler
import pygame

class Fog(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((224,224))):
        """
        Grundvärden för objekt av Fog-klassen
        """
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.inflate(-175,-180) # Hanterar så att dimman inte försvinner direkt när spelaren kolliderar med den, för att spelaren inte ska hinna se vad som finns i rummet
