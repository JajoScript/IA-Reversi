#	-- Dependencias. --
import numpy as np;

#	-- Funciones. --

#	-- Definición de clase. --
class Reversi():
	#	Propiedades.
	#	Definición del estado inicial del juego.
	#	Tablero vacio.
	ESTADO_JUEGO:list[list[int]];
	NUMERO_FILAS:int;
	NUMERO_COLUMNAS:int;

	#	Constructor.
	def __init__(self, numero_filas:int, numero_columnas:int) -> None:
		#	Definición del estado inicial del juego.
		#	Tablero vacio.
		self.NUMERO_FILAS = numero_filas;
		self.NUMERO_COLUMNAS = numero_columnas;
		self.ESTADO_JUEGO = np.zeros((numero_filas, numero_columnas));

	#	Metodos.
	def crear_estado_inicial(self):
		# Se define un nuevo inciial.
		estado_inicial:list[list[int]] = np.zeros((self.GET_numero_filas(), self.GET_numero_columnas()))

		# Posiciones Fichas blancas.
		estado_inicial[2][2] = 1;
		estado_inicial[3][3] = 1;

		# Posiciones Fichas negras.
		estado_inicial[2][3] = 2;
		estado_inicial[3][2] = 2;
		
		# Guardando el estado inicial.
		self.SET_estado_juego(estado_inicial);


	#	Getters & Setters.
		#	NUMERO FILAS.
	def GET_numero_filas(self) -> int:
		return self.NUMERO_FILAS;

	def SET_numero_filas(self, numero:int) -> None:
		self.NUMERO_FILAS = numero;

		#	NUMERO COLUMNAS.
	def GET_numero_columnas(self) -> int:
		return self.NUMERO_COLUMNAS;

	def SET_numero_columnas(self, numero:int) -> None:
		self.NUMERO_COLUMNAS = numero;

		#	ESTADO DE JUEGO.
	def GET_estado_juego(self) -> list[list[int]]:		
		return self.ESTADO_JUEGO;

	def SET_estado_juego(self, nuevo_estado) -> None:
		self.ESTADO_JUEGO = nuevo_estado;
	