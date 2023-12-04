from clase_enemigo import Enemigo
from clase_laser import Laser
from clase_recompensa import Recompensa
from clase_meteorito import Meteorito
import re
from pantalla_game_over import mostar_pantalla_perdio
from pantalla_gano import mostar_pantalla_gano
from funciones_bd import agregar_score
import pygame
import data
import random

pygame.init()
pygame.mixer.init()

"""Funciones auxiliares que crean objetos, manejan los updates y las colisiones"""
#CREAR LISTAS
def generar_lista_enemigos_y_disparos(cantidad_enemigos, ancho, alto, tiempo_entre_disparos, vidas_enemigos):
    lista_enemigos = []
    lista_lasers = []
    for i in range(cantidad_enemigos):
        enemigo = Enemigo(ancho, alto, tiempo_entre_disparos, vidas_enemigos)  
        lista_enemigos.append(enemigo)
    return lista_enemigos, lista_lasers

def crear_lista_recompensa(cantidad): 
    lista_recompensa = []
    for i in range(cantidad):
        recompensa = Recompensa() 
        lista_recompensa.append(recompensa)
    return lista_recompensa

def crear_lista_meteoritos(cantidad): 
    lista_meteoritos = []
    for i in range (cantidad):
        meteorioto = Meteorito()
        lista_meteoritos.append(meteorioto)
    return lista_meteoritos


#UPDATES
def update_jugador_y_lasers(jugador, lista_lasers, pantalla):
    jugador.update()
    pantalla.blit(jugador.imagen, jugador.rect)
    for laser in lista_lasers:
        laser.update()
        pantalla.blit(laser.imagen, laser.rect.topleft)

def update_enemigos_y_disparos(lista_enemigos, lista_lasers, pantalla, ancho_lasers, alto_lasers, tiempo_entre_disparos = 30):
    for enemigo in lista_enemigos:
        enemigo.update(pantalla)
        pantalla.blit(enemigo.imagen, (enemigo.rect.x, enemigo.rect.y))

        if enemigo.tiempo_entre_disparos <= 0:
            laser = Laser(enemigo.rect.centerx, enemigo.rect.bottom, "abajo", ancho_lasers, alto_lasers)
            lista_lasers.append(laser)
            enemigo.tiempo_entre_disparos = tiempo_entre_disparos  

        if enemigo.visible == False:
            enemigo.tiempo_entre_disparos = 200000

    for laser in lista_lasers:
        laser.update()
        pantalla.blit(laser.imagen, (laser.rect.x, laser.rect.bottom))

def update_listas_especiales(pantalla, lista): ##para meteoritos y reompensa
    for elemento in lista:
        pantalla.blit(elemento.imagen,elemento.rect)
        elemento.update()


#COLISIONES
def colision_jugador(jugador, lista_lasers_enemigos, pantalla, administrador):
    contador = 0
    for i, laser in enumerate(lista_lasers_enemigos):
        if laser.rect.colliderect(jugador.rect):
            laser_eliminado = lista_lasers_enemigos.pop(i)
            administrador.vidas -= 1
            administrador.score -= 20
            if administrador.vidas <=0:
                jugador.visible = False

def colision_enemigo(lista_enemigos, lista_lasers_jugador, administrador):
    sonido_explosion = pygame.mixer.Sound("sonidos\explosion.mp3")  
    sonido_explosion.set_volume(0.4)
    for enemigo in lista_enemigos:
        if enemigo.visible: 
            for i, laser in enumerate(lista_lasers_jugador):
                if laser.rect.colliderect(enemigo.rect):
                    laser_eliminado = lista_lasers_jugador.pop(i)
                    administrador.score += 70
                    enemigo.vida -= 1
                    if administrador.sonido == True:
                        sonido_explosion.play()
        if enemigo.vida == 0:
            enemigo.animacion()
            enemigo.visible = False

def colision_reusar_meterito(lista_meteoritos, pantalla, jugador, administrador):
    for meteorito in lista_meteoritos:
        if meteorito.rect.colliderect(jugador.rect):
            meteorito.rect.x = random.randint(10, 560) 
            meteorito.rect.y = random.randint(-300, -100)
            administrador.score -= 50
            administrador.vidas -= 1
        if meteorito.rect.y >= 700:
            meteorito.rect.x = random.randint(10, 560) 
            meteorito.rect.y = random.randint(-300, -100)

def colision_reusar_recompensa_jugador(lista_recompensas, pantalla, jugador, administrador):
    for recompensa in lista_recompensas:
        if recompensa.rect.colliderect(jugador.rect):
            recompensa.rect.x = random.randint(10, 560) 
            recompensa.rect.y = random.randint(-300, -100)
            administrador.score += 100
            administrador.vidas += 1
        if recompensa.rect.y >= 700:
            recompensa.rect.x = random.randint(10, 560) 
            recompensa.rect.y = random.randint(-300, -100)


#MOSTRAR VIDAS, SCORE Y TIEMPO
def mostrar_score_vidas(adminimistrador, pantalla):
    fuente = pygame.font.SysFont(data.FUENTE_1, 12, False, True)
    color = (255, 255, 255)
    mensaje_1 = f"life: {adminimistrador.vidas}"
    mensaje_2 = f"score:{adminimistrador.score}"
    mensaje_3 = f"time:{adminimistrador.tiempo}"
    texto_1 = fuente.render(mensaje_1, 1, color)
    texto_2 = fuente.render(mensaje_2, 1, color)
    texto_3 = fuente.render(mensaje_3, 1, color)
    pantalla.blit(texto_1, (10, 645))
    pantalla.blit(texto_2, (520, 645))
    pantalla.blit(texto_3, ((300 - texto_3.get_width()/2), 645))

#CHECK ESTADO DEL NIVEL
def check_nivel(administrador, jugador, lista_enemigos, pantalla):
    """Esta funcion es la encargada de ver si se perdio, se paso de nivel o ya se gano el juego.
    Tambian agrega el nombre y el puntaje de la partida a la base de datos cuando se pierde o se gana"""
    todos_enemigos_muertos = all (enemigo.visible == False for enemigo in lista_enemigos)

    nombre = jugador.nombre
    score = administrador.score
    
    if administrador.vidas <= 0:
        #print(f"Tu score {score}")
        #print(f'{administrador.tiempo}')
        agregar_score(nombre, score)
        return -1
        #mostar_pantalla_perdio(pantalla, administrador)


    elif todos_enemigos_muertos:
        if administrador.nivel < 3:
            administrador.nivel += 1
            administrador.score += 100
            return True ####PASA DE NIVEL
        else:
            #print(f"Tu score {score}")
            agregar_score(nombre, score)
            #mostar_pantalla_gano(pantalla, administrador)
            return 1


#VALIDACION DEL NOMBRE DEL JUGADORs
def validar_nombre(nombre):
    patron = r'^[a-zA-Z0-9]{2,10}$'
    if re.search(patron, nombre):
        return True
    else:
        return False
    
