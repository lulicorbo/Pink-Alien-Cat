import pygame
import sys
import funciones
import data
from pantalla_game_over import mostar_pantalla_perdio
from pantalla_gano import mostar_pantalla_gano

pygame.init()

pygame.mixer.init()

NIVEL_1 = 0
NIVEL_2 = 1
NIVEL_3 = 2 

COLORES = 1

FPS = 80
RELOJ = pygame.time.Clock() 

FUENTE = pygame.font.SysFont(data.FUENTE_1, 40, False, True)
FUENTE_CHICA = pygame.font.SysFont(data.FUENTE_1, 15, False, True)

timer = pygame.USEREVENT + 1 
intervalo_tiempo = 1000 
pygame.time.set_timer(timer, intervalo_tiempo)

def ejecutar_nivel(pantalla, jugador, administrador): 
    """Esta función recibe como parametro una pantalla, un jugador, y un administrador.
    Se encarga de ejecutar los niveles. Crea enemigos cantidad y tamaño de enemigos según 
    el nivel"""
    imagen_no_sonido = pygame.image.load("imagenes\img_no_musica.png")
    imagen_no_sonido = pygame.transform.scale(imagen_no_sonido, (25, 25))
    boton_no_sonido_marcado = None
    imagen_sonido = pygame.image.load("imagenes\img_musica.png")
    imagen_sonido = pygame.transform.scale(imagen_sonido, (25, 25))   
    boton_sonido_marcado = None
    
    #set up sonido y fondo de pantalla
    sonido_principal = pygame.mixer.Sound("sonidos\principal.mp3")  
    sonido_principal.set_volume(0.05)
    flag_sonido = administrador.sonido
    if flag_sonido:
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
    ancho_lasers = data.diccionario_niveles[nivel]["ancho_disparos"]
    alto_lasers = data.diccionario_niveles[nivel]["alto_disparos"]
    cantidad_recompensas = data.diccionario_niveles[nivel]["cantidad_recompensas"]
    cantidad_meteoritos = data.diccionario_niveles[nivel]["cantidad_meteoritos"]
    vidas_enemigos = data.diccionario_niveles[nivel]["vidas_enemigos"]
        
    lista_lasers_jugador = []  

    sonido_disparo_jugador = pygame.mixer.Sound("sonidos\laser.mp3")  
    sonido_disparo_jugador.set_volume(0.05)

    enemigos, lasers_enemigos = funciones.generar_lista_enemigos_y_disparos(cantidad_enemigos, ancho_enemigos, alto_enemigos, tiempo_entre_disparos,vidas_enemigos) 

    lista_recompensas = funciones.crear_lista_recompensa(cantidad_recompensas)
    lista_meteoritos = funciones.crear_lista_meteoritos(cantidad_meteoritos)

    flag_nivel = True
    flag_pausa = False

    while flag_nivel: #Mismo bloque while para todos los niveles
        RELOJ.tick(FPS)
        flag_sonido = administrador.sonido
        
        rect_no_sonido = imagen_no_sonido.get_rect(topleft=(10, 10))
        rect_sonido = imagen_sonido.get_rect(topleft=(50, 10))

        if flag_pausa == False:
            pantalla.blit(fondo, (0, 0))

            lista_eventos = pygame.event.get()
            for evento in lista_eventos:
                if evento.type == pygame.QUIT:
                    flag_nivel = False
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:  #Disparos jugador   ##### ###
                    if evento.key == pygame.K_SPACE:
                        nuevo_laser = jugador.crear_laser()
                        if administrador.sonido == True:
                            sonido_disparo_jugador.play()
                        lista_lasers_jugador.append(nuevo_laser)
                        administrador.score -= 1 
                elif evento.type == pygame.MOUSEBUTTONDOWN: #Se apreta botón               
                    if rect_sonido.collidepoint(evento.pos):
                        boton_sonido_marcado = True
                    elif rect_no_sonido.collidepoint(evento.pos):
                        boton_no_sonido_marcado = True
                elif evento.type == pygame.MOUSEBUTTONUP:  #Se suelta botón
                    if boton_no_sonido_marcado:
                        if administrador.sonido == True:
                            sonido_principal.stop()
                            administrador.sonido = False
                    if boton_sonido_marcado:
                        if administrador.sonido == False:
                            sonido_principal.play()
                            administrador.sonido = True
                            
                    boton_sonido_marcado = False
                    boton_no_sonido_marcado = False 

                elif evento.type == timer:
                    administrador.tiempo += 1
            
            keys = pygame.key.get_pressed()
            if True in keys:
                if keys[pygame.K_p]:
                    flag_pausa = True
                
        
            funciones.mostrar_score_vidas(administrador, pantalla)

            funciones.update_jugador_y_lasers(jugador, lista_lasers_jugador, pantalla)
            funciones.update_enemigos_y_disparos(enemigos, lasers_enemigos, pantalla, ancho_lasers, alto_lasers, tiempo_entre_disparos)
            funciones.update_listas_especiales(pantalla, lista_recompensas)
            funciones.update_listas_especiales(pantalla, lista_meteoritos)
            funciones.colision_jugador(jugador, lasers_enemigos, pantalla, administrador)
            funciones.colision_enemigo(enemigos, lista_lasers_jugador, administrador)
            funciones.colision_reusar_recompensa_jugador(lista_recompensas,pantalla, jugador, administrador)
            funciones.colision_reusar_meterito(lista_meteoritos, pantalla, jugador, administrador)

            pygame.draw.rect(pantalla, data.diccionario_set_up[COLORES]["NEGRO"], rect_sonido)
            pygame.draw.rect(pantalla, data.diccionario_set_up[COLORES]["NEGRO"], rect_no_sonido)

            pantalla.blit(imagen_no_sonido, rect_no_sonido)
            pantalla.blit(imagen_sonido, rect_sonido)
            
            #Se verifica si se termino el nivel (ganando o perdiendo)
            if funciones.check_nivel(administrador, jugador, enemigos, pantalla)== True:
                if flag_sonido:
                    sonido_principal.stop()
                flag_nivel = False 
            elif funciones.check_nivel(administrador, jugador, enemigos, pantalla) == -1:
                if flag_sonido:
                    sonido_principal.stop()
                #mostar_pantalla_perdio(pantalla, administrador)
                flag_nivel = False
            elif funciones.check_nivel(administrador, jugador, enemigos, pantalla) == 1:
                if flag_sonido:
                    sonido_principal.stop()
                #mostar_pantalla_gano(pantalla, administrador)
                flag_nivel = False
        

        if flag_pausa:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 
                    sys.exit()
            
            keys = pygame.key.get_pressed()
            if True in keys:
                if keys[pygame.K_RETURN]:
                    flag_pausa = False

            pantalla.fill(data.diccionario_set_up[COLORES]["NEGRO"])
            texto = FUENTE.render("PAUSED", 1, data.diccionario_set_up[COLORES]["ROSA_1"])
            texto_2 = FUENTE_CHICA.render("press enter to continue", 1, data.diccionario_set_up[COLORES]["ROSA_1"])
            pantalla.blit(texto, (data.ANCHO_VENTANA/2 - (texto.get_width()/2), 200))
            pantalla.blit(texto_2, (data.ANCHO_VENTANA/2 - (texto_2.get_width()/2), 500))
            pygame.display.update()

        pygame.display.flip()

       