import pygame

from map import Map

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

map = Map(screen, 100)

is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    screen.fill('White')

    map.update()
    map.draw()
    
    map.update()
    map.draw()
    
    pygame.display.update()
    clock.tick(33)