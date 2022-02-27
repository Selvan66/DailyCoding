import pygame
import random
import numpy as np

class Ant(pygame.sprite.Sprite):
    def __init__(self, angle, position):
        pygame.sprite.Sprite.__init__(self)
        self.v = 4
        self.ang = angle
        self.img = pygame.image.load('assets/ant.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.img, np.degrees(self.ang), 0.5)
        self.rect = self.image.get_rect(center=position) 
        self.goto = False
        self.goto_pos = (0, 0)
        self.goto_ang = 0
    
    def collision(self, rect):
        if not rect.colliderect(self.rect):
            self.ang += np.pi
    
    def move(self):
        if self.goto:
            vec = (self.rect.center[0] - self.goto_pos[0], self.rect.center[1] - self.goto_pos[1])
            if np.sqrt(vec[0] * vec[0] + vec[1] * vec[1]) <= 15:
                self.goto = False
            else:
                self.ang = self.goto_ang
                 
        way = random.randint(0, 3)
        if way == 0:
            self.ang -= np.pi / 18
        elif way == 3:
            self.ang += np.pi / 18
                
        vector = (-self.v * np.sin(self.ang), -self.v * np.cos(self.ang))
        return vector
    
    def go_to(self, position):
        self.goto = True
        self.goto_pos = position
        vec = (self.rect.center[0] - self.goto_pos[0], self.rect.center[1] - self.goto_pos[1])
        self.goto_ang = np.arctan2(vec[1], vec[0])
    
    def update(self):
        vector = self.move()
        
        self.rect.x += vector[0]
        self.rect.y += vector[1]
        
        self.image = pygame.transform.rotozoom(self.img, np.degrees(self.ang), 0.5)