# -- Dependencias. -- 
import typing
import sys
import pygame
import time
import random as rd
from pygame.locals import *

# Local imports
from IA import*
from GAME import *

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
ESTADO_JUEGO= [
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0]];

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
				pass

			# CASO 2 : celda con ficha blanca.
			elif ESTADO_JUEGO[fila][columna] == 1:
				ventana.blit(ficha_blanca, ((POSICION_X + 7), (POSICION_Y + 9)));

			# CASO 3 : celda con ficha negra.
			elif ESTADO_JUEGO[fila][columna] == 2:
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
	fondo_juego = controlador_assets("background-facil.jpg");
	ficha_blanca = controlador_assets("ficha_j2.png", True);
	ficha_negra = controlador_assets("ficha_j1.png", True);
	fuente_juego = pygame.font.Font('./src/assets/Roboto-Light.ttf', 20);

	# Control de fotogramas.
	FPS = pygame.time.Clock();
	FPS.tick(30);

	# Variables para el manejo del juego

	TURNO_BLANCA:bool = False; 
	TURNO_NEGRA:bool = True;
	FIN_DE_JUEGO:bool=False;	#Indica si se completo el tablero o ya no hay mas jugadas posibles
	BLANCAS:int=0;				#nº de fichas blancas en el tablero
	NEGRAS:int=0;				#nº de fichas negras en el tablero
	GANADOR:str=None; 			#Indica que jugador tiene mas fichas de su color en el tablero
	PERMISO:list=False; 		#Indica si ya se eligio la dificultad, si eso ocurre entonces el jugador puede empezar
	TIEMPO:float=0; 			#El tiempo que tarda el minimax o el alfabeta en devolver una respuesta
	LISTA:list=[]; 				#Lista de jugadas que realiza el minimax o el alfabeta, sirve para ver los nodos que explora
	PISTA=None; 				#Coordenada que puede jugar el usuario

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

				#ELIGIENDO DIFICULTAD
				if 55<=posicion_mouse[0]<=105 and 85<=posicion_mouse[1]<=100 and not PERMISO:
					juego.dificultad=2 #USA MINIMAX
					PERMISO=True

				elif 115<=posicion_mouse[0]<=170 and 85<=posicion_mouse[1]<=100 and not PERMISO:
					fondo_juego = controlador_assets("background-medio.jpg");
					juego.dificultad=2 #USA ALFABETA
					PERMISO=True
					
				elif 175<=posicion_mouse[0]<=225 and 85<=posicion_mouse[1]<=100 and not PERMISO:
					fondo_juego = controlador_assets("background-dificil.jpg");
					juego.dificultad=6  #USA ALFABETA
					PERMISO=True

				#REINICIANDO
				if 240<=posicion_mouse[0]<=390 and 75<=posicion_mouse[1]<=105:
					PERMISO=False
					juego.Resetear_tablero()
					LISTA=[]
					TIEMPO=0
					TURNO_NEGRA=True
					TURNO_BLANCA=False

				#PISTAS
				if 245 <= posicion_mouse[0] <= 395 and 40<=posicion_mouse[1]<=70:
					pistas= juego.Generador_Jugadas_validas(2)
					limite= len(pistas)
					if len(pistas)!=0:
						pista = rd.randint(0,limite-1)
						#traducir
						pistas[pista][0]=pistas[pista][0]+1
						if pistas[pista][1]==0:
							pistas[pista][1]="A"
						if pistas[pista][1]==1:
							pistas[pista][1]="B"
						if pistas[pista][1]==2:
							pistas[pista][1]="C"
						if pistas[pista][1]==3:
							pistas[pista][1]="D"
						if pistas[pista][1]==4:
							pistas[pista][1]="E"
						if pistas[pista][1]==5:
							pistas[pista][1]="F"
						PISTA=pistas[pista]
					

					
				#si ya eligio la dificultad la variable PERMISO se vuelve true
				if PERMISO:
					coordenadas_tablero = controlador_coordenadas(posicion_mouse);
					#Si el turno es de las negras y la jugada es valida
					if TURNO_NEGRA and juego.Jugar(coordenadas_tablero,2):
						TURNO_NEGRA=False
						TURNO_BLANCA=True

						#generamos una copia del tablero actual para usar en minimax o alfabeta
						copia = copy.deepcopy(juego.tablero)
						
							#Medimos el tiempo del algortimo
						inicio=time.time()
						jugada_blanca=alfabeta(juego,copia,0,1,-1000,1000,[],LISTA)
						fin=time.time()
						TIEMPO=round(fin-inicio,3)

						#Es posible que retorne directamente la utilidad, por lo que hay que sercirarse de que
						#retorne 2 elementos, la utilidad y la jugada
						if len(jugada_blanca)!=1:

							#Cuando no puede jugar la blanca retorna None
							if jugada_blanca[1] is not None:
								
								#Si es el turno de las blancas y la jugada es valida
								if TURNO_BLANCA and juego.Jugar(jugada_blanca[1],1):
									TURNO_NEGRA=True
									TURNO_BLANCA=False
							
							#Si la blanca no puede jugar, significa que el juego termino
							else:
								FIN_DE_JUEGO=True
								TURNO_NEGRA=False
								TURNO_BLANCA=False
						
						#Si el minimax o el alfabeta retornan solo la utilidad, es porque se lleno el tablero
						else:
							FIN_DE_JUEGO=True
							TURNO_NEGRA=False
							TURNO_BLANCA=False
					
					#Si la jugada de las negras no es valida pudo ser por error del jugador o porque ya no hay 
					#casillas disponibles
					else:

						#Si no hay casillas disponibles para las negras termina el juego
						if not juego.Puede_jugar(2):
							FIN_DE_JUEGO=True
							TURNO_NEGRA=False
							TURNO_BLANCA=False

						#si el jugador se equivoco se le permite volver a intentarlo
						else:
							pass
		
		#En cada ciclo del juego se revisa si no se ha completado el tablero
		if juego.Tablero_completo(juego.tablero) or not juego.Puede_jugar(2):
			FIN_DE_JUEGO=True
			TURNO_NEGRA=False
			TURNO_BLANCA=False

		#Contamos cuantas fichas de cada color hay en el tablero
		BLANCAS=juego.Contar_fichas(1)
		NEGRAS=juego.Contar_fichas(2)

		#En cada ciclo se evalua el ganador, pero solo se muestra si termina el juego
		if BLANCAS<NEGRAS:
			GANADOR="NEGRAS"
		elif BLANCAS > NEGRAS:
			GANADOR="BLANCAS"
		else:
			GANADOR= "EMPRATE"
		
		# Renderizado de texto: Turno de las fichas.
		if (TURNO_NEGRA):
			texto_turnos = pygame.font.Font.render(fuente_juego, "Turno: Ficha negra", True, COLOR_TEXTO);
			ventana.blit(texto_turnos, dest=(220, 668));
	
		elif (TURNO_BLANCA):
			texto_turnos = pygame.font.Font.render(fuente_juego, "Turno: Ficha blanca", True, COLOR_TEXTO);
			ventana.blit(texto_turnos, dest=(220, 668));
		
		elif (FIN_DE_JUEGO):
			texto_turnos = pygame.font.Font.render(fuente_juego, "GANADOR: "+str(GANADOR), True, COLOR_TEXTO);
			ventana.blit(texto_turnos, dest=(220,668));#300,120

		#MOSTRAR TIEMPO DE EJECUCION DE LA IA
		tiempo_ejecucion=pygame.font.Font.render(fuente_juego, str(TIEMPO), True, COLOR_TEXTO)
		ventana.blit(tiempo_ejecucion, dest=(500,80))
		
		#MOSTRAR NODOS EXPLORADOS POR LA IA
		nodos=pygame.font.Font.render(fuente_juego, str(len(LISTA)), True, COLOR_TEXTO)
		ventana.blit(nodos, dest=(500,45))
		
		#MOSTRAR EL NUMERO DE FICHAS BLANCAS EN JUEGO
		blancas=pygame.font.Font.render(fuente_juego, str(BLANCAS), True, COLOR_TEXTO)
		ventana.blit(blancas, dest=(83,121))
		
		#MOSTRAR EL NUMERO DE FICHAS NEGRAS EN JUEGO
		negras=pygame.font.Font.render(fuente_juego, str(NEGRAS), True, COLOR_TEXTO)
		ventana.blit(negras, dest=(180,121))

		#INDICAR QUE ELIGA LA DIFICULTAD AL USUARIO
		if not PERMISO:
			info=pygame.font.Font.render(fuente_juego, "Seleccione la dificultad", True, COLOR_TEXTO)
			ventana.blit(info, dest=(300,120))
		
		if PISTA is not None and PERMISO:
			info=pygame.font.Font.render(fuente_juego, str(PISTA), True, COLOR_TEXTO)
			ventana.blit(info, dest=(390,120))
		
		# Definición del tablero.
		controlador_tablero(ventana, ficha_blanca, ficha_negra);

		# Actualización de la ventana.
		pygame.display.flip();
