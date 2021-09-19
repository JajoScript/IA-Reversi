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
	def comprobar_tiene_adyacente(self) -> None:
		
		pass

	def comprobar_vacia(self, coordenadas:Tuple[int,int]) -> bool:
		"""..."""

		#	Traemos el tablero.
		tablero = self.GET_estado_juego();
		
		fila:int = coordenadas[0];
		columna:int = coordenadas[1];

		#	Comprobaciones.
		if (tablero[fila][columna] == 0):
			print("[DEV][GAME] La celda esta vacia.")
			#	Se retorna True, la celda SI esta vacia.
			return True;
		elif(tablero[fila][columna] != 0):
			#	Se retorna False, la celda NO esta vacia.
			return False;
		else:
			print("[DEV][GAME][comprobar_vacia]")
			print("[>] Error al comprobar si la celda esta vacia.")
			

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
			#	Se define la propiedad TERMINADO como False.
			self.SET_terminado(False);
			return False;


		#	ERROR: No se determino ningun caso.
	

	def iniciar_jugabilidad(self, coordenadas:Tuple[int, int], color_ficha:int) -> None:
		"""..."""

		print(f"[DEV][GAME] Iniciando la jugabilidad...")	
		columna:int = coordenadas[0];
		fila:int = coordenadas[1];

		#	Definiendo de quien es el turno.
		self.SET_jugador(color_ficha);

		#	Comprobar si el juego termino.
		esta_terminado:bool = self.comprobar_finalizacion();
		esta_vacia:bool = self.comprobar_vacia((fila, columna));

		#	Comprobaciones: Determinar si se puede o no jugar...
		if (esta_terminado):
			#	El juego termino.
			print("[DEV][GAME] el juego termino.")
			
		elif not (esta_terminado):
			#	El juego no termino.
			print("[DEV][GAME] El juego no termino...")
			print("[DEV][GAME] Procesando turno...")
			
			#	Comprobacion: La casilla seleccionada esta vacia.
			if (esta_vacia):
				print("[DEV][GAME] Continua la jugada...");
				print(f"[DEV][GAME] Esta jugando la ficha: {self.GET_jugador()}")

				#	Comprobación: La casilla seleccionada tiene una ficha adyacente.
				#	Comprobación: La casilla seleccionada es una jugada valida.
			

			elif not (esta_vacia):
				#	Se vuelve al tablero.
				print("[DEV][GAME] Se cancela la jugada, la celda no esta vacia...");
			else:
				print("[DEV][GAME][ERROR][iniciar_jugabilidad]")
				print("[>] Error al determinar la jugada.");
		else:
			print("[DEV][GAME][ERROR][iniciar_jugabilidad]")
			print("[>] Error al determinar la jugada.");
				

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
		print("[DEV][GAME] se definio un nuevo estado inicial para la partida");
		
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
	#		JUGADOR.
	def GET_jugador(self) -> int:
		return self.JUGADOR;
	
	def SET_jugador(self, color_ficha) -> None:
		self.JUGADOR = color_ficha;

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
