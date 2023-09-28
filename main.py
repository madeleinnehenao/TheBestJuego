import sys
import pygame
from pygame.math import Vector2
from Manzana import Manzana
from Culebra import Culebra
import random

class Main:
    """    
    Clase donde se aloja la lógica del juego.
    Se encarga de realizar los dibujos con base en los métodos de las 
    clases Culebra y Manzana. Además de actualizar, manejar las colisiones,
    como se termina el juego y las restricciones de movimieno de la culebra
    """

    def __init__(self):
        self.culebra = Culebra()
        self.manzana = Manzana(numero_bloque)
        self.count=0
        self.aleatorio = 0


    def actualizar(self):
        """
        Esta función se encarga de actualizar los movimientos de la culebra,
        teniendo en cuenta la colision con la manzana, además de 
        las restricciones del tablero para la culebra"""
        self.culebra.mov_culebra()

        if self.count == self.aleatorio:
            self.manzana.visible = True
            self.generar_cont_ale()

        self.encuentro()
        self.restricciones_culebra(numero_bloque)

        if self.count == 10:
            self.count = 0 

    
    def dibujar_elementos(self, bloque_tamano:int, pantalla:object):
        """
        Esta función se encarga de dibujar la culebra y 
        la manzana en la pantalla

        args:
        numero_bloque: int. Cantidad de bloques que hay en la matriz.
        pantalla: object. Pantalla donde serán dibujados los elementos.
        """
        # Dibujar la manzana
        if self.manzana.visible:
            self.manzana.dibujar_manzana(bloque_tamano, pantalla)
        # Dibujar la culebra
        self.culebra.dibujar_culebra(bloque_tamano, pantalla)


    def encuentro(self):
        """Funcion que revisa si hay colisión entre la posición
        de la manzana y la cabeza de la culebra. Si esto ocurre
        aparece una nueva manzana y a la culebra crece en tamaño"""

        if self.manzana.pos == self.culebra.cuerpo[0]:
            self.manzana.visible = False
            self.culebra.agregar_bloque()
            self.manzana.aparecer(numero_bloque)
                
        # Se asegura que nunca aparezca una manzana en el cuerpo
        # de la culebra
        for bloque in self.culebra.cuerpo[1:]:
            if bloque == self.manzana.pos:
                self.manzana.visible = False
                self.manzana.aparecer(numero_bloque)

    def restricciones_culebra(self, numero_bloque):
        """
        Esta función se encarga de delimitar los movimientos de la
        culebra en la pantalla.

        args:
        numero_bloque: int. Cantidad de bloques que hay en la matriz.

        """
        # Revisa si la cabeza de la culebra se sale de la
        # pantalla en el límite izquierda o derecha, además de arriba
        # y abajo.
        if ( not 0 <= self.culebra.cuerpo[0].x < numero_bloque
            or not 0 <= self.culebra.cuerpo[0].y < numero_bloque ):
            self.juego_terminado()
        
        # Termina el juego cuando la cabeza de la culebra 
        # choca con su cuerpo
        for bloque in self.culebra.cuerpo[1:]:
            if bloque == self.culebra.cuerpo[0]:
                self.juego_terminado()

    def juego_terminado(self):
        self.culebra.reset()
    
    def generar_cont_ale(self):
        self.aleatorio = random.randint(0,10)
    
    #funcion para desaparecer la manzana

pygame.init()

# Matriz de tamaño
tamano_bloque = 30
numero_bloque = 13
# Surface de inicio
screen = pygame.display.set_mode((tamano_bloque * numero_bloque,
                                  tamano_bloque * numero_bloque))
# Que tan rápido corre el juego
clock = pygame.time.Clock()
main_game = Main()

# Actualizar el input de un jugador cada 150ms
ACTUALIZAR_SCREEN = pygame.USEREVENT
pygame.time.set_timer(ACTUALIZAR_SCREEN, 150)

while True:
     # dibujar todos los elementos
    for event in pygame.event.get():
        # Cerrar el juego
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # Mover la culebra automáticamente
        if event.type == ACTUALIZAR_SCREEN:
            main_game.actualizar()
        # Según el input, modificar dirección
        if event.type == pygame.KEYDOWN:
            # Hacia arriba
            if event.key == pygame.K_w:
                # Revisa que previamente la culebra no se
                # estuviera moviendo hacia abajo para
                # permitir el cambio de dirección hacia arriba
                if main_game.culebra.direccion.y != 1:
                    main_game.culebra.direccion = Vector2(0, -1)
                    main_game.count += 1
            # Hacia la izquierda
            if event.key == pygame.K_a:
                # Si la culebra está yendo hacia la derecha
                # que no pueda devolverse en ella misma
                if main_game.culebra.direccion.x != 1:
                    main_game.culebra.direccion = Vector2(-1, 0)
                    main_game.count += 1
                    
            # Hacia la derecha
            if event.key == pygame.K_d:
                # Si la culebra está yendo hacia la derecha
                # que no pueda devolverse en ella misma
                if main_game.culebra.direccion.x != -1:
                    main_game.culebra.direccion = Vector2(1, 0)
                    main_game.count += 1
            # Hacia abajo
            if event.key == pygame.K_s:
                # Revisa que previamente la culebra no se
                # estuviera moviendo hacia arriba para
                # permitir el cambio de dirección hacia abajo
                if main_game.culebra.direccion.y != -1:
                    main_game.culebra.direccion = Vector2(0, 1)
                    main_game.count += 1
    # Color del fondo
    screen.fill((175,215,70))
    # Dibujar la manzan y culebra
    main_game.dibujar_elementos(tamano_bloque, screen)
    print(main_game.count)
    print("Aleatorio: ", main_game.aleatorio)
    pygame.display.update()
    # 60 'fps'
    clock.tick(60)