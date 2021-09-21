import copy

class Reversi:

	def __init__(self,tablero:list) -> None:

		#Lista de listas que representa el tablero, la entrega la GUI
		self.tablero= tablero

		#Booleano que indica si todas las casillas han sido ocupadas o si ya no se pueden realizar mas jugadas
		self.completo= False

		#Entero que indica la ganancia de cierto estado final, se calcula como negras-blancas
		self.utilidad= None

		#Booleano que restringe la funcion convertir, para verificar si una jugada es valida sin aplicarla
		self.generando_jugadas=False

		#Enetero que representa el nivel de profundidad que usara el minimax o el alfabeta
		self.dificultad=None

	def Permite_salto(self,coordenada:list,color:int) -> bool:

		"""Esta funcion evalua si al posicionar una ficha en la coordenada de tablero pasada como parametro es posible saltar 
			al menos una ficha del rival. Para esto se evaluan las 8 direcciones posibles hasta llegar al limite del tablero
			en busca de una o varias fichas del color contrario seguidas por una ficha del color que se pase como parametro.
			
			En caso de encontrar dicha situacion, la funcion convertira automaticamente todas las fichas del color contrario al color
			pasado como parametro. Una vez analizadas las 8 direcciones la funcion retornara verdadero si en al menos una direccion se pudo realizar
			el salto, de lo contrario retornara falso"""

		#coordenadas
		fila = coordenada[0]
		columna = coordenada[1]

		#lista de direciones en las que se podia saltar
		key=[False]*8

		#La coordenada en donde se desea posicionar la ficha debe ser adyacente a alguna ficha ya puesta
		if self.Es_adyacente(coordenada):

			#Por cada direccion se analiza si permite el salto

			#abajo
			aux = columna+1
			if aux<5 and aux>0:
				if color==1:
					if self.tablero[fila][aux]==2:
						for i in range(5-aux):
							if self.tablero[fila][aux+i+1]==1:
								if not self.generando_jugadas:
									self.Convertir([fila,aux],[fila,aux+i+1],"derecha",1)
								key[0]=True
				if color==2:
					if self.tablero[fila][aux]==1:
						for i in range(5-aux):
							if self.tablero[fila][aux+i+1]==2:
								if not self.generando_jugadas:
									self.Convertir([fila,aux],[fila,aux+i+1],"derecha",2)
								key[0]=True
			#arriba
			aux = columna-1
			if aux<5 and aux>0:
				if color==1:
					if self.tablero[fila][aux]==2:
						for i in range(aux):
							if self.tablero[fila][aux-i-1]==1:
								if not self.generando_jugadas:
									self.Convertir([fila,aux],[fila,aux-i-1],"izquierda",1)
								key[1]=True
				if color==2:
					if self.tablero[fila][aux]==1:
						for i in range(aux):
							if self.tablero[fila][aux-i-1]==2:
								if not self.generando_jugadas:
									self.Convertir([fila,aux],[fila,aux-i-1],"izquierda",2)
								key[1]=True
			#derecha
			aux = fila+1
			if aux<5 and aux>0:
				if color==1:
					if self.tablero[aux][columna]==2:
						for i in range(5-aux):
							if self.tablero[aux+i+1][columna]==1:
								if not self.generando_jugadas:
									self.Convertir([fila,columna],[aux+i+1,columna],"abajo",1)
								key[2]=True
				if color==2:
					if self.tablero[aux][columna]==1:
						for i in range(5-aux):
							if self.tablero[aux+i+1][columna]==2:
								if not self.generando_jugadas:
									self.Convertir([fila,columna],[aux+i+1,columna],"abajo",2)
								key[2]=True
			#izquierda
			aux = fila-1
			if aux<5 and aux>0:
				if color==1:
					if self.tablero[aux][columna]==2:
						for i in range(aux):
							if self.tablero[aux-i-1][columna]==1:
								if not self.generando_jugadas:
									self.Convertir([fila,columna],[aux-i-1,columna],"arriba",1)
								key[3]=True
				if color==2:
					if self.tablero[aux][columna]==1:
						for i in range(aux):
							if self.tablero[aux-i-1][columna]==2:
								if not self.generando_jugadas:
									self.Convertir([fila,columna],[aux-i-1,columna],"arriba",2)
								key[3]=True
			#abajo-izquerda
			aux = fila-1
			aux2 = columna+1
			if aux<5 and aux>0 and aux2<5 and aux2>0:
				par = [aux,5-aux2]
				if color==1:
					rango = min(par)
					if self.tablero[aux][aux2]==2:
						for i in range(rango):
							if self.tablero[aux-i-1][aux2+i+1]==1:
								if not self.generando_jugadas:
									self.Convertir([fila,columna],[aux-i-1,aux2+i+1],"arriba-derecha",1)
								key[4]=True
				if color==2:
					rango = min(par)
					if self.tablero[aux][aux2]==1:
						for i in range(rango):
							if self.tablero[aux-i-1][aux2+i+1]==2:
								if not self.generando_jugadas:
									self.Convertir([fila,columna],[aux-i-1,aux2+i+1],"arriba-derecha",2)
								key[4]=True

			#arriba-izquierda
			aux = fila-1
			aux2 = columna-1
			if aux<5 and aux>0 and aux2<5 and aux2>0:
				par = [aux,aux2]
				if color==1:
					rango = min(par)
					if self.tablero[aux][aux2]==2:
						for i in range(rango):
							if self.tablero[aux-i-1][aux2-i-1]==1:
								if not self.generando_jugadas:
									self.Convertir([fila,columna],[aux-i-1,aux2-i-1],"arriba-izquierda",1)
								key[5]=True
				if color==2:
					rango = min(par)
					if self.tablero[aux][aux2]==1:
						for i in range(rango):
							if self.tablero[aux-i-1][aux2-i-1]==2:
								if not self.generando_jugadas:
									self.Convertir([fila,columna],[aux-i-1,aux2-i-1],"arriba-izquierda",2)
								key[5]=True
			#abajo-derecha
			aux = fila+1
			aux2 = columna+1
			if aux<5 and aux>0 and aux2<5 and aux2>0:
				par = [5-aux,5-aux2]
				if color==1:
					rango = min(par)
					if self.tablero[aux][aux2]==2:
						for i in range(rango):
							if self.tablero[aux+i+1][aux2+i+1]==1:
								if not self.generando_jugadas:
									self.Convertir([fila,columna],[aux+i+1,aux2+i+1],"abajo-derecha",1)
								key[6]=True
				if color==2:
					rango = min(par)
					if self.tablero[aux][aux2]==1:
						for i in range(rango):
							if self.tablero[aux+i+1][aux2+i+1]==2:
								if not self.generando_jugadas:
									self.Convertir([fila,columna],[aux+i+1,aux2+i+1],"abajo-derecha",2)
								key[6]=True
			#arriba-derecha
			aux = fila+1
			aux2 = columna-1
			if aux<5 and aux>0 and aux2<5 and aux2>0:
				par = [5-aux,aux2]
				if color==1:
					rango = min(par)
					if self.tablero[aux][aux2]==2:
						for i in range(rango):
							if self.tablero[aux+i+1][aux2-i-1]==1:
								if not self.generando_jugadas:
									self.Convertir([fila,columna],[aux+i+1,aux2-i-1],"abajo-izquierd",1)
								key[7]=True
				if color==2:
					rango = min(par)
					if self.tablero[aux][aux2]==1:
						for i in range(rango):
							if self.tablero[aux+i+1][aux2-i-1]==2:
								if not self.generando_jugadas:
									self.Convertir([fila,columna],[aux+i+1,aux2-i-1],"abajo-izquierda",2)
								key[7]=True
			
			if True in key:
				return True
			else:
				return False
		else:
			return False

	def Esta_vacia(self,coordenada:list) -> bool:

		"""Esta funcion verifica si la coordenada del tablero en donde se desea poner una ficha no esta ocupada"""

		if self.tablero[coordenada[0]][coordenada[1]] == 0:
			return True
		else:
			return False

	def Es_adyacente(self,coordenada:list) -> bool:

		""" Verifica si alrededor de la coordenada de tablero donde se desea poner una ficha hay alguna otra ficha, si no es adyacente
			se sabe de inmediato que tampoco permite el salto, por lo cual se considerara como jugada invalida.
			
			Retorna verdadero en caso de haber alguna ficha adyacente, independiente del color"""

		x=coordenada[0] # FILA
		y=coordenada[1] # COLUMNA

		#Busqueda en el interior del tablero
		if x<5 and x>0 and y<5 and y>0 :
			if self.tablero[x+1][y]!=0:
				return True
			elif self.tablero[x-1][y]!=0:
				return True
			elif self.tablero[x+1][y+1]!=0:
				return True
			elif self.tablero[x-1][y-1]!=0:
				return True
			elif self.tablero[x+1][y-1]!=0:
				return True
			elif self.tablero[x-1][y+1]!=0:
				return True
			elif self.tablero[x][y+1]!=0:
				return True
			elif self.tablero[x][y-1]!=0:
				return True
			else:
				return False

		#Busqueda en los bordes del tablero
		if x==5 and y>0 and y<5 :
			if self.tablero[x-1][y]!=0:
				return True
			elif self.tablero[x-1][y-1]!=0:
				return True
			elif self.tablero[x-1][y+1]!=0:
				return True
			elif self.tablero[x][y+1]!=0:
				return True
			elif self.tablero[x][y-1]!=0:
				return True
			else:
				return False
		if x==0 and y>0 and y<5:
			if self.tablero[x+1][y]!=0:
				return True
			elif self.tablero[x+1][y+1]!=0:
				return True
			elif self.tablero[x+1][y-1]!=0:
				return True
			elif self.tablero[x][y+1]!=0:
				return True
			elif self.tablero[x][y-1]!=0:
				return True
			else:
				return False
		if y==5 and x<5 and x>0:
			if self.tablero[x+1][y]!=0:
				return True
			elif self.tablero[x-1][y]!=0:
				return True
			elif self.tablero[x-1][y-1]!=0:
				return True
			elif self.tablero[x+1][y-1]!=0:
				return True
			elif self.tablero[x][y-1]!=0:
				return True
			else:
				return False
		if y==0 and x<5 and x>0:
			if self.tablero[x+1][y]!=0:
				return True
			elif self.tablero[x-1][y]!=0:
				return True
			elif self.tablero[x+1][y+1]!=0:
				return True
			elif self.tablero[x-1][y+1]!=0:
				return True
			elif self.tablero[x][y+1]!=0:
				return True
			else:
				return False

		#busqueda en las esquinas del tablero
		if x==0 and y==0:
			if self.tablero[x+1][y]!=0:
				return True
			elif self.tablero[x+1][y+1]!=0:
				return True
			elif self.tablero[x][y+1]!=0:
				return True
			else:
				return False
		if x==0 and y==5:
			if self.tablero[x+1][y]!=0:
				return True
			elif self.tablero[x+1][y-1]!=0:
				return True
			elif self.tablero[x][y-1]!=0:
				return True
			else:
				return False
		if x==5 and y==0:
			if self.tablero[x-1][y]!=0:
				return True
			elif self.tablero[x-1][y+1]!=0:
				return True
			elif self.tablero[x][y+1]!=0:
				return True
			else:
				return False
		if x==5 and y==5:
			if self.tablero[x-1][y]!=0:
				return True
			elif self.tablero[x-1][y-1]!=0:
				return True
			elif self.tablero[x][y-1]!=0:
				return True
			else:
				return False

	def Convertir(self,inicio:list,fin:list,direccion:str,color:int) -> None:

		"""Esta funcion trabaja en conjunto con la funcion Permite_salto(), se encarga de transformar las fichas de un color al color que
			se le pase como parametro, no realiza ningun tipo de analisi, solo realiza la transformacion"""
		
		#coordenada de inicio
		x1=inicio[0]
		y1=inicio[1]

		#coordenada de destino
		x2=fin[0]
		y2=fin[1]

		if direccion=="derecha":
			while y1!=y2:
				self.tablero[x1][y1]=color
				y1=y1+1
		elif direccion=="izquierda":
			while y1!=y2:
				self.tablero[x1][y1]=color
				y1=y1-1
		elif direccion=="arriba":
			while x1!=x2:
				self.tablero[x1][y1]=color
				x1=x1-1
		elif direccion=="abajo":
			while x1!=x2:
				self.tablero[x1][y1]=color
				x1=x1+1
		elif direccion=="arriba-derecha":
			while x1!=x2:
				self.tablero[x1][y1]=color
				x1=x1-1
				y1=y1+1
		elif direccion=="arriba-izquierda":
			while x1!=x2:
				self.tablero[x1][y1]=color
				x1=x1-1
				y1=y1-1
		elif direccion=="abajo-derecha":
			while x1!=x2:
				self.tablero[x1][y1]=color
				x1=x1+1
				y1=y1+1
		elif direccion=="abajo-izquierda":
			while x1!=x2:
				self.tablero[x1][y1]=color
				x1=x1+1
				y1=y1-1

	def Jugar(self,coordenada:list,color:int) -> bool:

		"""Esta funcion sirve para posicionar la ficha en el tablero, utiliza las tres anteriores funciones para verificar que es
			posible posicionar la ficha del color que se le pase como parametro"""

		if color==2 and self.Esta_vacia(coordenada) and self.Es_adyacente(coordenada) and self.Permite_salto(coordenada,2):
			self.tablero[coordenada[0]][coordenada[1]]=2
			return True
		elif color==1 and self.Esta_vacia(coordenada) and self.Es_adyacente(coordenada) and self.Permite_salto(coordenada,1):
			self.tablero[coordenada[0]][coordenada[1]]=1
			return True
		else:
			return False

	def Generador_Jugadas_validas(self,color:int) -> list:

		""" Esta funcion retornara una lista con las posibles jugadas para el color que se le pase como parametro
			para hacerlo utiliza las funciones que usa la funcion Jugar() salvo la funcion convertir(), pues no queremos
			modificar el tablero de juego mientras llenamos la lista"""

		#Se fija esta variable en true para que la funcion Permite_salto() no convierta ninguna ficha del tablero
		self.generando_jugadas=True
		Jugadas_posibles=[]
		if color==2:
			for i in range(6):
				for j in range(6):
					if self.Esta_vacia([i,j]) and self.Es_adyacente([i,j]) and self.Permite_salto([i,j],2):
						Jugadas_posibles.append([i,j])
		elif color==1:
			for i in range(6):
				for j in range(6):
					if self.Esta_vacia([i,j]) and self.Es_adyacente([i,j]) and self.Permite_salto([i,j],1):
						Jugadas_posibles.append([i,j])
		self.generando_jugadas=False
		return Jugadas_posibles

	def Evaluar(self,profundidad:int) -> None:

		"""Esta funcion analiza el estado de juego en el algoritmo de minimax o alfabeta, ademas de calcular la utilidad de las
			jugadas que se exploren"""		

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
		
		""" Esta funcion es utilizada por el algoritmo de minimax y alfabeta, sirve para reconocer si se ha llegado a un estado
			terminal, o en este caso, se alcanzo la profundidad deseada, la profundidad dependera de la dficultad"""

		self.Evaluar(profundidad)
		if self.completo:
			return True
		else:
			return False

	def Devolver_estado(self,estado:list) -> None:
		"""Se utiliza en el algoritmo de minimax o alfabeta, permite devolver el tablero de juego al estado previo del analisis de jugada"""
		for i in range(6):
			for j in range(6):
				#Usamos deepcopy para que el minimax o el alfabeta realice cambios en copias y no en el tablero
				self.tablero[i][j]=copy.deepcopy(estado[i][j])

	def Puede_jugar(self,jugador:int) -> bool:
		"""Evalua si el jugador puede seguir jugando dada determinado estado del tablero"""
		jugadas_posibles=[]
		if jugador==1:
			jugadas_posibles=self.Generador_Jugadas_validas(1)
		else:
			jugadas_posibles=self.Generador_Jugadas_validas(2)
		if len(jugadas_posibles)==0:
			return False
		else:
			return True

	def Tablero_completo(self,matriz:list) -> bool:
		"""Evalua si ya se ha llenado todo el tablero de juego"""
		for i in range(6):
			for j in range(6):
				if matriz[i][j]==0:
					return False
		return True

	def Contar_fichas(self,color:int) -> int:
		"""Cuenta el numero de fichas del color que se le pase como parametro en un estado especifico del juego"""
		fichas=0
		if color==1:
			for i in range(6):
				for j in range(6):
					if self.tablero[i][j]==1:
						fichas=fichas+1
		if color==2:
			for i in range(6):
				for j in range(6):
					if self.tablero[i][j]==2:
						fichas=fichas+1
		return fichas

	def Resetear_tablero(self):
		for i in range(6):
			for j in range(6):
				self.tablero[i][j]=0
		self.tablero[2][2] = 1;
		self.tablero[3][3] = 1;
		self.tablero[3][2] = 2;
		self.tablero[2][3] = 2;
