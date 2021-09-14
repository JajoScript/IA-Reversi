import copy
 
class Reversi:
	def __init__(self,tablero):
		self.ESTADO_JUEGO= tablero 
		self.completo= False
		self.utilidad= None
		self.generando_jugadas=False
	
	#FUNCIONES PARA EL JUEGO NORMAL
	def Permite_salto_blanca(self,coordenada):
		fila = coordenada[0]
		columna = coordenada[1]
		v1=False;v2=False;v3=False;v4=False;v5=False;v6=False;v7=False;v8=False

		if self.Es_adyacente(coordenada):
			#Buscamos una ficha negra a la derecha
			aux = columna+1
			if aux<5 and aux>0:
				if self.ESTADO_JUEGO[fila][aux]==2:
					for i in range(5-aux):
						if self.ESTADO_JUEGO[fila][aux+i+1]==1:
							if not self.generando_jugadas:
								self.Convertir(fila,fila,aux,aux+i+1,"cde",1)
							v1=True
				else:
					v1=False
			else:
				v1=False

			#Buscamos una ficha negra a la izquierda
			aux = columna-1
			if aux<5 and aux>0:
				if self.ESTADO_JUEGO[fila][aux]==2:
					for i in range(aux):
						if self.ESTADO_JUEGO[fila][aux-i-1]==1:
							if not self.generando_jugadas:
								self.Convertir(fila,fila,aux,aux-i-1,"ciz",1)
							v2=True
				else:
					v2=False
			else:
				v2=False

			#Buscamos una ficha negra hacia abajo
			aux = fila+1
			if aux<5 and aux>0:
				if self.ESTADO_JUEGO[aux][columna]==2:
					for i in range(5-aux):
						if self.ESTADO_JUEGO[aux+i+1][columna]==1:
							if not self.generando_jugadas:
								self.Convertir(fila,aux+i+1,columna,columna,"abc",1)
							v3=True
				else:
					v3=False
			else:
				v3=False

			#Buscamos una ficha negra hacia arriba
			aux = fila-1
			if aux<5 and aux>0:
				if self.ESTADO_JUEGO[aux][columna]==2:
					for i in range(aux):
						if self.ESTADO_JUEGO[aux-i-1][columna]==1:
							if not self.generando_jugadas:
								self.Convertir(fila,aux-i-1,columna,columna,"arc",1)
							v4=True
				else:
					v4=False
			else:
				v4=False

			#Buscamos una ficha negra en la diagonal ascendente derecha
			aux = fila-1
			aux2 = columna+1
			if aux<5 and aux>0 and aux2<5 and aux2>0:
				par = [aux,5-aux2]
				rango = min(par)
				if self.ESTADO_JUEGO[aux][aux2]==2:
					for i in range(rango):
						if self.ESTADO_JUEGO[aux-i-1][aux2+i+1]==1:
							if not self.generando_jugadas:
								self.Convertir(fila,aux-i-1,columna,aux2+i+1,"arde",1)
							v5=True
				else:
					v5=False
			else:
				v5=False

			#Buscamos una ficha negra en la diagonal ascendente izquierda
			aux = fila-1
			aux2 = columna-1
			if aux<5 and aux>0 and aux2<5 and aux2>0:
				par = [aux,aux2]
				rango = min(par)
				if self.ESTADO_JUEGO[aux][aux2]==2:
					for i in range(rango):
						if self.ESTADO_JUEGO[aux-i-1][aux2-i-1]==1:
							if not self.generando_jugadas:
								self.Convertir(fila,aux-i-1,columna,aux2-i-1,"ariz",1)
							v6=True
				else:
					v6=False
			else:
				v6=False

			#Buscamos una ficha negra en la diagonal descendente derecha
			aux = fila+1
			aux2 = columna+1
			if aux<5 and aux>0 and aux2<5 and aux2>0:
				par = [5-aux,5-aux2]
				rango = min(par)
				if self.ESTADO_JUEGO[aux][aux2]==2:
					for i in range(rango):
						if self.ESTADO_JUEGO[aux+i+1][aux2+i+1]==1:
							if not self.generando_jugadas:
								self.Convertir(fila,aux+i+1,columna,aux2+i+1,"abde",1)
							v7=True
				else:
					v7=False
			else:
				v7=False

			#Buscamos una ficha negra en la diagonal descendente izquierda
			aux = fila+1
			aux2 = columna-1
			if aux<5 and aux>0 and aux2<5 and aux2>0:
				par = [5-aux,aux2]
				rango = min(par)
				if self.ESTADO_JUEGO[aux][aux2]==2:
					for i in range(rango):
						if self.ESTADO_JUEGO[aux+i+1][aux2-i-1]==1:
							if not self.generando_jugadas:
								self.Convertir(fila,aux+i+1,columna,aux2-i-1,"abiz",1)
							v8=True
				else:
					v8=False
			else:
				v8=False
			
			if v1 or v2 or v3 or v4 or v5 or v6 or v7 or v8:
				return True
			else:
				return False
		else:
			return False

	def Esta_vacia(self,coordenada):
		if self.ESTADO_JUEGO[coordenada[0]][coordenada[1]] == 0:
			return True
		else:
			return False

	def Permite_salto_negra(self,coordenada):
		fila = coordenada[0]
		columna = coordenada[1]
		v1 = False; v2 = False; v3 = False; v4 = False; v5 = False; v6 = False; v7 = False; v8 = False
		if self.Es_adyacente(coordenada):
			# Buscamos una ficha negra a la derecha
			aux = columna+1
			if aux < 5 and aux > 0:
				if self.ESTADO_JUEGO[fila][aux] == 1:
					for i in range(5-aux):
						if self.ESTADO_JUEGO[fila][aux+i+1] == 2:
							if not self.generando_jugadas:
								self.Convertir(fila,fila,aux,aux+i+1,"cde",2)
							v1 = True
				else:
					v1 = False
			else:
				v1 = False

			# Buscamos una ficha negra a la izquierda
			aux = columna-1
			if aux<5 and aux>0:
				if self.ESTADO_JUEGO[fila][aux]==1:
					for i in range(aux):
						if self.ESTADO_JUEGO[fila][aux-i-1]==2:
							if not self.generando_jugadas:
								self.Convertir(fila,fila,aux,aux-i-1,"ciz",2)
							v2=True
				else:
					v2=False
			else:
				v2=False

			# Buscamos una ficha negra hacia abajo
			aux = fila+1
			if aux<5 and aux>0:
				if self.ESTADO_JUEGO[aux][columna]==1:
					for i in range(5-aux):
						if self.ESTADO_JUEGO[aux+i+1][columna]==2:
							if not self.generando_jugadas:
								self.Convertir(fila,aux+i+1,columna,columna,"abc",2)
							v3=True
				else:
					v3=False
			else:
				v3=False

			# Buscamos una ficha negra hacia arriba
			aux = fila-1
			if aux<5 and aux>0:
				if self.ESTADO_JUEGO[aux][columna]==1:
					for i in range(aux):
						if self.ESTADO_JUEGO[aux-i-1][columna]==2:
							if not self.generando_jugadas:
								self.Convertir(fila,aux-i-1,columna,columna,"arc",2)
							v4=True
				else:
					v4=False
			else:
				v4=False

			# Buscamos una ficha negra en la diagonal ascendente derecha
			aux = fila-1
			aux2 = columna+1
			if aux<5 and aux>0 and aux2<5 and aux2>0:
				par = [aux,5-aux2]
				rango = min(par)
				if self.ESTADO_JUEGO[aux][aux2]==1:
					for i in range(rango):
						if self.ESTADO_JUEGO[aux-i-1][aux2+i+1]==2:
							if not self.generando_jugadas:
								self.Convertir(fila,aux-i-1,columna,aux2+i+1,"arde",2)
							v5=True
				else:
					v5=False
			else:
				v5=False

			# Buscamos una ficha negra en la diagonal ascendente izquierda
			aux = fila-1
			aux2 = columna-1
			if aux<5 and aux>0 and aux2<5 and aux2>0:
				par = [aux,aux2]
				rango = min(par)
				if self.ESTADO_JUEGO[aux][aux2]==1:
					for i in range(rango):
						if self.ESTADO_JUEGO[aux-i-1][aux2-i-1]==2:
							if not self.generando_jugadas:
								self.Convertir(fila,aux-i-1,columna,aux2-i-1,"ariz",2)
							v6=True
				else:
					v6=False
			else:
				v6=False

			# Buscamos una ficha negra en la diagonal descendente derecha
			aux = fila+1
			aux2 = columna+1
			if aux<5 and aux>0 and aux2<5 and aux2>0:
				par = [5-aux,5-aux2]
				rango = min(par)
				if self.ESTADO_JUEGO[aux][aux2]==1:
					for i in range(rango):
						if self.ESTADO_JUEGO[aux+i+1][aux2+i+1]==2:
							if not self.generando_jugadas:
								self.Convertir(fila,aux+i+1,columna,aux2+i+1,"abde",2)
							v7=True
				else:
					v7=False
			else:
				v7=False

			# Buscamos una ficha negra en la diagonal descendente izquierda
			aux = fila+1
			aux2 = columna-1
			if aux<5 and aux>0 and aux2<5 and aux2>0:
				par = [5-aux,aux2]
				rango = min(par)
				if self.ESTADO_JUEGO[aux][aux2]==1:
					for i in range(rango):
						if self.ESTADO_JUEGO[aux+i+1][aux2-i-1]==2:
							if not self.generando_jugadas:
								self.Convertir(fila,aux+i+1,columna,aux2-i-1,"abiz",2)
							v8=True
				else:
					v8=False
			else:
				v8=False
			
			if v1 or v2 or v3 or v4 or v5 or v6 or v7 or v8:
				return True
			else:
				return False
		else:
			return False

	def Convertir(self,x1,x2,y1,y2,modo,color):
		if modo=="cde":
			while y1!=y2:
				self.ESTADO_JUEGO[x1][y1]=color
				y1=y1+1
		elif modo=="ciz":
			while y1!=y2:
				self.ESTADO_JUEGO[x1][y1]=color
				y1=y1-1
		elif modo=="arc":
			while x1!=x2:
				self.ESTADO_JUEGO[x1][y1]=color
				x1=x1-1
		elif modo=="abc":
			while x1!=x2:
				self.ESTADO_JUEGO[x1][y1]=color
				x1=x1+1
		elif modo=="arde":
			while x1!=x2:
				self.ESTADO_JUEGO[x1][y1]=color
				x1=x1-1
				y1=y1+1
		elif modo=="ariz":
			while x1!=x2:
				self.ESTADO_JUEGO[x1][y1]=color
				x1=x1-1
				y1=y1-1
		elif modo=="abde":
			while x1!=x2:
				self.ESTADO_JUEGO[x1][y1]=color
				x1=x1+1
				y1=y1+1
		elif modo=="abiz":
			while x1!=x2:
				self.ESTADO_JUEGO[x1][y1]=color
				x1=x1+1
				y1=y1-1

	def Es_adyacente(self,coordenada):
		x=coordenada[0] # FILA
		y=coordenada[1] # COLUMNA
		if x<5 and x>0 and y<5 and y>0 :
			if self.ESTADO_JUEGO[x+1][y]!=0:
				return True
			elif self.ESTADO_JUEGO[x-1][y]!=0:
				return True
			elif self.ESTADO_JUEGO[x+1][y+1]!=0:
				return True
			elif self.ESTADO_JUEGO[x-1][y-1]!=0:
				return True
			elif self.ESTADO_JUEGO[x+1][y-1]!=0:
				return True
			elif self.ESTADO_JUEGO[x-1][y+1]!=0:
				return True
			elif self.ESTADO_JUEGO[x][y+1]!=0:
				return True
			elif self.ESTADO_JUEGO[x][y-1]!=0:
				return True
			else:
				return False
		if x==5 and y>0 and y<5 :
			if self.ESTADO_JUEGO[x-1][y]!=0:
				return True
			elif self.ESTADO_JUEGO[x-1][y-1]!=0:
				return True
			elif self.ESTADO_JUEGO[x-1][y+1]!=0:
				return True
			elif self.ESTADO_JUEGO[x][y+1]!=0:
				return True
			elif self.ESTADO_JUEGO[x][y-1]!=0:
				return True
			else:
				return False
		if x==0 and y>0 and y<5:
			if self.ESTADO_JUEGO[x+1][y]!=0:
				return True
			elif self.ESTADO_JUEGO[x+1][y+1]!=0:
				return True
			elif self.ESTADO_JUEGO[x+1][y-1]!=0:
				return True
			elif self.ESTADO_JUEGO[x][y+1]!=0:
				return True
			elif self.ESTADO_JUEGO[x][y-1]!=0:
				return True
			else:
				return False
		if y==5 and x<5 and x>0:
			if self.ESTADO_JUEGO[x+1][y]!=0:
				return True
			elif self.ESTADO_JUEGO[x-1][y]!=0:
				return True
			elif self.ESTADO_JUEGO[x-1][y-1]!=0:
				return True
			elif self.ESTADO_JUEGO[x+1][y-1]!=0:
				return True
			elif self.ESTADO_JUEGO[x][y-1]!=0:
				return True
			else:
				return False
		if y==0 and x<5 and x>0:
			if self.ESTADO_JUEGO[x+1][y]!=0:
				return True
			elif self.ESTADO_JUEGO[x-1][y]!=0:
				return True
			elif self.ESTADO_JUEGO[x+1][y+1]!=0:
				return True
			elif self.ESTADO_JUEGO[x-1][y+1]!=0:
				return True
			elif self.ESTADO_JUEGO[x][y+1]!=0:
				return True
			else:
				return False
		if x==0 and y==0:
			if self.ESTADO_JUEGO[x+1][y]!=0:
				return True
			elif self.ESTADO_JUEGO[x+1][y+1]!=0:
				return True
			elif self.ESTADO_JUEGO[x][y+1]!=0:
				return True
			else:
				return False
		if x==0 and y==5:
			if self.ESTADO_JUEGO[x+1][y]!=0:
				return True
			elif self.ESTADO_JUEGO[x+1][y-1]!=0:
				return True
			elif self.ESTADO_JUEGO[x][y-1]!=0:
				return True
			else:
				return False
		if x==5 and y==0:
			if self.ESTADO_JUEGO[x-1][y]!=0:
				return True
			elif self.ESTADO_JUEGO[x-1][y+1]!=0:
				return True
			elif self.ESTADO_JUEGO[x][y+1]!=0:
				return True
			else:
				return False
		if x==5 and y==5:
			if self.ESTADO_JUEGO[x-1][y]!=0:
				return True
			elif self.ESTADO_JUEGO[x-1][y-1]!=0:
				return True
			elif self.ESTADO_JUEGO[x][y-1]!=0:
				return True
			else:
				return False

	#FUNCIONES PARA LA IMPLEMENTACION DE IA
	def Generador_Jugadas_validas(self,jugador):
		self.generando_jugadas=True
		Jugadas_posibles=[]
		if jugador==1:
			for i in range(6):
				for j in range(6):
					if self.Esta_vacia([i,j]) and self.Es_adyacente([i,j]) and self.Permite_salto_negra([i,j]):
						Jugadas_posibles.append([i,j])
		else:
			for i in range(6):
				for j in range(6):
					if self.Esta_vacia([i,j]) and self.Es_adyacente([i,j]) and self.Permite_salto_blanca([i,j]):
						Jugadas_posibles.append([i,j])
		self.generando_jugadas=False
		return Jugadas_posibles

	def Evaluar(self,profundidad):
		if 0 not in self.ESTADO_JUEGO or profundidad == 2:
			self.completado=True
		else:
			self.completado=False
		blancas=0
		negras=0
		if self.completado:
			for i in range(6):
				for j in range(6):
					if self.ESTADO_JUEGO[i][j]==1:
						blancas=blancas+1
					if self.ESTADO_JUEGO[i][j]==2:
						negras=negras+1
			self.utilidad=negras-blancas    

	def Estado_final(self,profundidad):
		self.Evaluar(profundidad)
		if self.completado:
			return True
		else:
			return False

	def Devolver_estado(self,estado):
		for i in range(6):
			for j in range(6):
				self.ESTADO_JUEGO[i][j]=estado[i][j]
		
	#DEBUG
	def Jugar(self,coordenada,color):
		if color==1:
			if self.Esta_vacia(coordenada) and self.Es_adyacente(coordenada) and self.Permite_salto_blanca(coordenada):
				self.ESTADO_JUEGO[coordenada[0]][coordenada[1]]=1
				return True
			else:
				return False
		if color==2:
			if self.Esta_vacia(coordenada) and self.Es_adyacente(coordenada) and self.Permite_salto_negra(coordenada):
				self.ESTADO_JUEGO[coordenada[0]][coordenada[1]]=2
				return True
			else:
				return False
		
	def Identificador_fin_juego(self,estado_juego,color):
		if 0 not in estado_juego:
			return False
		if color==2:
			posibles_jugadas=self.Generador_Jugadas_validas(2)
		else:
			posibles_jugadas=self.Generador_Jugadas_validas(1)
		print(len(posibles_jugadas))
		if len(posibles_jugadas)==0:
			return False
		return True

def minimax(juego,estado,profundidad,etapa):
	if juego.Estado_final(profundidad):
		return [-1*juego.utilidad]

	if etapa == 1:
		valor = [-1000, None]
		jugadas_posibles = juego.Generador_Jugadas_validas(1)
	else:
		valor = [1000, None]
		jugadas_posibles = juego.Generador_Jugadas_validas(2)
	for jugada in jugadas_posibles:
		if etapa == 1:
			if juego.Esta_vacia(jugada) and juego.Es_adyacente(jugada) and juego.Permite_salto_negra(jugada):
				juego.ESTADO_JUEGO[jugada[0]][jugada[1]]=2
				juego.jugada.append(jugada)  
		else:
			if juego.Esta_vacia(jugada) and juego.Es_adyacente(jugada) and juego.Permite_salto_blanca(jugada):
				juego.ESTADO_JUEGO[jugada[0]][jugada[1]]=1
				juego.jugada.append(jugada)
		estado_de_juego=copy.deepcopy(juego.ESTADO_JUEGO)
		opcion = minimax(juego,estado_de_juego,profundidad+1,etapa*-1)
		#maximizar
		if etapa == 1:
			if valor[0] < opcion[0]:
				valor = [opcion[0], jugada]
		else:
			#minimizar
			if valor[0] > opcion[0]:
				valor = [opcion[0], jugada]
		juego.Devolver_estado(estado)
	return valor
