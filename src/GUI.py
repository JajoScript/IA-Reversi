# -- Dependencias. -- 
import typing
import sys
import pygame
import numpy as np
# import time
from pygame.locals import *

# Local imports
from GAME import *
from CLASE import *
from IA import *

# -- Definición de variables globales. --
# Configuración para la ventana.
ALTO_PANTALLA:int = 700;
ANCHO_PANTALLA:int = 600;

# Configuración para el tablero.
TAMAÑO_TABLERO:int = 440;
NUMERO_FILAS:int = 6;
NUMERO_COLUMNAS:int = 6;

# Configuración de posicionamiento.
POSICION_X:int = 80;
POSICION_Y:int = 220;

# Recordatorio: Configurar este tipo de dato [Float | Int].
TAMAÑO_CELDA_ALTO:int = int((TAMAÑO_TABLERO / NUMERO_FILAS)); 
TAMAÑO_CELDA_ANCHO:int = int((TAMAÑO_TABLERO / NUMERO_COLUMNAS)); # 73px

COLOR_CELDAS:tuple = (13, 171, 118);
COLOR_VACIO:tuple = (255, 255, 255, 255);
COLOR_TEXTO:tuple = (24, 27, 28);

# Definición del estado inicial del juego.
# Tablero vacio.
ESTADO_JUEGO=np.zeros((6,6))

# [0] : Celda vacia.
# [1] : Celda Blanca.
# [2] : Celda Negra.

# Estado incial del juego:
ESTADO_JUEGO[2][2] = 1;
ESTADO_JUEGO[3][3] = 1;
ESTADO_JUEGO[3][2] = 2;
ESTADO_JUEGO[2][3] = 2;


# -- Definición de funciones. --
def controlador_tablero(ventana, ficha_blanca, ficha_negra) -> None:
	"""..."""

	# Ciclo para recorrer y actualizar el juego.
	POSICION_Y = 220;
	for fila in range(0, NUMERO_FILAS):
		# Reinicio de la variable.
		POSICION_X = 80;

		for columna in range(0, NUMERO_COLUMNAS):

			# Configurando las coordenadas de poligono.
			coordenadas_poligono = [
				((POSICION_X)								,(POSICION_Y)),
				((POSICION_X + TAMAÑO_CELDA_ANCHO)	,(POSICION_Y)),
				((POSICION_X + TAMAÑO_CELDA_ANCHO)	,(POSICION_Y + TAMAÑO_CELDA_ALTO)),
				((POSICION_X)								,(POSICION_Y + TAMAÑO_CELDA_ALTO))]

			# Construcción de los estados del tablero.
			# CASO 1 : celda vacia.
			if ESTADO_JUEGO[fila][columna] == 0:
				# pygame.draw.polygon(ventana, COLOR_VACIO, coordenadas_poligono, 1);
				pass

			# CASO 2 : celda con ficha blanca.
			elif ESTADO_JUEGO[fila][columna] == 1:
				# pygame.draw.polygon(ventana, COLOR_VACIO, coordenadas_poligono, 1);
				ventana.blit(ficha_blanca, ((POSICION_X + 7), (POSICION_Y + 9)));

			# CASO 3 : celda con ficha negra.
			elif ESTADO_JUEGO[fila][columna] == 2:
				# pygame.draw.polygon(ventana, COLOR_VACIO, coordenadas_poligono, 1);
				ventana.blit(ficha_negra, ((POSICION_X + 7), (POSICION_Y + 9)));

			# Iteración del posicionamiento en columnas.
			POSICION_X += TAMAÑO_CELDA_ANCHO;
		
		# Iteración del posicionamiento en filas.
		POSICION_Y += TAMAÑO_CELDA_ALTO;


def controlador_assets(nombre_archivo:str, es_transparente:bool = False) -> typing.Any:
	"""..."""

	# Cargando el recurso solicitado.
	recurso = pygame.image.load(f"./src/assets/{nombre_archivo}");
	recurso = recurso.convert();

	# Habilitando la transparencia de fondo.
	if es_transparente:
		color = recurso.get_at((0, 0));
		recurso.set_colorkey(color, RLEACCEL);
	
	return recurso
	

def controlador_coordenadas(posicion_mouse: list) -> list:
	"""..."""
	# posicion_mouse[0] = x
	# posicion_mouse[1] = y

	# Coordenadas por defecto.
	coordenadas_x:int = -1;
	coordenadas_y:int = -1;

	# Definición de posiciones en X.
	if (posicion_mouse[0] in range(80, 150)):
		coordenadas_x = 0;
	elif (posicion_mouse[0] in range(150, 220)):
		coordenadas_x = 1;
	elif (posicion_mouse[0] in range(220, 300)):
		coordenadas_x = 2;
	elif (posicion_mouse[0] in range(300, 370)):
		coordenadas_x = 3;
	elif (posicion_mouse[0] in range(370, 440)):
		coordenadas_x = 4;
	elif (posicion_mouse[0] in range(440, 520)):
		coordenadas_x = 5;
	elif (posicion_mouse[0] in range(0, 80)):
		coordenadas_x = -1;
	else:
		coordenadas_x = -1;

	# Definición de posiciones en Y.
	if (posicion_mouse[1] in range(220, 290)):
		coordenadas_y = 0;
	elif (posicion_mouse[1] in range(290, 360)):
		coordenadas_y = 1;
	elif (posicion_mouse[1] in range(360, 440)):
		coordenadas_y = 2;
	elif (posicion_mouse[1] in range(440, 510)):
		coordenadas_y = 3;
	elif (posicion_mouse[1] in range(510, 580)):
		coordenadas_y = 4;
	elif (posicion_mouse[1] in range(580, 660)):
		coordenadas_y = 5;
	elif (posicion_mouse[1] in range(0, 220)):
		coordenadas_y = -1;
	else:
		coordenadas_y = -1;

	# Recordatorio: Cambie las posiciones de las coordenadas. Atte: Nico.
	if (coordenadas_x == -1 or coordenadas_y == -1):
		# Coordenadas invalidas.
		return list([-1, -1])
	else:
		# Coordenadas validas.
		return list([coordenadas_y, coordenadas_x]);


def controlador_interfaz(juego) -> None:
	""" ... """
	
	# Inicio de la ejecución de pygame.
	pygame.init();
	pygame.font.init();

	# Configuraciones de la ventana.
	ventana = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA));
	pygame.display.set_caption("REVERSI");
	icono = controlador_assets("icono.jpg");
	pygame.display.set_icon(icono);

	# Cargando los recursos del juego. 
	fondo_juego = controlador_assets("board.jpg");
	ficha_blanca = controlador_assets("ficha_j2.png", True);
	ficha_negra = controlador_assets("ficha_j1.png", True);
	fuente_juego = pygame.font.Font('./src/assets/Roboto-Light.ttf', 20);

	# Control de fotogramas.
	FPS = pygame.time.Clock();
	FPS.tick(30);

	# Recordatorio: Esto aparentemente es temporal. atte: Nico.
	# Variables para el manejo de turnos.
	TURNO_BLANCA:bool = False;
	TURNO_NEGRA:bool = True;
	resultado=None

	# Ciclo para correr el juego.
	while True:
		# Posicionando los recursos en la ventana.
		ventana.blit(fondo_juego, (0,0));

		# Control de eventos.
		for evento in pygame.event.get():
			# Evento: salir del juego.
			if evento.type == QUIT:
				sys.exit(0);
			
			if evento.type == MOUSEBUTTONDOWN:
				posicion_mouse: list = pygame.mouse.get_pos();
				
				# Gestionador de las coordenadas del tablero.
				coordenadas_tablero = controlador_coordenadas(posicion_mouse);
	
				# Implementando la jugabilidad.	
				if juego.Identificador_fin_juego(ESTADO_JUEGO,2):
					if juego.Esta_vacia(coordenadas_tablero) and juego.Es_adyacente(coordenadas_tablero) and juego.Permite_salto_negra(coordenadas_tablero):
						ESTADO_JUEGO[coordenadas_tablero[0]][coordenadas_tablero[1]]=2
						estado=copy.deepcopy(ESTADO_JUEGO)
						if juego.Identificador_fin_juego(ESTADO_JUEGO,1):
							resultado= minimax(juego,estado,0,-1)
							coordenada_blanca=resultado[1]
							juego.Jugar(coordenada_blanca,1)
						else:
							print("[JUEGO TERMINADO]")
				else:
					print("[JUEGO TERMINADO]")

					

				"""
				if (controlador_tablero_lleno(ESTADO_JUEGO)) and (coordenadas_tablero[0] != -1) and (coordenadas_tablero[1] != -1):
					lista_turnos:list[bool] = controlador_turnos(ESTADO_JUEGO, coordenadas_tablero, TURNO_BLANCA, TURNO_NEGRA);

					# Turnos de cada ficha.
					TURNO_BLANCA = lista_turnos[0];
					TURNO_NEGRA = lista_turnos[1];

					# Renderizado del texto
					if (TURNO_NEGRA):
						texto_turnos = pygame.font.Font.render(fuente_juego, "Turno: Ficha negra", True, (0, 0, 255));

					elif (TURNO_BLANCA):
						texto_turnos = pygame.font.Font.render(fuente_juego, "Turno: Ficha blanca", True, (0, 0, 255));
					else:
						texto_turnos = pygame.font.Font.render(fuente_juego, "No quedan más turnos", True, (0, 0, 255));

					print(f"[DEV] posicion mouse: {posicion_mouse}")
					print(f"[DEV] coordenadas grid: {coordenadas_tablero}")

				elif (coordenadas_tablero[0] == -1) or (coordenadas_tablero[1] == -1):
					print("[DEV] movimiento fuera del tablero!");
					print(f"[DEV] posicion mouse: {posicion_mouse}")
					print(f"[DEV] coordenadas grid: {coordenadas_tablero}")
				
				else:
					texto_turnos = pygame.font.Font.render(fuente_juego, "No quedan más turnos", True, (0, 0, 255));
				"""
					
				
		# Renderizado de texto: Turno de las fichas.
		if (TURNO_NEGRA):
			texto_turnos = pygame.font.Font.render(fuente_juego, "Turno: Ficha negra", True, COLOR_TEXTO);
	
		elif (TURNO_BLANCA):
			texto_turnos = pygame.font.Font.render(fuente_juego, "Turno: Ficha blanca", True, COLOR_TEXTO);

		ventana.blit(texto_turnos, dest=(220, 668));

		# Definición del tablero.
		controlador_tablero(ventana, ficha_blanca, ficha_negra);

		# Actualización de la ventana.
		pygame.display.flip();
