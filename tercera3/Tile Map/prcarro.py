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

up = False
down = True
izquierda = False
derecha = False


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
        return derecha

    elif teclado[K_a] or teclado[K_LEFT]:
        derecha = False
        izquierda = True
        up = False
        down = False 
        return izquierda

    elif teclado[K_w] or teclado[K_UP]:
        derecha = False
        izquierda = False
        up = True
        down = False
        return up
       
    elif teclado[K_s] or teclado[K_DOWN]:
        derecha = False
        izquierda = False
        up = False
        down = True
        return down
        
   


def main():
    pygame.init()
    W,H = 1000,600
    HW,HH = W/2,H/2
    AREA = W * H 
    x,y = 0,0
    
    ventana = pygame.display.set_mode((W,H))
    pygame.display.set_caption("Hola mundo!!")
    FPS = 500
    clock = pygame.time.Clock()
    
    def imagen(s):
        x_imagen = pygame.image.load(s)
        return x_imagen
    
    #Se define el carro
    CarroDerecha = imagen("imagenes_carros/carro_planoDerecha.png").convert_alpha()
    Carro_r_Derecha = pygame.transform.scale(CarroDerecha,(150,75))
    
    CarroIzquierda = imagen("imagenes_carros/carro_planoIzquierda.png").convert_alpha()
    Carro_r_Izquierda = pygame.transform.scale(CarroIzquierda,(150,75))
    
    CarroArriba = imagen("imagenes_carros/carro_planoUp.png").convert_alpha()
    Carro_r_Arriba = pygame.transform.scale(CarroArriba,(75,150))
    
    CarroAbajo = imagen("imagenes_carros/carro_planoDown.png").convert_alpha()
    Carro_r_Abajo = pygame.transform.scale(CarroAbajo,(75,150))
    
    fondo = imagen("fondo2.png").convert_alpha()
    fRs = pygame.transform.scale(fondo,(2000,1200))
    
    r_Carro = Carro_r_Derecha.get_rect()
    c_x_r_Carro = r_Carro.centerx
    c_y_r_Carro = r_Carro.centery
    posXc = HW-c_x_r_Carro
    posYc = HH-c_y_r_Carro
    
    r_Carro2 = Carro_r_Arriba.get_rect()
    c_x_r_Carro2 = r_Carro2.centerx
    c_y_r_Carro2 = r_Carro2.centery
    posXc2 = HW-c_x_r_Carro2
    posYc2 = HH-c_y_r_Carro2
    
    v_X_Carro = 0
    v_Y_Carro = 0
    
    
    #Se define el fondo
    bg = imagen("blank_back.gif").convert_alpha()
    bgWidth,bgHeight = bg.get_rect().size
    
    stageWidth = bgWidth * 2
    stagePosX = -1024
    stagePosY = -1024
    
    
    
    startScrollingPosX = HW
    
    while True:
      
        teclado()
        tkla = pygame.key.get_pressed()
        
        real_x = x % fRs.get_rect().width
        real_y = y % fRs.get_rect().height
        
        ventana.fill((255,255,255))       
        ventana.blit(fRs, (real_x - ventana.get_rect().width, real_y - y % fRs.get_rect().height))
        
        
        if derecha == True:
            ventana.blit(Carro_r_Derecha,[posXc,posYc])
            
            
        elif izquierda == True:
            ventana.blit(Carro_r_Izquierda,[posXc,posYc])
            
            
        elif up == True:
            ventana.blit(Carro_r_Arriba,[posXc2,posYc2])
            
            
        elif down == True:
            ventana.blit(Carro_r_Abajo,[posXc2,posYc2])
            
            
        
        if x < W:
            ventana.blit(fRs, (real_x,0))
        if tkla[K_RIGHT]:
            x -= 10
           
        if x > W:
            ventana.blit(fRs, (real_x,0))
        if tkla[K_LEFT]:
            x += 10
            
        if y > H:
            ventana.blit(fRs, (0,real_y))
        if tkla[K_UP]: 
            y += 10
            
        if y < H:
            ventana.blit(fRs, (0,real_y))
        elif tkla[K_DOWN]:
            y -= 10
        
        
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
                
                
                
                
                    
        pygame.display.update()
        clock.tick(120)
        


        
main()
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    