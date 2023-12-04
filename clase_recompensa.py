import pygame
import random

class Recompensa:
    def __init__(self) -> None:
        imagen = pygame.image.load("imagenes\hrecompensa.png")
        self.imagen = pygame.transform.scale(imagen, (30, 30))
        self.rect = self.imagen.get_rect()
        self.rect.x = random.randint(10, 560)
        self.rect.y = random.randint(-1000, -100)
        self.movimiento_y = random.randint(3, 6)

        
        
    def update(self):
        self.rect.y += self.movimiento_y

