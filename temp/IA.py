#	-- Dependencias. --
from typing import List, Any;
import copy

#	-- Funciones. --

#	-- Definición de clase. --
class InteligenciaArtificial():
	#	Propiedades.
	PUEDE_GENERAR_JUGADAS:bool;
	COMPLETADO:bool;
	PROFUNDIDAD:int;
	UTILIDAD:int;

	#	Constructor.
	def __init__(self, verificacion_jugadas:bool, profundidad:int, esta_completado:bool) -> None:
		self.PUEDE_GENERAR_JUGADAS = verificacion_jugadas;
		self.PROFUNDIDAD = profundidad;
		self.COMPLETADO = esta_completado;

	#	Metodos.
	def algoritmo_minmax(self, estado_copia, etapa:int) -> List:
		"""..."""

		#	Traemos la partida guardada.
		juego = self.GET_partida();
		estado_juego:List[List[int]] = juego.GET_estado_juego();

		#	Comprobamos el estado final.
		if (self.estado_final()):
			return [-1 * self.GET_utilidad()]

		if (etapa == 1):
			valor = [-1000, None];

			#	Calculando las jugadas posibles para las fichas blancas.
			jugadas_posibles = juego.generador_jugadas_validas(1);

		else:
			valor = [1000, None];
			#	Calculando las jugadas posibles para las fichas negras.
			jugadas_posibles = juego.generador_jugadas_validas(2);

		#	Recorriendo las jugadas posibles.
		for jugada in jugadas_posibles:
			if	(etapa == 1):
				if	((juego.validacion_esta_vacia(jugada)) and (juego.validacion_es_adyacente(jugada)) and (juego.validacion_salto(jugada, 2, 1))):
					estado_juego[jugada[0]][jugada[1]] = 2; #	Cambia la celda de color.
					juego.jugada.append(jugada);
			
			else:
				if ((juego.validacion_esta_vacia(jugada)) and (juego.validacion_es_adyacente(jugada)) and (juego.validacion_salto(jugada, 1, 2))):
					estado_juego[jugada[0]][jugada[1]] = 2; #	Cambia la celda de color.
					juego.jugada.append(jugada);

			#	Calculamos otra jugada dentro del tablero.
			nuevo_estado_juego = copy.deepcopy(juego.GET_estado_juego());
			opcion = self.algoritmo_minmax(nuevo_estado_juego, (etapa * -1));

			#	MAXimizar.
			if (etapa == 1):
				if (valor[0] < opcion[0]):
					valor = [opcion[0], jugada];
			
			#	MINimizando.
			else:
				if (valor[0] > opcion[0]):
					valor = [opcion[0], jugada];

			#	Retornamos el tablero a su posición inicial.
			self.devolver_estado(estado_copia);
		
		# Retorno del valor.
		return valor;


	def evaluar(self) -> None:
		"""..."""

		#	Traemos el objeto juego que contiene la información de la partida.
		juego = self.GET_partida();

		#	Traemos el tablero del juego.
		estado_juego:List[List[int]] = juego.GET_estado_juego();
		profundidad:int = self.GET_profundidad();

		#	Realizamos comprobaciones de profundidad y si el tablero esta completo.
		if ((not (0 in estado_juego)) or (profundidad == 2)):
			self.SET_completado(True);
		else:
			self.SET_completado(False);

		#	Definimos un estado inicial.
		numero_fichas_blancas:int = 0;
		numero_fichas_negras:int = 0;

		#	Traemos la completitud del tablero.
		completado:bool = self.GET_completado();

		if (completado):
			#	Recorriendo el tablero.
			for fila in range(6):
				for columna in range(6):
					#	Identificando si la ficha es blanca o negra.
					if (estado_juego[fila][columna] == 1):
						numero_fichas_blancas = (numero_fichas_blancas + 1);
					elif (estado_juego[fila][columna] == 2):
						numero_fichas_negras = (numero_fichas_negras + 1);
			
			#	Guardando la utilidad.
			self.SET_utilidad((numero_fichas_negras - numero_fichas_blancas));
		
	def estado_final(self) -> bool:
		"""..."""

		#	Evaluamos para actualizar el valor de la utilidad.
		# juego:Reversi = self.GET_partida(); # creo que esto sobra.
		self.evaluar();

		#	Comprobamos:
		if (self.GET_completado()):
			return True;
		else:
			return False;


	def devolver_estado(self, estado_nuevo:List[List[int]]) -> None:
		"""..."""

		#	Traemos el estado del juego.
		juego = self.GET_partida();
		estado_juego:List[List[int]] = juego.GET_estado_juego();

		#	Comparamos las casillas del estado nuevo con las del estado guardado.
		for fila in range(6):
			for columna in range(6):
				estado_juego[fila][columna] = estado_nuevo[fila][columna];

		#	Guardamos el nuevo estado del juego.
		juego.SET_estado_juego(estado_juego);

	#	Getters & Setters.
	#		PARTIDA
	def GET_partida(self) -> Any:
		return self.PARTIDA;

	def SET_partida(self, nueva_partida) -> None:
		self.PARTIDA = nueva_partida;

	#		UTILIDAD.
	def GET_utilidad(self) -> int:
		return self.UTILIDAD;

	def SET_utilidad(self, nueva_utilidad:int) -> None:
		self.UTILIDAD = nueva_utilidad;

	#		COMPLETADO.
	def GET_completado(self) -> bool:
		return self.COMPLETADO;

	def SET_completado(self, nueva_configuracion) -> None:
		self.COMPLETADO = nueva_configuracion;

	#		PROFUNDIDAD.
	def GET_profundidad(self) -> int:
		return self.PROFUNDIDAD;

	def SET_profundidad(self, nueva_profundidad:int) -> None:
		self.PROFUNDIDAD = nueva_profundidad;

	#		GENERAR JUGADAS.
	def GET_puede_generar_jugadas(self) -> bool:
		return self.PUEDE_GENERAR_JUGADAS;

	def SET_puede_generar_jugadas(self, nueva_configuracion) -> None:
		self.PUEDE_GENERAR_JUGADAS = nueva_configuracion;