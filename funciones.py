import clase_enemigo
import clase_laser
import re
import pantalla_game_over
import pantalla_gano
import funciones_bd
import pygame

pygame.init()
pygame.mixer.init()

def generar_lista_enemigos_y_disparos(cantidad_enemigos, ancho, alto):
    lista_enemigos = []
    lista_lasers = []

    for i in range(cantidad_enemigos):
        enemigo = clase_enemigo.Enemigo(ancho, alto)  
        lista_enemigos.append(enemigo)

    return lista_enemigos, lista_lasers


def update_enemigos_y_disparos(lista_enemigos, lista_lasers, pantalla, tiempo_entre_disparos = 30):
    for enemigo in lista_enemigos:
        enemigo.update(pantalla)
        pantalla.blit(enemigo.imagen, (enemigo.rect.x, enemigo.rect.y))

        if enemigo.tiempo_entre_disparos <= 0:
            laser = clase_laser.Laser(enemigo.rect.centerx, enemigo.rect.bottom, "abajo")
            lista_lasers.append(laser)
            enemigo.tiempo_entre_disparos = tiempo_entre_disparos  

        if enemigo.visible == False:
            enemigo.tiempo_entre_disparos = 200000

    for laser in lista_lasers:
        laser.update()
        pantalla.blit(laser.imagen, (laser.rect.x, laser.rect.bottom))


def update_jugador_y_lasers(jugador, lista_lasers, pantalla):
    jugador.update()
    pantalla.blit(jugador.imagen, jugador.rect)
    for laser in lista_lasers:
        laser.update()
        pantalla.blit(laser.imagen, laser.rect.topleft)




def colision_jugador(jugador, lista_lasers_enemigos, pantalla, administrador):
    contador = 0
    for i, laser in enumerate(lista_lasers_enemigos):
        if laser.rect.colliderect(jugador.rect):
            laser_eliminado = lista_lasers_enemigos.pop(i)
            administrador.vidas -= 1
            administrador.score -= 10
            if administrador.vidas <=0:
                jugador.visible = False

   

def colision_enemigo(lista_enemigos, lista_lasers_jugador, administrador):
    sonido_explosion = pygame.mixer.Sound("sonidos\explosion.mp3")  
    sonido_explosion.set_volume(0.4)
    
    for enemigo in lista_enemigos:

        for i, laser in enumerate(lista_lasers_jugador):
            if laser.rect.colliderect(enemigo.rect):
                laser_eliminado = lista_lasers_jugador.pop(i)
                administrador.score += 50
                enemigo.vida = 0
                sonido_explosion.play()
        if enemigo.vida == 0:
            enemigo.animacion()
            enemigo.visible = False




def check_nivel(administrador, jugador, lista_enemigos, pantalla):
    """Esta funcion es la encargada de ver si se perdio, se paso de nivel o ya se gano el juego.
    Tambian agrega el nombre y el puntaje de la partida a la base de datos cuando se pierde o se gana"""
    todos_enemigos_muertos = all (enemigo.visible == False for enemigo in lista_enemigos)

    nombre = jugador.nombre
    score = administrador.score
    
    if jugador.visible == False:
        print(f"Tu score {score}")
        funciones_bd.agregar_score(nombre, score)
        pantalla_game_over.mostar_pantalla_perdio(pantalla)

    elif todos_enemigos_muertos:
        if administrador.nivel < 3:
            administrador.nivel += 1
            administrador.score += 100
            return True ####PASA DE NIVEL
        else:
            print(f"Tu score {score}")
            funciones_bd.agregar_score(nombre, score)
            pantalla_gano.mostar_pantalla_gano(pantalla)


def validar_nombre(nombre):
    patron = r'^[a-zA-Z0-9]{2,10}$'
    if re.search(patron, nombre):
        return True
    else:
        return False
    
