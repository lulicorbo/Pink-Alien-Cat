import pygame
import sys
import data
import funciones

pygame.init()

FUENTE = pygame.font.SysFont(data.FUENTE_1, 30, False, True)
FUENTE_CHICA = pygame.font.SysFont(data.FUENTE_1, 15, False, True)
COLORES = 1

def mostar_pantalla_ingresar_nombre(pantalla: object)->str:
    """Esta función recibe como parametro una pantalla (objeto) y pide el ingreso del nombre
    del jugador. Si es valido retorna el nombre"""

    sonido_nombre = pygame.mixer.Sound("sonidos\gano.mp3")  
    sonido_nombre.set_volume(0.4)
    sonido_nombre.play()

    imagen = pygame.image.load("imagenes\jugador_01.png")
    texto = "NAME:"
    texto_max = "(alphanumeric only, 2-10 characters)"
    texto_enter = "press enter to continue"
    nombre = ""

    input_rect = pygame.Rect((data.ANCHO_VENTANA/2 - 90), 130, 180, 50)#Rectangulo para piner nombre
    color = data.diccionario_set_up[COLORES]["ROSA_1"]

    flag_ingreso = True

    while flag_ingreso:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()                
            if event.type == pygame.KEYDOWN:
                #Si se apretar Enter y el nombre es valido, se sale del while
                if event.key == pygame.K_RETURN and funciones.validar_nombre(nombre): 
                    print(nombre)
                    flag_ingreso = False
                    return nombre
                elif event.key == pygame.K_RETURN and funciones.validar_nombre(nombre) == False:
                    nombre = "" #Si no es valido se borra
                elif event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1] #Borrar caracter 
                else:
                    nombre += event.unicode #Agregar carcter
               
        pantalla.fill(data.diccionario_set_up[COLORES]["NEGRO"])

        texto_1 = FUENTE.render(texto, True, color)
        texto_2 = FUENTE.render(nombre, True, color)
        texto_3 = FUENTE_CHICA.render(texto_max, True, color)
        texto_4 = FUENTE.render(texto_enter, True, color)
       
        pygame.draw.rect(pantalla, color, input_rect, 2)
        
        #Se muestran todos los textos e imagen en pantalla
        pantalla.blit(texto_1, ((data.ANCHO_VENTANA/2) - (texto_1.get_width()/2), 80))
        pantalla.blit(texto_2, ((data.ANCHO_VENTANA/2) - (texto_2.get_width()/2), 130))
        pantalla.blit(texto_3, ((data.ANCHO_VENTANA/2) - (texto_3.get_width()/2), 220))
        pantalla.blit(imagen, ((data.ANCHO_VENTANA/2) - (imagen.get_width()/2), 270))
        pantalla.blit(texto_4, ((data.ANCHO_VENTANA/2) - (texto_4.get_width()/2), 550))

        pygame.display.flip()

