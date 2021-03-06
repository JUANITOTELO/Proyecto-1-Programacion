#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 13:07:02 2019

@author: lovelace
"""

import sys
import serial
import pygame
from pygame.locals import *
 
ser = serial.Serial('/dev/ttyACM0', 9600)
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Robot!')
pygame.mouse.set_visible(1)
 
estado = '-'
while estado != 'stop':
    
    tkla = pygame.key.get_pressed() 
    if tkla[K_UP]:
        ser.write(bytes(b'a'))
    elif tkla[K_LEFT]:
        ser.write(bytes(b'b'))
    elif tkla[K_RIGHT]:
        ser.write(bytes(b'd'))
    elif tkla[K_DOWN]:
        ser.write(bytes (b'e'))
    elif tkla[K_s]:
        ser.write(bytes(b'c'))    
    
        
    for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
                estado = 'stop'