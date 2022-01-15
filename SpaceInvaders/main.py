import pygame
from pygame import mixer

class Player:
    def __init__(self, pos, screen_size):
        self.pos = pos
        self.screen_size = screen_size
        self.img = pygame.image.load('assets\image\player.png')
        self.velo = 300
        self.size = self.img.get_size()
        self.dt_shot = 0
        self.create_bullet = False
        self.can_create_bullet = True
        
    def draw(self, screen):
        screen.blit(self.img, self.pos)
    
    def real_time_input(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.pos = (self.pos[0] - (dt * self.velo), self.pos[1])
        if keys[pygame.K_RIGHT]:
            self.pos = (self.pos[0] + (dt * self.velo), self.pos[1])
        if keys[pygame.K_SPACE]:
            self.create_bullet = True
    
    def update(self, dt):
        padding = 4
        if (self.pos[0] <= padding):
            self.pos = (5, self.pos[1])
        if (self.pos[0] >= self.screen_size[0] - (self.size[0]) - padding):
            self.pos = (self.screen_size[0] - (self.size[0]) - padding, self.pos[1])

    def get_bounding(self):
        return (self.pos[0], self.pos[1], self.img.get_size()[0], self.img.get_size()[1])
    
    def is_created_bullet(self, dt):
        if self.can_create_bullet:
            if self.create_bullet:
                self.can_create_bullet = False
                mixer.Sound('assets/sounds/laser.wav').play()
                return True
        else:
            self.dt_shot += dt
            if self.dt_shot >= 1:
                self.dt_shot = 0
                self.can_create_bullet = True
                self.create_bullet = False
        return False
class Enemy:
    def __init__(self, pos, screen_size):
        self.pos = pos
        self.screen_size = screen_size
        self.img = pygame.image.load('assets\image\enemy.png')
        self.velo = 100
        self.size = self.img.get_size()
        self.passed = 0
        self.left_side = False
        self.destroied = False
    
    def draw(self, screen):
        screen.blit(self.img, self.pos)
        
    def update(self, dt):
        if self.left_side:
            self.passed += (dt * self.velo)
            self.pos = (self.pos[0] - (dt * self.velo), self.pos[1])
        if not self.left_side:
            self.passed += (dt * self.velo)
            self.pos = (self.pos[0] + (dt * self.velo), self.pos[1])
        
        if self.passed >= self.screen_size[0] / 5:
            self.passed = 0
            self.left_side = not self.left_side
            self.pos = (self.pos[0], self.pos[1] + self.screen_size[1]/40)

    def get_bounding(self):
        return (self.pos[0], self.pos[1], self.img.get_size()[0], self.img.get_size()[1])
    
class Bullet:
    def __init__(self, pos):
        self.pos = pos
        self.velo = 500
        self.img = pygame.image.load('assets/image/bullet.png')
        self.destroied = False
            
    def draw(self, screen):
        screen.blit(self.img, self.pos)
    
    def update(self, dt):
        self.pos = (self.pos[0], self.pos[1] - (dt * self.velo))
        
    def get_bounding(self):
        return (self.pos[0], self.pos[1], self.img.get_size()[0], self.img.get_size()[1])
class Game:
    def __init__(self):
        pygame.init()
        self.init_display()      
        self.running = True
        self.player = Player((self.size[0]/2, self.size[1] * (5/6)), self.size)
        self.makes_enemies()
        self.bullets = []
        mixer.Sound('assets/sounds/background.wav').play(-1)
            
    def init_display(self):
        self.size = (800, 600)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Space Invanders")
        icon = pygame.image.load('assets/image/ufo.png')
        pygame.display.set_icon(icon)
        self.background = pygame.image.load('assets/image/background.png')
    
    def makes_enemies(self):
        self.enemies = [Enemy((self.size[0]/8 * (x + 1), self.size[1]/8 * (y + 1)), self.size) for x in range(5) for y in range(2)]
    
    
    def run(self):
        dt = 0
        fps = 60
        clock = pygame.time.Clock()
        clock.tick(fps)
        while self.running:
            dt = clock.tick(fps) / 1000.0
            self.process_input(dt)
            self.update(dt)
            self.draw()
        if self.enemies:
            print("Game over")
        else:
            print("You Win")
                 
    def process_input(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.player.real_time_input(dt)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        self.player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        for bullet in self.bullets:
            bullet.draw(self.screen)
        pygame.display.update()

    def update(self, dt):
        self.collision_test()
        self.player.update(dt)
        if self.player.is_created_bullet(dt):
            self.bullets.append(Bullet((self.player.pos[0] + self.player.get_bounding()[2] / 4, self.player.pos[1] - self.player.get_bounding()[3] / 4)))
        for enemy in self.enemies:
            enemy.update(dt)
        for bullet in self.bullets:
            bullet.update(dt)
        if not self.enemies:
            self.running = False
    
    def check_collision(self, a, b):
        left_top_a = (a[0], a[1])
        right_down_a = (a[0] + a[2], a[1] + a[3])
        left_top_b = (b[0], b[1])
        right_down_b =  (b[0] + b[2], b[1] + b[3])
        
        if left_top_a[0] <= left_top_b[0] <= right_down_a[0]:
            if left_top_a[1] <= left_top_b[1] <= right_down_a[1]:
                return True
            if left_top_a[1] <= right_down_b[1] <= right_down_a[1]:
                return True
        if left_top_a[0] <= right_down_b[0] <= right_down_a[0]:
            if left_top_a[1] <= left_top_b[1] <= right_down_a[1]:
                return True
            if left_top_a[1] <= right_down_b[1] <= right_down_a[1]:
                return True
        return False
    
    def collision_test(self):
        for enemy in self.enemies:
            if self.check_collision(enemy.get_bounding(), self.player.get_bounding()):
                self.running = False
            if not self.check_collision((0, 0, self.size[0], self.size[1]), enemy.get_bounding()):
                self.running = False
            for bullet in self.bullets:
                if self.check_collision(enemy.get_bounding(), bullet.get_bounding()):
                    mixer.Sound('assets/sounds/explosion.wav').play()
                    enemy.destroied = True
                    bullet.destroied = True            

        self.enemies = [x for x in self.enemies if not x.destroied]
        self.bullets = [x for x in self.bullets if not x.destroied]

if __name__ == '__main__':
    game = Game()
    game.run()