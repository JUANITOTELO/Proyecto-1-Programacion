#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
import sys
import time
from random import randint
from pygame.locals import *

x = 10
y = 10

def dibujarLineas(v,c,i,f,a,lista):
    pygame.draw.line(v,c,i,f,a)

def main():
    global x
    global y
    pygame.init()
    ventana = pygame.display.set_mode((700,600))
    pygame.display.set_caption("BatCar!!")
    FPS = 500
    clock = pygame.time.Clock()
    pInicio = [x,y]
    c = 10
    c2 = 0
    x = 10
    y = 10
    xf = 10
    yf = 10
    l = [pInicio,(xf,yf)]

    while True:
        ventana.fill((255,255,255))
        random_color = (randint(100,255), randint(0,199), randint(0,200))
        tkla = pygame.key.get_pressed() 
        
        oldxf = xf
        oldyf = yf
        
        if tkla[K_LEFT]:
            xf -= 2
            l.append((xf,yf))
            print(l)
            print(l[c2])
            c2 += 1

            
        if tkla[K_RIGHT]: 
            xf += 2
            l.append((xf,yf))
            print(l)
            print(l[c2])
            c2 += 1

            
        if tkla[K_DOWN]:
            yf += 2 
            l.append((xf,yf))
            print(l)
            print(l[c2])
            c2 += 1
            
        if tkla[K_UP]:
            yf -= 2
            l.append((xf,yf))
            print(l)
            print(l[c2])
            c2 += 1

        
        dibujarLineas(ventana,random_color,l[c2],l[c2+1],7,l)
        
        
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
		
        pygame.display.update()
        clock.tick(60)


main()

