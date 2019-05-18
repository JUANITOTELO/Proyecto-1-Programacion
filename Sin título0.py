# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:28:50 2019

@author: GIANCARLO GONZALEZ
"""
import sys
import serial
import pygame
from pygame.locals import *
 
ser = serial.Serial('COM3', 9600)
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Robot!')
pygame.mouse.set_visible(1)
 
estado = '-'
 
while estado != 'stop':
    
    tkla = pygame.key.get_pressed() 
    if tkla[K_UP]:
        ser.write(char('a')+bytes([13, 10]))
    elif tkla[K_LEFT]:
        ser.write(char('b'))
    elif tkla[K_RIGHT]:
        ser.write(estado.encode ('d')+ bytes([13, 10]))
    elif tkla[K_DOWN]:
        ser.write(estado.encode ('e')+ bytes([13, 10]))
    
        
    for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
                estado = 'stop'
		                