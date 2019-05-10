import pygame
import sys
import time
from random import randint
from pygame.locals import *

def main():
	pygame.init()
	ventana = pygame.display.set_mode((700,600))
	pygame.display.set_caption("BatCar!!")
	FPS = 500
	clock = pygame.time.Clock()
	
	while True:
		l = []
		c = 100
		x = 10
		y = 5
		ventana.fill((255,255,255)) 
		for i in range(c):
			r = [x,y,10,10]
			l.append(r)
			x += 10
			y += 5
		x = 0
		
		while x != len(l):
			random_color = (randint(100,255), randint(0,199), randint(0,200))
			pygame.draw.rect(ventana,random_color,l[x])
			x += 1
		
		
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
		
		pygame.display.update()
		clock.tick(120)


main()
	

