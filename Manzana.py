"""Modulo con todo lo referente a la clase Manzana"""
import random
import pygame
from pygame.math import Vector2

class Manzana:
    """
    Esta clase se encarga de dibujar la manzana en la pantalla, 
    además de desplazar la manzana a una posición aleatoria dentro
    de los límites de la pantalla

    Args:
    numero_bloque: int. Cantidad de bloques que hay en la matriz.
    """
    def __init__(self, numero_bloque: int):
        self.desplazar(numero_bloque)
        self.visible = False


    def dibujar_manzana(self, tamano_bloque:int,
                        pantalla:object) -> None:
        """
        Crea un rectángulo y dibuja el rectángulo en la pantalla
        simulando a una manzana.
        
        Args:
        tamano_bloque: Int. Es el tamaño que ocupará la manzana
        pantalla: Es un objeto de tipo surface, donde se dibujará
        la manzana
         
        Returns:
        None
        """
        manzana_rect = pygame.Rect(self.pos.x * tamano_bloque,
                                    self.pos.y * tamano_bloque,
                                    tamano_bloque, tamano_bloque)

        pygame.draw.rect(pantalla, (220, 0, 0), manzana_rect)

    # Generar posicion aleatoria
    def desplazar(self, numero_bloque: int) -> None:
        """
        Desplaza la manzana a una posición dentro de la matriz.
        
        Args:
        numero_bloque: int. Cantidad de bloques que hay en la matriz.

        Returns:
        None
        """
        self.x = random.randint(0, numero_bloque - 1)
        self.y = random.randint(0, numero_bloque - 1)
        self.pos = Vector2(self.x,self.y)


            

