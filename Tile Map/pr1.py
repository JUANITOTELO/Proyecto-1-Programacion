# -*- coding: utf-8 -*-
import pygame
import sys
import time
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((700,600))
pygame.display.set_caption("Hola mundo!!")

color = (255,24,72)
Color = (255,48,108)
colorDark = (0,0,0)
colorLight = (255,255,255)

posX = 0
posY = 300
posX1 = 0
posY1 = 200
posX2 = 200
posY2 = 0
vel = 3
vel1 = 0.5

cont = 2
i = 0
xixf = [(0,0,90,90),(90,0,90,90),(180,0,270,90)]
up = False
down = True
izquierda = False
derecha = False
def imagen(s):
    n_imagen = pygame.image.load(s)
    return n_imagen

def teclado():
    teclado = pygame.key.get_pressed()
    global cont
    global up
    global down
    global izquierda
    global derecha
    global posX
    global posY
    global posX2
    global posY2
    if teclado[K_d] or teclado[K_RIGHT]:
        derecha = True
        izquierda = False
        up = False
        down = False
        posX += 1
        posX2 += 1
        cont += 1

    elif teclado[K_a] or teclado[K_LEFT]:
        derecha = False
        izquierda = True
        up = False
        down = False
        posX -= 1
        posX2 -= 1
        cont += 1

    elif teclado[K_w] or teclado[K_UP]:
        derecha = False
        izquierda = False
        up = True
        down = False
        cont += 1
        posY -= 1
        posY2 -= 1

    elif teclado[K_s] or teclado[K_DOWN]:
        derecha = False
        izquierda = False
        up = False
        down = True
        cont += 1
        posY += 1
        posY2 += 1


    return


def sprite():
    global cont
    p = 3
    global i

    if cont == p:
        i = 0
    elif cont == p*2:
        i = 1
    elif cont == p*3:
        i = 2
        cont=0

    return

Mi_imagen = imagen("prP1.png")
Mi_imagen2 = imagen("pruebaPixeles1!.png")
sprite_abajo = imagen("sprite_prueba.png")
sprite_arriba = imagen("sprite_prueba2.png")
sprite_izquierda = imagen("sprite_prueba3i.png")
sprite_derecha = imagen("sprite_prueba4d.png")
rectangulo = pygame.Rect(300,250,50,100)

clock = pygame.time.Clock()

while True:
    time = clock.tick(60)
    teclado()
    sprite()
#   Generación de ventana
    ventana.fill(colorLight)
#  Generación de imagen
#    ventana.blit(Mi_imagen,(posX,posY))
    ventana.blit(Mi_imagen2,(posX1,posY1))
    if up == True:
        ventana.blit(sprite_arriba,(posX2,posY2),(xixf[i]))
    elif down == True:
        ventana.blit(sprite_abajo,(posX2,posY2),(xixf[i]))
    elif izquierda == True:
        ventana.blit(sprite_izquierda,(posX2,posY2),(xixf[i]))
    elif derecha == True:
        ventana.blit(sprite_derecha,(posX2,posY2),(xixf[i]))


#  Generación de rectangulo
    pygame.draw.rect(ventana,color,rectangulo)

#Instrucción para salir
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()



    if derecha == True:
        if posX1 < 600:
            posX1 += vel1
            rectangulo.left = posX1
        else:
            derecha = False
    else:
        if posX1 > 1:
            posX1 -= vel1
            rectangulo.left = posX1
        else:
            derecha = True

    pygame.display.update()
