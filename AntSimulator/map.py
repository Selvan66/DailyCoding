import pygame
import random, math
from enum import Enum

from ant import Ant

class Objects(Enum):
    NONE = 0
    NEST = 1
    LEAF = 2
    PHEROMONE = 3


class Map:
    def __init__(self, screen, side):
        self.screen = screen
        self.side = side
        self.side_size = screen.get_rect().width / side
        self.grid = {}
        for i in range(side):
            for j in range(side):
                self.grid[(i, j)] = Objects.NONE

        self.nest_pos = (side // 2, side // 2)
        self.grid[self.nest_pos] = Objects.NEST
    
        self.ants = pygame.sprite.Group()
        self.ants_amount = 30
        self.init_ants()
        
        self.leaf = pygame.image.load('assets/leaf.png').convert_alpha()
        self.leaf = pygame.transform.rotozoom(self.leaf, 0, 0.5)
        self.grid[(0, 0)] = Objects.LEAF
        self.grid[(1, 1)] = Objects.LEAF
        self.grid[(2, 2)] = Objects.LEAF
        
    def init_ants(self):
        pos = self.from_grid_to_pos(self.nest_pos)
        for _ in range(self.ants_amount):
            angle = random.randint(0, 359)
            self.ants.add(Ant(math.radians(angle), pos))
    
    def from_grid_to_pos(self, grid):
        return (grid[0] * self.side_size, grid[1] * self.side_size)
    
    def draw(self):
        self.draw_grid()
        
        self.ants.draw(self.screen)
        
        for (pos, obj) in self.grid.items():
            if obj == Objects.NEST:
                pygame.draw.circle(self.screen, 'Blue', self.from_grid_to_pos(pos), 20)
            elif obj == Objects.LEAF:
                self.screen.blit(self.leaf, pygame.Rect(self.from_grid_to_pos(pos), (10, 10)))
    
    def draw_grid(self):
        for i in range(self.side):
            pygame.draw.line(self.screen, 'Red', (0, i * self.side_size), (self.screen.get_rect().width, i * self.side_size))
        for i in range(self.side):
            pygame.draw.line(self.screen, 'Red', (i * self.side_size, 0), (i* self.side_size, self.screen.get_rect().height))
    def update(self):
        
        self.ants.update()
        for ant in self.ants:
            ant.collision(self.screen.get_rect())