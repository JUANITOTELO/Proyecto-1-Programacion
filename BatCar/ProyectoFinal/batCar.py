#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 14:43:35 2019

@author: Juan David Martinez
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
import serial
import sys
import time
import random
from random import randint
from pygame.locals import *

up = False
down = False
izquierda = False
derecha = False


def imagen(s):
    x_imagen = pygame.image.load(s)
    return x_imagen

def teclado():

    teclado = pygame.key.get_pressed()
    global up
    global down
    global izquierda
    global derecha
    global v_Y_Carro
    global v_X_Carro

    if (teclado[K_RIGHT] and teclado[K_UP]) or (teclado[K_RIGHT] and teclado[K_DOWN]):
        up = False
        down = False
        izquierda = False
        derecha = False

    if teclado[K_d] or teclado[K_RIGHT]:
        derecha = True
        izquierda = False
        up = False
        down = False


    elif teclado[K_a] or teclado[K_LEFT]:
        derecha = False
        izquierda = True
        up = False
        down = False


    elif teclado[K_w] or teclado[K_UP]:
        derecha = False
        izquierda = False
        up = True
        down = False


    elif teclado[K_s] or teclado[K_DOWN]:
        derecha = False
        izquierda = False
        up = False
        down = True
        
pygame.init()
random_color = (randint(100,255), randint(0,199), randint(0,200))
RED = (255,0,0,150)
class rectangle:
	def __init__(self, x, y, w, h,c, id):
		global random_color
		global RED
		self.x1 = x
		self.y1 = y
		self.x2 = x + w
		self.y2 = y + h
	
		self.w = w
		self.h = h
	
		self.fillColor = c
	
		self.stained = False
		self.id = id
	
	def setXY(self, xy):
		self.x1, self.y1 = xy
		self.x2 = xy[0] + self.w
		self.y2 = xy[1] + self.h
	
	def getXY(self):
		return (self.x1, self.y1)
	
	def rect(self):
		return self.getXY() + (self.w, self.h)
	
	def coords(self):
		return self.getXY() + (self.x2, self.y2)
	
	def hasCollided(self, target):
		tx1, ty1, tx2, ty2 = target.coords()
		if tx1 > self.x2 or tx2 < self.x1 or ty1 > self.y2 or ty2 < self.y1: return False
		return True
	
	def draw(self, surface = None):
		if not surface: surface = pygame.display.get_surface()
		pygame.draw.rect(surface, self.fillColor, self.rect(),0)
	
	def __str__(self):
		return ("x1:{0}\ny1:{1}\nx2:{2}\ny2:{3}\nid: {4}\n".format(self.x1,self.y1,self.x2,self.y2,self.id))
	
	
def detectarObs():
	obstaculo = False
	count = -2
	archivo = open("coor.txt","r")
	x = archivo.read()
	x = x.split("\n")
	nEntero = int(x[count])
	archivo.close()
	return nEntero
	
	
def main():
	
	ser = serial.Serial('COM6', 9600)
	
	W,H = 1080,900
	HW,HH = W/2,H/2
	AREA = W * H
	ventana = pygame.display.set_mode((W,H))
	pygame.display.set_caption("BatCar!!")
	FPS = 500
	clock = pygame.time.Clock()
	
	Carro = imagen("imagenes_carros/carro_planoDerecha.png").convert_alpha()
	Carro = pygame.transform.scale(Carro,(75,38))
	
	CarroIzquierda = imagen("imagenes_carros/carro_planoIzquierda.png").convert_alpha()
	Carro_r_Izquierda = pygame.transform.scale(CarroIzquierda,(75,38))
	
	CarroArriba = imagen("imagenes_carros/carro_planoUp.png").convert_alpha()
	Carro_r_Arriba = pygame.transform.scale(CarroArriba,(38,75))
	
	CarroAbajo = imagen("imagenes_carros/carro_planoDown.png").convert_alpha()
	Carro_r_Abajo = pygame.transform.scale(CarroAbajo,(38,75))
	
	fondo = imagen("fondo2.png").convert_alpha()
	fRs = pygame.transform.scale(fondo,(W,H))
	
	r_Carro = Carro.get_rect()
	c_x_r_Carro = r_Carro.centerx
	c_y_r_Carro = r_Carro.centery
	posXc = HW-c_x_r_Carro
	posYc = HH-c_y_r_Carro
	
	r_Carro2 = Carro_r_Arriba.get_rect()
	c_x_r_Carro2 = r_Carro2.centerx
	c_y_r_Carro2 = r_Carro2.centery
	posXc2 = HW-c_x_r_Carro2
	posYc2 = HH-c_y_r_Carro2
	
	while True:
		g = 0
		x = 593
		y = 345
		c = 2
		lx = [posXc+(r_Carro.width/2) + 90]
		ly = [posYc+(r_Carro.height/2)-5]
		lx2 = [posXc2+(r_Carro2.height/2)-21]
		ly2 = [posYc2+(r_Carro2.width/2) + 90]

		lxi = [posXc-(r_Carro.width/2) -30]
		lyi = [posYc-(r_Carro.height/2)+32]
		lx2i = [posXc2-(r_Carro2.height/2) +52]
		ly2i = [posYc2-(r_Carro2.width/2) - 30]

		random_color = (randint(100,255), randint(0,199), randint(0,200))
		rectangles = list([rectangle(lx[0],  ly[0], 10, 10,random_color, i) for i in range(0, c)])
		rectangles2 = list([rectangle(lx2[0],  ly2[0], 10, 10,random_color, i) for i in range(0, c)])
		rectanglesi = list([rectangle(lxi[0],  lyi[0], 10, 10,random_color, i) for i in range(0, c)])
		rectangles2i = list([rectangle(lx2i[0],  ly2i[0], 10, 10,random_color, i) for i in range(0, c)])

		rectanglesNot = list([rectangle(lx[0],  ly[0], 10, 10,RED, i) for i in range(0, c)])
		rectangles2Not = list([rectangle(lx2[0],  ly2[0], 10, 10,RED, i) for i in range(0, c)])
		rectanglesiNot = list([rectangle(lxi[0],  lyi[0], 10, 10,RED, i) for i in range(0, c)])
		rectangles2iNot = list([rectangle(lx2i[0],  ly2i[0], 10, 10,RED, i) for i in range(0, c)])
		teclado()
		tkla = pygame.key.get_pressed()
		ventana.fill((255,255,255))
		random_color = (randint(100,255), randint(0,199), randint(0,200))
		ventana.blit(fRs,[0,0])


		if izquierda == True:
			for r in rectanglesiNot:
				if r.id == 0: continue
				print("POSICIONES DE RECTANGULO IZQUIERDA:\n",r)
				r.draw()
			ventana.blit(Carro_r_Izquierda,[posXc,posYc])
		elif derecha == True:
			for r in rectanglesNot:
				if r.id == 0: continue
				print("POSICIONES DE RECTANGULO DERECHA:\n",r)
				r.draw()
			ventana.blit(Carro,[posXc,posYc])
		elif down == True:
			for r in rectangles2Not:
				if r.id == 0: continue
				print("POSICIONES DE RECTANGULO ABAJO:\n",r)
				r.draw()
			ventana.blit(Carro_r_Abajo,[posXc2,posYc2])
		elif up == True:
			for r in rectangles2iNot:
				if r.id == 0: continue
				print("POSICIONES DE RECTANGULO ARRIBA:\n",r)
				r.draw()
			ventana.blit(Carro_r_Arriba,[posXc2,posYc2])

		if tkla[K_a]:
			ser.write(bytes(b'b'))

		if tkla[K_LEFT]:
			ser.write(bytes(b'a'))
			obs = detectarObs()
			if obs <= 10:
				ser.write(bytes(b'c'))
				for r in rectanglesi:
					if r.id == 0: continue
					print("POSICIONES DE RECTANGULO IZQUIERDA:\n",r)
					r.draw()
			print(obs)
			posXc2 -= 2
			posXc -= 2

		if tkla[K_d]:
			ser.write(bytes(b'd'))

		if tkla[K_RIGHT]:
			ser.write(bytes(b'a'))
			obs = detectarObs()
			if obs <= 10:
				ser.write(bytes(b'c'))
				for r in rectangles:
					if r.id == 0: continue
					print("POSICIONES DE RECTANGULO DERECHA:\n",r)
					r.draw()
			print(obs)
			posXc += 2
			posXc2 += 2

	
		if tkla[K_DOWN]:
			ser.write(bytes (b'e'))
			obs = detectarObs()
			if obs <= 10:
				ser.write(bytes(b'c'))
				for r in rectangles2:
					if r.id == 0: continue
					print("POSICIONES DE RECTANGULO ABAJO:\n",r)
					r.draw()
			print(obs)
			posYc2 += 2
			posYc += 2

	
		if tkla[K_UP]:
			ser.write(bytes(b'a'))
			obs = detectarObs()
			if obs <= 10:
				ser.write(bytes(b'c'))
				for r in rectangles2i:
					if r.id == 0: continue
					print("POSICIONES DE RECTANGULO ARRIBA:\n",r)
					r.draw()
			print(obs)
			posYc -= 2
			posYc2 -= 2

	
		if tkla[K_s]:
			ser.write(bytes(b'c'))
	
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
	
		pygame.display.update()
		clock.tick(60)

main()
