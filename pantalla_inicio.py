import pygame
import sys
import data

pygame.init()
pygame.mixer.init()

FUENTE_TITULO = pygame.font.SysFont(data.FUENTE_1, 60, False, True)
FUENTE_BOTON = pygame.font.SysFont(data.FUENTE_1, 40, False, True)

COLORES = 1

def mostrar_pantalla_inicio(pantalla:object)->None:
    """Esta función recibe como parametro una pantalla (objeto) y muestra la pantalla de inicio
    del juego. Se sale de esta con el botón de START"""

    sonido_inicio = pygame.mixer.Sound("sonidos\gano.mp3")  
    sonido_inicio.set_volume(0.4)
    sonido_inicio.play()

    boton_start = pygame.Rect((data.ANCHO_VENTANA/2 - 80), 400, 160, 120)
    boton_marcado = None
    boton_presionado = None

    flag_inicio = True

    while flag_inicio :

        pantalla.fill((data.diccionario_set_up[COLORES]["NEGRO"]))

        titulo = FUENTE_TITULO.render("PINK ALIEN CAT", 1, data.diccionario_set_up[COLORES]["ROSA_1"])
        pantalla.blit(titulo, ((data.ANCHO_VENTANA/2) - (titulo.get_width()/2), 200))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEMOTION:   #Se mueve mouse sobre boton
                boton_marcado = boton_start.collidepoint(evento.pos)
            elif evento.type == pygame.MOUSEBUTTONDOWN: #Se apreta botón
                if boton_start.collidepoint(evento.pos):
                    boton_presionado = True
            elif evento.type == pygame.MOUSEBUTTONUP:  #Se suelta botón
                if boton_presionado:
                    #print("empieza")
                    flag_inicio = False 
                boton_presionado = False 

        if boton_marcado:
            color_bot = data.diccionario_set_up[COLORES]["ROSA_1"]
        else:
            color_bot = data.diccionario_set_up[COLORES]["ROSA_2"]
        
        pygame.draw.rect(pantalla, color_bot, boton_start)
      
        texto_boton = FUENTE_BOTON.render("START", True, data.diccionario_set_up[COLORES]["NEGRO"])
        texto_boton_rect = texto_boton.get_rect(center=boton_start.center)

        pantalla.blit(texto_boton, texto_boton_rect)

        pygame.display.update()
