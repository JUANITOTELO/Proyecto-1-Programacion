# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 22:12:29 2019

@author: asus
"""
import pygame
import sys
import time
from pygame.locals import *
colorLight = (255,255,255)
x,y = 100,250

class Personaje:
    def __init__(self,img,target_posn):
        self.image = img
        self.posn = target_posn
        self.anim_frame_count = 0
        self.curr_patch_num = 0
        
    def update(self):
        if self.anim_frame_count > 0:
            self.anim_frame_count = (self.anim_frame_count+1) % 60
        self.curr_patch_num = self.anim_frame_count // 6
        
    def draw(self,target_surface):
        patch_rect = (self.curr_patch_num*90, 0, 90,self.image.get_height())
        target_surface.blit(self.image,self.posn,patch_rect)
        
    def contains_point(self, pt):
        
        (my_x, my_y) = self.posn
        my_width = self.image.get_width() / 3
        my_height = self.image.get_height()
        [x, y] = pt
        return (x >= my_x and x < my_x + my_width and y >= my_y and y < my_y + my_height)
    
up = False
down = True
izquierda = False
derecha = False
cont = 1
    
def teclado():
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
        x += 1

    elif teclado[K_a] or teclado[K_LEFT]:
        derecha = False
        izquierda = True
        up = False
        down = False
        x -= 1
        

    elif teclado[K_w] or teclado[K_UP]:
        derecha = False
        izquierda = False
        up = True
        down = False
        y -= 1 
       
 

    elif teclado[K_s] or teclado[K_DOWN]:
        derecha = False
        izquierda = False
        up = False
        down = True
        y += 1
    
    

    return


    
    
def main():
    pygame.init()
    ventana = pygame.display.set_mode((700,600))
    pygame.display.set_caption("Hola mundo!!")
    pygame.time.Clock()
    def imagen(s):
        x_imagen = pygame.image.load(s)
        return x_imagen
    
    M_abajo = imagen("sprite_prueba.png")
    M_arriba = imagen("sprite_prueba2.png")
    M_izquierda = imagen("sprite_prueba3i.png")
    M_derecha = imagen("sprite_prueba4d.png")
    r1 = pygame.Rect(100,150,50,70)
    
    while True:
        global up
        global x
        global y
        persRa = Personaje(M_abajo,[x,y])
        persRarriba = Personaje(M_arriba,[x,y])
        persRizquier = Personaje(M_izquierda,[x,y])
        persRdere = Personaje(M_derecha,[x,y])
        
        teclado()
        
        ventana.fill(colorLight)
        pygame.draw.rect(ventana,(0,0,0),r1)
        oldy = y
        oldx = x
        if up == True:
            persRarriba.update()
            persRarriba.draw(ventana)
               
             
        elif down == True:
            persRa.update()
            persRa.draw(ventana)
            
            
        elif izquierda == True:
            persRizquier.update()
            persRizquier.draw(ventana)
            
        
        elif derecha == True:
            persRdere.update()
            persRdere.draw(ventana)
            
        
        if persRa.contains_point([100,150]):
            print("colisiono")
            up = False
            y = oldy
    
        for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()
        
    
    
        pygame.display.update()

main()
    
    
    
    
    
