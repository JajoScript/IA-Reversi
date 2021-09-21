#	-- Dependencias.
#	Dependencias externas.
from os import truncate
from typing import AsyncIterable, List, Any, Tuple;
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
	def convertir_fichas(self, fila_inicial:int, fila_final:int, columna_inicial:int, columna_final:int, modo:str) -> None:
		"""..."""

		#	Traemos el estado del juego.
		tablero:Any = self.GET_estado_juego();
		jugador:int = self.GET_jugador();

		print(f"[DEV][GAME][convertir_fichas][ficha: {jugador}] PRE-CONVERTIR [{modo}]");
		print(f"[DEV][GAME][convertir_fichas] fi:{fila_inicial}, ff:{fila_final}, ci:{columna_inicial}, cf:{columna_final}")
		self.mostrar_tablero();
		

		#	Convertir: Convertir fichas hacia arriba.
		if (modo == "ARRIBA"):
			while (fila_inicial != fila_final):
				tablero[(fila_inicial)][(columna_inicial)] = jugador;
				fila_inicial = (fila_inicial - 1);

		#	Convertir: Convertir fichas hacia la arriba a la derecha.
		elif (modo == "ARRIBA-DERECHA"):
			while (fila_inicial != fila_final):
				tablero[(fila_inicial)][(columna_inicial)] = jugador;
				fila_inicial = (fila_inicial - 1);
				columna_inicial = (columna_inicial + 1);

		#	Convertir: Convertir fichas hacia la arriba a la izquierda.
		elif (modo == "ARRIBA-IZQUIERDA"):
			while (fila_inicial != fila_final):
				tablero[(fila_inicial)][(columna_inicial)] = jugador;
				fila_inicial = (fila_inicial - 1);
				columna_inicial = (columna_inicial - 1);

		#	Convertir: Convertir fichas hacia la derecha.
		elif (modo == "CENTRO-DERECHA"):
			columna_inicial = columna_inicial - 1;	#	Parche para que funque bien ._.
			while (columna_inicial != columna_final):
				print(f"columna_inicial: {columna_inicial}")
				tablero[(fila_inicial)][(columna_inicial)] = jugador;
				columna_inicial = (columna_inicial + 1);
		
		#	Convertir: Convertir fichas hacia la izquierda.
		elif (modo == "CENTRO-IZQUIERDA"):
			columna_inicial = columna_inicial + 1; #	Parche para que funque bien ._.
			while (columna_inicial != columna_final):
				print(f"columna_inicial: {columna_inicial}")
				tablero[(fila_inicial)][(columna_inicial)] = jugador;
				columna_inicial = (columna_inicial - 1);

		#	Convertir: Convertir fichas hacia abajo.
		elif (modo == "ABAJO"):
			while (fila_inicial != fila_final):
				tablero[(fila_inicial)][(columna_inicial)] = jugador;
				fila_inicial = (fila_inicial + 1);

		#	Convertir: Convertir fichas hacia abajo a la derecha.
		elif (modo == "ABAJO-DERECHA"):
			while (fila_inicial != fila_final):
				tablero[(fila_inicial)][(columna_inicial)] = jugador;
				fila_inicial = (fila_inicial + 1);
				columna_inicial = (columna_inicial + 1);

		#	Convertir: Convertir fichas hacia abajo a la izquierda.
		elif (modo == "ABAJO-IZQUIERDA"):
			while (fila_inicial != fila_final):
				tablero[(fila_inicial)][(columna_inicial)] = jugador;
				fila_inicial = (fila_inicial + 1);
				columna_inicial = (columna_inicial - 1);

		#	Error: Error al determinar el modo de convertir.
		else:
			print("[DEV][GAME][ERROR][convertir_fichas]");
			print("[>] Error al determinar el modo de convertir.");

		#	Guardamos la nueva configuración del tablero.
		print(f"[DEV][GAME][convertir_fichas][ficha: {jugador}] POST-CONVERTIR [{modo}]");
		self.mostrar_tablero();
		self.SET_estado_juego(tablero);

	def validacion_jugadas(self, coordenadas:Tuple[int,int]) -> bool:
		"""..."""

		#	Variables locales.
		puede_editar:bool = self.GET_puede_editar();
		fila:int = coordenadas[0];
		columna:int = coordenadas[1];

		print(f"[DEV][GAME][validacion_jugadas] fila: {fila}, columna: {columna}");
		tablero:Any = self.GET_estado_juego();
		validaciones:List[bool] = [];
		jugador:int = self.GET_jugador();

		#	Determinación de la ficha objetivo.
		#	CASO 1: La ficha objetivo es Ficha Negra.
		if (jugador == 1):
			jugador_objetivo:int = 2;

		#	CASO 2: La ficha objetivo es Ficha Blanca.
		elif (jugador == 2):
			jugador_objetivo = 1;

		#	Error: Error al determinar la ficha objetivo.
		else:
			print("[DEV][GAME][ERROR][validacion_jugadas]");
			print("[>] Error al determinar la ficha objetivo.");
			return False;

	
		#	Re-comprobación: tiene adyacente.
		tiene_adyacente:bool = self.comprobar_tiene_adyacente(coordenadas=(fila, columna));

		#	La celda tiene adyacente.
		if (tiene_adyacente):
			#	Validación: Buscar ficha hacia arriba.
			fila_auxiliar:int = (fila - 1);

			#	Rango para celdas dentro del tablero.
			if (fila_auxiliar < 5 and fila_auxiliar > 0):
				#	Busqueda: Ficha objetivo.
				if (tablero[fila_auxiliar][columna] == jugador_objetivo):
					for iterador in range((fila_auxiliar)):
						#	Busqueda: Ficha jugador.
						if (tablero[(fila_auxiliar - iterador - 1)][(columna)] == jugador):
							#	Recordatorio: editar aquí para insertar la IA.

							if (puede_editar):
								self.convertir_fichas(fila, (fila_auxiliar - iterador - 1), columna, columna, "ARRIBA");

							elif not (puede_editar):
								print("[DEV][GAME][validacion_jugadas] Se valido la jugada pero no se edito.");

							else:
								print("[DEV][GAME][ERROR][validacion_jugadas]");
								print("[>] Error al verificar la edición del tablero.");
							
							#	Agregamos la validación a la lista de validaciones.
							validaciones.append(True);

				#	Busqueda: No se encuentra a la ficha objetivo.
				else:
					validaciones.append(False);
			#	La celda no esta en el rango determinado.
			else:
				validaciones.append(False);

			#	Validación: Buscar ficha hacia arriba-derecha.
			fila_auxiliar = (fila - 1);
			columna_auxiliar:int = (columna + 1);

			#	Rango para celdas dentro del tablero.
			if (fila_auxiliar < 5 and fila_auxiliar > 0) and (columna_auxiliar < 5 and columna_auxiliar > 0):
				par:List[int] = [fila_auxiliar, (5 - columna_auxiliar)];
				rango:int = min(par);

				#	Busqueda: Ficha objetivo.
				if (tablero[fila_auxiliar][columna_auxiliar] == jugador_objetivo):
					for iterador in range((rango)):
						#	Busqueda: Ficha jugador.
						if (tablero[(fila_auxiliar - iterador - 1)][(columna_auxiliar + iterador + 1)] == jugador):
							#	Recordatorio: editar aquí para insertar la IA.
							if (puede_editar):
								self.convertir_fichas(fila, (fila_auxiliar - iterador - 1), columna, (columna_auxiliar + iterador + 1), "ARRIBA-DERECHA");

							elif not (puede_editar):
								print("[DEV][GAME][validacion_jugadas] Se valido la jugada pero no se edito.");

							else:
								print("[DEV][GAME][ERROR][validacion_jugadas]");
								print("[>] Error al verificar la edición del tablero.");
							
							#	Agregamos la validación a la lista de validaciones.
							validaciones.append(True);

				#	Busqueda: No se encuentra a la ficha objetivo.
				else:
					validaciones.append(False);
			#	La celda no esta en el rango determinado.
			else:
				validaciones.append(False);

			#	Validación: Buscar ficha hacia arriba-izquierda.
			fila_auxiliar = (fila - 1);
			columna_auxiliar = (columna - 1);

			#	Rango para celdas dentro del tablero.
			if (fila_auxiliar < 5 and fila_auxiliar > 0) and (columna_auxiliar < 5 and columna_auxiliar > 0):
				par = [fila_auxiliar, columna_auxiliar];
				rango = min(par);

				#	Busqueda: Ficha objetivo.
				if (tablero[fila_auxiliar][columna_auxiliar] == jugador_objetivo):
					for iterador in range((rango)):
						#	Busqueda: Ficha jugador.
						if (tablero[(fila_auxiliar - iterador - 1)][(columna_auxiliar - iterador - 1)] == jugador):
							#	Recordatorio: editar aquí para insertar la IA.
							if (puede_editar):
								self.convertir_fichas(fila, (fila_auxiliar - iterador - 1), columna, (columna_auxiliar - iterador - 1), "ARRIBA-IZQUIERDA");

							elif not (puede_editar):
								print("[DEV][GAME][validacion_jugadas] Se valido la jugada pero no se edito.");

							else:
								print("[DEV][GAME][ERROR][validacion_jugadas]");
								print("[>] Error al verificar la edición del tablero.");
							
							#	Agregamos la validación a la lista de validaciones.
							validaciones.append(True);

				#	Busqueda: No se encuentra a la ficha objetivo.
				else:
					validaciones.append(False);
			#	La celda no esta en el rango determinado.
			else:
				validaciones.append(False);

			#	Validación: Buscar ficha a la centro-derecha.
			columna_auxiliar = (columna + 1);

			#	Rango para celdas dentro del tablero.
			if (columna_auxiliar < 5 and columna_auxiliar > 0):
				#	Busqueda: Ficha objetivo.
				if (tablero[fila][columna_auxiliar] == jugador_objetivo):
					for iterador in range(5 - columna_auxiliar):
						#	Busqueda: Ficha jugador.
						if (tablero[fila][(columna_auxiliar + iterador + 1)] == jugador):
							#	Recordatorio: editar aquí para insertar la IA.
							if (puede_editar):
								self.convertir_fichas(fila, fila, columna_auxiliar, (columna_auxiliar + iterador + 1), "CENTRO-DERECHA");

							elif not (puede_editar):
								print("[DEV][GAME][validacion_jugadas] Se valido la jugada pero no se edito.");

							else:
								print("[DEV][GAME][ERROR][validacion_jugadas]");
								print("[>] Error al verificar la edición del tablero.");
							
							#	Agregamos la validación a la lista de validaciones.
							validaciones.append(True);

				#	Busqueda: No se encuentra a la ficha objetivo.
				else:
					validaciones.append(False);
			#	La celda no esta en el rango determinado.
			else:
				validaciones.append(False);

			#	Validación: Buscar ficha hacia centro-izquierda.
			columna_auxiliar = (columna - 1);

			#	Rango para celdas dentro del tablero.
			if (columna_auxiliar < 5 and columna_auxiliar > 0):
				#	Busqueda: Ficha objetivo.
				if (tablero[fila][columna_auxiliar] == jugador_objetivo):
					for iterador in range(columna_auxiliar):
						#	Busqueda: Ficha jugador.
						if (tablero[fila][(columna_auxiliar - iterador - 1)] == jugador):
							#	Recordatorio: editar aquí para insertar la IA.
							if (puede_editar):
								self.convertir_fichas(fila, fila, columna_auxiliar, (columna_auxiliar - iterador - 1), "CENTRO-IZQUIERDA");

							elif not (puede_editar):
								print("[DEV][GAME][validacion_jugadas] Se valido la jugada pero no se edito.");
							else:
								print("[DEV][GAME][ERROR][validacion_jugadas]");
								print("[>] Error al verificar la edición del tablero.");
							
							#	Agregamos la validación a la lista de validaciones.
							validaciones.append(True);

				#	Busqueda: No se encuentra a la ficha objetivo.
				else:
					validaciones.append(False);
			#	La celda no esta en el rango determinado.
			else:
				validaciones.append(False);

			#	Validación: Buscar ficha hacia abajo.
			fila_auxiliar = (fila + 1);

			#	Rango para celdas dentro del tablero.
			if (fila_auxiliar < 5 and fila_auxiliar > 0):
				#	Busqueda: Ficha objetivo.
				if (tablero[fila_auxiliar][columna] == jugador_objetivo):
					for iterador in range((5 - fila_auxiliar)):
						#	Busqueda: Ficha jugador.
						if (tablero[(fila_auxiliar + iterador + 1)][(columna)] == jugador):
							#	Recordatorio: editar aquí para insertar la IA.
							if (puede_editar):
								self.convertir_fichas(fila, (fila_auxiliar + iterador + 1), columna, columna, "ABAJO");

							elif not (puede_editar):
								print("[DEV][GAME][validacion_jugadas] Se valido la jugada pero no se edito.");
							else:
								print("[DEV][GAME][ERROR][validacion_jugadas]");
								print("[>] Error al verificar la edición del tablero.");
							
							#	Agregamos la validación a la lista de validaciones.
							validaciones.append(True);

				#	Busqueda: No se encuentra a la ficha objetivo.
				else:
					validaciones.append(False);
			#	La celda no esta en el rango determinado.
			else:
				validaciones.append(False);

			#	Validación: Buscar ficha hacia abajo-derecha.
			fila_auxiliar = (fila + 1);
			columna_auxiliar = (columna + 1);

			#	Rango para celdas dentro del tablero.
			if (fila_auxiliar < 5 and fila_auxiliar > 0) and (columna_auxiliar < 5 and columna_auxiliar > 0):
				par = [(5 - fila_auxiliar), (5 - columna_auxiliar)];
				rango = min(par);

				#	Busqueda: Ficha objetivo.
				if (tablero[fila_auxiliar][columna_auxiliar] == jugador_objetivo):
					for iterador in range((rango)):
						#	Busqueda: Ficha jugador.
						if (tablero[(fila_auxiliar + iterador + 1)][(columna_auxiliar + iterador + 1)] == jugador):
							#	Recordatorio: editar aquí para insertar la IA.
							if (puede_editar):
								self.convertir_fichas(fila, (fila_auxiliar + iterador + 1), columna, (columna_auxiliar + iterador + 1), "ABAJO-DERECHA");

							elif not (puede_editar):
								print("[DEV][GAME][validacion_jugadas] Se valido la jugada pero no se edito.");
							else:
								print("[DEV][GAME][ERROR][validacion_jugadas]");
								print("[>] Error al verificar la edición del tablero.");
							
							#	Agregamos la validación a la lista de validaciones.
							validaciones.append(True);

				#	Busqueda: No se encuentra a la ficha objetivo.
				else:
					validaciones.append(False);
			#	La celda no esta en el rango determinado.
			else:
				validaciones.append(False);

			#	Validación: Buscar ficha hacia abajo-izquierda.
			fila_auxiliar = (fila + 1);
			columna_auxiliar = (columna - 1);

			#	Rango para celdas dentro del tablero.
			if (fila_auxiliar < 5 and fila_auxiliar > 0) and (columna_auxiliar < 5 and columna_auxiliar > 0):
				par = [(5 - fila_auxiliar), columna_auxiliar];
				rango = min(par);

				#	Busqueda: Ficha objetivo.
				if (tablero[fila_auxiliar][columna_auxiliar] == jugador_objetivo):
					for iterador in range((rango)):
						#	Busqueda: Ficha jugador.
						if (tablero[(fila_auxiliar + iterador + 1)][(columna_auxiliar - iterador - 1)] == jugador):
							#	Recordatorio: editar aquí para insertar la IA.
							if (puede_editar):
								self.convertir_fichas(fila, (fila_auxiliar + iterador + 1), columna, (columna_auxiliar - iterador - 1), "ABAJO-IZQUIERDA");

							elif not (puede_editar):
								print("[DEV][GAME][validacion_jugadas] Se valido la jugada pero no se edito.");
							else:
								print("[DEV][GAME][ERROR][validacion_jugadas]");
								print("[>] Error al verificar la edición del tablero.");
							
							#	Agregamos la validación a la lista de validaciones.
							validaciones.append(True);

				#	Busqueda: No se encuentra a la ficha objetivo.
				else:
					validaciones.append(False);
			#	La celda no esta en el rango determinado.
			else:
				validaciones.append(False);

			#	Comprobación de las validaciones.
			if (True in validaciones):
				#	Al menos una jugada es valida.
				return True;

			elif not(True in validaciones):
				#	Ninguna jugada es valida.
				return False;

			else:
				print("[DEV][GAME][ERROR][validacion_jugadas]");
				print("[>] Error al determinar las verificaciones.");
				return False;
			
		#	La celda no tiene adyacente.
		elif (not(tiene_adyacente)):
			return False;

		#	Error: no se determino la adyacencia.
		else:
			print("[DEV][GAME][ERROR][validacion_jugadas]");
			print("[>] Error al determinar el modo de convertir.");
			return False;
		

	def realizar_vistazos(self, fila:int, columna:int, modo:str) -> bool:
		"""..."""

		#	Traemos el tablero.
		tablero = self.GET_estado_juego();
		# self.mostrar_tablero();

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
				print("[DEV][GAME][ERROR][realizar_vistazos][ARRIBA]");
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
				print("[DEV][GAME][ERROR][realizar_vistazos][ARRIBA-DERECHA]");
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
				print("[DEV][GAME][ERROR][realizar_vistazos][ARRIBA-IZQUIERDA]");
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
				print("[DEV][GAME][ERROR][realizar_vistazos][CENTRO-DERECHA]");
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
				print("[DEV][GAME][ERROR][realizar_vistazos][CENTRO-IZQUIERDA]");
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
				print("[DEV][GAME][ERROR][realizar_vistazos][ABAJO]");
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
				print("[DEV][GAME][ERROR][realizar_vistazos][ABAJO-DERECHA]");
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
				print("[DEV][GAME][ERROR][realizar_vistazos][ABAJO-IZQUIERDA]");
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
		# self.mostrar_tablero();

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
			

	def comprobar_finalizacion(self) -> bool: # , coordenadas:Tuple[int,int]
		"""..."""

		#	Traemos el estado del juego.
		# fila:int = coordenadas[0];
		# columna:int = coordenadas[1];
		tablero = self.GET_estado_juego();

		#	CASO 1: No quedan casillas vacias.
		if not (0 in tablero):
			#	Se retorna True dado que, el juego SI termino.
			self.SET_terminado(True);
			return True;

		#	CASO 2: No quedan más movimientos para la ficha blanca.
		#	CASO 3: No quedan más movimientos para la ficha negra.
		# elif (self.validacion_jugadas((fila, columna))):
		# 	print("[DEV][GAME][comprobar_finalizacion] quedan movimientos.")
		# 	self.SET_terminado(False);
		# 	return False;

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
		print(f"[DEV][GAME][iniciar_jugabilidad] fila: {fila}, columna: {columna}")

		#	Definiendo la edición.
		#	Se configura como False, dado que no puede editar el tablero antes de jugar el turno.
		self.SET_puede_editar(False);

		#	Definiendo de quien es el turno.
		self.SET_jugador(color_ficha);

		#	Comprobar si el juego termino.
		esta_terminado:bool = self.comprobar_finalizacion();
		esta_vacia:bool = self.comprobar_vacia((fila, columna));

		#	Comprobaciones: Determinar si se puede o no jugar...
		if (esta_terminado):
			#	El juego termino.
			print("[DEV][GAME][PRE-GAME] el juego termino.");
			
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
					if (self.validacion_jugadas(coordenadas=(fila, columna))):
						#	Se habilita la edición.
						self.SET_puede_editar(True);
						validacion = self.validacion_jugadas(coordenadas=(fila, columna));

						#	Se deshabilita la edición.
						self.SET_puede_editar(False);

						print("[DEV] POST GAME");
						# self.mostrar_tablero();

						#	Realizar cambio de turnos.
						turnos:List[bool] = self.GET_turnos();
						nuevos_turnos:List[bool] = [not(turnos[0]), not(turnos[1])];
						self.SET_turnos(nuevos_turnos);

						#	Re-Comprobación: Verificar si el juego termino. Para actualizar la GUI.
						esta_terminado = self.comprobar_finalizacion();
						if (esta_terminado):
							print("[DEV][GAME][POST-GAME] el juego termino.");
						elif not (esta_terminado):
							print("[DEV][GAME][POST-GAME] el juego no termino.");

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
					 print(str(int(elemento)) + " |", end="");
				print(end="\n");
		print("-"*12);

	#	Getters & Setters.
	#		INTELIGENCIA ARTIFICIAL.
	def GET_inteligencia(self) -> Any:
		return self.INTELIGENCIA;

	def SET_inteligencia(self, nueva_ia:Any) -> None:
		self.INTELIGENCIA = nueva_ia;
	
	#		PUEDE_EDITAR.
	def GET_puede_editar(self) -> bool:
		return self.PUEDE_EDITAR;

	def SET_puede_editar(self, nueva_configuracion:bool) -> None:
		self.PUEDE_EDITAR = nueva_configuracion;

	#		TURNOS.
	def GET_turnos(self) -> List[bool]:
		return self.TURNOS;

	def SET_turnos(self, nuevos_turnos:List[bool]) -> None:
		self.TURNOS = nuevos_turnos;

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
