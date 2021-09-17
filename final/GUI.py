#	-- Dependencias.
#	Dependencias externas.
import pygame;
import os;
import sys;
import webbrowser;
from typing import Any, List, Tuple;

#	Dependencias Internas.

#   -- Clases.
#	Definición de la clase.
class Interfaz():
	#	Propiedades.
	#	Constructor.
	def __init__(self, DIR:str) -> None:
		#	Configuraciones iniciales.
		self.ALTO_PANTALLA:int = 700;
		self.ANCHO_PANTALLA:int = 600;
		self.DIRECTORIO:str = DIR;

		#	Configurando los turnos de cada jugador.
		#	[0]: Jugador ficha blanca.
		#	[1]: Jugador ficha negra.

		self.TURNOS:List[bool] = [False, True]; 

	#   Metodos.
	def renderizar_fichas(self, partida) -> None:
		"""..."""

		#	Traemos la ventana.
		ventana = self.GET_ventana();

		#	Traemos la instancia de la partida junto con el tablero.
		tablero = partida.GET_estado_juego();

		#	Calculando la posición del tablero.
		tamaño_tablero:int = 440;
		alto_celda:int = int((tamaño_tablero / 6));
		ancho_celda:int = int((tamaño_tablero / 6));

		#	Recorriendo el tablero, para renderizarlo.
		posicion_y:float = 220;
		for fila in tablero:
			posicion_x:float = 80;
			for elemento in fila:
				#	Caso: Ficha blanca.
				if (elemento == 1):
					ficha = self.GET_ficha(elemento);
					ventana.blit(ficha, ((posicion_x + 7), (posicion_y + 9)));
				
				#	Caso: Ficha negra	.
				elif (elemento == 2):
					ficha = self.GET_ficha(elemento);
					ventana.blit(ficha, ((posicion_x + 7), (posicion_y + 9)));

				elif (elemento == 0):
					pass

				else:
					print("[DEV][renderizar_fichas][ERROR] elemento no conocido en el tablero.");

				posicion_x += ancho_celda + 0.5;
			posicion_y += alto_celda + 0.5;


	def renderizar_texto(self, ventana):
		"""..."""
		
		#	Traemos los valores de las fichas.
		numero_fichas_blancas:int = self.GET_numero_fichas(1);
		numero_fichas_negras:int = self.GET_numero_fichas(2);
		turnos:List[bool] = self.GET_turnos(); # 0, blanca, 1, negra.

		fuente_juego = self.GET_fuente();
		texto_fichas_blancas = pygame.font.Font.render(fuente_juego, str(numero_fichas_blancas), True, (24, 27, 28));
		texto_fichas_negras = pygame.font.Font.render(fuente_juego, str(numero_fichas_negras), True, (24, 27, 28));
		texto_turno_blanca = pygame.font.Font.render(fuente_juego, "Turno: Ficha blanca", True, (24, 27, 28));
		texto_turno_negra = pygame.font.Font.render(fuente_juego, "Turno: Ficha negra", True, (24, 27, 28));

		#	Renderizado del texto.
		#	TURNO: ficha blanca.
		if (turnos[0]):
			ventana.blit(texto_turno_blanca, dest=(220, 668));

		#	TURNO: ficha negra.
		elif (turnos[1]):
			ventana.blit(texto_turno_negra, dest=(220, 668));

		#	Posicionamiento fichas blancas.
		if (len(str(numero_fichas_blancas)) == 1):
			ventana.blit(texto_fichas_blancas, dest=(86, 122));
		else:
			ventana.blit(texto_fichas_blancas, dest=(79, 122));
		
		#	Posicionamiento fichas blancas.
		if (len(str(numero_fichas_negras)) == 1):
			ventana.blit(texto_fichas_negras, dest=(182, 122));
		else:
			ventana.blit(texto_fichas_negras, dest=(174, 122));


	def renderizado_objetos(self, partida) -> None:
		"""..."""

		#   Trayendo la instancia de ventana.
		ventana = self.GET_ventana();

		#	Cargando los objetos que deben renderizarse.
		ventana.blit(self.GET_background(), (0,0));
		
		#	Renderizar texto
		self.renderizar_texto(ventana);

		#	Renderizado de fichas del tablero.
		self.renderizar_fichas(partida);


		#	Actualización de la ventana.
		pygame.display.flip();
		

	def cargador_assets(self, tipo:str, nombre_archivo:str, es_png:bool= False) -> Any:
		"""..."""

		#	CASO: el asset es una imagen.
		if (tipo == "img"):
			recurso:Any = pygame.image.load(os.path.join(self.GET_directorio(), 'assets', nombre_archivo));
			recurso.convert();

			if (es_png == True):
				color:Any = recurso.get_at((0, 0));
				recurso.set_colorkey(color, pygame.RLEACCEL);

			return recurso;

		#	CASO: el asset es una fuente.
		elif (tipo == "font"):
			recurso = pygame.font.Font(os.path.join(self.GET_directorio(),'assets', nombre_archivo), 20);
			return recurso;

		#	CASO: Error, no se especifica.
		else:
			print("[DEV][ERROR] Error al cargar el assets, no hay tipo definido.");
			return None;


	def controlador_coordenadas_tablero(self, coordenadas:Tuple[int, int]) -> Tuple[int, int]:
		"""..."""

		#	Coordenadas.
		coordenada_x:int = coordenadas[0];
		coordenada_y:int = coordenadas[1];
		indice_x:int;
		indice_y:int;

		#	Determinación coordenadas EJE Y.
		if (coordenada_y in range(222, 290)):
			indice_y = 0;
		elif (coordenada_y in range(290, 364)):
			indice_y = 1;
		elif (coordenada_y in range(364, 438)):
			indice_y = 2;
		elif (coordenada_y in range(438, 514)):
			indice_y = 3;
		elif (coordenada_y in range(514, 584)):
			indice_y = 4;
		elif (coordenada_y in range(584, 656)):
			indice_y = 5;
		else:
			print("[DEV][ERROR] Error al momento de determinar la coordenada del tablero en el eje Y.");
			return (-1, -1);
		
		#	Determinación coordenadas EJE X.
		if (coordenada_x in range(80, 148)):
			indice_x = 0;
		elif (coordenada_x in range(148, 222)):
			indice_x = 1;
		elif (coordenada_x in range(222, 298)):
			indice_x = 2;
		elif (coordenada_x in range(298, 370)):
			indice_x = 3;
		elif (coordenada_x in range(370, 446)):
			indice_x = 4;
		elif (coordenada_x in range(446, 520)):
			indice_x = 5;
		else:
			print("[DEV][ERROR] Error al momento de determinar la coordenada del tablero en el eje X.");
			return (-1, -1);

		return (indice_x, indice_y);


	def activar_boton_dificultad(self, dificultad:str) -> None:
		"""..."""

		#	Determinando funcionalidad dependiendo de la dificultad.
		if (dificultad == "FACIL"):
			print("[DEV][EVENTO] Se pulso el boton FACIL");
			#	Agregar funcionalidad...

		elif (dificultad == "MEDIO"):
			print("[DEV][EVENTO] Se pulso el boton MEDIO");
			#	Agregar funcionalidad...

		elif (dificultad == "DIFICIL"):
			print("[DEV][EVENTO] Se pulso el boton DIFICIL");
			#	Agregar funcionalidad...

		else:
			print("[DEV][activar_boton_dificultad][ERROR] no esta definido el boton seleccionado.");


	def activar_boton_nuevo_juego(self) -> None:
		"""..."""
		print("[DEV] Se pulso el boton de nuevo juego!");
		pass


	def activar_boton_pista(self) -> None:
		"""..."""
		print("[DEV] Se pulso el boton de pista!");
		pass

	def activar_boton_repositorio(self) -> None:
		"""..."""
		print("[DEV] abriendo el repositorio en el navegador...")
		webbrowser.open("https://github.com/JajoScript/IA-Reversi", new=2, autoraise=True);

	def controlador_coordenadas(self, coordenadas:Tuple[int, int]) -> Tuple[int, int]:
		"""..."""

		#	Coordenadas.
		coordenada_x:int = coordenadas[0];
		coordenada_y:int = coordenadas[1];
		
		#	Boton: 'Facil'.
		if (coordenada_x in range(56, 108) and coordenada_y in range(82, 96)):
			self.activar_boton_dificultad("FACIL");
		
		#	Boton: 'Medio'.
		elif (coordenada_x in range(116, 167) and coordenada_y in range(82,96)):
			self.activar_boton_dificultad("MEDIO");

		#	Boton: 'Dificil'.
		elif (coordenada_x in range(176, 226) and coordenada_y in range(82, 96)):
			self.activar_boton_dificultad("DIFICIL");

		#	Boton: 'Pista'.
		elif (coordenada_x in range(242, 392) and coordenada_y in range(40, 70)):
			self.activar_boton_pista();

		#	Boton: 'Nuevo Juego'.
		elif (coordenada_x in range(242, 392) and coordenada_y in range(76, 106)):
			self.activar_boton_nuevo_juego();

		#	Boton: 'repositorio'.
		elif (coordenada_x in range(546, 582) and coordenada_y in range(640, 670)):
			self.activar_boton_repositorio();


		#	Boton: 'TABLERO'.
		elif (coordenada_x in range(78, 520) and coordenada_y in range(222, 660)):
			tablero_coordenadas:Tuple[int, int] = self.controlador_coordenadas_tablero(coordenadas);
			print("[DEV][EVENTO] Se pulso el tablero.");
			print(tablero_coordenadas)
			return tablero_coordenadas;

		#	ERROR: Indeterminación.
		else:
			print("[DEV][ERROR][controlador_coordenadas] Indeterminación a la hora de conocer donde pulso.");

		#	Retorno general.
		return (-1, -1)


	def contador_fichas(self, partida) -> None:
		"""..."""

		#	Traemos el tablero de la instancia de partida.
		tablero = partida.GET_estado_juego();

		#	Variables inciales. 
		numero_fichas_blancas:int = 0;
		numero_fichas_negras:int = 0;

		#	Ciclo para recorrer el tablero y conar cada uno de sus elementos.
		for fila in tablero:
			for elemento in fila:
				if (elemento == 1):
					numero_fichas_blancas += 1;
				elif (elemento == 2):
					numero_fichas_negras += 1;

		#	Guardando los valores de las fichas.
		self.SET_numero_fichas(1, numero_fichas_blancas);
		self.SET_numero_fichas(2, numero_fichas_negras);


	def controlador_ventana(self, partida) -> None:
		"""..."""

		#   Configuración de la ventana.
		pygame.init();
		pygame.font.init();

		ventana:Any = pygame.display.set_mode((self.GET_ancho_pantalla(), self.GET_alto_pantalla()));
		self.SET_ventana(ventana);
		pygame.display.set_caption("REVERSI");

		#	Configurando el icono del juego.
		icono:Any = self.cargador_assets(tipo="img", nombre_archivo="icono.jpg", es_png=False);
		pygame.display.set_icon(icono);

		#	Cargando recursos del juego.
		fondo_juego:Any = self.cargador_assets("img", "background.jpg", es_png=False);
		self.SET_background(fondo_juego);

		ficha_blanca:Any = self.cargador_assets("img", "ficha_j2.png", es_png=True);
		self.SET_ficha(1, ficha_blanca);

		ficha_negra:Any = self.cargador_assets("img", "ficha_j1.png", es_png=True);
		self.SET_ficha(2, ficha_negra);

		fuente_juego:Any = self.cargador_assets("font", "Roboto-Light.ttf");
		self.SET_fuente(fuente_juego);

		#	Control de fotogramas.
		FPS = pygame.time.Clock();
		FPS.tick(30);

		#	Ciclo de ejecución.
		while True:
			#	Contador de fichas.
			self.contador_fichas(partida);

			#   Renderizando los elementos en pantalla.
			self.renderizado_objetos(partida);

			#   Manejo de eventos del usuario.
			for evento in pygame.event.get():
				#	EVENTO: Salir del juego.
				if evento.type == pygame.QUIT:
					sys.exit(0);

				#	EVENTO: se pulsa el click.
				if evento.type == pygame.MOUSEBUTTONDOWN:
					#	Capturando la posición del mouse.
					posicion_mouse:Tuple[int, int] = pygame.mouse.get_pos();
					print(f"[DEV] Mouse click (x: {posicion_mouse[0]}, y: {posicion_mouse[1]})")

					#	Implementación de la jugabilidad.
					coordenadas:Tuple[int, int] = self.controlador_coordenadas(posicion_mouse);

					#	CASO: No es valido pasarle las coordenadas al juego.
					if ((coordenadas[0] == -1) or (coordenadas[1] == -1)):
						print("[DEV] Se pulso fuera del tablero.");

					elif ((coordenadas[0] != -1) or (coordenadas[1] != -1)):
						#	Posiciones del tablero.
						indice_y:int = coordenadas[1];
						indice_x:int = coordenadas[0];

						print(f"[DEV y: {indice_y}, x: {indice_x}");

						#	Insertar jugabilidad aqui...
						tablero = partida.GET_estado_juego();
						tablero[indice_y][indice_x] = 2;

						partida.SET_estado_juego(tablero);


					#	Prueba de turnos.
					turnos:List[bool] = self.GET_turnos()
					nuevos_turnos = [not(turnos[0]), not(turnos[1])]
					self.SET_turnos(nuevos_turnos);
					


	#	Getters & Setters.
	#		NUMERO FICHAS
	def GET_numero_fichas(self, color_ficha:int) -> int:
		#	CASO: Ficha blanca.
		if (color_ficha == 1):
			return self.NUMERO_BLANCAS;

		#	CASO: Ficha negra.
		elif (color_ficha == 2):
			return self.NUMERO_NEGRAS;

		#	CASO: Error.
		else:
			print("[DEV][get_numero_fichas] Error al retornar el valor de fichas.");
			return 0;

	def SET_numero_fichas(self, color_ficha:int, numero_ficha:int) -> None:
		#	CASO: Ficha blanca.
		if (color_ficha == 1):
			self.NUMERO_BLANCAS = numero_ficha;

		#	CASO: Ficha negra.
		elif (color_ficha == 2):
			self.NUMERO_NEGRAS = numero_ficha;

		#	CASO: Error.
		else:
			print("[DEV][set_fichas] Error al cargar el numero de fichas.");

	#		TURNOS.
	def GET_turnos(self) -> List[bool]:
		return self.TURNOS;

	def SET_turnos(self, nuevos_turnos: List[bool]) -> None:
		self.TURNOS = nuevos_turnos;

	#		BACKGROUND.
	def GET_background(self) -> Any:
		return self.BACKGROUND;
	
	def SET_background(self, nuevo_fondo:Any) -> None:
		self.BACKGROUND = nuevo_fondo;

	#		FUENTE JUEGO.
	def GET_fuente(self) -> Any:
		return self.FUENTE_JUEGO;

	def SET_fuente(self, nueva_fuente:Any) -> None:
		self.FUENTE_JUEGO = nueva_fuente;

	#		FICHAS.
	def GET_ficha(self, color_ficha:int) -> Any:
		#	CASO: Ficha Blanca.
		if (color_ficha == 1):
			return self.FICHA_BLANCA;

		#	CASO: Ficha Negra.
		elif (color_ficha == 2):
			return self.FICHA_NEGRA;
		
		#	CASO: Error, No especificado.
		else:
			print("[DEV][GET_ficha] Error al cargar ficha, color no especificado.");
			return None;

	def SET_ficha(self, color_ficha:int, nueva_ficha:Any) -> None:
		#	CASO: Ficha Blanca.
		if (color_ficha == 1):
			self.FICHA_BLANCA = nueva_ficha;
		
		#	CASO: Ficha Negra.
		elif (color_ficha == 2):
			self.FICHA_NEGRA = nueva_ficha;
		
		#	CASO: Error, No especificado.
		else:
			print("[DEV][SET_ficha] Error al cargar ficha, color no especificado. ");
			return None;

	#		DIRECTORIO.
	def GET_directorio(self) -> str:
		return self.DIRECTORIO;
	
	def SET_directorio(self, nuevo_DIR) -> None:
		self.DIRECTORIO = nuevo_DIR;

	#		VENTANA.
	def GET_ventana(self) -> Any:
		return self.VENTANA;
	
	def SET_ventana(self, nueva_ventana) -> None:
		self.VENTANA = nueva_ventana;

	#		ALTO PANTALLA.
	def GET_alto_pantalla(self) -> int:
		return self.ALTO_PANTALLA;
	
	def SET_alto_pantalla(self, nuevo_alto) -> None:
		self.ALTO_PANTALLA = nuevo_alto;

	#		ANCHO PANTALLA.
	def GET_ancho_pantalla(self) -> int:
		return self.ANCHO_PANTALLA;

	def SET_ancho_pantalla(self, nuevo_ancho) -> None:
		self.ANCHO_PANTALLA = nuevo_ancho;