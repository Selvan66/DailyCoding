import pygame

class Player:
    def __init__(self, pos, screen_size):
        self.pos = pos
        self.screen_size = screen_size
        self.img = pygame.image.load('assets\image\player.png')
        self.velo = 300
        self.size = self.img.get_size()
        
    def draw(self, screen):
        screen.blit(self.img, self.pos)
    
    def real_time_input(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.pos = (self.pos[0] - (dt * self.velo), self.pos[1])
        if keys[pygame.K_RIGHT]:
            self.pos = (self.pos[0] + (dt * self.velo), self.pos[1])       
    
    def update(self, dt):
        padding = 4
        if (self.pos[0] <= padding):
            self.pos = (5, self.pos[1])
        if (self.pos[0] >= self.screen_size[0] - (self.size[0]) - padding):
            self.pos = (self.screen_size[0] - (self.size[0]) - padding, self.pos[1])

class Enemy:
    def __init__(self, pos, screen_size):
        self.pos = pos
        self.screen_size = screen_size
        self.img = pygame.image.load('assets\image\enemy.png')
        self.velo = 100
        self.size = self.img.get_size()
        self.passed = 0
        self.left_side = False
    
    def draw(self, screen):
        screen.blit(self.img, self.pos)
        
    def update(self, dt):
        if self.left_side:
            self.passed += (dt * self.velo)
            self.pos = (self.pos[0] - (dt * self.velo), self.pos[1])
        if not self.left_side:
            self.passed += (dt * self.velo)
            self.pos = (self.pos[0] + (dt * self.velo), self.pos[1])
        
        if self.passed >= self.screen_size[0] / 7:
            self.passed = 0
            self.left_side = not self.left_side
            self.pos = (self.pos[0], self.pos[1] + self.screen_size[1]/40)
   
class Game:
    def __init__(self):
        pygame.init()
        self.init_display()      
        self.running = True
        self.player = Player((self.size[0]/2, self.size[1] * (5/6)), self.size)
        self.makes_enemies()
        
    def init_display(self):
        self.size = (800, 600)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Space Invanders")
        icon = pygame.image.load('assets/image/ufo.png')
        pygame.display.set_icon(icon)
    
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
                 
    def process_input(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.player.real_time_input(dt)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        pygame.display.update()

    def update(self, dt):
        if self.check_game_over():
            self.running = False
        self.player.update(dt)
        for enemy in self.enemies:
            enemy.update(dt)
    
    def check_game_over(self):
        for enemy in self.enemies:
            if enemy.pos[1] >= self.player.pos[1]:
                return True
        return False

if __name__ == '__main__':
    game = Game()
    game.run()