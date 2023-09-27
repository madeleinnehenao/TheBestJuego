import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la ventana
size = (700, 500)
screen = pygame.display.set_mode(size)

# Configurar la fuente y el color
font_big = pygame.font.Font(None, 72)
font_small = pygame.font.Font(None, 24)
color = (255, 0, 255)  # RGB para morado

# Crear los textos
text_big = font_big.render("PLAY GAME", True, color)
text_small = font_small.render("Para jugar utiliza las teclas W-A-S-D", True, color)

# Obtener las posiciones centradas para los textos
position_big = text_big.get_rect(center=(size[0]/2, size[1]/2 - 50))
position_small = text_small.get_rect(center=(size[0]/2, size[1]/2 + 50))

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Rellenar la pantalla con negro
    screen.fill((0, 0, 0))

    # Dibujar los textos
    screen.blit(text_big, position_big)
    screen.blit(text_small, position_small)

    # Actualizar la pantalla
    pygame.display.flip()
