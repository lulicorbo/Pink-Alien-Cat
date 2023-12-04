import pygame
#Clase Laser
#Misma clase para lasers del jugadr y enemigos. Se pasa por parametro la dirección que indica que tipo son.
class Laser:
    def __init__(self, x, y, direccion, ancho=10, alto=20,) -> None:
        self.ancho = ancho
        self.alto = alto
        self.direccion = direccion
        if direccion == "arriba": #Laser jugador
            self.mov_y = -10 
            imagen = pygame.image.load("imagenes/imagen_laser_rosa.png")

        if direccion == "abajo": #Laser enemigo
            self.mov_y = 10
            imagen = pygame.image.load("imagenes/imagen_laser_azul.png")

        self.imagen = pygame.transform.scale(imagen, (ancho, alto))
        self.rect = self.imagen.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def update(self): #Actualiza mov
        self.rect.y += self.mov_y
