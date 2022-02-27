import pygame

from nest import Nest

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

nest = Nest((400, 400), 3, screen)

is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    screen.fill('White')

    nest.draw()
    nest.update()
    pygame.draw.circle(screen, 'Red', (100, 100), 5)
    pygame.display.update()
    clock.tick(33)