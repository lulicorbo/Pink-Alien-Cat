import pygame
import random

class Meteorito:
    def __init__(self) -> None:
        imagen = pygame.image.load("imagenes\meteorito.png")
        self.imagen = pygame.transform.scale(imagen, (30, 70))
        self.rect = self.imagen.get_rect()
        self.rect.x = random.randint(10, 560)
        self.rect.y = random.randint(-1000, -100)
        self.movimiento_y = random.randint(3, 10)

        
        
    def update(self):
        self.rect.y += self.movimiento_y

