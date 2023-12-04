import pygame
import sys
import data

pygame.init()
pygame.mixer.init()

FUENTE_TITULO = pygame.font.SysFont(data.FUENTE_1, 60, False, True)
FUENTE_BOTON = pygame.font.SysFont(data.FUENTE_1, 40, False, True)
FUENTE_CHICA = pygame.font.SysFont(data.FUENTE_1, 20, False, True)

COLORES = 1

def mostrar_pantalla_inicio(pantalla, administrador):
    """Esta función recibe como parametro una pantalla (objeto) y administrador y muestra la pantalla 
    de inicio del juego. Muestra botones de EXIT, START y sonido"""

    sonido_inicio = pygame.mixer.Sound("sonidos\gano.mp3")  
    sonido_inicio.set_volume(0.2)
    sonido_inicio.play()

    boton_start = pygame.Rect((data.ANCHO_VENTANA/2 - 80), 400, 160, 120)
    boton_start_marcado = None
    boton_start_presionado = None

    boton_exit = pygame.Rect((data.ANCHO_VENTANA - 100), 0, 100, 60)
    boton_exit_marcado = None
    boton_exit_presionado = None

    imagen_no_sonido = pygame.image.load("imagenes\img_no_musica.png")
    imagen_no_sonido = pygame.transform.scale(imagen_no_sonido, (50, 50))
    boton_no_sonido_marcado = None

    imagen_sonido = pygame.image.load("imagenes\img_musica.png")
    imagen_sonido = pygame.transform.scale(imagen_sonido, (50, 50))   
    boton_sonido_marcado = None

    flag_sonido = None
    flag_inicio = True
    flag_salir = False

    while flag_inicio :
        
        rect_no_sonido = imagen_no_sonido.get_rect(topleft=(10, 10))
        rect_sonido = imagen_sonido.get_rect(topleft=(80, 10))

        pantalla.fill((data.diccionario_set_up[COLORES]["NEGRO"]))

        titulo = FUENTE_TITULO.render("PINK ALIEN CAT", 1, data.diccionario_set_up[COLORES]["ROSA_1"])
        pantalla.blit(titulo, ((data.ANCHO_VENTANA/2) - (titulo.get_width()/2), 200))

        for evento in pygame.event.get():
            if (evento.type == pygame.QUIT) or flag_salir:
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.MOUSEMOTION:   #Se mueve mouse sobre boton
                boton_start_marcado = boton_start.collidepoint(evento.pos)
                boton_exit_marcado = boton_exit.collidepoint(evento.pos)

            elif evento.type == pygame.MOUSEBUTTONDOWN: #Se apreta botón
                if boton_start.collidepoint(evento.pos):
                    boton_start_presionado = True
                elif boton_exit.collidepoint(evento.pos):
                    boton_exit_presionado = True
                elif rect_sonido.collidepoint(evento.pos):
                    boton_sonido_marcado = True
                elif rect_no_sonido.collidepoint(evento.pos):
                    boton_no_sonido_marcado = True

            elif evento.type == pygame.MOUSEBUTTONUP:  #Se suelta botón
                if boton_start_presionado: ###EXPIEZA
                    flag_inicio = False 
                if boton_exit_presionado:
                    flag_salir = True
                if boton_no_sonido_marcado:
                    administrador.sonido = False
                if boton_sonido_marcado:
                    administrador.sonido = True
                boton_start_presionado = False ###
                boton_exit_presionado = False
                boton_sonido_marcado = False
                boton_no_sonido_marcado = False

            
        color_sonido = data.diccionario_set_up[COLORES]["NEGRO"]
        color_no_sonido = data.diccionario_set_up[COLORES]["NEGRO"]
        if boton_start_marcado:
            color_bot = data.diccionario_set_up[COLORES]["ROSA_1"]
        else:
            color_bot = data.diccionario_set_up[COLORES]["ROSA_2"]
        
        if boton_exit_marcado:
            color_bot_exit = data.diccionario_set_up[COLORES]["ROSA_1"]
        else:
            color_bot_exit = data.diccionario_set_up[COLORES]["ROSA_2"]

        if boton_sonido_marcado: 
            color_sonido = data.diccionario_set_up[COLORES]["ROSA_1"]
        if boton_no_sonido_marcado:
            color_no_sonido = data.diccionario_set_up[COLORES]["ROSA_1"]

        pygame.draw.rect(pantalla, color_bot, boton_start)
        pygame.draw.rect(pantalla, color_bot_exit, boton_exit) 
        pygame.draw.rect(pantalla, color_sonido, rect_sonido)
        pygame.draw.rect(pantalla, color_no_sonido, rect_no_sonido)

        texto_boton = FUENTE_BOTON.render("START", True, data.diccionario_set_up[COLORES]["NEGRO"])
        texto_boton_rect = texto_boton.get_rect(center=boton_start.center)

        texto_boton_exit = FUENTE_CHICA.render("EXIT", True, data.diccionario_set_up[COLORES]["NEGRO"])
        texto_boton_exit_rect = texto_boton_exit.get_rect(center=boton_exit.center)

        pantalla.blit(texto_boton, texto_boton_rect)
        pantalla.blit(texto_boton_exit, texto_boton_exit_rect)
        pantalla.blit(imagen_no_sonido, rect_no_sonido)
        pantalla.blit(imagen_sonido, rect_sonido)


        pygame.display.update()
