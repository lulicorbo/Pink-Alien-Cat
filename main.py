import pygame
import data
from clase_administrador import Administrador
from pantalla_inicio import mostrar_pantalla_inicio
from pantalla_nombre import mostar_pantalla_ingresar_nombre
from pantalla_niveles import mostar_pantalla_entre_niveles
from clase_jugador import Jugador
from niveles import ejecutar_nivel
from funciones_bd import crear_base_de_datos_score
from funciones import check_nivel
from pantalla_game_over import mostar_pantalla_perdio
from pantalla_gano import mostar_pantalla_gano


pygame.init()

#Se crea base de datos si no existe
crear_base_de_datos_score()

#Set up
PANTALLA = pygame.display.set_mode((data.ANCHO_VENTANA, data.LARGO_VENTANA))

pygame.display.set_caption("Pink Alien Cat") 
icono = pygame.image.load("imagenes\jugador.png")
icono = pygame.transform.scale(icono, (10, 10))
pygame.display.set_icon(icono)

flag_jugar = True
def jugar():

    #Se crea administrador (maneja tiempo, score, niveles y sonido)y jugador principal
    administrador = Administrador(5)
    jugador_principal = Jugador()

    #Pantalla de inicio
    mostrar_pantalla_inicio(PANTALLA, administrador)


    #Pantalla ingreso nombre
    nombre = mostar_pantalla_ingresar_nombre(PANTALLA, administrador)
    jugador_principal.nombre = nombre


    #Se ejecutan los diferentes niveles y pantalla previa
    mostar_pantalla_entre_niveles(administrador, PANTALLA)
    ejecutar_nivel(PANTALLA, jugador_principal, administrador)
    if administrador.nivel == 2:
        mostar_pantalla_entre_niveles(administrador, PANTALLA)
        ejecutar_nivel(PANTALLA, jugador_principal, administrador)
    if administrador.nivel == 3:
        mostar_pantalla_entre_niveles(administrador, PANTALLA)
        ejecutar_nivel(PANTALLA, jugador_principal, administrador)

    if administrador.vidas > 0:
        mostar_pantalla_gano(PANTALLA, administrador)       
    else: 
        mostar_pantalla_perdio(PANTALLA, administrador)

while flag_jugar:    
    jugar()
