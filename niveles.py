import pygame
import sys
import funciones
import data
import pantalla_game_over
import pantalla_gano

pygame.init()

pygame.mixer.init()

NIVEL_1 = 0
NIVEL_2 = 1
NIVEL_3 = 2 

COLORES = 1

FPS = 45
RELOJ = pygame.time.Clock() 

def ejecutar_nivel(pantalla: object, jugador: object, administrador: object): 
    """Esta función recibe como parametro una pantalla, un jugador, y un administrador.
    Se encarga de ejecutar los niveles. Crea enemigos cantidad y tamaño de enemigos según 
    el nivel"""

    #set up sonido y fondo de pantalla
    sonido_principal = pygame.mixer.Sound("sonidos\principal.mp3")  
    sonido_principal.set_volume(0.3)
    sonido_principal.play()

    fondo = pygame.image.load("imagenes\galaxia_fondo.png")
    fondo = pygame.transform.scale(fondo, (data.ANCHO_VENTANA, data.LARGO_VENTANA))


    #Para ver cuantos y como son los enemigos
    match (administrador.nivel):
        case 1:
            nivel = NIVEL_1
        case 2:
            nivel = NIVEL_2
        case 3:
            nivel = NIVEL_3

    cantidad_enemigos = data.diccionario_niveles[nivel]["cantidad_enemigos"]
    ancho_enemigos = data.diccionario_niveles[nivel]["ancho_enemigos"]
    alto_enemigos = data.diccionario_niveles[nivel]["alto_elemigos"]
    tiempo_entre_disparos = data.diccionario_niveles[nivel]["tiempo_entre_disparos"]
        
    lista_lasers_jugador = []  

    sonido_disparo_jugador = pygame.mixer.Sound("sonidos\laser.mp3")  
    sonido_disparo_jugador.set_volume(0.3)

    enemigos, lasers_enemigos = funciones.generar_lista_enemigos_y_disparos(cantidad_enemigos, ancho_enemigos, alto_enemigos) 

    flag_nivel = True

    while flag_nivel: #Mismo bloque while para todos los niveles
        RELOJ.tick(FPS)
        pantalla.blit(fondo, (0, 0))

        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag_nivel = False
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:  #Disparos jugador
                if evento.key == pygame.K_SPACE:
                    nuevo_laser = jugador.crear_laser()
                    sonido_disparo_jugador.play()
                    lista_lasers_jugador.append(nuevo_laser)
                    administrador.score -= 2  

        funciones.update_jugador_y_lasers(jugador, lista_lasers_jugador, pantalla)
        funciones.update_enemigos_y_disparos(enemigos, lasers_enemigos, pantalla, tiempo_entre_disparos)
        funciones.colision_jugador(jugador, lasers_enemigos, pantalla, administrador)
        funciones.colision_enemigo(enemigos, lista_lasers_jugador, administrador)

        #Se verifica si se termino el nivel (ganando o perdiendo)
        if funciones.check_nivel(administrador, jugador, enemigos, pantalla):
            sonido_principal.stop()
            flag_nivel = False  

        pygame.display.flip()

       