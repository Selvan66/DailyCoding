import pygame as pg
import math, sys
from random import randint

pg.init()
screen = pg.display.set_mode((800, 400))
pg.display.set_caption('Fourier Series')

clock = pg.time.Clock()

radius = 100

num = 7
points = []

colors = []
for i in range(num + 1):
    colors.append((randint(0, 255), randint(0, 255), randint(0, 255)))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    time = pg.time.get_ticks() / 1000
            
    circle_pos = (screen.get_width() / 4, screen.get_height() / 2)
    x = 0
    y = 0
    
    for i in range(num):
        n = i * 2 + 1
        radius = 70 * (4 / (n * math.pi))
        x = radius * math.cos(n * time) + circle_pos[0]
        y = radius * math.sin(n * time) + circle_pos[1]
        pg.draw.circle(screen, colors[i], circle_pos, radius, 2)
        pg.draw.line(screen, colors[i], circle_pos, (x, y))
        circle_pos = (x, y)
        pg.draw.circle(screen , colors[i], (x, y), 3)
    points = [y] + points
    if (len(points) > 300):
        points.pop()
    for i in range(len(points)):
        pg.draw.circle(screen, colors[-1], (i + 500, points[i]), 1)
    pg.draw.line(screen, colors[-1], (x, y), (500, points[0]), 2)
    pg.display.update()
    clock.tick(60)