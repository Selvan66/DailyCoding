import pygame
import random, math

from ant import Ant

class Nest:
    def __init__(self, position, amount, screen):
        self.pos = position
        self.amount = amount
        self.screen = screen
        self.r = 20
        self.grupe = pygame.sprite.Group()
        self.init_ants()
        for ant in self.grupe:
            ant.go_to((100, 100))
    
    def init_ants(self):
        for _ in range(self.amount):
            angle = random.randint(0, 359)
            self.grupe.add(Ant(math.radians(angle), self.pos))
    
    def draw(self):
        pygame.draw.circle(self.screen, 'Blue', self.pos, self.r)
        self.grupe.draw(self.screen)
    
    def update(self):
        self.grupe.update()
        
        for ant in self.grupe:
            ant.collision(self.screen.get_rect())