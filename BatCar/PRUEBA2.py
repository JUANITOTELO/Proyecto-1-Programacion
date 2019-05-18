#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 14:43:35 2019

@author: lovelace
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
import serial
import sys
import time
from random import randint
from pygame.locals import *

up = False
down = False
izquierda = False
derecha = False



def dibujarLineas(v,c,i,f,a,lista):
    pygame.draw.line(v,c,i,f,a)
    
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
WHITE = (255, 255, 255, 255)
random_color = (randint(100,255), randint(0,199), randint(0,200))
class rectangle:
	def __init__(self, x, y, w, h, id):
		global random_color
		
		self.x1 = x
		self.y1 = y
		self.x2 = x + w
		self.y2 = y + h
		
		self.w = w
		self.h = h
		
		self.fillColor = random_color

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
		pygame.draw.rect(surface, self.fillColor, self.rect(), 0)
		

def main():
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
        rectangles = list([rectangle(random.randint(0, W), random.randint(0, H), random.randint(8, 8), random.randint(8, 8), i) for i in range(0, 20)])
        teclado()
        tkla = pygame.key.get_pressed() 
        ventana.fill((255,255,255))
        random_color = (randint(100,255), randint(0,199), randint(0,200))
        ventana.blit(fRs,[0,0])
        
        for r in rectangles:
            if r.id == 0: continue
            r.draw()
            
        
            
        if izquierda == True:
            ventana.blit(Carro_r_Izquierda,[posXc,posYc])
        if tkla[K_LEFT]:
            posXc2 -= 2
            posXc -= 2
            
        if derecha == True:
            ventana.blit(Carro,[posXc,posYc])
        if tkla[K_RIGHT] or tkla[K_d]:
            posXc += 2
            posXc2 += 2

        if down == True:
            ventana.blit(Carro_r_Abajo,[posXc2,posYc2])
        if tkla[K_DOWN]:
            posYc2 += 2
            posYc += 2
                        
        if up == True:
            ventana.blit(Carro_r_Arriba,[posXc2,posYc2])
        if tkla[K_UP]:
            posYc -= 2
            posYc2 -= 2
        
        
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
		
        pygame.display.update()
        clock.tick(60)


main()

