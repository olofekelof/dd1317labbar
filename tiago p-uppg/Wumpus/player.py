# Skapad av: Tiago Venhammar
"""
Denna modul hanterar skapandet av spelaren och dess animationer

Modulen består av 1 klass med 9 metoder

"""


# Importera nödvändiga moduler
import pygame
from settings import *
from support import import_folder

class Player(pygame.sprite.Sprite):
    """
    Skapar ett objekt av klassen Player
    """
    def __init__(self, pos, groups, obstacle_sprites, create_arrow):
        """
        Intialiseringsvärden för spelaren

        INPUT = pos, vart spelaren ska placeras
                groups, vilka grupper spelarklassen tillhör
                obstacle_sprites, att spelaren ska känna av hinder
                create_arrow, initialiserar pilen i level-modulen
        """

        super().__init__(groups)

        # Spelarens grundbild
        self.image = pygame.image.load('graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-15,-20)

        # Värden för animation av spelaren
        self.import_player_assets()
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        # Värden för rörelse av spelaren
        self.direction = pygame.math.Vector2()
        self.speed = 2
        self.shoot = False
        self.shoot_cooldown = 4000
        self.shoot_time = None

        self.obstacle_sprites = obstacle_sprites

        # Grundvärde för pilar
        self.create_arrow = create_arrow
        self.arrows = 5

        # Fotstegsljud
        self.footstep = pygame.mixer.Sound('audio/footstep.mp3')
        self.footstep.set_volume(0.05)

    def import_player_assets(self):
        """
        Hanterar import av bilderna för spelarens animation
        """
        character_path = 'graphics/player_animation/'

        # Dictionary för animationer
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
        'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
        'right_shoot': [], 'left_shoot': [], 'up_shoot': [], 'down_shoot': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        """
        Hanterar användarens input för spelarens rörelse
        Samt sätter self.status för att senare ladda in rätt bild beroende på vilken riktning spelaren har
        """
        if not self.shoot:
            keys = pygame.key.get_pressed()


            if keys[pygame.K_UP]:
                self.direction.y = -1
                self.status = 'up'
                self.footstep.play()
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status = 'down'
                self.footstep.play()
            else:
                self.direction.y = 0

            if keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status = 'right'
                self.footstep.play()
            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = 'left'
                self.footstep.play()
            else:
                self.direction.x = 0

            # Input för att skjuta pil
            if keys[pygame.K_SPACE]:
                self.shoot = True
                self.shoot_time = pygame.time.get_ticks()

    def get_status(self):
        """
        Tar reda på om spelaren rör sig eller står still för att hantera animation, även om spelaren skjuter eller inte
        """

        # idle status
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'shoot' in self.status:
                self.status = self.status + '_idle'
        
        if self.shoot:
            self.direction.x = 0
            self.direction.y = 0
            if not 'shoot' in self.status:
                if 'idle' in self.status:
                    #overwrite idle
                    self.status = self.status.replace('_idle', '_shoot')
                else:
                    self.status = self.status + '_shoot'
        else:
            if 'shoot' in self.status:
                self.status = self.status.replace('_shoot', '')


    def move(self,speed):
        """
        Förflyttar spelaren
        INPUT = speed, spelarens hastighet enl. variabel
        """
        if not self.shoot:
            if self.direction.magnitude() != 0:
                self.direction = self.direction.normalize() # Vektorn går alltid i 1 även när spelaren går diagonalt

            self.hitbox.x += self.direction.x * speed
            self.collision('horizontal')
            self.hitbox.y += self.direction.y * speed
            self.collision('vertical')
            self.rect.center = self.hitbox.center
            
    def collision(self, direction):
        """
        Hanterar om spelaren kolliderar
        """
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox): # Berättar om det är en kollision
                    if self.direction.x > 0: # rör sig höger
                        self.hitbox.right = sprite.hitbox.left # om något som rör sig höger kolliderar med något så kolliderar det med sakens vänstra sida
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox): # Berättar om det är en kollision
                    if self.direction.y > 0: # RÖR SIG NEDÅT
                        self.hitbox.bottom = sprite.hitbox.top # om något rör sig neråt är det sakens botten som kolliderar med något annans topp
                    if self.direction.y < 0: # rör sig uppåt
                        self.hitbox.top = sprite.hitbox.bottom


        if direction == 'vertical':
            pass

    def cooldown(self):
        """
        Cooldown efter att spelaren skjutit en pil, innan denne kan skjuta igen
        """
        current_time = pygame.time.get_ticks()

        if self.shoot:
            if current_time - self.shoot_time >= self.shoot_cooldown:
                self.shoot = False

    def animate(self):
        """
        Hanterar spelarens animation
        """
        animation = self.animations[self.status]

        #loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        #set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)


    def update(self):
        """
        Kör metoder
        """
        self.input()
        self.cooldown()
        self.get_status()
        self.animate()
        self.move(self.speed)
