#!/usr/bin/env python
# -*- codigon: utf-8 -*-
# Dependencias.
import typing
import sys, pygame
from pygame import color
from pygame.locals import *

# Variables globales.
alto: int = 700;
ancho: int = 600;

# Colores.
color_ficha_1 = pygame.Color(24, 27, 28)     # Ficha negra.
color_ficha_2 = pygame.Color(255, 255, 255)  # Ficha blanca.
color_tablero = pygame.Color(13, 171, 118)   # Tablero

# Tablero: Coordenadas.

tablero_coordenadas = [
	[(86, 228), (0,0), (0,0), (0,0), (0,0), (0,0)],
	[(0,0), (0,0), (0,0), (0,0), (0,0), (0,0)],
	[(0,0), (0,0), (0,0), (0,0), (0,0), (0,0)],
	[(0,0), (0,0), (0,0), (0,0), (0,0), (0,0)],
   [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0)],
	[(0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
];

# Definiciones de entidades.
class Ficha(pygame.sprite.Sprite):
	# Propiedades.
	# Constructor.
	def __init__(self, ID_jugador: str) -> None:
		# Super constructor.
		super().__init__();
		
		# Cargando la imagen de la ficha.
		self.image = pygame.image.load(f"./assets/ficha_j{ID_jugador}.png")


	# Metodos.
	# Getters & Setters.
	# Destructor.
	pass

class Tablero():
	# Propiedades.
	# Constructor.
	# Metodos.
	# Getters & Setters.
	# Destructor.
	pass

# Funciones.
def cargarAssets(nombre_archivo: str, transparencia: bool = False) -> typing.Any:
	imagen = pygame.image.load(f"./src/assets/{nombre_archivo}");
	imagen = imagen.convert()
	
	# Habilitando la transparencia del fondo.
	if transparencia:
		color = imagen.get_at((0,0))
		imagen.set_colorkey(color, RLEACCEL)
	
	return imagen


def mostrarVentana() -> None:
	# Creación de la ventana del juego.
	ventana = pygame.display.set_mode((ancho, alto));

	# Configuración: Titulo de la ventana.
	pygame.display.set_caption("Reversi game!");

	# Cargando el fondo del juego.
	juego_fondo = cargarAssets('board.jpg', transparencia=False);

	# Cargar fichas :EJEMPLO
	ficha_j1 = cargarAssets("ficha_j1.png", transparencia=True);
	# ficha_j2 = cargarAssets("ficha_j2.png", transparencia=True);

	# Control de fotogramas.
	FPS = pygame.time.Clock()
	FPS.tick(60)

	# Ciclo para mostrar constante mente la ventana del juego.
	while True:
		# Control de eventos.
		for evento in pygame.event.get():
			# Evento: Salir del juego.
			if evento.type == QUIT:
				sys.exit(0);

			print(evento)

		# Posicionando la imagen.
		ventana.blit(juego_fondo, (0,0));

		# Cargando el tablero.

		ventana.blit(ficha_j1, tablero_coordenadas[0][0]);
		# ventana.blit(ficha_j2, (114, 260));

		# Ficha_1 = pygame.draw.circle(ventana, color_ficha_1, (114, 260), 25);
		# Ficha_1 = pygame.draw.circle(ventana, color_ficha_1, (180, 260), 25);
		
		

		# pygame.display.flip();

		# Actualización de la ventana.
		pygame.display.update();


def main() -> None:
	# Iniciando el juego.
	pygame.init();

	# Función para mostrar la ventana del juego.
	mostrarVentana();

	# Finalización del juego.
	return 0;

# Inicio de ejecución.
if __name__ == "__main__":
	main();