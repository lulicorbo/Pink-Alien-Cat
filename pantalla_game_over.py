import pygame
import sys
import data
import funciones_bd


FUENTE = pygame.font.SysFont(data.FUENTE_1, 50, False, True)
FUENTE_CHICA = pygame.font.SysFont(data.FUENTE_1, 15, False, True)

COLORES = 1

def mostar_pantalla_perdio(pantalla:object)->None:

    lista_top_score = funciones_bd.generar_top_5()
    #print(lista_top_score)

    sonido_perdio = pygame.mixer.Sound("sonidos\game over.mp3")  
    sonido_perdio.set_volume(0.5)
    sonido_perdio.play()

    flag_perdio = True

    while flag_perdio :

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pantalla.fill((data.diccionario_set_up[COLORES]["NEGRO"]))

        texto = FUENTE.render(f'GAME OVER', 1, data.diccionario_set_up[COLORES]["ROSA_1"])
        texto_pierde = FUENTE.render(f'next time!', 1, data.diccionario_set_up[COLORES]["ROSA_1"])
        texto_continuar = FUENTE_CHICA.render(f'Press enter to exit', 1, data.diccionario_set_up[COLORES]["ROSA_1"])
        texto_score = FUENTE_CHICA.render("TOP SCORE", 1, data.diccionario_set_up[COLORES]["ROSA_1"])

        pantalla.blit(texto, (data.ANCHO_VENTANA/2 - (texto.get_width()/2), 100))
        pantalla.blit(texto_pierde, (data.ANCHO_VENTANA/2 - (texto_pierde.get_width()/2), 200))
        pantalla.blit(texto_continuar, (data.ANCHO_VENTANA/2 - (texto_continuar.get_width()/2), 300))
        pantalla.blit(texto_score, (data.ANCHO_VENTANA/2 - (texto_score.get_width()/2), 380))

        for i,elemento in enumerate(lista_top_score):
            texto_a_mostrar = f'{elemento[0]}.......{elemento[1]}'
            texto_tabla = FUENTE_CHICA.render(texto_a_mostrar, 1, data.diccionario_set_up[COLORES]["ROSA_1"])
            pantalla.blit(texto_tabla, (data.ANCHO_VENTANA/2 - (texto_tabla.get_width()/2), 50*i + 420))

        
        enter = pygame.key.get_pressed()
        if enter[pygame.K_RETURN]:
            sonido_perdio.stop()
            flag_perdio = False
            pygame.quit()
            sys.exit()
        pygame.display.update()
            