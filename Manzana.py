"""Modulo con todo lo referente a la clase Manzana"""
import random
import pygame
from pygame.math import Vector2

class Manzana(pygame.sprite.Sprite):
    def __init__(self, numero_bloque: int):
        pygame.sprite.Sprite.__init__(self)
        self.aparecer(numero_bloque)
        self.visible = False


    def dibujar_manzana(self, tamano_bloque:int,
                        pantalla:object) ->None:
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

        pygame.draw.rect(pantalla, (220, 0, 0), manzana_rect)

    # Generar posicion aleatoria
    def aparecer(self, numero_bloque: int):
        """Crea una posición aleatoria dentro de la matriz,
        en la cual aparecerá la manzana
        
        args:
        numero_bloque: int. Cantidad de bloques que hay en la matriz."""
        self.x = random.randint(0, numero_bloque - 1)
        self.y = random.randint(0, numero_bloque - 1)
        self.pos = Vector2(self.x,self.y)

            

