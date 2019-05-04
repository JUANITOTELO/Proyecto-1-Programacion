import pygame
import sys
import time
from pygame.locals import *
from random import randint
posX = 150
posY = 250
posX2 = 10
posY2 = 250
alto2 = 100
ancho2 = 50
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
black = (0,0,0)

def puntosRectangulo(x,y,w,h):
    
    p1 = [x,y]
    pH1 = [x,y+(h/2)]
    p2 = [x+(w/2),y]
    pH2 = [x+(w/2),(h/2)+y]
    pTotales = [p1,pH1,p2,pH2]
    
    return pTotales  


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



def main():
    arbol = imagen("imagenes/arbol.png")
    sprite_arbol = pygame.sprite.Sprite()
    sprite_arbol.image = arbol
    sprite_arbol.rect = arbol.get_rect()
    sprite_arbol.rect.top = posX
    sprite_arbol.rect.left = posY
    rectangulo = pygame.Rect(posX2,posY2,ancho2,alto2)
    pygame.init()
    #Generación de ventana
    ventana = pygame.display.set_mode((700,600))
    pygame.display.set_caption("Hola mundo!!")
    clock = pygame.time.Clock()


    

    while True:
        colorR = (nr,nr1,nr2)
        #Salir del juego
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
        #Teclas
        teclado()
        #Fondo
        ventana.fill(black)
        #Objetos
        ventana.blit(sprite_arbol.image,sprite_arbol.rect)
        pygame.draw.rect(ventana,colorR,rectangulo)
        time = clock.tick(65)
        
    
            
        if derecha == True:
            rectangulo.right = posX2

        elif izquierda == True:
            rectangulo.right = posX2

        puntos_del_rectangulo = puntosRectangulo(posX2,posY2,ancho2,alto2)
        puntos_del_arbol = puntosRectangulo(posX,posY,102,187) 

        if (puntos_del_rectangulo[3][0]) >= (puntos_del_arbol[1][0]) and puntos_del_rectangulo[3][0] == 277:   
            print("Colisiono.\nRetangulo {0}\nArbol {1}".format(puntos_del_rectangulo[3][0],puntos_del_arbol[1][0]))
            
        



        

        pygame.display.update()
#Ejecución
main()
