
def Permite_salto_blanca(coordenada):
		fila = coordenada[0]
		columna = coordenada[1]
		v1=False;v2=False;v3=False;v4=False;v5=False;v6=False;v7=False;v8=False

		if Es_adyacente(coordenada):
				#Buscamos una ficha negra a la derecha
				aux = columna+1
				if aux<5 and aux>0:
					 if ESTADO_JUEGO[fila][aux]==2:
						for i in range(5-aux):
								if ESTADO_JUEGO[fila][aux+i+1]==1:
									 Convertir(fila,fila,aux,aux+i+1,"cde",1)
									 v1=True
					 else:
						v1=False
				else:
					 v1=False

				#Buscamos una ficha negra a la izquierda
				aux = columna-1
				if aux<5 and aux>0:
					 if ESTADO_JUEGO[fila][aux]==2:
						for i in range(aux):
								if ESTADO_JUEGO[fila][aux-i-1]==1:
									 Convertir(fila,fila,aux,aux-i-1,"ciz",1)
									 v2=True
					 else:
						v2=False
				else:
					 v2=False

				#Buscamos una ficha negra hacia abajo
				aux = fila+1
				if aux<5 and aux>0:
					 if ESTADO_JUEGO[aux][columna]==2:
						for i in range(5-aux):
								if ESTADO_JUEGO[aux+i+1][columna]==1:
									 Convertir(fila,aux+i+1,columna,columna,"abc",1)
									 v3=True
					 else:
						v3=False
				else:
					 v3=False

				#Buscamos una ficha negra hacia arriba
				aux = fila-1
				if aux<5 and aux>0:
					 if ESTADO_JUEGO[aux][columna]==2:
						for i in range(aux):
								if ESTADO_JUEGO[aux-i-1][columna]==1:
									 Convertir(fila,aux-i-1,columna,columna,"arc",1)
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
					 if ESTADO_JUEGO[aux][aux2]==2:
						for i in range(rango):
								if ESTADO_JUEGO[aux-i-1][aux2+i+1]==1:
									 Convertir(fila,aux-i-1,columna,aux2+i+1,"arde",1)
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
					 if ESTADO_JUEGO[aux][aux2]==2:
						for i in range(rango):
								if ESTADO_JUEGO[aux-i-1][aux2-i-1]==1:
									 Convertir(fila,aux-i-1,columna,aux2-i-1,"ariz",1)
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
					 if ESTADO_JUEGO[aux][aux2]==2:
						for i in range(rango):
								if ESTADO_JUEGO[aux+i+1][aux2+i+1]==1:
									 Convertir(fila,aux+i+1,columna,aux2+i+1,"abde",1)
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
					 if ESTADO_JUEGO[aux][aux2]==2:
						for i in range(rango):
								if ESTADO_JUEGO[aux+i+1][aux2-i-1]==1:
									 Convertir(fila,aux+i+1,columna,aux2-i-1,"abiz",1)
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


def Esta_vacia(coordenada):
	if ESTADO_JUEGO[coordenada[0]][coordenada[1]] == 0:
		return True
	else:
		return False


def Permite_salto_negra(coordenada):
		fila = coordenada[0]
		columna = coordenada[1]
		v1 = False; v2 = False; v3 = False; v4 = False; v5 = False; v6 = False; v7 = False; v8 = False
		if Es_adyacente(coordenada):
				# Buscamos una ficha negra a la derecha
				aux = columna+1
				if aux < 5 and aux > 0:
					 if ESTADO_JUEGO[fila][aux] == 1:
						for i in range(5-aux):
								if ESTADO_JUEGO[fila][aux+i+1] == 2:
									 Convertir(fila, fila, aux, aux+i+1, "cde", 2)
									 v1 = True
					 else:
						v1 = False
				else:
					 v1 = False

				# Buscamos una ficha negra a la izquierda
				aux = columna-1
				if aux<5 and aux>0:
					 if ESTADO_JUEGO[fila][aux]==1:
						for i in range(aux):
								if ESTADO_JUEGO[fila][aux-i-1]==2:
									 Convertir(fila,fila,aux,aux-i-1,"ciz",2)
									 v2=True
					 else:
						v2=False
				else:
					 v2=False

				# Buscamos una ficha negra hacia abajo
				aux = fila+1
				if aux<5 and aux>0:
					 if ESTADO_JUEGO[aux][columna]==1:
						for i in range(5-aux):
								if ESTADO_JUEGO[aux+i+1][columna]==2:
									 Convertir(fila,aux+i+1,columna,columna,"abc",2)
									 v3=True
					 else:
						v3=False
				else:
					 v3=False

				# Buscamos una ficha negra hacia arriba
				aux = fila-1
				if aux<5 and aux>0:
					 if ESTADO_JUEGO[aux][columna]==1:
						for i in range(aux):
								if ESTADO_JUEGO[aux-i-1][columna]==2:
									 Convertir(fila,aux-i-1,columna,columna,"arc",2)
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
					 if ESTADO_JUEGO[aux][aux2]==1:
						for i in range(rango):
								if ESTADO_JUEGO[aux-i-1][aux2+i+1]==2:
									 Convertir(fila,aux-i-1,columna,aux2+i+1,"arde",2)
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
					 if ESTADO_JUEGO[aux][aux2]==1:
						for i in range(rango):
								if ESTADO_JUEGO[aux-i-1][aux2-i-1]==2:
									 Convertir(fila,aux-i-1,columna,aux2-i-1,"ariz",2)
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
					 if ESTADO_JUEGO[aux][aux2]==1:
						for i in range(rango):
								if ESTADO_JUEGO[aux+i+1][aux2+i+1]==2:
									 Convertir(fila,aux+i+1,columna,aux2+i+1,"abde",2)
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
					 if ESTADO_JUEGO[aux][aux2]==1:
						for i in range(rango):
								if ESTADO_JUEGO[aux+i+1][aux2-i-1]==2:
									 Convertir(fila,aux+i+1,columna,aux2-i-1,"abiz",2)
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


def Convertir(x1,x2,y1,y2,modo,color):
	"""..."""
		if modo=="cde":
				while y1!=y2:
					 ESTADO_JUEGO[x1][y1]=color
					 y1=y1+1
		elif modo=="ciz":
				while y1!=y2:
					 ESTADO_JUEGO[x1][y1]=color
					 y1=y1-1
		elif modo=="arc":
				while x1!=x2:
					 ESTADO_JUEGO[x1][y1]=color
					 x1=x1-1
		elif modo=="abc":
				while x1!=x2:
					 ESTADO_JUEGO[x1][y1]=color
					 x1=x1+1
		elif modo=="arde":
				while x1!=x2:
					 ESTADO_JUEGO[x1][y1]=color
					 x1=x1-1
					 y1=y1+1
		elif modo=="ariz":
				while x1!=x2:
					 ESTADO_JUEGO[x1][y1]=color
					 x1=x1-1
					 y1=y1-1
		elif modo=="abde":
				while x1!=x2:
					 ESTADO_JUEGO[x1][y1]=color
					 x1=x1+1
					 y1=y1+1
		elif modo=="abiz":
				while x1!=x2:
					 ESTADO_JUEGO[x1][y1]=color
					 x1=x1+1
					 y1=y1-1


def Es_adyacente(coordenada):
	"""..."""

	 x=coordenada[0]
	 y=coordenada[1]
	 if x<5 and x>0 and y<5 and y>0 :
		if ESTADO_JUEGO[x+1][y]!=0:
				return True
		elif ESTADO_JUEGO[x-1][y]!=0:
				return True
		elif ESTADO_JUEGO[x+1][y+1]!=0:
				return True
		elif ESTADO_JUEGO[x-1][y-1]!=0:
				return True
		elif ESTADO_JUEGO[x+1][y-1]!=0:
				return True
		elif ESTADO_JUEGO[x-1][y+1]!=0:
				return True
		elif ESTADO_JUEGO[x][y+1]!=0:
				return True
		elif ESTADO_JUEGO[x][y-1]!=0:
				return True
		else:
				return False
	 if x==5 and y>0 and y<5 :
		if ESTADO_JUEGO[x-1][y]!=0:
				return True
		elif ESTADO_JUEGO[x-1][y-1]!=0:
				return True
		elif ESTADO_JUEGO[x-1][y+1]!=0:
				return True
		elif ESTADO_JUEGO[x][y+1]!=0:
				return True
		elif ESTADO_JUEGO[x][y-1]!=0:
				return True
		else:
				return False
	 if x==0 and y>0 and y<5:
		if ESTADO_JUEGO[x+1][y]!=0:
				return True
		elif ESTADO_JUEGO[x+1][y+1]!=0:
				return True
		elif ESTADO_JUEGO[x+1][y-1]!=0:
				return True
		elif ESTADO_JUEGO[x][y+1]!=0:
				return True
		elif ESTADO_JUEGO[x][y-1]!=0:
				return True
		else:
				return False
	 if y==5 and x<5 and x>0:
		if ESTADO_JUEGO[x+1][y]!=0:
				return True
		elif ESTADO_JUEGO[x-1][y]!=0:
				return True
		elif ESTADO_JUEGO[x-1][y-1]!=0:
				return True
		elif ESTADO_JUEGO[x+1][y-1]!=0:
				return True
		elif ESTADO_JUEGO[x][y-1]!=0:
				return True
		else:
				return False
	 if y==0 and x<5 and x>0:
		if ESTADO_JUEGO[x+1][y]!=0:
				return True
		elif ESTADO_JUEGO[x-1][y]!=0:
				return True
		elif ESTADO_JUEGO[x+1][y+1]!=0:
				return True
		elif ESTADO_JUEGO[x-1][y+1]!=0:
				return True
		elif ESTADO_JUEGO[x][y+1]!=0:
				return True
		else:
				return False
	 if x==0 and y==0:
		if ESTADO_JUEGO[x+1][y]!=0:
				return True
		elif ESTADO_JUEGO[x+1][y+1]!=0:
				return True
		elif ESTADO_JUEGO[x][y+1]!=0:
				return True
		else:
				return False
	 if x==0 and y==5:
		if ESTADO_JUEGO[x+1][y]!=0:
				return True
		elif ESTADO_JUEGO[x+1][y-1]!=0:
				return True
		elif ESTADO_JUEGO[x][y-1]!=0:
				return True
		else:
				return False
	 if x==5 and y==0:
		if ESTADO_JUEGO[x-1][y]!=0:
				return True
		elif ESTADO_JUEGO[x-1][y+1]!=0:
				return True
		elif ESTADO_JUEGO[x][y+1]!=0:
				return True
		else:
				return False
	 if x==5 and y==5:
		if ESTADO_JUEGO[x-1][y]!=0:
				return True
		elif ESTADO_JUEGO[x-1][y-1]!=0:
				return True
		elif ESTADO_JUEGO[x][y-1]!=0:
				return True
		else:
				return False