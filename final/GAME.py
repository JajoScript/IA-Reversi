#	-- Dependencias.
#	Dependencias externas.
from typing import List, Any, Tuple;
import numpy as np;

#	Dependencias Internas.

#	-- Clases.
#	Definición de la clase.
class Juego():
	#	Propiedades.
	#	Constructor.
	def __init__(self, numero_filas:int, numero_columnas:int) -> None:
		#	Creación del tablero.
		self.estado_juego:Any= np.zeros((numero_filas, numero_columnas));
		self.numero_filas = numero_filas;
		self.numero_columnas = numero_columnas;

	#	Metodos.
	def comprobar_finalizacion(self) -> bool:
		"""..."""

		#	Traemos el estado del juego.
		tablero = self.GET_estado_juego();

		#	CASO 1: No quedan casillas vacias.
		if not (0 in tablero):
			#	Se retorna True dado que, el juego SI termino.
			self.SET_terminado(True);
			return True;
		#	CASO 2: No quedan más movimientos para la ficha blanca.

		#	CASO 3: No quedan más movimientos para la ficha negra.
		else:
			#	Se retorna False dado que, el juego NO termino.
			self.SET_terminado(False);
			return False;


		#	ERROR: No se determino ningun caso.
	

	def iniciar_jugabilidad(self, coordenadas:Tuple[int, int]) -> None:
		"""..."""

		print(f"[DEV] Iniciando la jugabilidad...")	
		print(f"[DEV] (x: {coordenadas[0]}, y: {coordenadas[1]})");
		
		#	Comprobar si el juego termino.
		esta_terminado:bool = self.comprobar_finalizacion();

		if (esta_terminado):
			#	El juego termino.
			print("[DEV] el juego termino.")
			
		else:
			#	El juego no termino.
			print("[DEV] el juego no termino...")
			print("[DEV] Iniciando calculos...")
			# Más jugabilidad aqui....
		

	def definir_estado_inicial(self) -> None:
		"""..."""
		
		#	Definiendo el estado inicial.
		tablero:Any= np.zeros((self.numero_filas, self.numero_columnas));
		tablero[2][2] = 1;
		tablero[3][3] = 1;
		tablero[2][3] = 2;
		tablero[3][2] = 2;

		#	Guardamos la configuración inicial del tablero.
		self.SET_estado_juego(tablero);
		print("[DEV] se definio un nuevo estado inicial para la partida");
		
	def mostrar_tablero(self) -> None:
		"""..."""

		#	Trayendo el tablero.
		tablero = self.GET_estado_juego();
		print("-- Estado del juego --");
		for fila in tablero:
				print("|", end="");
				for elemento in fila:
					 print(str(elemento) + " |", end="");
				print(end="\n");
		print("-"*12);

	#	Getters & Setters.
	#		TERMINADO.
	def GET_terminado(self) -> bool:
		return self.TERMINADO;

	def SET_terminado(self, nueva_configuracion) -> None:
		self.TERMINADO = nueva_configuracion;

	#		ESTADO DEL JUEGO.
	def GET_estado_juego(self) -> Any:
		return self.estado_juego;

	def SET_estado_juego(self, nuevo_estado) -> None:
		self.estado_juego = nuevo_estado;
