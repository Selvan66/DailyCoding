import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((64, 64), pg.SCALED | pg.RESIZABLE)
img = pg.image.load('a.jpg').convert()
points = []
clock = pg.time.Clock()



while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            with open('points.txt', 'w') as file:
                for p in points:
                    file.write(str(p) + '\n')
            sys.exit()
            
    if pg.mouse.get_pressed()[0]:
        points.append(pg.mouse.get_pos())
    
    screen.fill('Black')
    screen.blit(img, (0, 0))
    for p in points:
        pg.draw.rect(screen, 'Red', pg.Rect(p, (1, 1)))
    pg.display.update()
    clock.tick(33)