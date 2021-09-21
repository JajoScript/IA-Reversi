import copy
from GAME import *

def alfabeta(juego:Reversi,estado_inicial:list,profundidad:int,etapa:int,alfa:int,beta:int,secuencia:list,secuencias:list) -> list:
	if juego.Estado_final(profundidad):
		secuencias.append(secuencia.copy())
		return [-1*juego.utilidad]
	if etapa==1:
		valor = [-1000, None]
		jugadas_posibles = juego.Generador_Jugadas_validas(1)
	else:
		valor = [1000, None]
		jugadas_posibles = juego.Generador_Jugadas_validas(2)
	for jugada in jugadas_posibles:
		juego.Devolver_estado(estado_inicial)
		if etapa==1:
			juego.Jugar(jugada,1)
		else:
			juego.Jugar(jugada,2)
		copia=copy.deepcopy(juego.tablero)
		secuencia.append(jugada)
		opcion = alfabeta(juego,copia,profundidad+1,etapa*-1,alfa,beta,secuencia,secuencias)
		if etapa==1:
			if valor[0]<opcion[0]:
				valor=[opcion[0],jugada]
			if valor[0]>alfa:
				alfa=valor[0]
			if valor[0]>=beta:
				juego.Devolver_estado(estado_inicial)
				secuencia.pop()
				break
		else:
			if valor[0]>opcion[0]:
				valor=[opcion[0],jugada]
			if valor[0]<beta:
				beta=valor[0]
			if valor[0]<=alfa:
				juego.Devolver_estado(estado_inicial)
				secuencia.pop()
				break
		juego.Devolver_estado(estado_inicial)
		secuencia.pop()
	return valor

	
