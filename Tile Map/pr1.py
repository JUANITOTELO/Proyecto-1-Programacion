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
posX3 = 300
posY3 = 350
vel = 3
vel1 = 0.5

def imagen(s):
    n_imagen = pygame.image.load(s)
    return n_imagen

Mi_imagen = imagen("imagenes/arbol.png")
M_abajo = imagen("sprite_prueba.png")
M_arriba = imagen("sprite_prueba2.png")
M_izquierda = imagen("sprite_prueba3i.png")
M_derecha = imagen("sprite_prueba4d.png")
rectangulo = pygame.Rect(300,250,50,100)
#Sprite de arbol
sprite_arbol = pygame.sprite.Sprite()
sprite_arbol.image = Mi_imagen
sprite_arbol.rect = Mi_imagen.get_rect()
sprite_arbol.rect.top = posX3
sprite_arbol.rect.left = posY3
#Sprites de mavimiento

sprite_arriba = pygame.sprite.Sprite()
sprite_arriba.image = M_arriba
sprite_arriba.rect = M_arriba.get_rect()
sprite_arriba.rect.top = posY2
sprite_arriba.rect.left = posX2

sprite_abajo = pygame.sprite.Sprite()
sprite_abajo.image = M_abajo
sprite_abajo.rect = M_abajo.get_rect()
sprite_abajo.rect.top = posY2
sprite_abajo.rect.left = posX2

sprite_izquierda = pygame.sprite.Sprite()
sprite_izquierda.image = M_izquierda
sprite_izquierda.rect = M_izquierda.get_rect()
sprite_izquierda.rect.top = posY2
sprite_izquierda.rect.left = posX2

sprite_derecha = pygame.sprite.Sprite()
sprite_derecha.image = M_derecha
sprite_derecha.rect = M_derecha.get_rect()
sprite_derecha.rect.top = posY2
sprite_derecha.rect.left = posX2

clock = pygame.time.Clock()

cont = 2
i = 0
xixf = [(0,0,90,90),(90,0,90,90),(180,0,270,90)]
up = False
down = True
izquierda = False
derecha = False

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
        sprite_derecha.rect.top += 1
        sprite_izquierda.rect.top += 1
        sprite_arriba.rect.top += 1
        sprite_abajo.rect.top += 1
        cont += 1

    elif teclado[K_a] or teclado[K_LEFT]:
        derecha = False
        izquierda = True
        up = False
        down = False
        sprite_derecha.rect.top -= 1
        sprite_izquierda.rect.top -= 1
        sprite_arriba.rect.top -= 1
        sprite_abajo.rect.top -= 1
        cont += 1

    elif teclado[K_w] or teclado[K_UP]:
        derecha = False
        izquierda = False
        up = True
        down = False
        cont += 1
        sprite_derecha.rect.left -= 1
        sprite_izquierda.rect.left -= 1
        sprite_arriba.rect.left -= 1
        sprite_abajo.rect.left -= 1

    elif teclado[K_s] or teclado[K_DOWN]:
        derecha = False
        izquierda = False
        up = False
        down = True
        cont += 1
        sprite_derecha.rect.left += 1
        sprite_izquierda.rect.left += 1
        sprite_arriba.rect.left += 1
        sprite_abajo.rect.left += 1


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

while True:
    time = clock.tick(60)
    teclado()
    sprite()
#   Generación de ventana
    ventana.fill(colorLight)
#  Generación de imagen
    ventana.blit(sprite_arbol.image,sprite_arbol.rect)
    if up == True:
        ventana.blit(sprite_arriba.image,(sprite_arriba.rect.top,sprite_arriba.rect.left),(xixf[i]))

    elif down == True:
        ventana.blit(sprite_abajo.image,(sprite_abajo.rect.top,sprite_abajo.rect.left),(xixf[i]))

    elif izquierda == True:
        ventana.blit(sprite_izquierda.image,(sprite_izquierda.rect.top,sprite_izquierda.rect.left),(xixf[i]))

    elif derecha == True:
        ventana.blit(sprite_derecha.image,(sprite_derecha.rect.top,sprite_derecha.rect.left),(xixf[i]))




#  Generación de rectangulo
#    pygame.draw.rect(ventana,color,rectangulo)

#Instrucción para salir
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()



    if derecha == True:
        if posX1 < 600:
            posX1 += vel1
            rectangulo.left = posX
        else:
            derecha = False
    else:
        if posX1 > 1:
            posX1 -= vel1
            rectangulo.left = posX
        else:
            derecha = True

    pygame.display.update()
