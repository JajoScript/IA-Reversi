#	-- Dependencias.
#	Dependencias externas.
from typing import List, Tuple, Any;
from GAME import Juego;
import copy

#	Dependencias Internas.

#	-- Clases.
#	Definición de la clase.
class Inteligencia():
	#	Propiedades.
	#	Constructor.
	def __init__(self) -> None:
		#	Definimos el estado de profundidad incial.
		self.PROFUNDIDAD = 2; # Facilito.

	#	Metodos.
	def evaluar(self, profundidad:int) -> None:
		"""..."""

		#	Traemos la profundidad
		dificultad:int = self.GET_profundidad();
		partida:Juego = self.GET_partida();
		tablero = partida.GET_estado_juego();

		#	Se comprueba si el tablero esta completo.
		if (partida.comprobar_finalizacion() or profundidad == dificultad):
			self.SET_completo(True);
		else:
			self.SET_completo(False);
		
		#	Cantidad de fichas
		numero_blancas = 0;
		numero_negras = 0;

		if (self.GET_completo()):
			for fila in range(6):
				for columna in range(6):
					#	Encontre una ficha blanca.
					if (tablero[fila][columna] == 1):
						numero_blancas += 1;

					#	Encontre una ficha negra.
					elif (tablero[fila][columna] == 2):	
						numero_negras += 1;
					#	Encontre una celda vacia.
					elif (tablero[fila][columna] == 0):
						pass	
					else:
						print("[DEV][IA][ERROR][evaluar]");
						print("[>] ERROR: Error al determinar que wea hay en el tablero."); #	Recordatorio: cambiar esta linea XD.
			
			#	Definimos la utilidad.
			nueva_utilidad:int = (numero_negras - numero_blancas);
			self.SET_utilidad(nueva_utilidad);

	def estado_final(self, profundidad:int) -> bool:
		"""..."""

		#	Comprobamos si el tablero esta completo.
		esta_completo = self.GET_completo();

		#	Evaluamos segun la profundidad.
		self.evaluar(profundidad);

		#	CASO 1: El juego esta completo. 
		if (esta_completo == True):
			return True;

		#	CASO 2: El juego no esta completo. 
		elif (esta_completo == False):
			return False;

		#	ERROR: no se pudo determinar si el tablero esta completo. 
		else:
			print("[DEV][IA][ERROR][estado_final]");
			print("[>] ERROR: Error al determinar si el juego estaba completo.")
			return False;


	def generar_jugadas_posibles(self, jugador:int):
		"""..."""

		partida:Juego = self.GET_partida();
		
		#	Habilitamos la edición.
		partida.SET_puede_editar(True);
		jugadas_posibles = [];

		if (jugador == 1):
			for fila in range(6):
				for columna in range(6):
					if (partida.comprobar_vacia((fila, columna)) and partida.comprobar_tiene_adyacente((fila, columna)) and partida.validacion_jugadas((fila, columna))):
						jugadas_posibles.append([fila, columna]);
					
		elif (jugador == 2):
			for fila in range(6):
				for columna in range(6):
					if (partida.comprobar_vacia((fila, columna)) and partida.comprobar_tiene_adyacente((fila, columna)) and partida.validacion_jugadas((fila, columna))):
						jugadas_posibles.append([fila, columna]);
		else:
			print("[DEV][IA][ERROR][generar_jugadas_posibles]");
		
		#	Deshabilitamos la edición del tablero.
		partida.SET_puede_editar(False);
		return jugadas_posibles;


	def minimax(self, partida:Juego, tablero, profundidad:int, etapa:int, secuencia, secuencias) -> Any:
		"""..."""
		print("[DEV] Ejecutando minimax...");

		#	ETAPA = 1: (MAX) Ficha blanca.
		#	ETAPA = -1: (MIN) Ficha NEGRA.
 
		#	Guardamos la partida como propiedad de la clase.
		self.SET_partida(partida);

		#	Traemos el tablero.
		print("[DEV][IA][minimax]")
		partida.mostrar_tablero();

		#	Comprobamos si el tablero esta completo o no.
		esta_completo:bool = partida.comprobar_finalizacion();
		self.SET_completo(esta_completo);

		#	Comprobamos si el tablero esta completo.
		if (self.estado_final(profundidad)):
			secuencia.append(secuencia.copy());
			return [-1 * self.GET_utilidad()];

		#	Maximizamos para blanca.
		if (etapa == 1):
			valor = [-1000, None];
			jugadas_posibles = self.generar_jugadas_posibles(1);

		#	Maximizamos para negra.
		elif (etapa == -1):
			valor = [1000, None];
			jugadas_posibles = self.generar_jugadas_posibles(2);

		else:
			print("[DEV][IA][ERROR][minimax]");

		#	Revisamos las jugadas posibles.
		for jugada in jugadas_posibles:
			if (etapa == 1):
				partida.iniciar_jugabilidad(jugada, color_ficha=1);

			elif (etapa == -1):
				partida.iniciar_jugabilidad(jugada, color_ficha=2);

			#
			copia = copy.deepcopy(tablero);
			secuencia.append(jugada);
			opcion = self.minimax(partida, copia, profundidad=(profundidad + 1), etapa=(etapa * -1), secuencia=secuencia, secuencias=secuencias);

			if (etapa == 1):
				if (valor[0] < opcion[0]):
					valor = [opcion[0], jugada];

			elif (etapa == -1):
				if (valor[0] > opcion[0]):
					valor = [opcion[0], jugada];
			else:
				print("[DEV][IA][ERROR][minimax]");
				print("[>] ERROR: error al identificar la etapa dentro del analisis de jugadas posibles.");
		
			#	Volvemos a la normalidad el tablero.
			partida.SET_estado_juego(tablero);
			secuencia.pop();
		return valor;


	#	Getters & Setters.
	#		UTILIDAD.
	def GET_utilidad(self) -> int:
		return self.UTILIDAD;

	def SET_utilidad(self, nueva_utilidad:int) -> None:
		self.UTILIDAD = nueva_utilidad;

	#		PARTIDA o JUEGO.
	def GET_partida(self) -> Any:
		return self.PARTIDA;

	def SET_partida(self, nueva_partida:Any) -> None:
		self.PARTIDA = nueva_partida;

	#		COMPLETO.
	def GET_completo(self) -> bool:
		return self.COMPLETO;

	def SET_completo(self, esta_completo:bool) -> None:
		self.COMPLETO = esta_completo;
 
	#		PROFUNDIDAD.
	def GET_profundidad(self) -> int:
		return self.PROFUNDIDAD;

	def SET_profundidad(self, nueva_profundidad:int) -> None:
		self.PROFUNDIDAD = nueva_profundidad;

	#		ESTADO JUEGO.
	def GET_estado_juego(self) -> Any:
		return self.ESTADO_JUEGO;

	def SET_estado_juego(self, nuevo_estado) -> None:
		self.ESTADO_JUEGO = nuevo_estado;
