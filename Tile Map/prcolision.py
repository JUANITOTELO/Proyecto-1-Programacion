import pygame
import sys
import time
from pygame.locals import *
from random import randint
posX = 10
posY = 250
vel = 1
derecha = True
izquierda = False
up = False
down = False
def colision(r1,r2):
    #Se definen los puntos del rectangulo 1(r1)
    coor_r1 = [r1[0],r1[1]]
    r1W = r1[2]
    r1H = r1[3]
    Pr1 = {'A':coor_r1,'B':[r1W + coor_r1[0],coor_r1[1]],'C':[coor_r1[0],r1H + coor_r1[1]],'D':[r1W + coor_r1[0],r1H + coor_r1[1]]}

    #Se definen los puntos del rectangulo 2(r2)
    coor_r2 = [r2[0],r2[1]]
    r2W = r2[2]
    r2H = r2[3]
    Pr2 = {'A':coor_r2,'B':[r2W + coor_r2[0],coor_r2[1]],'C':[coor_r2[0],r2H + coor_r2[1]],'D':[r2W + coor_r2[0],r2H + coor_r2[1]]}
                                    #1                                                                  #3
    if ((Pr1['B'][0] >= Pr2['A'][0]) and (Pr1['B'][0] <= Pr2['B'][0])) and ((Pr1['B'][1] >= Pr2['A'][1]) and (Pr1['B'][1] <= Pr2['C'][1])):
        print("Colisionó.\n{0}".format(coor_r1))

    elif ((Pr1['B'][0] >= Pr2['A'][0]) and (Pr1['B'][0] <= Pr2['B'][0])) and ((Pr1['D'][0] >= Pr2['C'][0]) and (Pr1['D'][0] <= Pr2['D'][0])):
        print("Colisionó.")

    elif ((Pr1['D'][0] >= Pr2['C'][0]) and (Pr1['D'][0] <= Pr2['D'][0])) and ((Pr1['B'][1] >= Pr2['A'][1]) and (Pr1['B'][1] <= Pr2['C'][1])):
        print("Colisionó.")

    elif ((Pr1['B'][0] >= Pr2['A'][0]) and (Pr1['B'][0] <= Pr2['B'][0])) and ((Pr1['D'][1] >= Pr2['A'][1]) and (Pr1['D'][1] <= Pr2['C'][1])):
        print("Colisionó.")

    elif ((Pr1['D'][0] >= Pr2['C'][0]) and (Pr1['D'][0] <= Pr2['D'][0])) and ((Pr1['D'][1] >= Pr2['A'][1]) and (Pr1['D'][1] <= Pr2['C'][1])):
        print("Colisionó.")

    elif ((Pr1['B'][1] >= Pr2['A'][1]) and (Pr1['B'][1] <= Pr2['C'][1])) and ((Pr1['D'][1] >= Pr2['A'][1]) and (Pr1['D'][1] <= Pr2['C'][1])):
        print("Colisionó.")

    #elif ((Pr1['B'][0] >= Pr2['A'][0]) and (Pr1['B'][0] <= Pr2['B'][0])):
    #    print("Colisionó.")

#    elif ((Pr1['D'][0] >= Pr2['C'][0]) and (Pr1['D'][0] <= Pr2['D'][0])):
#        print("Colisionó.")

#    elif ((Pr1['B'][1] >= Pr2['A'][1]) and (Pr1['B'][1] <= Pr2['C'][1])):
#        print("Colisionó.")

#    elif ((Pr1['D'][1] >= Pr2['A'][1]) and (Pr1['D'][1] <= Pr2['C'][1])):
#        print("Colisionó.")
    else:
        print("No colisionó.")

def teclado():
    teclado = pygame.key.get_pressed()
    global vel
    global up
    global down
    global izquierda
    global derecha
    global posX
    global posY

    if teclado[K_d] or teclado[K_RIGHT]:
        derecha = True
        izquierda = False
        up = False
        down = False
        posX += vel

    elif teclado[K_a] or teclado[K_LEFT]:
        derecha = False
        izquierda = True
        up = False
        down = False
        posX -= vel



    elif teclado[K_w] or teclado[K_UP]:
        derecha = False
        izquierda = False
        up = True
        down = False
        posY -= vel


    elif teclado[K_s] or teclado[K_DOWN]:
        derecha = False
        izquierda = False
        up = False
        down = True
        posY += vel

    return




def main():
    """Preparar el juego y correr el ciclo principal"""
    pygame.init() #preparar el módulo de juego
    surf_sz = 480 #Tamaño de la superficie
    #Crear la superficie y ventana que la contiene
    main_surf = pygame.display.set_mode((surf_sz, surf_sz))
    clock = pygame.time.Clock()
    #Definir las propiedades de un rectángulo

    x2 = 240#int(input("x2: "))
    y2 = 240#int(input("y2: "))

    small_rect = pygame.Rect(posX,posY,90,90)
    some_color = (255,0,0) #Rojo, Verde y Azul

    another_small_rect = pygame.Rect(x2,y2,90,100)
    another_color = (0,255,0) #Rojo, Verde y Azul


    while True:
        ev = pygame.event.poll() #Busque cualquier evento
        if ev.type == pygame.QUIT: #Presionó botón cerrar?
            break
        #Salga del ciclo
        #Actualice objetos y estructuras del juego aquí...
        #En cada frame dibujamos todo de nuevo.
        #Primero llenamos con el color de fondo
        main_surf.fill((0,200,255))
        #Pinte un rectángulo sobre la superficie principal
        main_surf.fill(some_color, small_rect)
        main_surf.fill(another_color, another_small_rect)
        time = clock.tick(65)
        teclado()
        #prueba colisión
        colision(small_rect, another_small_rect)

        if derecha == True:
            small_rect.right = posX

        elif izquierda == True:
            small_rect.right = posX

        elif up == True:
            small_rect.top = posY

        elif down == True:
            small_rect.top = posY

        #Muestre la escena
        pygame.display.flip()
    pygame.quit() #Cierre la ventana

#Ejecución...
main()
