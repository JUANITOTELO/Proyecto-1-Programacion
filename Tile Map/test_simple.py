import pygame


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
    
    if ((Pr1['B'][0] >= Pr2['A'][0]) and (Pr1['B'][0] <= Pr2['B'][0])) and ((Pr1['B'][1] >= Pr2['A'][1]) and (Pr1['B'][1] <= Pr2['C'][1])):
        print("Colisiono.{0}".format(x))
        
    elif ((Pr1['A'][0] <= Pr2['B'][0]) and (Pr1['A'][0] >= Pr2['A'][0])) and ((Pr1['A'][1] >= Pr2['A'][1]) and (Pr1['A'][1] <= Pr2['D'][1])):
        print("Colisiono.")

    else:
        print("No colicionó.")



def main():
    """Preparar el juego y correr el ciclo principal"""
    pygame.init() #preparar el módulo de juego
    surf_sz = 480 #Tamaño de la superficie
    #Crear la superficie y ventana que la contiene
    main_surf = pygame.display.set_mode((surf_sz, surf_sz))

    #Definir las propiedades de un rectángulo
    x1 = 200#int(input("x1: "))
    y1 = 120#int(input("y1: "))
    x2 = 300#int(input("x2: "))
    y2 = 200#int(input("y2: "))
    
    small_rect = (x1,y1,150,90)
    some_color = (255,0,0) #Rojo, Verde y Azul
    
    another_small_rect = (x2,y2,90,100)
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


        #prueba colisión
        colision(small_rect, another_small_rect)
        
        
        #Muestre la escena
        pygame.display.flip()
    pygame.quit() #Cierre la ventana

#Ejecución...
main()
