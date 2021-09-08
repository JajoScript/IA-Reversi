# Dependencias.
import typing, pygame, sys
import numpy as np
from pygame.locals import *
from pygame.sprite import collide_rect

# Declaración de variables globales.
NUMERO_FILAS: int = 6;
NUMERO_COLUMNAS: int = 6;
ALTO_PANTALLA: int = 700;
ANCHO_PANTALLA: int = 600;
TAMAÑO_TABLERO: int = 440;

TAMAÑO_CELDA_ALTO: int = (TAMAÑO_TABLERO / NUMERO_FILAS);
TAMAÑO_CELDA_ANCHO: int = (TAMAÑO_TABLERO / NUMERO_COLUMNAS);

COLOR_CELDAS = (13, 171, 118);


# Definición del estado inicial del juego.
ESTADO_JUEGO = np.zeros((NUMERO_COLUMNAS, NUMERO_FILAS))

# 0 : Celda vacia.
# 1 : Celda Blanca.
# 2 : Celda Negra.

# Estado incial del juego:
ESTADO_JUEGO[2][2] = 1;
ESTADO_JUEGO[3][3] = 1;
ESTADO_JUEGO[3][2] = 2;
ESTADO_JUEGO[2][3] = 2;

print(ESTADO_JUEGO)

# Definición de funciones.
def controlador_tablero(ventana, blanca, negra) -> None:
	""" ... """

	# valores por defecto.
	posicion_x = 80
	posicion_y = 220

	# Ciclo para crear la hitbox del tablero.
	for fila in range(0, NUMERO_FILAS):
		posicion_x = 80;
		for columna in range(0, NUMERO_COLUMNAS):
		
			poligono = [   
				(posicion_x, posicion_y),
				(posicion_x + TAMAÑO_CELDA_ANCHO, posicion_y),
				(posicion_x + TAMAÑO_CELDA_ANCHO, posicion_y + TAMAÑO_CELDA_ALTO),
				(posicion_x, posicion_y + TAMAÑO_CELDA_ALTO)]


			# Construcción de los estados.
			# CASO: celda vacia.
			if ESTADO_JUEGO[fila][columna] == 0:
				pygame.draw.polygon(ventana, (255,255,255,255), poligono, 1); # Casilla vacia.

			# CASO: Ficha blanca.
			elif ESTADO_JUEGO[fila][columna] == 1:
				celda = pygame.draw.polygon(ventana, (255,255,255,255), poligono, 1);
				ventana.blit(blanca, ((posicion_x + 7), (posicion_y + 9)))

			# CASO: Ficha negra.
			elif ESTADO_JUEGO[fila][columna] == 2:
				celda = pygame.draw.polygon(ventana, (255,255,255,255), poligono, 1);
				ventana.blit(negra, ((posicion_x + 7), (posicion_y + 9)))

			# Iteración de las columnas.
			posicion_x += TAMAÑO_CELDA_ANCHO;

		# Iteración de las filas.
		posicion_y += TAMAÑO_CELDA_ALTO;

def cargador_assets(nombre_archivo: str, es_transparente: bool = False) -> typing.Any:
	""" ... """

	# Cargando la imagen solicitada.
	recurso = pygame.image.load(f"./src/assets/{nombre_archivo}");
	recurso = recurso.convert();

	# Habilitando la transparencia de fondo.
	if es_transparente:
		color = recurso.get_at((0,0))
		recurso.set_colorkey(color, RLEACCEL);
	
	return recurso

def controlador_coordenadas(posicion_mouse: list) -> list:
	""" ... """

	# 80, 220
	coordenada_X: int = -1;
	coordenada_Y: int = -1;
	
	# Definición de la posición en X.
	if (posicion_mouse[0] in range(80, 150)):
		coordenada_X: int = 0;

	elif(posicion_mouse[0] in range(150, 220)):
		coordenada_X: int = 1;

	elif(posicion_mouse[0] in range(220, 300)):
		coordenada_X: int = 2;

	elif(posicion_mouse[0] in range(300, 370)):
		coordenada_X: int = 3;
	
	elif(posicion_mouse[0] in range(370, 440)):
		coordenada_X: int = 4;
	
	else:
		coordenada_X: int = 5;
	
	# Definición de la posición en Y.
	if (posicion_mouse[1] in range(220, 290)):
		coordenada_Y: int = 0;

	elif(posicion_mouse[1] in range(290, 360)):
		coordenada_Y: int = 1;

	elif(posicion_mouse[1] in range(360, 440)):
		coordenada_Y: int = 2;

	elif(posicion_mouse[1] in range(440, 520)):
		coordenada_Y: int = 3;
	
	elif(posicion_mouse[1] in range(520, 580)):
		coordenada_Y: int = 4;
	
	else:
		coordenada_Y: int = 5;
	
	return list([coordenada_X, coordenada_Y])

def controlador_juego() -> None:
	""" ... """
	
	# Inicio de la ejecución de pygame.
	pygame.init()

	# Configuraciones de la ventana.
	ventana = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA));
	pygame.display.set_caption("REVERSI");
	icono = cargador_assets("icono.jpg");
	pygame.display.set_icon(icono);

	# Cargando los recursos del juego. 
	fondo_juego = cargador_assets("board.jpg");
	ficha_blanca = cargador_assets("ficha_j2.png", True);
	ficha_negra = cargador_assets("ficha_j1.png", True);

	# Control de fotogramas.
	FPS = pygame.time.Clock();
	FPS.tick(30);

	# Ciclo para correr el juego.
	while True:
		# Control de eventos.
		for evento in pygame.event.get():
			# Evento: salir del juego.
			if evento.type == QUIT:
				sys.exit(0);
			
			if evento.type == MOUSEBUTTONDOWN:
				posicion_mouse = pygame.mouse.get_pos();
				print(f"[DEV] posición: {posicion_mouse}");

				# Gestionador de las coordenadas del tablero.
				coordenadas_tablero = controlador_coordenadas(posicion_mouse);
				print(f"[DEV] coordenadas grid: {coordenadas_tablero}")

		# Posicionando los recursos en la ventana.
		ventana.blit(fondo_juego, (0,0));
		
		# Definición del tablero.
		controlador_tablero(ventana, ficha_blanca, ficha_negra);

		# Actualización de la ventana.
		pygame.display.flip();


def main() -> None:
	""" ... """

	# CALL: controlador_juego()
	controlador_juego();

	pass

# Inicio de las ejecuciones.
if __name__ == "__main__": 
	main();