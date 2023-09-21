"""Módulo con todo lo referente a la culebra"""
import pygame
from pygame.math import Vector2

class Culebra:
    """Clase con lo referente a dibujar la culebra"""
    def __init__(self):
        self.cuerpo = [ Vector2(5,10), Vector2(6, 10), Vector2(7, 10) ]
        self.direccion = Vector2(1,0)


    def dibujar_culebra(self, tamano_bloque:int,
                         pantalla:object) -> None:
        """Método con lo necesario para dibujar a la culebra

        args:
        tamano_bloque: Int. Es el tamaño que ocupará el bloque de
        culebra.
        pantalla: Es un objeto de tipo surface, donde se dibujará
        la culebra.

        returns.
        No hace un return específico, sólo dibuja la culebra
        """
        for bloque in self.cuerpo:
            # Crear un rectángulo
            bloque_rect = pygame.Rect(bloque.x * tamano_bloque,
                                      bloque.y * tamano_bloque,
                                      tamano_bloque, tamano_bloque)
            # Dibujar el rectángulo de la culebra
            pygame.draw.rect(pantalla, (183, 111, 121), bloque_rect)


    def mov_culebra(self) -> None:
        """Función que simula el movimiento de la culebra.

        A la cabeza de la culebra se le añade un vector 
        de posición, lo que simula el movimiento de la culebra.
        Después se hace una copia del cuerpo (sin tener en 
        cuenta la cola) y se añade a la cabeza.
        """
        # Copia del cuerpo sin la cola
        copia_cuerpo = self.cuerpo[:-1]
        # Se añade la cabeza al cuerpo, con su nueva dirección
        copia_cuerpo.insert(0, copia_cuerpo[0] + self.direccion)
        # Actualizar el cuerpo
        self.cuerpo = copia_cuerpo[:]
