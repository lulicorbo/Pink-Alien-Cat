import pygame
import data
import clase_administrador
import pantalla_inicio
import pantalla_nombre
import pantalla_niveles
import clase_jugador
import niveles
import funciones_bd

pygame.init()

#Se crea base de datos si no existe
funciones_bd.crear_base_de_datos_score()

#Set up
PANTALLA = pygame.display.set_mode((data.ANCHO_VENTANA, data.LARGO_VENTANA))

pygame.display.set_caption("Pink Alien Cat") 
icono = pygame.image.load("imagenes\jugador.png")
icono = pygame.transform.scale(icono, (10, 10))
pygame.display.set_icon(icono)

#Pantalla de inicio
pantalla_inicio.mostrar_pantalla_inicio(PANTALLA)

#Se crea administrador (maneja tiempo, score, niveles)y jugador principal
administrador = clase_administrador.Administrador(3)
jugador_principal = clase_jugador.Jugador()

#Pantalla ingreso nombre
nombre = pantalla_nombre.mostar_pantalla_ingresar_nombre(PANTALLA)
jugador_principal.nombre = nombre

#Se ejecutan los diferentes niveles y pantalla previa
pantalla_niveles.mostar_pantalla_entre_niveles(administrador, PANTALLA)
niveles.ejecutar_nivel(PANTALLA, jugador_principal, administrador)
pantalla_niveles.mostar_pantalla_entre_niveles(administrador, PANTALLA)
niveles.ejecutar_nivel(PANTALLA, jugador_principal, administrador)
pantalla_niveles.mostar_pantalla_entre_niveles(administrador, PANTALLA)
niveles.ejecutar_nivel(PANTALLA, jugador_principal, administrador)

 
