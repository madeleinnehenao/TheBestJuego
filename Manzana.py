import pygame
import random
from pygame.math import Vector2

class Manzana:
    def __init__(self, numero_bloque: int):
        """ Genera aleatoriamente una manzana
        args:
        numero_bloque:Int. Cantidad de bloques que hay en la 
        matriz."""
        # la resta asegura que siempre estemos en la pantalla
        self.x = random.randint(0, numero_bloque - 1)
        self.y = random.randint(0, numero_bloque - 1)
        self.pos = Vector2(self.x,self.y)

    def dibujar_manzana(self, tamano_bloque:int, pantalla:object):
        """Crea un rectángulo y dibuja el 
        rectángulo en la pantalla
        
        args:
        tamano_bloque: Int. Es el tamaño que ocupará la manzana
        pantalla: Es un objeto de tipo surface, donde se dibujará
        la manzana
         
        returns:
        No hace un return específico, sólo dibuja la manzana """

        manzana_rect = pygame.Rect(self.pos.x * tamano_bloque,
                                   self.pos.y * tamano_bloque,
                                   tamano_bloque, tamano_bloque)

        pygame.draw.rect(pantalla, (126,166, 114), manzana_rect)