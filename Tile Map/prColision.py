import pygame
import sys
import time
from pygame.locals import *
from random import randint
posX = 150
posY = 250
posX2 = 10
posY2 = 250
vel = 2
cont = 1
derecha = True
izquierda = False
up = False
down = False
colorLight = (255,255,255)
nr = randint(20,255)
nr1 = randint(10,255)
nr2 = randint(30,255)
colorR = (nr,nr1,nr2)
def imagen(s):
    n_imagen = pygame.image.load(s)
    return n_imagen

def teclado():
    teclado = pygame.key.get_pressed()
    global cont
    global vel
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
        posX2 += vel
        cont += 1

    elif teclado[K_a] or teclado[K_LEFT]:
        derecha = False
        izquierda = True
        up = False
        down = False
        posX -= 1
        posX2 -= vel
        cont += 1

    elif teclado[K_w] or teclado[K_UP]:
        derecha = False
        izquierda = False
        up = True
        down = False
        cont += 1
        posY -= 1
        posY2 -= vel

    elif teclado[K_s] or teclado[K_DOWN]:
        derecha = False
        izquierda = False
        up = False
        down = True
        cont += 1
        posY += 1
        posY2 += vel


    return


arbol = imagen("imagenes/arbol.png")
sprite_arbol = pygame.sprite.Sprite()
sprite_arbol.image = arbol
sprite_arbol.rect = arbol.get_rect()
sprite_arbol.rect.top = posY
sprite_arbol.rect.left = posX
rectangulo = pygame.Rect(posX2,posY2,50,100)



def main():
    pygame.init()
    #Generación de ventana
    ventana = pygame.display.set_mode((700,600))
    pygame.display.set_caption("Hola mundo!!")
    clock = pygame.time.Clock()




    while True:
        #Salir del juego
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
        #Teclas
        teclado()
        #Fondo
        ventana.fill(colorLight)
        #Objetos
        ventana.blit(sprite_arbol.image,sprite_arbol.rect)
        pygame.draw.rect(ventana,colorR,rectangulo)
        time = clock.tick(65)
        oldPosX = rectangulo.right

        if derecha == True:
            rectangulo.right = posX2

        if izquierda == True:
            rectangulo.right = posX2

        if rectangulo.colliderect(sprite_arbol.rect):
            rectangulo.right = oldPosX
            print(oldPosX)




        #fondo = pygame.image.load("mapa1.png").convert_alpha()
        #ventana.blit(fondo,(0,0))

        pygame.display.update()
#Ejecución
main()
