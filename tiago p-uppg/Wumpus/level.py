# Skapad av: Tiago Venhammar

"""
Modulen som hanterar det mesta vad gäller spelet

Den här blev överdrivet komplicerad och i efterhand hade jag velat dela upp en del av
metoderna i den här modulen i andra moduler.

Innehåller 2 klasser
- Level
    Hanterar nästan allt i spelloopen
    Består av 13 metoder
- YSortCameraGroup
    Hanterar hur alla sprites ska röra sig i förhållande till spelaren, skapar en illusion av att spelaren rör sig
    Består av 3 metoder

"""



# Importera nödvändiga moduler
import pygame
from settings import *
from tile import Tile
from player import Player
from support import *
import random
import math
from arrow import Arrow
from entity import Entity
from ui import UI
from fog import Fog
from menu import Menu


class Level:
    def __init__(self):
        """
        Initialvärden för objektet Level
        """

        # Importerar skärmdata som initialiserats i main.py
        self.display_surface = pygame.display.get_surface()

        # Spritegrupper
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.bats_sprites = pygame.sprite.Group()
        self.pit_sprites = pygame.sprite.Group()
        self.empty_room_sprite = pygame.sprite.Group()
        self.wumpus_sprite = pygame.sprite.Group()
        self.fog_sprites = YSortCameraGroup()
        self.dummy_player = pygame.image.load('graphics/player.png').convert_alpha()

        # Menu
        self.menu = Menu()

        # sprite setup
        self.arrow_timer = pygame.time.get_ticks()
        self.timer = 0
        self.create_map()

        # Skapar en instans av klassen UI från ui.py, där en stor del av gränssnittet hanteras
        self.ui = UI()

        # Variabelinitialisering
        self.fog = True
        self.player_teleport = False
        self.wumpus_teleport = False
        self.dummy_spawned = False
        self.dummy_player_rect = None
        self.player_win = False
        self.darkness = True
        self.arrow_control = False
        self.arrow_created = False
        self.sound_playing = False
        self.sound_start_time = 0
        self.sound = True
        self.music_play = False

        # Sounds
        self.arrow_fire = pygame.mixer.Sound('audio/shoot.wav')
        self.menu_click = pygame.mixer.Sound('audio/click.wav')
        self.bat_sound = pygame.mixer.Sound('audio/bat.wav')
        self.pit_sound = pygame.mixer.Sound('audio/fall.wav')
        self.win_sound = pygame.mixer.Sound('audio/win.mp3')
        self.game_over = pygame.mixer.Sound('audio/game_over.wav')
        self.music = pygame.mixer.Sound('audio/music.wav')
        self.wumpus_sound = pygame.mixer.Sound('audio/wumpus.wav')

        # Ljudkanaler
        self.channel0 = pygame.mixer.Channel(0) # Musik
        self.channel1 = pygame.mixer.Channel(1) # Spelljud
        self.channel2 = pygame.mixer.Channel(2) # Game-over ljud
        

    def create_map(self):
        """
        Skapar samtliga objekt som ska finnas i spelet och placerar ut dem enligt .csv matriser
        - "boundary" osynlig gräns som håller spelaren i rummen
        - "spawnpoints" samtliga rum
        - "fog" svarta rutor som agerar som "dimma" för att dölja outforskade rum
        - "walls" laddar in rummens väggar, från början användes bara en stor bild, men nu ger spelet ett intryck av djup
        
        """

        # Variabelinitialisering för att hantera så att spelaren och Wumpus bara kan placeras ut en gång
        self.wumpus_spawned = False
        self.player_spawned = False

        spawns = [] # Lista med koordinater på alla objekt som placerats ut för att senare kunna modifiera dessa
        
        # Importerar samtliga .csv filer med matriser
        layout = {
            'boundary': import_csv_layout('code/map/map_Edge.csv'), # import_csv_layout är en metod i modulen support
            'spawnpoints': import_csv_layout('code/map/Spawn_points.csv'),
            'fog': import_csv_layout('code/map/map_Fog.csv'),
            'walls': import_csv_layout('code/map/map_Walls.csv')
        }
        
        # Importerar bilder på väggar så att dessa can matcha med sin placering i .csv matrisen "walls"
        wall_graphics = {'walls': import_folder('graphics/walls')}
        
        # Loop för att placera ut objekt på respektive plats
        for style, layout in layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1': # -1 betyder "ingenting" i .csv filerna
                        x = col_index * TILESIZE # TILESIZE är en global variabel från settings-modulen
                        y = row_index * TILESIZE

                        if style == 'boundary':
                            Tile((x,y), [self.obstacle_sprites], 'invisible') # Tile är en klass från tile-modulen
                        
                        if style == 'walls':
                            wall_image = wall_graphics['walls'][int(col)]
                            Tile((x,y), [self.visible_sprites], 'visible', wall_image)


                        if style == 'spawnpoints':

                            spawns.append((x,y)) # Lägger till objektens placering i spawns-listan
                            if len(spawns) >= 20: # Det finns 20 rum

                                spawned_coordinates = set()
                                unique_spawns = random.sample(spawns, len(spawns))
                                for spawn_point in unique_spawns:
                                    x, y = spawn_point

                                    # Placerar spelaren, Player är en klass från player-modulen
                                    if not self.player_spawned:
                                        self.player_spawned = True
                                        self.player = Player((x,y), [self.visible_sprites], self.obstacle_sprites, self.create_arrow)
                                        spawned_coordinates.add((x,y)) 

                                    # Övriga objekt definieras som Entity i entity-modulen
                                    elif not self.wumpus_spawned:
                                        self.wumpus_spawned = True 
                                        self.wumpus_image = pygame.image.load('graphics/entities/Wumpus.png').convert_alpha()
                                        self.wumpus = Entity((x, y), [self.visible_sprites, self.wumpus_sprite], 'entities', self.wumpus_image)
                                        print ("The Wumpus has been spawned!!")
                                        spawned_coordinates.add((x,y))


                                    else:
                                        # Placerar övriga entiteter efter att Wumpus placerats
                                        bats = pygame.image.load('graphics/entities/bats.png').convert_alpha()
                                        pit = pygame.image.load('graphics/entities/pit.png').convert_alpha()
                                        empty_room = pygame.image.load('graphics/nothing.png').convert_alpha()
                                        entity_images = [bats, pit, empty_room]

                                        # Hoppar över en koordinat om den redan används
                                        if (x,y) in spawned_coordinates:
                                            continue

                                        # Ställ in sannolikhet för vad som finns i rummen, modifieras i menu-modulen av svårighetsggrad
                                        entity_probabilities = [self.menu.bat_spawn_rate, self.menu.pit_spawn_rate, self.menu.empty_room_spawn_rate]

                                        # Slumpar baserat på spawnrates, vilken entitet som ska placeras i ett rum
                                        random_entity = random.choices(entity_images, weights=entity_probabilities)[0]
                                        
                                        if random_entity == bats:
                                            Entity((x, y), [self.visible_sprites, self.bats_sprites], 'entities', random_entity)
                                        elif random_entity == pit:
                                            Entity((x, y), [self.visible_sprites, self.pit_sprites], 'entities', random_entity)
                                        else:
                                            Entity((x, y), [self.visible_sprites, self.empty_room_sprite], 'entities', random_entity)
                                        
                                        spawned_coordinates.add((x,y))

                                spawns = []
                        # Placera dimma på rum spelaren inte varit i        
                        if style == 'fog':
                            fog = pygame.image.load('graphics/fog.png').convert_alpha()
                            fog_x = x+16
                            fog_y = y+16
                            Fog((fog_x,fog_y), [self.fog_sprites], 'fog_of_war', fog)
                            
    def wumpus_movement(self):
        """
        Hanterar wumpus rörelse ifall svårighetsgraden är "svår"
        Metoden kallas varje gång spelaren går in i ett tidigare outforskat rum
        """
        if self.wumpus_spawned:
            print("Wumpus has moved...")
            if not self.wumpus_teleport:
                self.wumpus_teleport = True
                self.wumpus.kill() # Tar bort Wumpus från hans tidigare rum
                self.wumpus_drop() # wumpus_drop metoden hanterar Wumpus nya placering
                self.timer = 0
                self.wumpus_teleport = False

    def wumpus_drop(self):
            """
            Metoden väljer ett rum som wumpus ska placeras i, han kan enbart placeras i tomma rum
            """
            empty_rooms_list = list(self.empty_room_sprite)
            if empty_rooms_list:
                player_position = self.player.rect.center

                # Räkna ut avståndet från spelaren till alla tomma rum
                distances = [math.dist(empty_room.rect.center, player_position) for empty_room in empty_rooms_list]

                # Hitta indikationer på de 2 närmaste rummen till spelaren
                min_distance_indices = sorted(range(len(distances)), key=lambda k: distances[k])[:2]

                # Välj rummet med det näst minsta avståndet till spelare, för att förhindra att wumpus placeras i samma rum som spelaren
                empty_room_index = min_distance_indices[1]
                selected_empty_room = empty_rooms_list[empty_room_index]

                # Placerar Wumpus i det valda rummet
                self.wumpus = Entity((selected_empty_room.rect.topleft), [self.visible_sprites, self.wumpus_sprite], 'entities', self.wumpus_image)
                print("Wumpus is close...")

    def play_sound(self, sound, duration):
        """
        Hanterar uppspelning av olika ljud i spelet
        INPUT = sound, vilket ljud som ska spelas; duration, hur länge ljudet ska spelas
        """
        if not self.sound_playing:
            self.channel1.play(sound)
            self.sound_playing = True
            self.sound_start_time = pygame.time.get_ticks()
            if pygame.time.get_ticks() - self.sound_start_time >= duration:
                self.sound_playing = False


    def create_arrow(self):
        """
        Skapar en instans av pilen när spelaren vill avfyra en pil
        OUTPUT = self.arrow, används i en mängd andra uttryck för att hantera pilen och dess rörelse
        """
        self.arrow = Arrow(self.player, [self.visible_sprites], self.obstacle_sprites)
        return self.arrow

    def move_arrow(self):
        """
        Kallar på self.arrow.move som är en metod i arrow-modulen
        denne används för att styra pilens rörelse
        """
        if self.arrow_created:
            self.arrow.move()

    def is_clear_line_of_sight(self, start_position, end_position):
        """
        Kontrollerar vad som finns i intilligande rum genom att skicka ut en "dummy" i varje riktning
        tillser att entiteter inte "upptäcks" om det är en vägg mellan dem och spelare
        detta för att spelaren inte ska upptäcka entiteter i intilligande rum om det inte finns en väg till det rummet

        INPUT = start_position, end_position; används för att bestämma var dummyn ska börja och
                vad den ska kollidera med
        OUTPUT = not obstacles_collision, returnerar True om dummyn inte kolliderar med en vägg, och False om den gör det
        """
        # Skapar dummyn
        dummy_sprite = pygame.sprite.Sprite()
        
        # Skapar en rektangel som är spelarens "line_of_sight"
        line_of_sight_rect = pygame.Rect(start_position, (end_position[0] - start_position[0], end_position[1] - start_position[1]))

        dummy_sprite.rect = line_of_sight_rect

        # Kontrollera om det är en vägg i vägen för dummyn
        obstacles_collision = pygame.sprite.spritecollide(dummy_sprite, self.obstacle_sprites, False)

        return not obstacles_collision
    
    def check_entities_nearby(self):
        """
        Kontrollerar om dummyn från is_clear_line_of_sight kolliderar med entiteter i andra rum
        Om den gör det så spelas ett meddelande upp på skärmen
        """
        # Avgör spelarens position baserat på self.players position
        player_position = self.player.rect.center

        # Letar efter intilligande entiteter enligt angiven "distance" (cirka ett rum bort som kontrolleras)
        for sprite_group in [self.bats_sprites, self.pit_sprites, self.wumpus_sprite]:
            for sprite in sprite_group:
                entity_position = sprite.rect.center

                line_of_sight_clear = self.is_clear_line_of_sight(player_position, entity_position)

                # Om is_clear_line_of_sight ger True så kontrolleras avståndet till närliggande entiteter
                if line_of_sight_clear:
                    distance = pygame.math.Vector2(entity_position[0] - player_position[0], entity_position[1] - player_position[1]).length()

                    # Om avståndet är mindre än 220 så spelas ett meddelande upp
                    if distance <= 220:
                        if sprite in self.bats_sprites:
                            self.ui.draw_text("Jag hör fladdermöss!", 4000, (WIDTH // 2, HEIGHT // 2 - 220))
                        if sprite in self.pit_sprites:
                            self.ui.draw_text2("Jag känner vinddrag!", 4000, (WIDTH // 2, HEIGHT // 2 - 240))
                        if sprite in self.wumpus_sprite:
                            self.ui.draw_text3("Jag känner lukten av Wumpus...", 4000, (WIDTH // 2, HEIGHT // 2 - 260))
                            

    def remove_fog(self):
        """
        Enkel metod som med ett booleanskt värde anger om dimman ska lyftas
        """
        self.fog = False

    def bat_drop(self):
        """
        Metod för att förflytta spelaren ifall denne kolliderar med "bats" i ett rum
        Letar efter tomma rum och placerar spelaren i ett av dem
        """
        empty_rooms_list = list(self.empty_room_sprite)
        self.timer = pygame.time.get_ticks()
        
        if empty_rooms_list:
            empty_room = random.choice(empty_rooms_list)
            self.player = Player((empty_room.rect.center), [self.visible_sprites], self.obstacle_sprites, self.create_arrow)
            print("Player has been dropped in a new room!")
            self.sound_playing = False

    def run(self):
        """
        Metod som hanterar det mesta:
        - Initierar menyn
        - Hanterar musik och ljudspelning
        - Hur allt ska ritas, "Kamerans" hantering
        - Visar UI
        - Hanterar pilen
        - Hanterar alla möjliga kollisioner för spelaren och pilen
        """

        # Kör menyn
        self.menu.run()

        if not self.music_play:
            self.channel0.play(self.music, loops=-1)
            self.channel0.set_volume(0.3)
            self.music_play = True
        
        # Om pilen inte har skapats så är "kameran" centrerad på spelaren
        if not self.arrow_control:
            self.visible_sprites.custom_draw(self.player)
            if self.fog:
                self.fog_sprites.custom_draw_fog(self.player)
        
        # Om pilen har skapats så är "kameran" centrerad på pilen
        if self.arrow_control:
            self.visible_sprites.custom_draw(self.arrow)
            if self.fog:
                self.fog_sprites.custom_draw_fog(self.arrow)

        # Uppdaterar alla synliga sprites position i förhållande till spelarens rörelse
        self.visible_sprites.update()

        # Anger hur långt spelaren ska kunna se, definieras i UI - modulen
        if self.darkness:
            self.ui.fog_of_war()

        # Visar spelarens "UI", antal pilar, knappinfo, score, osv.
        self.ui.display()

        # Booleanskt värde för att hantera när text spelas upp om en spelare går in i ett rum
        no_collision_detected = True

        # Skapar pilen när spelaren avfyrar, drar även av poäng för varje avfyrad pil
        if self.player.shoot and not self.arrow_created:
            self.arrow = self.create_arrow()
            self.arrow_timer = pygame.time.get_ticks()
            self.arrow_created = True
            self.channel1.play(self.arrow_fire)
            self.ui.score_counter2()
        
        # Hanterar pilens interaktion med spelet
        if self.arrow_created:
            self.arrow.input() # Metod i arrow-modulen som låter spelaren styra pilens bana
            self.move_arrow()
            self.arrow_control = True # Anger att spelaren styr pilen

            # Visar ett meddelande när pilen avfyras, varar i 2 sekunder
            if pygame.time.get_ticks() - self.arrow_timer <= 2000:
                self.ui.fire_arrow("Pil avfyrad!")

            # Tillser att pilen lyfter dimman från outforskade rum som den flyger genom
            pygame.sprite.spritecollide(self.arrow, self.fog_sprites , True)
            
            # Hanterar om pilen träffar Wumpus
            for sprite in self.wumpus_sprite:    
                if sprite.hitbox.colliderect(self.arrow):
                    self.player.kill()
                    self.arrow.kill()
                    self.darkness = False
                    self.ui.draw_text("Du har dödat Wumpus!", 5000, (WIDTH//2, HEIGHT//2 - 200))
                    self.channel0.stop()
                    self.play_sound(self.win_sound, 10000)
                    self.ui.winlose_text("DU VANN!")
                    no_collision_detected = False
                    self.player_win = True
                    self.menu.add_high_score(self.ui.score_amount)
                    if pygame.time.get_ticks() - self.arrow_timer > 9000:
                        self.ui.fire_arrow("Tryck esc för att återvända till startmenyn")

        # Hanterar vad som ska hända när pilen försvinner
        if self.arrow_created and pygame.time.get_ticks() - self.arrow_timer > 4000 and not self.player_win:

             # Hanterar om spelaren har slut på pilar och den sista pilen inte träffar Wumpus
            if self.ui.arrow_counter():
                self.arrow.kill()
                self.arrow_control = False
                self.ui.draw_text("Dina pilar är slut!", 5000, (WIDTH//2, HEIGHT//2 - 200))
                self.remove_fog()
                self.player.kill()
                self.darkness = False
                self.channel0.stop()
                self.channel2.play(self.game_over)
                self.ui.winlose_text("GAME OVER")
                self.ui.fire_arrow("Tryck esc för att återvända till startmenyn")

            # Spelaren har inte slut på pilar
            else:
                self.arrow.kill()
                self.arrow_created = False
                self.arrow_control = False
                no_collision_detected = True

        # Hanterar om spelaren går in i ett rum med Wumpus
        for sprite in self.wumpus_sprite:    
            if sprite.hitbox.colliderect(self.player):
                self.ui.draw_text("Du har blivit uppäten av Wumpus!", 5000, (WIDTH//2, HEIGHT//2 - 200))
                self.play_sound(self.wumpus_sound, 10000)
                self.player.kill()
                self.darkness = False
                self.remove_fog()
                self.channel0.stop()
                self.channel2.play(self.game_over)
                self.ui.winlose_text("GAME OVER")
                self.ui.fire_arrow("Tryck esc för att återvända till startmenyn")
                no_collision_detected = False

        # Hanterar om spelaren går in i ett rum med ett bottenlöst hål
        for sprite in self.pit_sprites:    
            if sprite.hitbox.colliderect(self.player):
                self.ui.draw_text("Du klev just ner i ett bottenlöst hål!", 5000, (WIDTH//2, HEIGHT//2 - 200))
                self.play_sound(self.pit_sound, 10000)
                self.player.kill()
                self.darkness = False
                self.remove_fog()
                self.channel0.stop()
                self.channel2.play(self.game_over)
                self.ui.winlose_text("GAME OVER")
                self.ui.fire_arrow("Tryck esc för att återvända till startmenyn")
                no_collision_detected = False

        # Hanterar om spelaren går in i ett rum med fladdermöss
        for sprite in self.bats_sprites:    
            if sprite.hitbox.colliderect(self.player):
                pygame.sprite.spritecollide(sprite, self.fog_sprites , True)
                self.play_sound(self.bat_sound, 1)
                
                if not self.player_teleport:
                    self.timer = pygame.time.get_ticks()
                    pos = (WIDTH//2,HEIGHT//2)

                    self.player_teleport = True
                    
                    # Animering där en bild av spelaren flyger uppåt
                    if not self.dummy_spawned:
                        self.dummy_spawned = True
                        self.dummy_player_rect = self.dummy_player.get_rect(center=pos)
                        self.player.kill()

                self.display_surface.blit(self.dummy_player, self.dummy_player_rect)
                self.dummy_player_rect.y -= 3

                if pygame.time.get_ticks() - self.timer < 2900:                
                    self.ui.draw_text("Du känner fladdermusvingar mot kinden och lyfts uppåt!", 1000, (WIDTH//2, HEIGHT//2 - 200))
                    no_collision_detected = False
                if 2900 <= pygame.time.get_ticks() - self.timer <= 3000:
                    no_collision_detected = True
                if pygame.time.get_ticks() - self.timer > 3000:
                    self.ui.draw_text("Efter en kort flygtur släpper fladdermössen ner dig i ett nytt rum.", 500, (WIDTH//2, HEIGHT//2 - 200))
                    no_collision_detected = False
                    if pygame.time.get_ticks() - self.timer >= 6000:
                        self.bat_drop() # Förflyttar spelaren till ett nytt rum
                        self.timer = 0
                        self.player_teleport = False
                        self.dummy_spawned = False           
                
        # Hanterar när spelaren går in i ett tomt rum
        for sprite in self.empty_room_sprite:    
            if sprite.hitbox.colliderect(self.player): # Berättar om det är en kollision
                self.check_entities_nearby() # Kontrollerar intilligande rum efter entiteter
                no_collision_detected = False

        # Återställer textemeddelande om en spelare lämnar ett rum
        if no_collision_detected:
            self.ui.reset_text()

        # Hanterar spelarens kollision med dimma
        for sprite in self.fog_sprites:
            if sprite.hitbox.colliderect(self.player):
                self.ui.score_counter()
                pygame.sprite.spritecollide(self.player, self.fog_sprites , True)
                if self.menu.wumpus_follow:
                    self.wumpus_movement()


    def mute(self):
        """
        Stänger av ljudet
        """
        self.sound = not self.sound
        if self.music_play:
            self.channel0.set_volume(0.1)
            self.channel1.set_volume(0.1)
        if not self.sound:
            self.channel0.set_volume(0)
            self.channel1.set_volume(0)

class YSortCameraGroup(pygame.sprite.Group):
    """
    Klass som hanterar alla visible_sprites förflyttning i förhållande till spelaren/pilen
    """
    def __init__(self):
        """
        Initialiseringsvärden
        """
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # Definierar golvytan
        self.floor_surface = pygame.image.load('graphics/ground.png').convert_alpha()
        self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))

    def custom_draw(self, player):
        """
        Ritar sprites i förhållande till spelaren

        INPUT = player, spelarens position
        """
        
        # Avgör offseten, dvs. hur "kartan" ska flyttas beroende på spelarens position
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # Ritar golvytan
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface, floor_offset_pos)

        # Ritar alla element sorterat efter deras y-position
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery): # Flyttar alla sprites i förhållande till spelaren för att imitera en kamera
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

    def custom_draw_fog(self, player):
        """
        Ritar "dimman" i förhållande till spelaren

        INPUT = player, spelarens position
        """
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
