#	-- Dependencias. --
import numpy as np;
from typing import List

#	-- Funciones. --

#	-- Definición de clase. --
class Reversi():
	#	Propiedades.
	#	Definición del estado inicial del juego.
	#	Tablero vacio.
	ESTADO_JUEGO:List[List[int]];
	NUMERO_FILAS:int;
	NUMERO_COLUMNAS:int;

	#	Validaciones.
	esta_completo:bool = False; #	No puede iniciar completo.


	#	Constructor.
	def __init__(self, numero_filas:int, numero_columnas:int) -> None:
		#	Definición del estado inicial del juego.
		#	Tablero vacio.
		self.NUMERO_FILAS = numero_filas;
		self.NUMERO_COLUMNAS = numero_columnas;
		self.ESTADO_JUEGO = np.zeros((numero_filas, numero_columnas));


	#	Metodos.
	def crear_estado_inicial(self) -> None:
		#	Se define un nuevo inciial.
		estado_inicial:List[List[int]] = np.zeros((self.GET_numero_filas(), self.GET_numero_columnas()))

		#	Posiciones Fichas blancas.
		estado_inicial[2][2] = 1;
		estado_inicial[3][3] = 1;

		#	Posiciones Fichas negras.
		estado_inicial[2][3] = 2;
		estado_inicial[3][2] = 2;
		
		#	Guardando el estado inicial.
		self.SET_estado_juego(estado_inicial);


	def validacion_fin_del_juego(self) -> None:
		pass


	def validacion_salto_blanca(self, coordenadas:List[int]) -> None:
		"""..."""

		#	Variables locales.
		fila:int = coordenadas[0];
		columna:int = coordenadas[1];
		validaciones:List[bool];


	def validacion_salto_negra(self):
		pass

	
	def realizar_vistazos(self, tablero, indice_y, indice_x, modo) -> bool:
		#	Realizar vistazo según lo indica.
		if (modo == "arriba"):
			if (tablero[indice_y - 1][indice_x] != 0):
				return True

		elif(modo == "arriba-derecha"):
			if (tablero[indice_y - 1][indice_x + 1] != 0):
				return True

		elif(modo == "arriba-izquierda"):
			if (tablero[indice_y - 1][indice_x - 1] != 0):
				return True

		elif(modo == "centro"):
			if(tablero[indice_y][indice_x] != 0):
				return True
			
		elif(modo == "centro-derecha"):
			if(tablero[indice_y][indice_x + 1] != 0):
				return True
			
		elif(modo == "centro-izquierda"):
			if(tablero[indice_y][indice_x - 1] != 0):
				return True

		elif(modo == "abajo"):
			if (tablero[indice_y + 1][indice_x] != 0):
				return True

		elif(modo == "abajo-derecha"):
			if (tablero[indice_y + 1][indice_x + 1] != 0):
				return True
		
		elif(modo == "abajo-izquierda"):
			if (tablero[indice_y + 1][indice_x - 1] != 0):
				return True

		#	Retorno global de False.
		return False
		

	def validacion_es_adyacente(self, coordenadas:List[int]) -> bool:
		#	Recordatorio: El estandar de coordenada es: [y][x] == [fila][columna];
		#	Variables locales.
		indice_y:int = coordenadas[0];
		indice_x:int = coordenadas[1];

		#	Traemos el actual estado del juego.
		estado_juego:List[List[int]] = self.GET_estado_juego();

		#	Comprobaciones: Para celdas que no esten presentes en los bordes.
		if ((indice_y < 5) and (indice_y > 0)) and ((indice_x < 5) and (indice_x > 0)):
			#	Realizar vistazos.
			if (self.realizar_vistazos(estado_juego, indice_y, indice_x, "arriba")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "arriba-derecha")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "arriba-izquierda")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "centro-derecha")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "centro-izquierda")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "abajo")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "abajo-derecha")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "abajo-izquierda")):
				return True;
			else:
				return False;

		#	Comprobaciones: Para celdas que estan el borde inferior sin contar las celdas de las esquinas.
		elif((indice_y == 5) and ((indice_x < 5) and (indice_x > 0))):
			#	Realizar vistazos.
			if (self.realizar_vistazos(estado_juego, indice_y, indice_x, "arriba")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "arriba-derecha")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "arriba-izquierda")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "centro-derecha")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "centro-izquierda")):
				return True;
			else:
				return False;

		#	Comprobaciones: Para celdas que estan el borde superior sin contar las celdas de las esquinas.
		elif((indice_y == 0) and ((indice_x < 5) and (indice_x > 0))):
			#	Realizar vistazos.
			if (self.realizar_vistazos(estado_juego, indice_y, indice_x, "centro-derecha")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "centro-izquierda")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "abajo")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "abajo-derecha")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "abajo-izquierda")):
				return True;
			else:
				return False;

		#	Comprobaciones: Para celdas que estan el borde derecho sin contar las celdas de las esquinas.
		elif(((indice_y < 5) and (indice_y > 0)) and (indice_x == 5)):
			#	Realizar vistazos.
			if (self.realizar_vistazos(estado_juego, indice_y, indice_x, "arriba")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "ariba-izquierda")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "centro-izquierda")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "abajo")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "abajo-izquierda")):
				return True;
			else:
				return False;
		
		#	Comprobaciones: Para celdas que estan el borde izquierda sin contar las celdas de las esquinas.
		elif(((indice_y < 5) and (indice_y > 0)) and (indice_x == 0)):
			#	Realizar vistazos.
			if (self.realizar_vistazos(estado_juego, indice_y, indice_x, "arriba")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "ariba-derecha")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "centro-derecha")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "abajo")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "abajo-derecha")):
				return True;
			else:
				return False;
		
		#	Comprobaciones: Para celda esquinera arriba-derecha
		elif((indice_y == 0) and (indice_x == 5)):
			#	Realizar vistazos.
			if (self.realizar_vistazos(estado_juego, indice_y, indice_x, "centro-izquierda")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "abajo")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "abajo-izquierda")):
				return True;
			else:
				return False;

		#	Comprobaciones: Para celda esquinera arriba-izquierda
		elif((indice_y == 0) and (indice_x == 0)):
			#	Realizar vistazos.
			if (self.realizar_vistazos(estado_juego, indice_y, indice_x, "centro-derecha")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "abajo")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "abajo-derecha")):
				return True;
			else:
				return False;

		#	Comprobaciones: Para celda esquinera abajo-derecha
		elif((indice_y == 5) and (indice_x == 5)):
			#	Realizar vistazos.
			if (self.realizar_vistazos(estado_juego, indice_y, indice_x, "arriba")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "arriba-izquierda")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "centro-izquierda")):
				return True;
			else:
				return False;
		
		#	Comprobaciones: Para celda esquinera abajo-izquierda
		elif((indice_y == 0) and (indice_x == 0)):
			#	Realizar vistazos.
			if (self.realizar_vistazos(estado_juego, indice_y, indice_x, "arriba")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "arriba-derecha")):
				return True;
			elif (self.realizar_vistazos(estado_juego, indice_y, indice_x, "centro-derecha")):
				return True;
			else:
				return False;

		#	Retorno general.
		return False;


	def validacion_esta_vacia(self, coordenadas:List[int]) -> bool:
		#	Recordatorio: El estandar de coordenada es: [y][x] == [fila][columna];
		indice_y:int = coordenadas[0];
		indice_x:int = coordenadas[1];

		#	Traemos el estado del juego.
		estado_juego = self.GET_estado_juego();
		
		if estado_juego[indice_y][indice_x] == 0:
			return True;
		else:
			return False;


	def convertir_fichas(self) -> None:
		pass


	def algoritmo_MINMAX(self) -> None:
		pass


	#	Getters & Setters.
	#		NUMERO FILAS.
	def GET_numero_filas(self) -> int:
		return self.NUMERO_FILAS;

	def SET_numero_filas(self, numero:int) -> None:
		self.NUMERO_FILAS = numero;

	#		NUMERO COLUMNAS.
	def GET_numero_columnas(self) -> int:
		return self.NUMERO_COLUMNAS;

	def SET_numero_columnas(self, numero:int) -> None:
		self.NUMERO_COLUMNAS = numero;

	#		ESTA COMPLETO.
	def GET_esta_completo(self) -> bool:
		return self.esta_completo;

	def SET_esta_completo(self, nueva_configuracion:bool) -> None:
		self.esta_completo = nueva_configuracion; 

	#		ESTADO DE JUEGO.
	def GET_estado_juego(self) -> List[List[int]]:		
		return self.ESTADO_JUEGO;

	def SET_estado_juego(self, nuevo_estado) -> None:
		self.ESTADO_JUEGO = nuevo_estado;
	