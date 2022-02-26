import pygame
import math

from ant import Ant

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()


ants = pygame.sprite.Group()
ants.add(Ant(90, (200, 200)))
ants.add(Ant(90, (200, 200)))
ants.add(Ant(90, (200, 200)))
ants.add(Ant(90, (200, 200)))
ants.add(Ant(90, (200, 200)))
ants.add(Ant(90, (200, 200)))
ants.add(Ant(90, (200, 200)))
ants.add(Ant(90, (200, 200)))
ants.add(Ant(90, (200, 200)))
ants.add(Ant(90, (200, 200)))
ants.add(Ant(90, (200, 200)))
ants.add(Ant(90, (200, 200)))
ants.add(Ant(90, (200, 200)))
ants.add(Ant(90, (200, 200)))
ants.add(Ant(90, (200, 200)))
ants.add(Ant(90, (200, 200)))
ants.add(Ant(90, (200, 200)))
ants.add(Ant(90, (200, 200)))
ants.add(Ant(90, (200, 200)))
ants.add(Ant(180, (200, 300)))
ants.add(Ant(270, (200, 400)))
ants.add(Ant(180, (300, 100)))
ants.add(Ant(90, (300, 200)))
ants.add(Ant(0, (300, 300)))
ants.add(Ant(180, (400, 400)))

is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    screen.fill('White')

    for ant in ants:
        ant.turn_back(screen)
    
    
    ants.draw(screen)
    ants.update()
    
    pygame.display.update()
    clock.tick(33)