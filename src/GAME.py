# Dependencias.
from typing import Any

# Definición de funciones.
def controlador_turnos(ventana, fuente_juego, TURNO_BLANCA: bool, TURNO_NEGRA:bool) -> Any:
	""" ... """
	print("[DEV] gestionando turnos...");
	pass


def validacion_movimiento_blancas(estado_juego, coordenadas) -> bool:
	""" ... """

	fila: int = coordenadas[0];
	columna:int = coordenadas[1];

	# Validaciones.
	# Recordatorio: Esto se puede simplificar con un arreglo definido.
	validacion_1:bool = False;
	validacion_2:bool = False;
	validacion_3:bool = False;
	validacion_4:bool = False;
	validacion_5:bool = False;
	validacion_6:bool = False;
	validacion_7:bool = False;
	validacion_8:bool = False;

	if (controlador_adyacentes(estado_juego, coordenadas)):
		# Busqueda: Ficha negra a la derecha.
		auxiliar:int = columna + 1;

		if (auxiliar < 5) and (auxiliar > 0):
			if estado_juego[fila][auxiliar] == 2:
				for i in range(5 - auxiliar):
					if (estado_juego[fila][auxiliar + i + 1] == 1):
						controlador_convertir_fichas(estado_juego, fila, fila, auxiliar, (auxiliar + i + 1), "cde", 1)
						validacion_1 = True;
			else:
				validacion_1 = False;
		else:
			validacion_1 = False

		# Busqueda: Ficha Negra a la izquierda.
		auxiliar = columna - 1;

		if (auxiliar < 5) and (auxiliar > 0):
			if (estado_juego[fila][auxiliar] == 2):
				for i in range(auxiliar):
					if (estado_juego[fila][auxiliar - i - 1] == 1):
						controlador_convertir_fichas(estado_juego, fila, fila, auxiliar, (auxiliar - i - 1), "ciz", 1);
						validacion_2 = True;
			else:
				validacion_2 = False;
		else: 
			validacion_2 = False;

		# Busqueda: Ficha negra abajo.
		auxiliar = fila + 1;

		if (auxiliar < 5) and (auxiliar > 0):
			if (estado_juego[auxiliar][columna] == 2):
				for i in range(5 - auxiliar):
					if (estado_juego[auxiliar + i + 1][columna] == 1):
						controlador_convertir_fichas(estado_juego, fila, (auxiliar + i + 1), columna, columna, "abc", 1);
						validacion_3 = True;
			else:
				validacion_3 = False;
		else: 
			validacion_2 = False;

		# Busqueda: Ficha negra arriba.
		auxiliar = fila - 1;

		if (auxiliar < 5) and (auxiliar > 0):
			if (estado_juego[auxiliar][columna] == 2):
				for i in range(auxiliar):
					if (estado_juego[auxiliar - i - 1][columna] == 1):
						controlador_convertir_fichas(estado_juego, fila, (auxiliar - i - 1), columna, columna, "arc", 1);
						validacion_4 = True;
			else:
				validacion_4 = False;
		else: 
			validacion_4 = False;

		# Busqueda: Ficha negra diagonal arriba derecha.
		auxiliar = (fila - 1);
		auxiliar_2:int = (columna + 1);

		if (auxiliar < 5) and (auxiliar > 0) and (auxiliar_2 < 5) and (auxiliar_2 > 0):
			par:list[int] = [auxiliar, (5 - auxiliar_2)];
			rango = min(par);
			
			if estado_juego[auxiliar][auxiliar_2]==2:
				for i in range(rango):
					if (estado_juego[(auxiliar - i - 1)][(auxiliar_2 + i + 1)] == 1):
						controlador_convertir_fichas(estado_juego, fila, (auxiliar - i- 1), columna, (auxiliar_2 + i + 1), "arde",1)
						validacion_5 = True;
			else:
				validacion_5 = False;
		else:
			validacion_5 = False;

		# Busqueda: Ficha negra diagonal arriba izquierda.
		auxiliar = (fila - 1);
		auxiliar_2 = (columna - 1);

		if (auxiliar < 5) and (auxiliar > 0) and (auxiliar_2 < 5) and (auxiliar_2 > 0):
			par = [auxiliar, auxiliar_2];
			rango = min(par);

			if (estado_juego[auxiliar][auxiliar_2] == 2):
				for i in range(rango):
					if (estado_juego[(auxiliar - i - 1)][auxiliar_2 - i - 1] == 1):
						controlador_convertir_fichas(estado_juego, fila, (auxiliar - i - 1), columna, (auxiliar_2 - i - 1), "ariz", 1)
						validacion_6 = True;
			else:
				validacion_6 = False;
		else:
			validacion_6 = False;

		# Busqueda: Ficha negra diagonal abajo derecha.
		auxiliar = (fila + 1);
		auxiliar_2 = (columna + 1);

		if (auxiliar < 5) and (auxiliar > 0) and (auxiliar_2 < 5) and (auxiliar_2 > 0):
			par = [ (5 - auxiliar), (5 - auxiliar_2)];
			rango = min(par);
			
			if (estado_juego[auxiliar][auxiliar_2] == 2):
				for i in range(rango):
					if estado_juego[(auxiliar + i + 1)][auxiliar_2+i+1]==1:
						controlador_convertir_fichas(estado_juego, fila, (auxiliar + i + 1), columna, (auxiliar_2 + i + 1), "abde", 1)
						validacion_7 = True;
			else:
				validacion_7 = False;
		else:
			validacion_7 = False;

		# Busqueda: Ficha negra diagonal abajo izquierda.
		auxiliar = (fila + 1);
		auxiliar_2 = (columna - 1);
		
		if (auxiliar < 5) and (auxiliar > 0) and (auxiliar_2 < 5) and (auxiliar_2 > 0):
			par = [5-auxiliar,auxiliar_2];
			rango = min(par);
			
			if (estado_juego[auxiliar][auxiliar_2] == 2):
				for i in range(rango):
					if (estado_juego[(auxiliar + i + 1)][(auxiliar_2 - i - 1)] == 1):
						controlador_convertir_fichas(estado_juego, fila,(auxiliar + i + 1), columna, (auxiliar_2 - i - 1), "abiz", 1)
						validacion_8 = True;
			else:
				validacion_8 = False;
		else:
			validacion_8 = False;

		# Analisis de validaciones.	
		if (validacion_1) or (validacion_2) or (validacion_3) or (validacion_4) or (validacion_5) or (validacion_6) or (validacion_7) or (validacion_8):
			return True;
		else:
			return False;
	else:
		return False;

def validacion_movimiento_negras(estado_juego:list[list[int]], coordenadas:list[int]) -> bool:
	""" ... """

	fila:int = coordenadas[0];
	columna: int = coordenadas[1];

	validacion_1:bool = False; 
	validacion_2:bool = False; 
	validacion_3:bool = False; 
	validacion_4:bool = False; 
	validacion_5:bool = False; 
	validacion_6:bool = False; 
	validacion_7:bool = False; 
	validacion_8:bool = False;

	if controlador_adyacentes(estado_juego, coordenadas):
		# Busqueda: Ficha negra derecha.
		auxiliar:int = (columna + 1);

		if (auxiliar < 5) and (auxiliar > 0):
			if (estado_juego[fila][auxiliar] == 1):
				for i in range(5 - auxiliar):
					if estado_juego[fila][auxiliar+i+1] == 2:
						controlador_convertir_fichas(estado_juego, fila, fila, auxiliar, (auxiliar + i + 1), "cde", 2)
						validacion_1 = True;
			else:
				validacion_1 = False;
		else:
			validacion_1 = False

		# Busqueda: Ficha negra izquierda.
		auxiliar = (columna - 1);
		
		if (auxiliar < 5) and (auxiliar > 0):
			if (estado_juego[fila][auxiliar] == 1):
				for i in range(auxiliar):
					if (estado_juego[fila][(auxiliar - i - 1)] == 2):
						controlador_convertir_fichas(estado_juego, fila, fila, auxiliar, (auxiliar - i - 1), "ciz", 2);
						validacion_2 = True;
			else:
				validacion_2 = False;
		else:
			validacion_2 = False;

		# Busqueda: Ficha negra abajo.
		auxiliar = (fila + 1);
		if (auxiliar < 5) and (auxiliar > 0):
			if (estado_juego[auxiliar][columna] == 1):
				for i in range((5 - auxiliar)):
					if (estado_juego[auxiliar+i+1][columna] == 2):
						controlador_convertir_fichas(estado_juego, fila, (auxiliar + i + 1), columna, columna, "abc", 2);
						validacion_3 = True;
			else:
				validacion_3 = False;
		else:
			validacion_3 = False;

		# Busqueda: Ficha negra arriba.
		auxiliar = (fila - 1);
		if (auxiliar < 5) and (auxiliar > 0):
			if (estado_juego[auxiliar][columna] == 1):
				for i in range(auxiliar):
					if (estado_juego[(auxiliar - i - 1)][columna] == 2):
						controlador_convertir_fichas(estado_juego, fila, (auxiliar - i - 1), columna, columna, "arc", 2);
						validacion_4 = True;
			else:
				validacion_4 = False;
		else:
			validacion_4 = False;

		# Busqueda: Ficha negra diagonal arriba derecha.
		auxiliar = (fila - 1);
		auxiliar_2:int = (columna + 1);
		
		if (auxiliar < 5) and (auxiliar > 0) and (auxiliar_2 < 5) and (auxiliar_2>0):
			par:list[int] = [auxiliar,5-auxiliar_2];
			rango = min(par);

			if (estado_juego[auxiliar][auxiliar_2] == 1):
				for i in range(rango):
					if (estado_juego[auxiliar-i-1][(auxiliar_2 + i + 1)] == 2):
						controlador_convertir_fichas(estado_juego, fila, (auxiliar - i - 1), columna, (auxiliar_2 + i + 1), "arde", 2)
						validacion_5 = True;
			else:
				validacion_5 = False;
		else:
			validacion_5 = False;

		# Busqueda: Ficha negra diagonal arriba izquierda.
		auxiliar = (fila - 1);
		auxiliar_2 = (columna - 1);
		
		if (auxiliar < 5) and (auxiliar > 0) and (auxiliar_2 < 5) and (auxiliar_2 > 0):
			par = [auxiliar, auxiliar_2];
			rango = min(par)
			
			if (estado_juego[auxiliar][auxiliar_2] == 1):
				for i in range(rango):
					if (estado_juego[(auxiliar - i - 1)][(auxiliar_2 - i - 1)] == 2):
						controlador_convertir_fichas(estado_juego, fila, (auxiliar - i - 1), columna, (auxiliar_2 - i - 1), "ariz", 2);
						validacion_6 = True;
			else:
				validacion_6 = False;
		else:
			validacion_6 = False;

		# Busqueda: Ficha negra diagonal descendente derecha.
		auxiliar = (fila + 1);
		auxiliar_2 = (columna + 1);
		
		if (auxiliar < 5) and (auxiliar > 0) and (auxiliar_2 < 5) and (auxiliar_2 > 0):
			par = [(5 - auxiliar), (5 - auxiliar_2)];
			rango = min(par);

			if (estado_juego[auxiliar][auxiliar_2] == 1):
				for i in range(rango):
					if (estado_juego[(auxiliar + i + 1)][(auxiliar_2 + i + 1)] == 2):
						controlador_convertir_fichas(estado_juego, fila, (auxiliar + i + 1), columna, (auxiliar_2 + i + 1), "abde", 2)
						validacion_7 = True;
			else:
				validacion_7 = False;
		else:
			validacion_7 = False;

		# Busqueda: Ficha negra diagonal descendente izquierda.
		auxiliar = (fila + 1);
		auxiliar_2 = (columna - 1);
		
		if (auxiliar < 5) and (auxiliar > 0) and (auxiliar_2 < 5) and (auxiliar_2 > 0):
			par = [5-auxiliar,auxiliar_2];
			rango = min(par);
			
			if (estado_juego[auxiliar][auxiliar_2] == 1):
				for i in range(rango):
					if (estado_juego[(auxiliar + i + 1)][(auxiliar_2 - i - 1)] == 2):
						controlador_convertir_fichas(estado_juego, fila, (auxiliar + i + 1), columna, (auxiliar_2 - i - 1), "abiz", 2);
						validacion_8 = True;
			else:
				validacion_8 = False;
		else:
			validacion_8 = False;

		# Analisis de validaciones.		
		if (validacion_1) or (validacion_2) or (validacion_3) or (validacion_4) or (validacion_5) or (validacion_6) or (validacion_7) or (validacion_8):
			return True;
		else:
			return False;
	else:
		return False;


def controlador_convertir_fichas(estado_juego:list[list[int]], x1:int, x2:int, y1:int, y2:int, modo:str, color:int)-> None:
	""" ... """

	if		(modo == "cde"):
		while (y1 != y2):
			estado_juego[x1][y1] = color;
			y1 = (y1 + 1);
	
	elif	(modo == "ciz"):
		while (y1 != y2):
			estado_juego[x1][y1] = color;

	elif	(modo == "arc"):
		while	(x1 != x2):
			estado_juego[x1][y1] = color;
			x1 = (x1 - 1);

	elif	(modo == "abc"):
		while	(x1 != x2):
			estado_juego[x1][y1] = color;
			x1 = (x1 + 1);

	elif	(modo == "arde"):
		while	(x1 != x2):
			estado_juego[x1][y1] = color;
			x1 = (x1 - 1);
			y1 = (y1 + 1);
	
	elif	(modo == "ariz"):
		while	(x1 != x2):
			estado_juego[x1][y1] = color;
			x1 = (x1 - 1);
			y1 = (y1 - 1);

	elif	(modo == "abde"):
		while	(x1 != x2):
			estado_juego[x1][y1] = color;
			x1 = (x1 + 1);
			y1 = (y1 + 1);

	elif	(modo == "abiz"):
		while	(x1 != x2):
			estado_juego[x1][y1] = color;
			x1 = (x1 + 1);
			y1 = (y1 -1);


def controlador_vacias(estado_juego:list[list[int]], coordenadas:list[int]) -> bool:
	""" ... """

	if (estado_juego[coordenadas[0]][coordenadas[1]] == 0):
		return True
	else:
		return False


def controlador_adyacentes(estado_juego:list[list[int]], coordenadas:list[int]) -> bool:
	""" ... """

	x:int = coordenadas[0];
	y:int = coordenadas[1];

	# Comprobaciones.
	if	(x < 5) and (x > 0) and (y < 5) and (y > 0):
		if		(estado_juego[x + 1][y] != 0):
			return True;
		elif	(estado_juego[x - 1][y] != 0):
			return True;

		elif	(estado_juego[x][y + 1] != 0):
			return True;
		elif	(estado_juego[x][y - 1] != 0):
			return True;
			
		elif	(estado_juego[x + 1][y + 1] != 0):
			return True;
		elif	(estado_juego[x - 1][y - 1] != 0):
			return True;
		
		elif	(estado_juego[x + 1][y - 1] != 0):
			return True;
		elif	(estado_juego[x - 1][y + 1] != 0):
			return True;
		
		else:
			return False;
	
	if (x == 5) and (y > 0) and (y < 5):
		if		(estado_juego[x - 1][y] != 0):
			return True;
		
		elif	(estado_juego[x - 1][ y - 1] != 0):
			return True;
		elif	(estado_juego[x - 1][ y + 1] != 0):
			return True;
		
		elif	(estado_juego[x][ y + 1] != 0):
			return True;
		elif	(estado_juego[x][ y - 1] != 0):
			return True;

		else:
			return False;
	
	if	(x == 0) and (y > 0) and (y < 5):
		if		(estado_juego[x + 1][y] != 0):
			return True;

		elif	(estado_juego[x + 1][y + 1] != 0):
			return True;
		elif	(estado_juego[x + 1][y - 1] != 0):
			return True;

		elif	(estado_juego[x][y + 1] != 0):
			return True;
		elif	(estado_juego[x][y - 1] != 0):
			return True;
		else:
			return False;
	
	if (y == 5) and (x < 5) and (x > 0):
		if		(estado_juego[x + 1][y] != 0):
			return True;
		elif	(estado_juego[x - 1][y] != 0):
			return True;
		
		elif	(estado_juego[x - 1][y - 1] != 0):
			return True;
		elif	(estado_juego[x + 1][y - 1] != 0):
			return True;

		elif	(estado_juego[x][y - 1] != 0):
			return True;

		else:
			return False;
	
	if	(y == 0) and (x < 5) and (x > 0):
		if		(estado_juego[x + 1][y] != 0):
			return True;
		elif	(estado_juego[x - 1][y] != 0):
			return True;

		elif	(estado_juego[x + 1][y + 1] != 0):
			return True;
		elif	(estado_juego[x - 1][y + 1] != 0):
			return True;

		elif	(estado_juego[x][y + 1] != 0):
			return True;

		else:
			return False; 	

	if	(x == 0) and (y == 0):
		if		(estado_juego[x + 1][y] != 0):
			return True;
		elif	(estado_juego[x + 1][y + 1] != 0):
			return True;
		elif	(estado_juego[x][y + 1] != 0):
			return True;
		else:
			return False;
	
	if (x == 0) and (y == 5):
		if 	(estado_juego[x + 1][y] != 0):
			return True;
		elif	(estado_juego[x + 1][y - 1] != 0):
			return True;
		else:
			return False;

	if (x == 5) and (y == 0):
		if		(estado_juego[x - 1][y] != 0):
			return True;
		elif	(estado_juego[x - 1][y + 1] != 0):
			return True;
		elif	(estado_juego[x][y + 1] != 0):
			return True;
		else:
			return False;

	if (x == 5) and (y == 5):
		if (estado_juego[x - 1][y] != 0):
			return True;
		elif (estado_juego[x - 1][y - 1] != 0):
			return True;
		elif (estado_juego[x][y - 1] != 0):
			return True;
		else:
			return False;
	
	else:
		return False;