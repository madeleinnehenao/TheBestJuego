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
    como se termina el juego y las restricciones de movimieno de la culebra.

    También realiza el manejo de pantallas de introducción y del juego principal.
    """

    def __init__(self):
        self.culebra = Culebra()
        self.manzana = Manzana(numero_bloque)
        self.count = 0
        self.aleatorio = 0
        self.estado = "intro"


    def actualizar(self):
        """
        Actualiza los movimientos de la culebra en el juego, considerando colisiones con la manzana
        y restricciones del tablero.

        Esta función se llama en el bucle principal del juego para actualizar el movimiento de la culebra.
        Realiza las siguientes acciones:
        - Llama a la función 'mov_culebra()' para actualizar la posición de la culebra.
        - Comprueba si el contador 'count' es igual al valor aleatorio 'aleatorio'. Si es así, muestra
        la manzana en el juego y genera un nuevo valor aleatorio llamando a 'generar_cont_ale()'.
        - Llama a la función 'encuentro()' para verificar si la culebra ha colisionado con la manzana y
        tomar las acciones correspondientes, como hacer crecer la culebra y generar una nueva posición
        para la manzana.
        - Aplica restricciones al movimiento de la culebra para asegurarse de que no salga del tablero
        llamando a 'restricciones_culebra(numero_bloque)'.
        - Si el contador 'count' alcanza el valor 10, se reinicia a 0.

        Returns:
            None
        """
        
        self.culebra.mov_culebra()

        if self.count == self.aleatorio:
            self.manzana.visible = True
            self.generar_cont_ale()

        self.encuentro()
        self.restricciones_culebra(numero_bloque)

        if self.count == 10:
            self.count = 0


    def dibujar_elementos(self, bloque_tamano:int, pantalla:object) -> None:
        """
        Esta función se encarga de dibujar la culebra y 
        la manzana en la pantalla

        Args:
        numero_bloque: int. Cantidad de bloques que hay en la matriz.
        pantalla: object. Pantalla donde serán dibujados los elementos.

        Returns:
        None
        """
        # Dibujar la manzana sólo si cumple las condiciones
        if self.manzana.visible:
            self.manzana.dibujar_manzana(bloque_tamano, pantalla)
        # Dibujar la culebra
        self.culebra.dibujar_culebra(bloque_tamano, pantalla)


    def encuentro(self):
        """
        Función que verifica si hay una colisión entre la posición de la manzana y la cabeza de la culebra.
        Si hay una colisión, se "genera" una nueva manzana y la culebra crece en tamaño.

        Esta función se llama en el bucle principal del juego para verificar si la cabeza de la culebra
        ha alcanzado la posición de la manzana. Si la colisión ocurre, se realiza lo siguiente:
        - La manzana actual se vuelve invisible (se desaparece).
        - La culebra crece en tamaño llamando a la función 'agregar_bloque()' de la culebra.
        - Se genera una nueva posición para la manzana utilizando la función 'desplazar()' de la manzana.

        Además, la función se asegura de que no aparezca una manzana en el cuerpo de la culebra.
        Si la posición de la manzana coincide con alguna posición en el cuerpo de la culebra (excepto la cabeza),
        la manzana se vuelve invisible y se genera una nueva posición para evitar la colisión.

        Returns:
            None

        """

        if self.manzana.pos == self.culebra.cuerpo[0]:
            # Desaparece la manzana
            self.manzana.visible = False
            self.culebra.agregar_bloque()
            # Crece la culebra
            self.manzana.desplazar(numero_bloque)
                
        # Se asegura que nunca aparezca una manzana en el cuerpo
        # de la culebra
        for bloque in self.culebra.cuerpo[1:]:
            if bloque == self.manzana.pos:
                self.manzana.visible = False
                self.manzana.desplazar(numero_bloque)


    def restricciones_culebra(self, numero_bloque) -> None:
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
                

    def juego_terminado(self) -> None:
        """
        Función encargada de reposicionar a la culebra en el punto inicial.
        Da la ilusión de que el juego se terminó

        """
        self.culebra.reset()


    def generar_cont_ale(self) -> None:
        """
        Genera un número aleatorio.

        Se usa para comparar que la manzana salga en una
        cantidad aleatoria de movimientos de la culebra.

        """
        self.aleatorio = random.randint(1,10)


    def intro(self, tamano_bloque, numero_bloque) -> None:
        """
        Pantalla de inicio del juego.

        Esta función representa la pantalla inicial del juego, que se muestra en el bucle
        principal del juego. Muestra el título del juego, instrucciones para jugar y espera
        a que el jugador presione la tecla Enter para comenzar a jugar.

        Args:
            tamano_bloque (int): El tamaño de un bloque en píxeles.
            numero_bloque (int): El número de bloques en el tablero.

        Returns:
            None

        En esta función, se realiza lo siguiente:
        - Se crea una ventana con un título, basada en el tamaño de bloque y el número de bloques.
        - Se configuran las fuentes y colores utilizados para el texto.
        - Se crea el texto del título "LA CULEBRITA", las instrucciones y el mensaje de
        "PRESIONE ENTER PARA JUGAR" utilizando las fuentes y colores definidos.
        - Se calculan las posiciones centradas para los textos en la pantalla.
        - Se verifica si se ha recibido un evento de cierre de la ventana (pygame.QUIT) o si
        se ha presionado la tecla Enter (pygame.K_RETURN) para cambiar el estado del juego
        a "main_game".

        Si el estado del juego es "intro", se realiza lo siguiente:
        - Se llena la pantalla con un color negro (RGB: 0, 0, 0).
        - Se dibujan los textos en la pantalla en las posiciones calculadas.
        - Se actualiza la pantalla con los cambios realizados.

        La función no devuelve ningún valor, ya que su objetivo es mostrar la pantalla de
        inicio y cambiar el estado del juego cuando el jugador presiona Enter.

        """
        size = [tamano_bloque * numero_bloque,
                tamano_bloque * numero_bloque]
                # Configurar la fuente y el color
        font_big = pygame.font.Font(None, 72)
        font_small = pygame.font.Font(None, 24)
        color = (255, 0, 255)  # RGB para morado

        # Crear los textos
        text_big = font_big.render("LA CULEBRITA", True, color)
        text_small = font_small.render("Para jugar utiliza las teclas W-A-S-D", True, color)
        text_enter = font_small.render("PRESIONE ENTER PARA JUGAR", True, color)

        # Obtener las posiciones centradas para los textos
        position_big = text_big.get_rect(center=(size[0] / 2, size[1] / 2 - 50))
        position_small = text_small.get_rect(center=(size[0] / 2, size[1] / 2 + 50))
        position_enter = text_enter.get_rect(center=(size[0] / 2, size[1] / 2 + 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Se presionó Enter
                    self.estado = "main_game"

            if self.estado == "intro":
                # Rellenar la pantalla con negro
                screen.fill((0, 0, 0))

                # Dibujar los textos
                screen.blit(text_big, position_big)
                screen.blit(text_small, position_small)
                screen.blit(text_enter, position_enter)

                # Actualizar la pantalla
                pygame.display.flip()


    def main_game_screen(self) -> None:
        """
        Dibuja todos los elementos del juego en la pantalla.

        
        Esta función se encarga de dibujar todos los elementos del juego en la pantalla,
        incluyendo la culebra y la manzana. También maneja eventos de cierre
        de la ventana y eventos de teclado para cambiar la dirección de la culebra.

        - Si el estado del juego es "main_game", se realiza lo siguiente:
        - Se verifica si se ha recibido un evento de cierre de la ventana (pygame.QUIT),
            en cuyo caso se cierra el juego.
        - Si se recibe un evento personalizado ACTUALIZAR_SCREEN, se llama a la función
            'actualizar()' del juego principal y se incrementa el contador 'count'.
        - Si se recibe un evento de teclado (pygame.KEYDOWN), se verifica qué tecla se ha
            presionado y se cambia la dirección de la culebra según la tecla:
            - Tecla 'W' (pygame.K_w): Mueve la culebra hacia arriba, si no se estaba moviendo
            hacia abajo previamente.
            - Tecla 'A' (pygame.K_a): Mueve la culebra hacia la izquierda, si no se estaba
            moviendo hacia la derecha previamente.
            - Tecla 'D' (pygame.K_d): Mueve la culebra hacia la derecha, si no se estaba
            moviendo hacia la izquierda previamente.
            - Tecla 'S' (pygame.K_s): Mueve la culebra hacia abajo, si no se estaba moviendo
            hacia arriba previamente.

        - Luego, se llena la pantalla con un color de fondo (RGB: 255, 250, 205).
        - Se dibujan los elementos del juego llamando a la función 'dibujar_elementos()' del
        juego principal (main_game).
        - Se imprime en la consola el valor del contador 'count' y el valor aleatorio generado.

        Finalmente, se actualiza la pantalla con los cambios realizados. 
        
        """
        # dibujar todos los elementos
        if self.estado == "main_game":
            for event in pygame.event.get():
                # Cerrar el juego
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                # Mover la culebra automáticamente
                if event.type == ACTUALIZAR_SCREEN:
                    main_game.actualizar()
                    main_game.count += 1
                # Según el input, modificar dirección
                if event.type == pygame.KEYDOWN:
                    # Hacia arriba
                    if event.key == pygame.K_w:
                        # Revisa que previamente la culebra no se
                        # estuviera moviendo hacia abajo para
                        # permitir el cambio de dirección hacia arriba
                        if main_game.culebra.direccion.y != 1:
                            main_game.culebra.direccion = Vector2(0, -1)
                    # Hacia la izquierda
                    if event.key == pygame.K_a:
                        # Si la culebra está yendo hacia la derecha
                        # que no pueda devolverse en ella misma
                        if main_game.culebra.direccion.x != 1:
                            main_game.culebra.direccion = Vector2(-1, 0)
                            
                    # Hacia la derecha
                    if event.key == pygame.K_d:
                        # Si la culebra está yendo hacia la derecha
                        # que no pueda devolverse en ella misma
                        if main_game.culebra.direccion.x != -1:
                            main_game.culebra.direccion = Vector2(1, 0)
                    # Hacia abajo
                    if event.key == pygame.K_s:
                        # Revisa que previamente la culebra no se
                        # estuviera moviendo hacia arriba para
                        # permitir el cambio de dirección hacia abajo
                        if main_game.culebra.direccion.y != -1:
                            main_game.culebra.direccion = Vector2(0, 1)
            # Color del fondo
            screen.fill((255, 250, 205))
            # Dibujar la manzan y culebra
            main_game.dibujar_elementos(tamano_bloque, screen)
    
            pygame.display.update()
    

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
    if main_game.estado == "intro":
        main_game.intro(tamano_bloque, numero_bloque)
    elif main_game.estado == "main_game":
        main_game.main_game_screen()
    # 60 'fps'
    clock.tick(60)
