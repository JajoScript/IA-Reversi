import copy
from Juego import *

""""
PARAMETROS

JUEGO :ES UN OBJETO DE TIPO JUEGO, DE EL DEBIAN SALIR TODAS LAS FUNCIONES QUE SE USAN EN EL MINIMAX
ESTADO_INICIAL :ES UNA MATRIZ QUE REPRESENTA EL ESTADO DE JUEGO ANTES QUE JUEGUEN LAS BLANCAS
                LO MEJOR ES USAR UNA COPIA
PROFUNDIDAD: VALOR QUE IRA AUMENTANDO RECURSIVAMENTE HASTA LLEGAR A LA PROFUNDIDAD QUE DEPENDE DE LA DIFICULTAD
ETAPA: VALOR QUE REPRESENTA SI SOMOS MAX O MIN (1:MAX, -1:MIN)
SECUENCIA Y SECUENCIAS SON LISTAS EN LAS CUALES SE VAN AÑADIENDO LAS JUGADAS

EL MINIMAX SE LLAMARA ASI: MINIMAX(JUEGO,ESTADO_JUEGO,0,1,[],[]) Y RETORNARA UNA LISTA DE LA FORMA [UTILIDAD,[JUGADA]]
"""

def minimax(juego,estado_inicial,profundidad,etapa,secuencia,secuencias):
    #ESTA FUNCION DEBE EVALUAR SI EL TABLERO SE LLENO O SI SE ALCANZO UNA DETERMINADA PROFUNDIDAD
    #QUE DEPENDE DE LA DIFICULTAD
	"""
	def Evaluar(self,profundidad:int) -> None:

		if self.Tablero_completo(self.tablero) or profundidad == self.dificultad:
			self.completo=True
		else:
			self.completo=False
		blancas=0	#nº fichas blancas en el tablero
		negras=0	#nº fichas negras en el tablero
		
		#si se completo el tablero o se alcanzo la profundidad deseada( minimax o alfabeta )
		if self.completo:
			for i in range(6):
				for j in range(6):
					if self.tablero[i][j]==1:
						blancas=blancas+1
					if self.tablero[i][j]==2:
						negras=negras+1
			self.utilidad=negras-blancas
			
	def Estado_final(self,profundidad:int) -> bool:
		self.Evaluar(profundidad)
		if self.completo:
			return True
		else:
			return False
	"""
	if juego.Estado_final(profundidad):
		secuencias.append(secuencia.copy())
        #UTILIDAD = NEGRAS - BLANCAS
		return [-1*juego.utilidad]
	if etapa == 1:
		valor = [-1000, None]
        #AQUI SE USA LA FUNCION QUE DEVUELVE LA LISTA CON JUGADAS VALIDAD PARA CADA COLOR
		jugadas_posibles = juego.Generador_Jugadas_validas(1)
	else:
		valor = [1000, None]
        #AQUI SE USA LA FUNCION QUE DEVUELVE LA LISTA CON JUGADAS VALIDAD PARA CADA COLOR
		jugadas_posibles = juego.Generador_Jugadas_validas(2)
		
	for jugada in jugadas_posibles:
		if etapa==1:
            #SE USA LA FUNCION PARA APLICAR LA JUGADA
			juego.Jugar(jugada,1)
		else:
            #SE USA LA FUNCION PARA APLICAR LA JUGADA
			juego.Jugar(jugada,2)

        #SE GENERA UNA COPIA DEL ESTADO ACTUAL DEL JUEGO PARA PODER REVERTIR JUGADAS
		copia=copy.deepcopy(juego.tablero)
		secuencia.append(jugada)
		opcion = minimax(juego,copia,profundidad+1,etapa*-1,secuencia,secuencias)
		
		if etapa == 1:
			if valor[0] < opcion[0]:
				valor = [opcion[0], jugada]
		else:
			if valor[0] > opcion[0]:
				valor = [opcion[0], jugada]
		
		#ESTA FUNCION HACE QUE EL TABLERO DE JUEGO SEA IGUAL A LA MATRIZ QUE SE LE PASE COMO PARAMETRO A LA FUNCION
		"""	def Devolver_estado(self,estado:list) -> None:
		for i in range(6):
			for j in range(6):
				#Usamos deepcopy para que el minimax o el alfabeta realice cambios en copias y no en el tablero
				self.tablero[i][j]=copy.deepcopy(estado[i][j])
                
        """
		juego.Devolver_estado(estado_inicial)
		secuencia.pop()
	return valor




#EL ALFABETA ES LA MISMA HISTORIA QUE CON EL MINIMAX
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