import sys
import pygame
from pygame.math import Vector2
from Manzana import Manzana
from Culebra import Culebra

class Main:
    def __init__(self):
        self.culebra = Culebra()
        self.manzana = Manzana(numero_bloque)


    def actualizar(self):
        self.culebra.mov_culebra()
        self.encuentro()

    
    def dibujar_elementos(self, bloque_tamano:int, pantalla:object):
        # Dibujar la manzana
        self.manzana.dibujar_manzana(bloque_tamano, pantalla)
        # Dibujar la culebra
        self.culebra.dibujar_culebra(bloque_tamano, pantalla)

    def encuentro(self):
        if self.manzana.pos == self.culebra.cuerpo[0]:
            self.manzana.aparecer(numero_bloque)
            self.culebra.agregar_bloque()

pygame.init()

# Matriz de tamaño
tamano_bloque = 30
numero_bloque = 20
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
                main_game.culebra.direccion = Vector2(0, -1)
            # Hacia la izquierda
            if event.key == pygame.K_a:
                main_game.culebra.direccion = Vector2(-1, 0)
            # Hacia la derecha
            if event.key == pygame.K_d:
                main_game.culebra.direccion = Vector2(1, 0)
            # Hacia abajo
            if event.key == pygame.K_s:
                main_game.culebra.direccion = Vector2(0, 1)
    # Color del fondo
    screen.fill((175,215,70))
    # Dibujar la manzan y culebra
    main_game.dibujar_elementos(tamano_bloque, screen)
    pygame.display.update()
    # 60 'fps'
    clock.tick(60)