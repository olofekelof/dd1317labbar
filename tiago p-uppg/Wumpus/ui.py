# Skapad av: Tiago Venhammar
"""
Modul som hanterar spelets UI
"""

# Importera nödvändiga moduler
import pygame
from settings import *

class UI:
    def __init__(self):
        """
        Initialiserar grundvärden
        """
        
        # Bilder
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.light = pygame.image.load('graphics/light.png').convert_alpha()
        self.light2 = pygame.image.load('graphics/light2.png').convert_alpha()
        self.arrow = pygame.image.load('graphics/arrow_animation/up.png').convert_alpha()
        self.arrow = pygame.transform.scale(self.arrow, (int(40), int(40)))
        self.key_bindings = pygame.image.load('graphics/key_input.png').convert_alpha()
        
        # Grundvärden för text
        self.arrow_rect = pygame.Rect(680, 540, TEXT_BAR_WIDTH, TEXT_BAR_HEIGHT)
        self.arrow_rect2 = pygame.Rect(685, 545, TEXT_BAR_WIDTH - 10, TEXT_BAR_HEIGHT - 10)
        self.current_frame = 0
        self.current_frame2 = 0
        self.current_frame3 = 0
        self.text_finished = False
        self.text_finished2 = False
        self.text_finished3 = False
        self.typed_text = ""
        self.typed_text2 = ""
        self.typed_text3 = ""

        # Grundvärden för "game over" texten
        self.initial_scale = 1.0
        self.max_scale = 6.0
        self.current_scale = self.initial_scale

        # Grundvärde för spelarens poäng
        self.score_amount = 0

        # Grundvärden för spelarens mängd pilar i nedre högra hörnet
        self.arrow_group = pygame.sprite.Group()
        self.arrow_positions = [(675 + i * 15, 545) for i in range(ARROW_AMOUNT)]
        
        for position in self.arrow_positions:
            arrow_sprite = pygame.sprite.Sprite()
            arrow_sprite.image = self.arrow
            arrow_sprite.rect = self.arrow.get_rect(topleft=position)
            self.arrow_group.add(arrow_sprite)

    def display(self):
        """
        Ritar grafiska delar av UI
        """
        self.display_surface.blit(self.light2, (-85, -85)) # Grunddimma
        self.display_surface.blit(self.key_bindings, (0,465))
        pygame.draw.rect(self.display_surface,'gray',self.arrow_rect)
        pygame.draw.rect(self.display_surface,'black',self.arrow_rect2)
        self.arrow_group.draw(self.display_surface)
        self.score()

    def fog_of_war(self):
        """
        Ritar huvuddimman som begränsar spelarens synfält
        OBS inte samma som Fog-tiles
        """
        self.display_surface.blit(self.light, (-85, -85))

    def draw_text(self, text, duration, pos):
        """
        Ritar "skrollande" text

        INPUT = text, vilken text som ska skrivas
                duration, hur länge texten ska visas
                pos, var texten ska visas
        """
        typing_speed = 2
        text_surface = self.font.render(self.typed_text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.center = (pos)

        if self.current_frame % typing_speed == 0 and len(self.typed_text) < len(text):
            self.typed_text += text[len(self.typed_text)]

        self.display_surface.blit(text_surface, text_rect)
        self.current_frame += 1

        if len(self.typed_text) == len(text) and not self.text_finished:
            self.text_finished = True
            self.text_timer = pygame.time.get_ticks()

        if self.text_finished and pygame.time.get_ticks() - self.text_timer > duration:
            self.typed_text = ""

    def draw_text2(self, text, duration, pos):
        """
        Ritar "skrollande" text
        """
        typing_speed = 2
        text_surface = self.font.render(self.typed_text2, True, TEXT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.center = (pos)

        if self.current_frame2 % typing_speed == 0 and len(self.typed_text2) < len(text):
            self.typed_text2 += text[len(self.typed_text2)]

        self.display_surface.blit(text_surface, text_rect)
        self.current_frame2 += 1

        if len(self.typed_text2) == len(text) and not self.text_finished2:
            self.text_finished2 = True
            self.text_timer2 = pygame.time.get_ticks()

        if self.text_finished2 and pygame.time.get_ticks() - self.text_timer2 > duration:
            self.typed_text2 = ""
    
    def draw_text3(self, text, duration, pos):
        """
        Ritar "skrollande" text
        """
        typing_speed = 2
        text_surface = self.font.render(self.typed_text3, True, TEXT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.center = (pos)

        if self.current_frame3 % typing_speed == 0 and len(self.typed_text3) < len(text):
            self.typed_text3 += text[len(self.typed_text3)]

        self.display_surface.blit(text_surface, text_rect)
        self.current_frame3 += 1

        if len(self.typed_text3) == len(text) and not self.text_finished3:
            self.text_finished3 = True
            self.text_timer3 = pygame.time.get_ticks()

        if self.text_finished3 and pygame.time.get_ticks() - self.text_timer3 > duration:
            self.typed_text3 = ""

    def fire_arrow(self, text):
        """
        Ritar text när spelaren avfyrar en pil
        """
        text_surface = self.font.render(text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.center = (WIDTH//2, HEIGHT//2 + 200)
        self.display_surface.blit(text_surface, text_rect)

    def reset_text(self):
        """
        Återställer text
        """
        self.text_finished = False
        self.typed_text = ""

    def arrow_counter(self):
        """
        Räknar hur många pilar som finns kvar
        """
        out_of_arrows = False
        # Check if there are any arrows in the group
        if self.arrow_group:
            # Remove the first arrow from the group
            removed_arrow = self.arrow_group.sprites()[0]
            self.arrow_group.remove(removed_arrow)
        if len(self.arrow_group.sprites()) < 1:
            out_of_arrows = True

        if out_of_arrows:
            print("Out of ammo")

        return out_of_arrows
    
    def winlose_text(self, text):
        """
        Text för game over eller vinst
        """
        # Set up the initial text surface
        text_surface = self.font.render(text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.center = (WIDTH // 2, HEIGHT // 2)

        # Draw the scaled text surface
        scaled_surface = pygame.transform.scale(text_surface, (int(text_rect.width * self.current_scale), int(text_rect.height * self.current_scale)))
        scaled_rect = scaled_surface.get_rect()
        scaled_rect.center = (WIDTH // 2, HEIGHT // 2)
        self.display_surface.blit(scaled_surface, scaled_rect)

        # Update the scale over time
        self.current_scale += 0.05  # Adjust the increment value based on your preference

        # Limit the scale to the maximum value
        if self.current_scale > self.max_scale:
            self.current_scale = self.max_scale
                    
    def score(self):
        """
        Visar spelarens poäng
        """

        text_surface = self.font.render(" " + str(self.score_amount) + " ", True, TEXT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.center = (20, 20)
        self.display_surface.blit(text_surface, text_rect)

    def score_counter(self):
        """
        Lägger till poäng (vilket är dåligt) om spelaren går in i ett nytt rum
        """
        self.score_amount += 1

    def score_counter2(self):
        """
        Lägger till poäng om spellaren skjuter en pil
        """
        self.score_amount += 5

