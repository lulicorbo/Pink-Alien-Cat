import pygame
import random

#Clase enemigo
class Enemigo:
    def __init__(self, ancho, alto, tiempo_entre_disparos = 20) -> None:
        self.ancho = ancho
        self.alto = alto
        imagen = pygame.image.load("imagenes/imagen_nave_enemiga00.png")
        self.imagen = pygame.transform.scale(imagen, (ancho, alto))
        self.rect = self.imagen.get_rect()
        self.rect.x = random.randint(0, 600 - ancho)
        self.rect.y = random.randint(0, 450 - alto)
        self.movimiento_x = random.randint(-10, 10) #Movimientos aleatorios de enemigos
        self.movimiento_y = random.randint(-10, 10)
        self.tiempo_entre_disparos = tiempo_entre_disparos
        self.visible = True
        self.vida = 1
        self.explosion = [pygame.image.load("Imagenes\exp_1.png"),
            pygame.image.load("Imagenes\exp_2.png"),
            pygame.image.load("Imagenes\exp_3.png"),
            pygame.image.load("Imagenes\exp_4.png"),
            pygame.image.load("Imagenes\exp_5.png"),
            pygame.image.load("Imagenes\exp_6.png")]
        self.indice_imagen_explosion = 0
          
    def update(self, pantalla):  
        if self.movimiento_x == 0: #Para evitar mov vertical
            self.movimiento_x += 1
        elif self.movimiento_y == 0: #para evitar mov horizontal
            self.movimiento_y += 1
        self.rect.x += self.movimiento_x
        self.rect.y += self.movimiento_y

        self.tiempo_entre_disparos -= 1

        if self.rect.x > (600 - self.ancho) or self.rect.x < 0: #Para que no salga de los margenes de pantalla horizontalemnte
            self.movimiento_x = -self.movimiento_x
        if self.rect.y > 450 or self.rect.y < 0:  #Para que llegue hasta  y = 450 y no entre enzona del jugador
            self.movimiento_y = -self.movimiento_y

    def animacion(self): #Pasa la secuencia de imagenes de la lista explosion
        self.imagen = self.explosion[self.indice_imagen_explosion]
        if self.indice_imagen_explosion < (len(self.explosion) - 1):
            self.indice_imagen_explosion += 1


    