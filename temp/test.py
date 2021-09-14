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