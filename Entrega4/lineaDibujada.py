import pygame
import sys
import time
from random import randint
from pygame.locals import *

x = 10
y = 10

def main():
	global x
	global y
	pygame.init()
	ventana = pygame.display.set_mode((700,600))
	pygame.display.set_caption("BatCar!!")
	FPS = 500
	clock = pygame.time.Clock()
	l = [[x,y,10,10]]
	c = 10
	c2 = 0
	x = 10
	y = 10
	xf = 10
	yf = 10

	while True:
		ventana.fill((255,255,255))
		random_color = (randint(100,255), randint(0,199), randint(0,200))
		pInicio = [x,y]
		tkla = pygame.key.get_pressed() 
		oldxf = xf
		oldyf = yf
		if tkla[K_LEFT]:
			xf -= 5
		elif tkla[K_RIGHT]: 
			xf += 5
		
		if tkla[K_DOWN]:
			yf += 5  
		elif tkla[K_UP]:
			yf -= 5
		
		pygame.draw.line(ventana,random_color,pInicio,(xf,yf),7)
		
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
		
		pygame.display.update()
		clock.tick(60)


main()
