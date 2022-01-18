import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_walk_1 = pygame.image.load('graphics/player/player_walk1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/player/player_walk2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/player/player_jump.png').convert_alpha()
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound('audio/jump.wav')
        self.jump_sound.set_volume(0.3)
        
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()
            
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
            
    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
    
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()
        
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        pygame.sprite.Sprite.__init__(self)
        
        if type == 'fly':
            fly_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
            fly_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))
        
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
        
    def destroy(self):
        if self.rect.x <= -100:
            self.kill() 
        
    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()
        
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption('Dodge Runner')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('font/Pixeltype.ttf', 50)
        self.game_active = False
        self.time_start = 0
        self.score = 0
        
        bg_music = pygame.mixer.Sound('audio/music.wav')
        bg_music.set_volume(0.3)
        bg_music.play(loops = -1)
        
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())
        
        self.obstacle = pygame.sprite.Group()
        
        self.sky = pygame.image.load('graphics/sky.png').convert()
        self.ground = pygame.image.load('graphics/ground.png').convert()
    
        self.player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
        self.player_stand = pygame.transform.rotozoom(self.player_stand, 0, 2)
        self.player_stand_rect = self.player_stand.get_rect(center = (self.screen.get_rect().center))
        
        self.game_name = self.font.render('Pixel Runner', False, (111, 196, 169))
        self.game_name_rect = self.game_name.get_rect(midbottom = (self.player_stand_rect.midtop))
        
        self.game_message = self.font.render('Press space to run', False, (111, 196, 169))
        self.game_message_rect = self.game_message.get_rect(midtop = (self.player_stand_rect.midbottom))
        
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1500)
    
    def display_score(self):
        current_time = int(pygame.time.get_ticks() / 1000) - self.time_start
        score_surf = self.font.render(f'Score: {current_time}', False, (64, 64, 64))
        score_rect = score_surf.get_rect(center = (400, 50))
        self.screen.blit(score_surf, score_rect)
        return current_time
    
    def collision_sprite(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.obstacle, False):
            self.obstacle.empty()
            return False
        return True
    
    def draw_intro(self):
        self.screen.fill((94, 129, 162))
        self.screen.blit(self.player_stand, self.player_stand_rect)
        self.screen.blit(self.game_name, self.game_name_rect)
        if self.score == 0:
            self.screen.blit(self.game_message, self.game_message_rect)
        else:
            score_message = self.font.render(f'Your socre {self.score}', False, (111, 196, 169))
            self.screen.blit(score_message, self.game_message_rect)

    
    def draw_game(self):
        self.screen.blit(self.sky, (0, 0))
        self.screen.blit(self.ground, (0, 300))
        score = self.display_score()
        
        self.player.draw(self.screen)
        self.player.update()
        
        self.obstacle.draw(self.screen)
        self.obstacle.update()
              
    
    def process_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if self.game_active:
                if event.type == self.obstacle_timer:
                    self.obstacle.add(Obstacle(choice(['fly', 'snail', 'snail'])))
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.game_active = True
                    self.time_start = int(pygame.time.get_ticks() / 1000)
                    
    def run(self):
        while True:
            self.process_event()
            if self.game_active:
                self.draw_game()
                self.game_active = self.collision_sprite()
            else:
                self.draw_intro()
            pygame.display.update()
            self.clock.tick(60)
            
if __name__ == '__main__':
    game = Game()
    game.run()