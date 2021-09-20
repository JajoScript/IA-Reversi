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
	def realizar_vistazos(self, fila:int, columna:int, modo:str) -> bool:
		"""..."""

		#	Traemos el tablero.
		print("[DEV] PRE GAME (realizar_vistazos):");
		tablero = self.GET_estado_juego();
		self.mostrar_tablero();

		#	Vistazo: Realiza un vistazo a la casilla de arriba.
		if	(modo == "ARRIBA"):
			#	Se encuentra con una ficha blanca o negra arriba.
			if (tablero[(fila - 1)][(columna)] != 0):
				return True;
			#	Se encuentra con una celda vacia.
			elif (tablero[(fila - 1)][(columna)] == 0):
				return False;
			#	Error: No se determina el vistazo.
			else:
				print("[DEV][GAME][ERROR][realizar_vistazos]");
				print("[>] Error al realizar el vistazo hacia arriba.");
				return False;
		
		#	Vistazo: Realiza un vistazo a la casilla de arriba a la derecha.
		elif	(modo == "ARRIBA-DERECHA"):
			#	Se encuentra con una ficha blanca o negra arriba a la derecha.
			if (tablero[(fila - 1)][(columna + 1)] != 0):
				return True;
			#	Se encuentra con una celda vacia.
			elif (tablero[(fila - 1)][(columna + 1)] == 0):
				return False;
			#	Error: No se determina el vistazo.
			else:
				print("[DEV][GAME][ERROR][realizar_vistazos]");
				print("[>] Error al realizar el vistazo hacia arriba a la derecha.");
				return False;
		
		#	Vistazo: Realiza un vistazo a la casilla de arriba a la izquierda.
		elif	(modo == "ARRIBA-IZQUIERDA"):
			#	Se encuentra con una ficha blanca o negra arriba a la izquierda.
			if (tablero[(fila - 1)][(columna - 1)] != 0):
				return True;
			#	Se encuentra con una celda vacia.
			elif (tablero[(fila - 1)][(columna - 1)] == 0):
				return False;
			#	Error: No se determina el vistazo.
			else:
				print("[DEV][GAME][ERROR][realizar_vistazos]");
				print("[>] Error al realizar el vistazo hacia arriba a la izquierda.");
				return False;

		#	Vistazo: Realiza un vistazo a la casilla de la derecha.
		elif	(modo == "CENTRO-DERECHA"):
			#	Se encuentra con una ficha blanca o negra la derecha.
			if (tablero[(fila)][(columna + 1)] != 0):
				return True;
			#	Se encuentra con una celda vacia.
			elif (tablero[(fila)][(columna + 1)] == 0):
				return False;
			#	Error: No se determina el vistazo.
			else:
				print("[DEV][GAME][ERROR][realizar_vistazos]");
				print("[>] Error al realizar el vistazo hacia la derecha.");
				return False;

		#	Vistazo: Realiza un vistazo a la casilla de la izquierda.
		elif	(modo == "CENTRO-IZQUIERDA"):
			#	Se encuentra con una ficha blanca o negra la izquierda.
			if (tablero[(fila)][(columna - 1)] != 0):
				return True;
			#	Se encuentra con una celda vacia.
			elif (tablero[(fila)][(columna - 1)] == 0):
				return False;
			#	Error: No se determina el vistazo.
			else:
				print("[DEV][GAME][ERROR][realizar_vistazos]");
				print("[>] Error al realizar el vistazo hacia la izquierda.");
				return False;

		#	Vistazo: Realiza un vistazo a la casilla de abajo.
		elif (modo == "ABAJO"):
			#	Se encuentra con una ficha blanca o negra abajo.
			if (tablero[(fila + 1)][(columna)] != 0):
				return True;
			#	Se encuentra con una celda vacia.
			elif (tablero[(fila + 1)][(columna)] == 0):
				return False;
			#	Error: No se determina el vistazo.
			else:
				print("[DEV][GAME][ERROR][realizar_vistazos]");
				print("[>] Error al realizar el vistazo hacia abajo.");
				return False;

		#	Vistazo: Realiza un vistazo a la casilla de abajo a la derecha.
		elif (modo == "ABAJO-DERECHA"):
			#	Se encuentra con una ficha blanca o negra abajo a la derecha.
			if (tablero[(fila + 1)][(columna + 1)] != 0):
				return True;
			#	Se encuentra con una celda vacia.
			elif (tablero[(fila + 1)][(columna + 1)] == 0):
				return False;
			#	Error: No se determina el vistazo.
			else:
				print("[DEV][GAME][ERROR][realizar_vistazos]");
				print("[>] Error al realizar el vistazo hacia abajo a la derecha.");
				return False;

		#	Vistazo: Realiza un vistazo a la casilla de abajo a la izquierda.
		elif (modo == "ABAJO-IZQUIERDA"):
			#	Se encuentra con una ficha blanca o negra abajo a la izquierda.
			if (tablero[(fila + 1)][(columna - 1)] != 0):
				return True;
			#	Se encuentra con una celda vacia.
			elif (tablero[(fila + 1)][(columna - 1)] == 0):
				return False;
			#	Error: No se determina el vistazo.
			else:
				print("[DEV][GAME][ERROR][realizar_vistazos]");
				print("[>] Error al realizar el vistazo hacia abajo a la izquierda.");
				return False;

		#	Error: No se determina el modo. 
		else:
			print("[DEV][GAME][ERROR][realizar_vistazos]");
			print("[>] Error al determinar el tipo de vistazo solicitado.");
			return False;


	def comprobar_tiene_adyacente(self, coordenadas:Tuple[int,int]) -> bool:
		"""..."""
		#	Variables locales.
		fila:int = coordenadas[0];
		columna:int = coordenadas[1];

		#	Traemos el estado del juego.
		tablero:Any = self.GET_estado_juego()
		print("[DEV] PRE GAME (comprobar_tiene_adyacente):");
		self.mostrar_tablero()

		#	Verificación: Revisar Fichas que estan en el centro del tablero.
		if (((fila < 5) and (fila > 0)) and ((columna < 5) and (columna > 0))):
			#	Vistazos que va a realizar la comprobación.
			modos:List[str] = ["ARRIBA", "ARRIBA-DERECHA", "ARRIBA-IZQUIERDA", "CENTRO-DERECHA", "CENTRO-IZQUIERDA", "ABAJO", "ABAJO-DERECHA", "ABAJO-IZQUIERDA"];

			#	Ciclo para realizar todos los vistazos.
			for modo in modos:
				vistazo:bool = self.realizar_vistazos(fila=fila, columna=columna, modo=modo);
				if (vistazo == True):
					#	Si alguno de los vistazos es TRUE, se retorna a la función principal.
					return True;

			#	Si ninguno resulta ser TRUE, se retorna FALSE.
			return False;

		#	Verificación: Revisar las Fichas que estan en el borde inferior del tablero, sin contar las esquinas.
		elif ((fila == 5) and ((columna > 0) and (columna < 5))):
			#	Vistazos que va a realizar la comprobación.
			modos = ["ARRIBA", "ARRIBA-DERECHA", "ARRIBA-IZQUIERDA", "CENTRO-DERECHA", "CENTRO-IZQUIERDA"];

			#	Ciclo para realizar todos los vistazos.
			for modo in modos:
				vistazo = self.realizar_vistazos(fila=fila, columna=columna, modo=modo);
				if (vistazo == True):
					#	Si alguno de los vistazos es TRUE, se retorna a la función principal.
					return True;
					
			#	Si ninguno resulta ser TRUE, se retorna FALSE.
			return False;
	
		#	Verificación: Revisar las Fichas que estan en el borde superior del tablero, sin contar las esquinas.
		elif ((fila == 0) and ((columna > 0) and (columna < 5))):
			#	Vistazos que va a realizar la comprobación.
			modos = ["CENTRO-DERECHA", "CENTRO-IZQUIERDA", "ABAJO", "ABAJO-DERECHA", "ABAJO-IZQUIERDA"];

			#	Ciclo para realizar todos los vistazos.
			for modo in modos:
				vistazo = self.realizar_vistazos(fila=fila, columna=columna, modo=modo);
				if (vistazo == True):
					#	Si alguno de los vistazos es TRUE, se retorna a la función principal.
					return True;
					
			#	Si ninguno resulta ser TRUE, se retorna FALSE.
			return False;

		#	Verificación: Revisar las Fichas que estan en el borde derecho del tablero, sin contar las esquinas.
		elif (((fila > 0) and (fila < 5)) and ((columna == 5))):
			#	Vistazos que va a realizar la comprobación.
			modos = ["ARRIBA", "ARRIBA-IZQUIERDA", "CENTRO-IZQUIERDA", "ABAJO", "ABAJO-IZQUIERDA"];

			#	Ciclo para realizar todos los vistazos.
			for modo in modos:
				vistazo = self.realizar_vistazos(fila=fila, columna=columna, modo=modo);
				if (vistazo == True):
					#	Si alguno de los vistazos es TRUE, se retorna a la función principal.
					return True;
					
			#	Si ninguno resulta ser TRUE, se retorna FALSE.
			return False;

		#	Verificación: Revisar las Fichas que estan en el borde izquierdo del tablero, sin contar las esquinas.
		elif (((fila > 0) and (fila < 5)) and ((columna == 0))):
			#	Vistazos que va a realizar la comprobación.
			modos = ["ARRIBA", "ARRIBA-DERECHA", "CENTRO-DERECHA", "ABAJO", "ABAJO-DERECHA"];

			#	Ciclo para realizar todos los vistazos.
			for modo in modos:
				vistazo = self.realizar_vistazos(fila=fila, columna=columna, modo=modo);
				if (vistazo == True):
					#	Si alguno de los vistazos es TRUE, se retorna a la función principal.
					return True;
					
			#	Si ninguno resulta ser TRUE, se retorna FALSE.
			return False;
			
		#	Verificación: Revisar la esquina superior izquierda.
		elif (((fila == 0)) and ((columna == 0))):
			#	Vistazos que va a realizar la comprobación.
			modos = ["CENTRO-DERECHA", "ABAJO", "ABAJO-DERECHA"];

			#	Ciclo para realizar todos los vistazos.
			for modo in modos:
				vistazo = self.realizar_vistazos(fila=fila, columna=columna, modo=modo);
				if (vistazo == True):
					#	Si alguno de los vistazos es TRUE, se retorna a la función principal.
					return True;
					
			#	Si ninguno resulta ser TRUE, se retorna FALSE.
			return False;
			
		#	Verificación: Revisar la esquina superior derecha.
		elif (((fila == 0)) and ((columna == 5))):
			#	Vistazos que va a realizar la comprobación.
			modos = ["CENTRO-IZQUIERDA", "ABAJO", "ABAJO-IZQUIERDA"];

			#	Ciclo para realizar todos los vistazos.
			for modo in modos:
				vistazo = self.realizar_vistazos(fila=fila, columna=columna, modo=modo);
				if (vistazo == True):
					#	Si alguno de los vistazos es TRUE, se retorna a la función principal.
					return True;
					
			#	Si ninguno resulta ser TRUE, se retorna FALSE.
			return False;
		
		#	Verificación: Revisar la esquina inferior izquierda.
		elif (((fila == 5)) and ((columna == 0))):
			#	Vistazos que va a realizar la comprobación.
			modos = ["ARRIBA", "ARRIBA-DERECHA", "CENTRO-DERECHA"];

			#	Ciclo para realizar todos los vistazos.
			for modo in modos:
				vistazo = self.realizar_vistazos(fila=fila, columna=columna, modo=modo);
				if (vistazo == True):
					#	Si alguno de los vistazos es TRUE, se retorna a la función principal.
					return True;
					
			#	Si ninguno resulta ser TRUE, se retorna FALSE.
			return False;

		#	Verificación: Revisar la esquina inferior derecha.
		elif (((fila == 5)) and ((columna == 5))):
			#	Vistazos que va a realizar la comprobación.
			modos = ["ARRIBA", "ARRIBA-IZQUIERDA", "CENTRO-IZQUIERDA"];

			#	Ciclo para realizar todos los vistazos.
			for modo in modos:
				vistazo = self.realizar_vistazos(fila=fila, columna=columna, modo=modo);
				if (vistazo == True):
					#	Si alguno de los vistazos es TRUE, se retorna a la función principal.
					return True;
					
			#	Si ninguno resulta ser TRUE, se retorna FALSE.
			return False;

		#	ERROR: No se determino la zona de estudio.
		else:
			print("[DEV][GAME][ERROR][comprobar_tiene_adyacente]");
			print("[>] Error al comprobar si la celda tiene adyacente.");
			return False;
			

	def comprobar_vacia(self, coordenadas:Tuple[int,int]) -> bool:
		"""..."""

		#	Traemos el tablero.
		tablero = self.GET_estado_juego();
		
		fila:int = coordenadas[0];
		columna:int = coordenadas[1];

		#	Comprobaciones.
		if (tablero[fila][columna] == 0):
			print("[DEV][GAME] La celda esta vacia.");
			#	Se retorna True, la celda SI esta vacia.
			return True;
		elif(tablero[fila][columna] != 0):
			#	Se retorna False, la celda NO esta vacia.
			return False;
		else:
			print("[DEV][GAME][ERROR][comprobar_vacia]");
			print("[>] Error al comprobar si la celda esta vacia.");
			return False;
			

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
			print("[DEV][GAME] el juego termino.");
			
		elif not (esta_terminado):
			#	El juego no termino.
			print("[DEV][GAME] El juego no termino...");
			print("[DEV][GAME] Procesando turno...");
			
			#	Comprobacion: La casilla seleccionada esta vacia.
			if (esta_vacia):
				print("[DEV][GAME] Continua la jugada...");
				print(f"[DEV][GAME] Esta jugando la ficha: {self.GET_jugador()}");

				#	Comprobación: La casilla seleccionada tiene una ficha adyacente.
				tiene_adyacente:bool = self.comprobar_tiene_adyacente((fila, columna));

				if (tiene_adyacente == True):
					print("[DEV] La celda tiene adyancente, procediendo a la siguiente comprobación.");

					#	Comprobación: La casilla seleccionada es una jugada valida.
					nuevo_tablero = self.GET_estado_juego();
					nuevo_tablero[fila][columna] = color_ficha;
					self.SET_estado_juego(nuevo_tablero);

					print("[DEV] POST GAME");
					self.mostrar_tablero();

				elif (tiene_adyacente == False):
					#	Se vuelve al tablero.
					print("[DEV][GAME] Se cancela la jugada, la celda no tiene adyacente...");

			elif not (esta_vacia):
				#	Se vuelve al tablero.
				print("[DEV][GAME] Se cancela la jugada, la celda no esta vacia...");
			else:
				print("[DEV][GAME][ERROR][iniciar_jugabilidad]");
				print("[>] Error al determinar la jugada.");
		else:
			print("[DEV][GAME][ERROR][iniciar_jugabilidad]");
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
