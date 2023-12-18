# Skapad av: Tiago Venhammar

"""
Denna modul hanterar pilen som avfyras från spelare och hur den ska styras.

Modulen består av en klass med 4 metoder

"""


# Importera nödvändiga moduler
import pygame

class Arrow(pygame.sprite.Sprite):
    def __init__(self, player, group, obstacle_sprites):
        """
        Hantera var pilen ska placeras i förhållande till spelaren när den avfyras
        """
        super().__init__(group)
        self.direction = pygame.math.Vector2()
        self.firing_direction = player.status.split('_')[0]
        self.status = None
        self.obstacle_sprites = obstacle_sprites

        # Bilden på pilen, laddar in en av 4 bilder beroende på self.firing_direction
        self.image = pygame.image.load('graphics/arrow_animation/'+ str(self.firing_direction) +'.png')


        # Var pilen ska placeras
        if self.firing_direction == 'right':
            self.rect = self.image.get_rect(midleft = player.rect.midright)

        elif self.firing_direction == 'left':
            self.rect = self.image.get_rect(midright = player.rect.midleft)


        elif self.firing_direction == 'down':
            self.rect = self.image.get_rect(midtop = player.rect.midbottom)           

        else: 
            self.rect = self.image.get_rect(midbottom = player.rect.midtop)

        self.hitbox = self.rect.inflate(0,0)

        # Variabel för pilens hastighet
        self.speed = 2

    def input(self):
        """
        Hanterar spelarens knapptryckningar och hur det ska påverka pilens förflyttning
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
            self.image = pygame.image.load('graphics/arrow_animation/'+ str(self.status) +'.png')
            
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
            self.image = pygame.image.load('graphics/arrow_animation/'+ str(self.status) +'.png')

        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
            self.image = pygame.image.load('graphics/arrow_animation/'+ str(self.status) +'.png')

        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
            self.image = pygame.image.load('graphics/arrow_animation/'+ str(self.status) +'.png')

        else:
            self.direction.x = 0


    def move(self):
        """
        Förflyttar pilen
        """

        # Förflyttar pilen på x och y axeln
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

        # Hantera om pilen träffar väggar
        self.hitbox.x += self.direction.x * self.speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * self.speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center


    def collision(self, direction):
        """
        Hanterar pilens kollision med self.obstacle_sprites dvs. väggar
        """
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox): # Berättar om det är en kollision
                    if self.direction.x > 0: # Rör sig höger
                        self.hitbox.right = sprite.hitbox.left # Om något som rör sig höger kolliderar med något så kolliderar det med sakens vänstra sida
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox): # Berättar om det är en kollision
                    if self.direction.y > 0: # Rör sig nedåt
                        self.hitbox.bottom = sprite.hitbox.top # Om något rör sig neråt är det sakens botten som kolliderar med något annats topp
                    if self.direction.y < 0: # Rör sig uppåt
                        self.hitbox.top = sprite.hitbox.bottom
            
