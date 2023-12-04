import pygame
import sys
import data
from funciones_bd import generar_top_5


FUENTE = pygame.font.SysFont(data.FUENTE_1, 60, False, True)
FUENTE_MEDIA = pygame.font.SysFont(data.FUENTE_1, 40, False, True)
FUENTE_CHICA = pygame.font.SysFont(data.FUENTE_1, 20, False, True)

COLORES = 1

def mostar_pantalla_perdio(pantalla, administrador):
    
    flag_sonido = administrador.sonido

    lista_top_score = generar_top_5()
    #print(lista_top_score)

    sonido_perdio = pygame.mixer.Sound("sonidos\game over.mp3")  
    sonido_perdio.set_volume(0.5)
    if flag_sonido:
        sonido_perdio.play()

    flag_perdio = True

    while flag_perdio :

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pantalla.fill((data.diccionario_set_up[COLORES]["NEGRO"]))

        texto = FUENTE.render(f'GAME OVER', 1, data.diccionario_set_up[COLORES]["ROSA_1"])
        texto_pierde = FUENTE_MEDIA.render(f'next time!', 1, data.diccionario_set_up[COLORES]["ROSA_1"])
        texto_continuar = FUENTE_CHICA.render(f'Press enter to restart', 1, data.diccionario_set_up[COLORES]["ROSA_1"])
        texto_score = FUENTE_CHICA.render("TOP SCORE", 1, data.diccionario_set_up[COLORES]["ROSA_1"])
        texto_tu_score = FUENTE_CHICA.render(f"your score {administrador.score}", 1, data.diccionario_set_up[COLORES]["ROSA_1"])
        texto_salir = FUENTE_CHICA.render(f'Press esc to exit', 1, data.diccionario_set_up[COLORES]["ROSA_1"])
        
        pantalla.blit(texto, (data.ANCHO_VENTANA/2 - (texto.get_width()/2), 60))
        pantalla.blit(texto_pierde, (data.ANCHO_VENTANA/2 - (texto_pierde.get_width()/2), 150))
        pantalla.blit(texto_continuar, (data.ANCHO_VENTANA/2 - (texto_continuar.get_width()/2), 565))
        pantalla.blit(texto_score, (data.ANCHO_VENTANA/2 - (texto_score.get_width()/2), 270))
        pantalla.blit(texto_tu_score, (data.ANCHO_VENTANA/2 - (texto_tu_score.get_width()/2), 205))
        pantalla.blit(texto_salir, (data.ANCHO_VENTANA/2 - (texto_continuar.get_width()/2), 605))

        for i,elemento in enumerate(lista_top_score):
            texto_a_mostrar = f'{elemento[0]}.......{elemento[1]}'
            texto_tabla = FUENTE_CHICA.render(texto_a_mostrar, 1, data.diccionario_set_up[COLORES]["ROSA_1"])
            pantalla.blit(texto_tabla, (data.ANCHO_VENTANA/2 - (texto_tabla.get_width()/2), 45*i + 305))

        
        enter = pygame.key.get_pressed()
        if enter[pygame.K_RETURN]:
            if flag_sonido:
                sonido_perdio.stop()
            flag_perdio = False
            #pygame.quit()
            #sys.exit()
            

        if enter[pygame.K_ESCAPE]:
            flag_perdio = False
            pygame.quit()
            sys.exit()
            
        pygame.display.update()
            