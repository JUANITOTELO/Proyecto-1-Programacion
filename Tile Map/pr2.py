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
        
    def draw(self,target_surface):
        patch_rect = (self.curr_patch_num*34.6, 0, 34.6,self.image.get_height())
        target_surface.blit(self.image,self.posn,patch_rect)
        
    def contains_point(self, pt):
        
        (my_x, my_y) = self.posn
        my_width = self.image.get_width() / 3
        my_height = self.image.get_height()
        [x, y] = pt
        return (x >= my_x and x < my_x + my_width and y >= my_y and y < my_y + my_height)


def colision(r1,r2,coor_r1,coor_r2):
    
    #Se definen los puntos del rectangulo 1(r1)
    [r1x,r1y] = coor_r1 
    r1W = r1.get_width()/3
    r1H = r1.get_height()
    Pr1 = {'A':[0,0],'B':[r1W + coor_r2[0],0],'C':[0,r1H + coor_r2[1]],'D':[r1W + coor_r2[0],r1H + coor_r2[1]]}
    
    #Se definen los puntos del rectangulo 2(r2)
    [r2x,r2y] = coor_r2
    r2W = r2.get_width()
    r2H = r2.get_height()
    Pr2 = {'A':[0,0],'B':[r2W + coor_r2[0],0],'C':[0,r2H + coor_r2[1]],'D':[r2W + coor_r2[0],r2H + coor_r2[1]]}
    
    
    if ((Pr1['B'][0] >= Pr2['A'][0]) and (Pr1['B'][0] <= Pr2['B'][0])) and ((Pr1['B'][1] >= Pr2['A'][1]) and (Pr1['B'][1] <= Pr2['C'][1])):
        print("Colisiono.")
        
    elif ((Pr1['A'][0] <= Pr2['B'][0]) and (Pr1['A'][0] >= Pr2['A'][0])) and ((Pr1['A'][1] >= Pr2['A'][1]) and (Pr1['A'][1] <= Pr2['D'][1])):
        print("Colisiono.")
    
    
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
    W,H = 700,600
    HW,HH = W/2,H/2
    AREA = W * H 
    pygame.init()
    ventana = pygame.display.set_mode((W,H))
    pygame.display.set_caption("Hola mundo!!")
    clock = pygame.time.Clock()
    def imagen(s):
        x_imagen = pygame.image.load(s)
        return x_imagen
    fondo = imagen("fondo2.png").convert_alpha()
    arbol = imagen("imagenes/arbol.png").convert_alpha()
    
    M_abajo = imagen("sprite_prueba.png").convert_alpha()
    M_abajoR = M_abajo.get_rect()
    
    M_arriba = imagen("sprite_prueba2.png").convert_alpha()
    M_arribaR = M_abajo.get_rect()
    
    M_izquierda = imagen("sprite_prueba3i.png").convert_alpha()
    M_izquierdaR = M_abajo.get_rect()
    
    M_derecha = imagen("sprite_prueba4d.png").convert_alpha()
    M_derechaR = M_abajo.get_rect()
    
    stairs = imagen("stairsRC.png").convert_alpha()
    stairs_mask = pygame.mask.from_surface(stairs)
    stairs_rect = stairs.get_rect()
    ox = HW - stairs_rect.center[0]
    oy = HH - stairs_rect.center[1]
    
    r1 = pygame.Rect(100,150,50,70)
    c = 0
    
    while True:
        global up
        global x
        global y
        
        
        persRa = Personaje(M_abajo,[x,y])
        persRarriba = Personaje(M_arriba,[x,y])
        persRizquier = Personaje(M_izquierda,[x,y])
        persRdere = Personaje(M_derecha,[x,y])
        ventana.blit(fondo,(0,0))
        teclado()

        pygame.draw.rect(ventana,(0,0,0),r1)
        oldy = y
        oldx = x
        colision(arbol, M_arriba, [100,150], [x,y])
        colision(arbol, M_abajo, [100,150], [x,y])
        colision(arbol, M_izquierda, [100,150], [x,y])
        colision(arbol, M_derecha, [100,150], [x,y])
        if up == True:

            persRarriba.draw(ventana)
               
             
        elif down == True:
            
            persRa.draw(ventana)
            
            
        elif izquierda == True:

            persRizquier.draw(ventana)
            
        
        elif derecha == True:
            
            persRdere.draw(ventana)
            
        
        if persRa.contains_point([100,150]):
            print("colisiono: {0}".format(c))
            up = False
            y = oldy
            c += 1
    
        for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()
        
    
    
        pygame.display.update()
        clock.tick(120)
        
main()
    
    
    
    
    
