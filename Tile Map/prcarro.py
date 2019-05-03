#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:30:44 2019

@author: lovelace
"""

import pygame
import sys
import time
from pygame.locals import *

x,y = 100,250
up = False
down = True
izquierda = False
derecha = False
cont = 1

def teclado():
    vel = 2
    teclado = pygame.key.get_pressed()
    global cont
    global up
    global down
    global izquierda
    global derecha
    global x
    global y
    if teclado[K_d] or teclado[K_RIGHT]:
        derecha = True
        izquierda = False
        up = False
        down = False
        x += vel

    elif teclado[K_a] or teclado[K_LEFT]:
        derecha = False
        izquierda = True
        up = False
        down = False
        x -= vel
        

    elif teclado[K_w] or teclado[K_UP]:
        derecha = False
        izquierda = False
        up = True
        down = False
        y -= vel
       
 

    elif teclado[K_s] or teclado[K_DOWN]:
        derecha = False
        izquierda = False
        up = False
        down = True
        y += vel
    
    

    return

def main():
    pygame.init()
    W,H = 700,600
    HW,HH = W/2,H/2
    AREA = W * H 
    
    ventana = pygame.display.set_mode((W,H))
    pygame.display.set_caption("Hola mundo!!")
    clock = pygame.time.Clock()
    
    def imagen(s):
        x_imagen = pygame.image.load(s)
        return x_imagen
    Carro = imagen("carro_plano.png").convert_alpha()
    
    while True:
        global up
        global x
        global y
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
                
                
                
                
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    