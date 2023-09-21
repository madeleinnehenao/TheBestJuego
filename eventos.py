import sys
import pygame
from pygame.math import Vector2
from Manzana import Manzana
from Culebra import Culebra

pygame.init()

# Matriz de tamaño
tamano_bloque = 30
numero_bloque = 20
# Surface de inicio
screen = pygame.display.set_mode((tamano_bloque * numero_bloque,
                                  tamano_bloque * numero_bloque))
# Que tan rápido corre el juego
clock = pygame.time.Clock()
# Inicializo la manzana con los numeros de bloques
manzana = Manzana(numero_bloque)
# Inicializo a la culebra 
culebra = Culebra()

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
            culebra.mov_culebra()
        # Según el input, modificar dirección
        if event.type == pygame.KEYDOWN:
            # Hacia arriba
            if event.key == pygame.K_w:
                culebra.direccion = Vector2(0, -1)
            # Hacia la izquierda
            if event.key == pygame.K_a:
                culebra.direccion = Vector2(-1, 0)
            # Hacia la derecha
            if event.key == pygame.K_d:
                culebra.direccion = Vector2(1, 0)
            # Hacia abajo
            if event.key == pygame.K_s:
                culebra.direccion = Vector2(0, 1)
    # Color del fondo
    screen.fill((175,215,70))
    # Dibujar la manzana
    manzana.dibujar_manzana(tamano_bloque, screen)
    # Dibujar la culebra
    culebra.dibujar_culebra(tamano_bloque, screen)
    # Actualizando constantemente la pantalla
    pygame.display.update()
    # 60 'fps'
    clock.tick(60)