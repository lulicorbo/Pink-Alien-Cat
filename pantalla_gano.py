import pygame
import sys
import data
import funciones_bd

pygame.init()
pygame.mixer.init()

FUENTE = pygame.font.SysFont(data.FUENTE_1, 60, False, True)
FUENTE_CHICA = pygame.font.SysFont(data.FUENTE_1, 15, False, True)

COLORES = 1

def mostar_pantalla_gano(pantalla:object)->None:

    lista_top_score = funciones_bd.generar_top_5()
    #print(lista_top_score)

    sonido_victoria = pygame.mixer.Sound("sonidos\gano.mp3")  
    sonido_victoria.set_volume(0.5)
    sonido_victoria.play()

    flag_gano = True

    while flag_gano :

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pantalla.fill((data.diccionario_set_up[COLORES]["NEGRO"]))

        texto = FUENTE.render(f'GAME OVER', 1, data.diccionario_set_up[COLORES]["ROSA_1"])
        texto_gana = FUENTE.render(f'you won!', 1, data.diccionario_set_up[COLORES]["ROSA_1"])
        texto_continuar = FUENTE_CHICA.render(f'Press enter to exit', 1, data.diccionario_set_up[COLORES]["ROSA_1"])
        texto_score = FUENTE_CHICA.render("TOP SCORE", 1, data.diccionario_set_up[COLORES]["ROSA_1"])

        pantalla.blit(texto, (data.ANCHO_VENTANA/2 - (texto.get_width()/2), 100))
        pantalla.blit(texto_gana, (data.ANCHO_VENTANA/2 - (texto_gana.get_width()/2), 200))
        pantalla.blit(texto_continuar, (data.ANCHO_VENTANA/2 - (texto_continuar.get_width()/2), 300))
        pantalla.blit(texto_score, (data.ANCHO_VENTANA/2 - (texto_score.get_width()/2), 380))

        for i,elemento in enumerate(lista_top_score):
            texto_a_mostrar = f'{elemento[0]}.......{elemento[1]}'
            texto_tabla = FUENTE_CHICA.render(texto_a_mostrar, 1, data.diccionario_set_up[COLORES]["ROSA_1"])
            pantalla.blit(texto_tabla, (data.ANCHO_VENTANA/2 - (texto_tabla.get_width()/2), 50*i + 420))
            
        enter = pygame.key.get_pressed()
        if enter[pygame.K_RETURN]:
            sonido_victoria.stop()
            flag_gano = False
            pygame.quit()
            sys.exit()
        pygame.display.update()
