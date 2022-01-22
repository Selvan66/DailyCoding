import pygame as pg
import math, sys
from dft import dft

def readPointsFromFile(file):
    p = []
    with open(file) as f:
        for line in f.readlines():
            p.append(eval(line))
    return p

############### SETUP #####################
pg.init()
screen = pg.display.set_mode((800, 800))
pg.display.set_caption('Fourier Series')

clock = pg.time.Clock()
time = 0

num = 200
path = []

sygnal = [100 * math.sin(2 * math.pi * i * 3 * 1/num) for i in range(num)]
fourierX = dft(sygnal)
sygnal = [50 * math.cos(2 * math.pi * i * 5 * 1/num) for i in range(num)]
fourierY = dft(sygnal)


############################################

def drawFourier(x, y, rotation, fourier):
	num = len(fourier)
	for i in range(num):
		prev = (x, y)
		freq = fourier[i][2]
		radius = fourier[i][3]
		phase = fourier[i][4]
		x += radius * math.cos(freq * time + phase + rotation)
		y += radius * math.sin(freq * time + phase + rotation)
		
		pg.draw.circle(screen, 'White', prev, radius, 2)
		pg.draw.line(screen, 'White', prev, (x, y))
		
	return (x, y)
	
	
	
while True:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()

	screen.fill((0, 0, 0))
			
	vx = drawFourier(screen.get_width() / 2 + 100, 100, 0, fourierX) 
	vy = drawFourier(100, screen.get_height() / 2 + 100, math.pi/2, fourierY) 
	v = (vx[0], vy[1])
	path.insert(0, v)
	
	if len(path) != 1:
		pg.draw.lines(screen, 'White', False, path)
	
	pg.draw.line(screen, 'White', vx, v)
	pg.draw.line(screen, 'White', vy, v)
 
	if len(path) > 300:
		path.pop()
 
	dt = 2 * math.pi / num
	time += dt
	
	if time > 2 * math.pi:
		time = 0
		path = []
	
	pg.display.update()
	clock.tick(33)