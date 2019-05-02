# -*- coding: utf-8 -*-
"""
Created on Wed May  1 21:00:05 2019

@author: asus
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 22:12:29 2019

@author: asus
"""
import pygame
import sys
import time
from pygame.locals import *
colorLight = (255,255,255,177)
x,y = 100,250
i = 1
e = 1
framesAbajoC = [(0,0,100,100),(100,0,100,100),(200,0,100,100),(300,0,100,100),(400,0,100,100),(500,0,100,100)]
framesDerechaC = [(0,100,100,100),(100,100,100,100),(200,100,100,100),(300,100,100,100),(400,100,100,100),(500,100,100,100)]
framesArribaC = [(0,200,100,100),(100,200,100,100),(200,200,100,100),(300,200,100,100),(400,200,100,100),(500,200,100,100)]
framesIzquierdaC = [(0,300,100,100),(100,300,100,100),(200,300,100,100),(300,300,100,100),(400,300,100,100),(500,300,100,100)]
cont = 1

def partsR():
    global cont
    p = 6
    global i

    if cont == p:
        i = 0
    elif cont == p*2:
        i = 1
    elif cont == p*3:
        i = 2
    elif cont == p*4:
        i = 3
    elif cont == p*5:
        i = 4
    elif cont == p*6:
        i = 5
        cont=0

framesAbajoE = [(0,0,100,100),(100,0,100,100),(200,0,100,100),(300,0,100,100),(400,0,100,100),(500,0,100,100),(600,0,100,100),(700,0,100,100),(800,0,100,100),(900,0,100,100)]
framesDerechaE = [(0,100,100,100),(100,100,100,100),(200,100,100,100),(300,100,100,100),(400,100,100,100),(500,100,100,100),(600,100,100,100),(700,100,100,100),(800,100,100,100),(900,100,100,100)]
framesArribaE = [(0,200,100,100),(100,200,100,100),(200,200,100,100),(300,200,100,100),(400,200,100,100),(500,200,100,100),(600,200,100,100),(700,200,100,100),(800,200,100,100),(900,200,100,100)]
framesIzquierdaE = [(0,300,100,100),(100,300,100,100),(200,300,100,100),(300,300,100,100),(400,300,100,100),(500,300,100,100),(600,300,100,100),(700,300,100,100),(800,300,100,100),(900,300,100,100)]
contE = 0
def partsE():
    global contE
    p = 10
    global e

    if contE == p:
        e = 0
    elif contE == p*2:
        e = 1
    elif contE == p*3:
        e = 2
    elif contE == p*4:
        e = 3
    elif contE == p*5:
        e = 4
    elif contE == p*6:
        e = 5
    elif contE == p*7:
        e = 6
    elif contE == p*8:
        e = 7
    elif contE == p*9:
        e = 8
    elif contE == p*10:
        e = 9
        contE = 0

       
up = False
down = True
izquierda = False
derecha = False
stand = True

        
def teclado():
    vel = 2
    teclado = pygame.key.get_pressed()
    global cont
    global contE
    global up
    global down
    global izquierda
    global derecha
    global stand
    global x
    global y
    
    
        
    if teclado[K_d] or teclado[K_RIGHT]:
        derecha = True
        izquierda = False
        up = False
        down = False
        stand = False
        x += vel
        cont += 1

    elif teclado[K_a] or teclado[K_LEFT]:
        derecha = False
        izquierda = True
        up = False
        down = False
        stand = False
        x -= vel
        cont += 1

    elif teclado[K_w] or teclado[K_UP]:
        derecha = False
        izquierda = False
        up = True
        down = False
        stand = False
        y -= vel
        cont += 1
 

    elif teclado[K_s] or teclado[K_DOWN]:
        derecha = False
        izquierda = False
        up = False
        down = True
        stand = False
        y += vel
        cont += 1
        
    elif ((teclado[K_d] or teclado[K_RIGHT]) and (teclado[K_a] or teclado[K_LEFT]) and (teclado[K_w] or teclado[K_UP]) and (teclado[K_s] or teclado[K_DONW])) == False:
        stand = True
        contE += 1
        
    
        
        
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
    stair = imagen("stairsRC.png").convert_alpha()
    stairR = pygame.transform.scale(stair,(90,90))
    TR_r = imagen("trump_run.png").convert_alpha()
    TR_s = imagen("trump_iddle.png").convert_alpha()
    TR_sR = pygame.transform.scale(TR_s,(100,100))
    
    
    r1 = pygame.Rect(100,150,50,70)
    c = 0
    
    while True:
        global up
        global x
        global y
                
        ventana.blit(fondo,(0,0))
        ventana.blit(stairR,(300,500))
        ventana.blit(stairR,(400,400))
        
        teclado()
        partsR()
        partsE()

        pygame.draw.rect(ventana,(0,0,0),r1)
        oldy = y
        oldx = x
        
        if up == True:

            ventana.blit(TR_r,[x,y],framesArribaC[i])
               
             
        elif down == True:
            
            ventana.blit(TR_r,[x,y],framesAbajoC[i])
            
            
        elif izquierda == True:

            ventana.blit(TR_r,[x,y],framesIzquierdaC[i])
            
        
        elif derecha == True:
            
            ventana.blit(TR_r,[x,y],framesDerechaC[i])
            
            
        elif (stand == True and up == False):

            ventana.blit(TR_sR,[x,y],framesArribaE[i])
               
             
        elif (stand == True and down == False):
            
            ventana.blit(TR_sR,[x,y],framesAbajoE[i])
            
            
        elif (stand == True and izquierda == False):

            ventana.blit(TR_sR,[x,y],framesIzquierdaE[i])
            
        
        elif (stand == True and derecha == False):
            
            ventana.blit(TR_sR,[x,y],framesDerechaE[i])
            
    
        for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()
        
    
    
        pygame.display.update()
        clock.tick(120)
        
main()