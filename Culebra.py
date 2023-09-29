"""Módulo con todo lo referente a la culebra"""
import pygame
from pygame.math import Vector2

class Culebra:
    """
    Clase con lo referente a dibujar la culebra
    
    """
    def __init__(self):
        self.cuerpo = [ Vector2(5,10), Vector2(4, 10), Vector2(3, 10) ]
        self.direccion = Vector2(1,0)
        self.nuevo_bloque = False


    def dibujar_culebra(self, tamano_bloque:int,
                         pantalla:object) -> None:
        """
        Dibuja la culebra en la pantalla utilizando bloques del tamaño especificado.    

        Esta función se encarga de dibujar la culebra en la pantalla utilizando bloques rectangulares.
        Recorre los segmentos del cuerpo de la culebra y dibuja cada bloque en la posición correspondiente
        en la superficie de la pantalla. Además, resalta la cabeza de la culebra con un color diferente
        para indicar su posición.

        Args:
            - tamano_bloque (int): El tamaño en píxeles que ocupará cada bloque de la culebra.
            - pantalla (pygame.Surface): La superficie de la pantalla en la que se dibujará la culebra.

        Returns:
            None

        """
        for bloque in self.cuerpo:
            # Crear un rectángulo

            bloque_rect = pygame.Rect(bloque.x * tamano_bloque,
                                      bloque.y * tamano_bloque,
                                      tamano_bloque, tamano_bloque)
            # Dibujar el rectángulo de la culebra
            pygame.draw.rect(pantalla, (204, 102, 0), bloque_rect)
            if bloque == self.cuerpo[0]:
                pygame.draw.rect(pantalla, (255, 255, 0), bloque_rect)


    def mov_culebra(self) -> None:
        """
        Simula el movimiento de la culebra en el juego.

        Esta función se encarga de simular el movimiento de la culebra en el juego.
        La cabeza de la culebra se desplaza en la dirección especificada por el atributo
        'direccion'. Para lograr esto, se realiza una copia del cuerpo de la culebra
        (sin tener en cuenta la cola) y se ajusta la posición de la cabeza de acuerdo a
        la nueva dirección. Luego, se actualiza el cuerpo de la culebra con la nueva posición.

        Si se debe agregar un nuevo bloque a la culebra (por haber comido una manzana),
        se duplica la última posición del cuerpo (cola) y se agrega antes de la cabeza
        para que la culebra crezca en tamaño.

        Returns:
            None

        Detalles:
        - Si 'nuevo_bloque' es True (indicando que se debe agregar un nuevo bloque),
          la función realiza lo siguiente:
        - Hace una copia del cuerpo de la culebra.
        - Calcula la posición de la nueva cola duplicando la posición de la cola actual y
            restando la posición del segmento anterior. Esto asegura que la
            culebra crezca por la cola.
        - Agrega la nueva cola al final del cuerpo de la culebra.
        - Actualiza el cuerpo de la culebra con la nueva configuración.
        - Establece 'nuevo_bloque' en False para evitar que la culebra crezca indefinidamente.

        - Si 'nuevo_bloque' es False (indicando que no se debe agregar un nuevo bloque),
          la función realiza lo siguiente:
        - Calcula la nueva posición de la cabeza de la culebra sumando la
          dirección actual a la posición actual de la cabeza.
        - Mueve cada segmento del cuerpo hacia el segmento delante de él,
          asegurando que la culebra siga la cabeza.
        - Asigna la nueva posición a la cabeza de la culebra.

        La función se llama en cada iteración del bucle principal del juego
        para mantener actualizada la posición de la culebra y lograr el efecto
        de movimiento en el juego.
        """
        if self.nuevo_bloque:
            # Copia del cuerpo 
            copia_cuerpo = self.cuerpo[:]
            # Duplicar la cola y agregarla al final
            nueva_cola = 2 * self.cuerpo[-1] - self.cuerpo[-2]
            copia_cuerpo.append(nueva_cola)
            # Actualizar el cuerpo
            self.cuerpo = copia_cuerpo[:]
            # Sin esto, la culebra crece indefinidamente
            self.nuevo_bloque = False
        else:
            nueva_cabeza = self.cuerpo[0] + self.direccion
            # Mover cada segmento del cuerpo hacia el segmento delante de él
            for i in range(len(self.cuerpo) - 1, 0, -1):
                self.cuerpo[i] = self.cuerpo[i - 1]  # Mueve el segmento al segmento delante de él
            # Asignar la nueva posición a la cabeza
            self.cuerpo[0] = nueva_cabeza
            

    def agregar_bloque(self) -> None:
        """
        Funcion para cambiar el estado de nuevo bloque. De manera
        automática es falso, cuando se quiera agregar el bloque, el estado
        de nuevo bloque cambiar a veradero, afectando la función mov_culebra.
        
        Returns:
        None
        
        """
        self.nuevo_bloque = True

    def reset(self):
        """
        Función para reposicionar a la culebra, reiniciando su dirección.
        
        Returns:
        None
        """
        
        self.cuerpo = [ Vector2(5,10), Vector2(4, 10), Vector2(3, 10) ]
        self.direccion = Vector2(0,0)

