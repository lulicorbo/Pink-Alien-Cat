import pygame
import clase_laser

#Clase Jugador
class Jugador:
    def __init__(self) -> None:
        imagen = pygame.image.load("imagenes\jugador_01.png")
        self.imagen = pygame.transform.scale(imagen, (100, 60))
        self.visible = True
        self.rect = self.imagen.get_rect()
        self.rect.x = 275
        self.rect.y = 580
        self.nombre = ""
    def update(self): #Movimiento del jugador con flechitas
        lista_teclas = pygame.key.get_pressed()
        
        if True in lista_teclas:
            if lista_teclas[pygame.K_RIGHT]:
                nueva_x = self.rect.x + 15
                if 0 < nueva_x < 500:
                    self.rect.x += 5
            elif lista_teclas[pygame.K_LEFT]:
                nueva_x = self.rect.x - 15
                if 0 < nueva_x < 500:
                    self.rect.x -= 5

    def crear_laser(self):
        laser = clase_laser.Laser(self.rect.centerx, self.rect.top, "arriba")
        return laser
 
