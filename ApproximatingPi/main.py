import pygame as pg
import random as rd
import math
import sys


pg.init()
screen = pg.display.set_mode((400, 450))
clock = pg.time.Clock()

font = pg.font.Font('Sansation.ttf', 30)

approx = 0
corrent = 0
text_pi = font.render(f'Pi: {approx}', False, 'White')
text_pi_rec = text_pi.get_rect(bottomleft=(5, 445))

shot = 0
text_shots = font.render(f'Shots: {shot}', False, 'indianred2')
text_shots_rec = text_shots.get_rect(topleft=(0, 0))

circle_radius = 190
circle_pos = (200, 220)

points = set()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    shot += 1
    x = rd.randint(10, 390)
    y = rd.randint(30, 410)
    
    if math.sqrt(math.pow((x - circle_pos[0]),2) + math.pow((y - circle_pos[1]), 2)) <= circle_radius:
        corrent += 1
        points.add((x, y, 'chartreuse3'))  
    else:
        points.add((x, y, 'indianred2')) 
        
    approx = (corrent/shot) * 4
    text_pi = font.render('Pi: %.5f' % approx, False, 'White')
    text_shots = font.render(f'Shots: {shot}', False, 'indianred2')
    
    screen.fill((0, 0, 0))
    
    screen.blit(text_pi, text_pi_rec)
    screen.blit(text_shots, text_shots_rec)
    pg.draw.circle(screen, 'White', circle_pos, circle_radius, 1)
    
    for p in points:
        pg.draw.circle(screen, p[2], (p[0], p[1]), 2)
    
    pg.display.update()
    #clock.tick(60)