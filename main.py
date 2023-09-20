import sys
import pygame
from Manzana import Manzana

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

while True:
     # dibujar todos los elementos
    for event in pygame.event.get():
        # Cerrar el juego
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((175,215,70))
    manzana.dibujar_manzana(tamano_bloque, screen)
    pygame.display.update()
    # 60 'fps'
    clock.tick(60)