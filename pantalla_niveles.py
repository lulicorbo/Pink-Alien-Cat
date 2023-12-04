import pygame
import sys
import data

FUENTE = pygame.font.SysFont(data.FUENTE_1, 40, False, True)

COLORES = 1

pygame.init()

def mostar_pantalla_entre_niveles(administrador, pantalla):
    """Esta función recibe como parametro una pantalla (objeto) y administrador
    y muestra cual es el proximo nivel a jugar."""

    flag_sonido = administrador.sonido
    sonido_entre_niveles = pygame.mixer.Sound("sonidos\gano.mp3")  
    sonido_entre_niveles.set_volume(0.2)
    if administrador.sonido == True:
        sonido_entre_niveles.play()

    flag_lapso = True
    pantalla.fill(data.diccionario_set_up[COLORES]["NEGRO"])
    pygame.display.update()

    tiempo_actual = 0
    inicio_del_nivel = 0
    
    while flag_lapso:

        pygame.time.delay(5)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag_lapso = False
                pygame.quit() 
                sys.exit()

        if inicio_del_nivel == 0: #Guarda tiempo de inicio primera vez
            inicio_del_nivel = pygame.time.get_ticks()

        tiempo_actual = pygame.time.get_ticks() #Guarda tiempo actual
        tiempo_transcurrido = tiempo_actual - inicio_del_nivel  #Guarda cuanto tiempo paso
        
        texto = FUENTE.render(f'LEVEL {administrador.nivel}', 1, data.diccionario_set_up[COLORES]["ROSA_1"])

        pantalla.blit(texto, (data.ANCHO_VENTANA/2 - (texto.get_width()/2), 300))
        
        pygame.display.update()
        
        if tiempo_transcurrido > 2000: #Si pasan más de 2 segundos se deja de mostrar pantalla
            break
            