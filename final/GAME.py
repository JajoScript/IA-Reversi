#	-- Dependencias.
#	Dependencias externas.
from typing import List, Any;
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

	#	Metodos.
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
	def GET_estado_juego(self) -> Any:
		return self.estado_juego;

	def SET_estado_juego(self, nuevo_estado) -> None:
		self.estado_juego = nuevo_estado;
