import pygame as pg
import math, sys
from random import randint

from dft import dft

pg.init()
screen = pg.display.set_mode((800, 800))
pg.display.set_caption('Fourier Series')

clock = pg.time.Clock()

num = 200
points = []
sygnal = [100 * math.cos(2 * math.pi * i * 1/num) for i in range(num)]
fourier = dft(sygnal)
time = 0

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill((0, 0, 0))
            
    circle_pos = (screen.get_width() / 4, screen.get_height() / 2)
    x = 0
    y = 0
    
    for i in range(num):
        freq = fourier[i][2]
        radius = fourier[i][3]
        phase = fourier[i][4]
        x = radius * math.cos(freq * time + phase + math.pi/2) + circle_pos[0]
        y = radius * math.sin(freq * time + phase + math.pi/2) + circle_pos[1]
        
        
        pg.draw.circle(screen, 'White', circle_pos, radius, 2)
        pg.draw.line(screen, 'White', circle_pos, (x, y))
        circle_pos = (x, y)
        pg.draw.circle(screen , 'White', (x, y), 3)
        
        
    points = [y] + points
    if (len(points) > 300):
        points.pop()
        
    for i in range(len(points) - 1):
        pg.draw.aaline(screen, 'White', (i + 500, points[i]), (i + 501, points[i + 1]))
    pg.draw.line(screen, 'White', (x, y), (500, points[0]), 2)
    pg.display.update()
    
    dt = 2 * math.pi / num
    time += dt
    
    if time > 2 * math.pi:
        time = 0
    
    clock.tick(60)