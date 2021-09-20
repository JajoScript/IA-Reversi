#	-- Dependencias.
#	Dependencias externas.
from typing import List, Tuple;

#	Dependencias Internas.

#	-- Clases.
#	Definición de la clase.
class Inteligencia():
	#	Propiedades.
	#	Constructor.
	def __init__(self) -> None:
		pass

	#	Metodos.
	def generar_jugadas_validas(self, jugador:int, partida:Any) -> None:
		"""..."""

		#	Creamos una variable para almacenar las jugadas posibles.
		partida.mostrar_tablero();
		jugadadas_posibles:List[Tuple[int,int]] = [];

		#	Generando las jugadas para el jugador: Ficha Blanca.
		if	(jugador == 1):
			for fila in range(6):
				for columna in range(6):
					pass

		#	Generando las jugadas para el jugador: Ficha Negra.
		elif (jugador == 2):
			pass
		#	Error: No se determina el jugador.
		else:
			print("[DEV][IA][ERROR][generar_jugadas_validas]")
			print("[>] ERROR: No se pudo determinar el jugador.");

	#	Getters & Setters.

