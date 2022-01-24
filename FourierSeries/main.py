import pygame as pg
import math, sys
from dft import dft

def readPointsFromFile(file):
	p = []
	with open(file) as f:
		for line in f.readlines():
			p.append(eval(line))
	return p

def readPointsFromDrawing(screen):
	p = []
	start = False
	clock = pg.time.Clock()
	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			if event.type == pg.MOUSEBUTTONDOWN:
				start = True
			if event.type == pg.MOUSEBUTTONUP:
				start = False
		if p and not start:
			return p
		if start:
			p.append(pg.mouse.get_pos())
		screen.fill('Black')
		if len(p) > 1:
			pg.draw.aalines(screen, 'White', False, p)
		pg.display.update()	
		clock.tick(33)
  

def drawFourier(x, y, rotation, fourier):
	num = len(fourier)
	for i in range(num):
		prev = (x, y)
		freq = fourier[i][2]
		radius = fourier[i][3]
		phase = fourier[i][4]
		x += radius * math.cos(freq * time + phase + rotation)
		y += radius * math.sin(freq * time + phase + rotation)
		
		pg.draw.circle(screen, 'White', prev, radius, 5)
		pg.draw.line(screen, 'White', prev, (x, y))
		
	return (x, y)

############### SETUP #####################
pg.init()
screen = pg.display.set_mode((800, 800))
pg.display.set_caption('Fourier Series')

clock = pg.time.Clock()
time = 0

path = []

points = readPointsFromFile('img/points.txt')
vec = (points[0])
sygnal = [(points[i][0] - vec[0]) * 3 for i in range(0, len(points), 5)]
fourierX = dft(sygnal)
sygnal = [(points[i][1] - vec[1]) * 3 for i in range(0, len(points), 5)]
fourierY = dft(sygnal)
num = len(fourierX)


############################################
	
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
 
	dt = 2 * math.pi / num
	time += dt
	
	if time > 2 * math.pi:
		time = 0
		path = []
	
	pg.display.update()
	clock.tick(33)