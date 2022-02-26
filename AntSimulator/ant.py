from multiprocessing.spawn import import_main_path
import pygame
import random
import math

class Ant(pygame.sprite.Sprite):
    def __init__(self, angle, position):
        pygame.sprite.Sprite.__init__(self)
        self.v = 4
        self.ang = angle
        self.img = pygame.image.load('assets/ant.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.img, angle, 0.5)
        self.rect = self.image.get_rect(center=position) 
    
    
    def turn_back(self, screen):
        if not screen.get_rect().colliderect(self.rect):
            self.ang += 180
    
    def update(self):
        # random pick the way (left, straight, right)
        way = random.randint(0, 3)
        if way == 0:
            self.ang -= 10
        elif way == 3:
            self.ang += 10
        
        self.ang = self.ang % 360
        vector = (-self.v * math.sin(math.radians(self.ang)), -self.v * math.cos(math.radians(self.ang)))
        self.rect.x += vector[0]
        self.rect.y += vector[1]
        
        self.image = pygame.transform.rotozoom(self.img, self.ang, 0.5)