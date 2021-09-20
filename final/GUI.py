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
	def renderizar_fichas(self) -> None:
		"""..."""

		#	Traemos la ventana.
		ventana = self.GET_ventana();

		#	Traemos la instancia de la partida junto con el tablero.
		partida = self.GET_partida();
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
					print("[DEV][GUI][ERROR][renderizar_fichas]")
					print("[>] Elemento no conocido en el tablero.");

				posicion_x += ancho_celda + 0.5;
			posicion_y += alto_celda + 0.5;


	def renderizar_texto(self, ventana) -> None:
		"""..."""
		
		#	Traemos los valores de las fichas.
		numero_fichas_blancas:int = self.GET_numero_fichas(1);
		numero_fichas_negras:int = self.GET_numero_fichas(2);
		termino = self.GET_terminado();

		turnos:List[bool] = self.GET_turnos(); # 0, blanca, 1, negra.

		fuente_juego = self.GET_fuente();
		texto_fichas_blancas = pygame.font.Font.render(fuente_juego, str(numero_fichas_blancas), True, (24, 27, 28));
		texto_fichas_negras = pygame.font.Font.render(fuente_juego, str(numero_fichas_negras), True, (24, 27, 28));
		texto_turno_blanca = pygame.font.Font.render(fuente_juego, "Turno: Ficha blanca", True, (24, 27, 28));
		texto_turno_negra = pygame.font.Font.render(fuente_juego, "Turno: Ficha negra", True, (24, 27, 28));
		texto_termino_partida = pygame.font.Font.render(fuente_juego, "Empataron", True, (24, 27, 28));
		texto_gana_blanco = pygame.font.Font.render(fuente_juego, "Gana Ficha blanca", True, (24, 27, 28));
		texto_gana_negro = pygame.font.Font.render(fuente_juego, "Gana Ficha negra", True, (24, 27, 28));

		#	Renderizado del texto.
		#	TURNO: ficha blanca.
		if (termino):
			#	Comprobando: victoria ficha blanca.
			if (numero_fichas_blancas > numero_fichas_negras):
				ventana.blit(texto_gana_blanco, dest=(220, 668));

			#	Comprobando: victoria ficha negra.
			elif (numero_fichas_blancas < numero_fichas_negras):
				ventana.blit(texto_gana_negro, dest=(220, 668));

			#	Comprobando: Empate.
			elif (numero_fichas_blancas == numero_fichas_negras):
				ventana.blit(texto_termino_partida, dest=(250, 668));

			#	ERROR: Error al determinar quien es ganador.
			else:
				print("[DEV][GUI][ERROR][renderizar_texto]")
				print("[>] Error al determinar al ganador.");

		elif (turnos[0]):
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
			ventana.blit(texto_fichas_negras, dest=(178, 122));


	def renderizado_objetos(self) -> None:
		"""..."""

		#	Trayendo la instancia de ventana.
		ventana = self.GET_ventana();

		#	Trayendo los estados de dificultad
		dificultad = self.GET_estado_dificultad();
		if (dificultad[0]):
			ventana.blit(self.GET_dificultad(1), (0,0));
		elif(dificultad[1]):
			ventana.blit(self.GET_dificultad(2), (0,0));
		elif(dificultad[2]):	
			ventana.blit(self.GET_dificultad(3), (0,0));
		
		#	Renderizar texto
		self.renderizar_texto(ventana);

		#	Renderizado de fichas del tablero.
		self.renderizar_fichas();

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
			print("[DEV][GUI][ERROR][cargador_assets]")
			print("[>] Error al cargar el assets, no hay tipo definido.");
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
			print("[DEV][GUI][ERROR][controlador_coordenadas_tablero]")
			print("[>] Error al momento de determinar la coordenada del tablero en el eje Y.");
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
			print("[DEV][GUI][ERROR][controlador_coordenadas_tablero]")
			print("[>] Error al momento de determinar la coordenada del tablero en el eje X.");
			return (-1, -1);

		return (indice_x, indice_y);


	def activar_boton_dificultad(self, dificultad:str) -> None:
		"""..."""

		#	Determinando funcionalidad dependiendo de la dificultad.
		if (dificultad == "FACIL"):
			print("[DEV][GUI][EVENTO] Se pulso el boton FACIL");
			#	Reincio del tablero.
			self.activar_boton_nuevo_juego();

			#	Definiendo los estados.
			estado_dificultad = [True, False, False]
			self.SET_estado_dificultad(estado_dificultad);

			#	Agregar funcionalidad...

		elif (dificultad == "MEDIO"):
			print("[DEV][GUI][EVENTO] Se pulso el boton MEDIO");
			#	Reincio del tablero.
			self.activar_boton_nuevo_juego();

			#	Definiendo los estados.
			estado_dificultad = [False, True, False]
			self.SET_estado_dificultad(estado_dificultad);

			#	Agregar funcionalidad...

		elif (dificultad == "DIFICIL"):
			print("[DEV][GUI][EVENTO] Se pulso el boton DIFICIL");
			#	Reincio del tablero.
			self.activar_boton_nuevo_juego();
			
			#	Definiendo los estados.
			estado_dificultad = [False, False, True]
			self.SET_estado_dificultad(estado_dificultad);

			#	Agregar funcionalidad...

		else:
			print("[DEV][GUI][ERROR][activar_boton_dificultad]")
			print("[>] No esta definido el boton seleccionado.");


	def activar_boton_nuevo_juego(self) -> None:
		"""..."""
		print("[DEV][GUI] Se pulso el boton de nuevo juego!");

		#	Traemos la instancia de la partida.
		juego = self.GET_partida();
		print(f"[DEV][GUI] juego 221: {juego}");
		juego.definir_estado_inicial();

		#	Definimos los turnos.
		nuevos_turnos = [False, True]; # [0] ficha blanca. [0] Ficha Negra.
		self.SET_turnos(nuevos_turnos)


	def activar_boton_pista(self) -> None:
		"""..."""
		
		print("[DEV][GUI] Se pulso el boton de pista!");
		pass

	def activar_boton_repositorio(self) -> None:
		"""..."""

		try:
			print("[DEV][GUI] abriendo el repositorio en el navegador...");
			webbrowser.open("https://github.com/JajoScript/IA-Reversi", new=2, autoraise=True);
		except:
			print("[DEV][GUI][ERROR][activar_boton_repositorio]");
			print("[>] Error al abrir el repositorio.");
		

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
			print("[DEV][GUI][EVENTO] Se pulso el tablero.");
			print(tablero_coordenadas)
			return tablero_coordenadas;

		#	ERROR: Indeterminación.
		else:
			print("[DEV][GUI][ERROR][controlador_coordenadas]")
			print("[>] Indeterminación a la hora de conocer donde pulso.");

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

		#	Definimos como propiedad la partida.
		print(f"[DEV][GUI] partida 309: {partida}")
		self.SET_partida(partida);

		#	Definimos un estado inicial para la dificultad.
		#	Esta configuración es para que al comenzar el juego, la IA este definida como Facil.
		self.SET_estado_dificultad([True, False, False]);
		self.SET_terminado(False);

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
		modo_facil:Any = self.cargador_assets("img", "background-facil.jpg", es_png=False);
		self.SET_dificultad(1, modo_facil);
		modo_medio:Any = self.cargador_assets("img", "background-medio.jpg", es_png=False);
		self.SET_dificultad(2, modo_medio);
		modo_dificil:Any = self.cargador_assets("img", "background-dificil.jpg", es_png=False);
		self.SET_dificultad(3, modo_dificil);

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
			self.renderizado_objetos();

			#   Manejo de eventos del usuario.
			for evento in pygame.event.get():
				#	EVENTO: Salir del juego.
				if evento.type == pygame.QUIT:
					sys.exit(0);

				#	EVENTO: se pulsa el click.
				if evento.type == pygame.MOUSEBUTTONDOWN:
					#	Capturando la posición del mouse.
					posicion_mouse:Tuple[int, int] = pygame.mouse.get_pos();
					print(f"[DEV][GUI] Mouse click (x: {posicion_mouse[0]}, y: {posicion_mouse[1]})")

					#	Implementación de la jugabilidad.
					coordenadas:Tuple[int, int] = self.controlador_coordenadas(posicion_mouse);

					#	CASO: No es valido pasarle las coordenadas al juego.
					if ((coordenadas[0] == -1) or (coordenadas[1] == -1)):
						print("[DEV][GUI] Se pulso fuera del tablero.");

					elif ((coordenadas[0] != -1) or (coordenadas[1] != -1)):
						#	Posiciones del tablero.
						indice_y:int = coordenadas[1];
						indice_x:int = coordenadas[0];

						print(f"[DEV y: {indice_y}, x: {indice_x}");

						#	Determinando de quien es el turno.
						turnos:List[bool] = self.GET_turnos();
						if(turnos[0]):
							print("[DEV][GUI] Jugada de ficha: blanca.");
							partida.iniciar_jugabilidad((indice_x, indice_y), color_ficha=1);
							
						elif (turnos[1]):
							print("[DEV][GUI] Jugada de ficha: negra.");
							partida.iniciar_jugabilidad((indice_x, indice_y), color_ficha=2);
						
						
						#	Procesos POST-partida.
						terminado_juego:bool = partida.GET_terminado();
						if (terminado_juego == True):
							print("[DEV][GUI] El juego termino");
							self.SET_terminado(partida.GET_terminado());

						elif (terminado_juego == False):
							print("[DEV][GUI] El juego no termino");
							self.SET_terminado(partida.GET_terminado());
				

	#	Getters & Setters.
	#		TERMINADO.
	def GET_terminado(self) -> bool:
		return self.TERMINADO;

	def SET_terminado(self, configuracion:bool) -> None:
		self.TERMINADO = configuracion;

	#		LISTA DIFICULTAD.
	def GET_estado_dificultad(self) -> List[bool]:
		return self.ESTADO_DIFICULTAD;

	def SET_estado_dificultad(self, nuevo_estado:List[bool]) -> None:
		self.ESTADO_DIFICULTAD = nuevo_estado;

	#		MODO DIFICULTAD
	def GET_dificultad(self, nivel:int) -> Any:
		#	Modo: Facil.
		if(nivel == 1):
			return self.MODO_FACIL;

		#	Modo: Medio.
		elif (nivel == 2):
			return self.MODO_MEDIO;
		
		#	Modo: Dificil.
		elif (nivel == 3):
			return self.MODO_DIFICIL;

		else:
			print("[DEV][GUI][ERROR][GET_dificultad]")
			print("[>] No se encuentra el nivel especificado.");

	def SET_dificultad(self, nivel:int, recurso:Any) -> None:
		#	Modo: Facil.
		if(nivel == 1):
			self.MODO_FACIL = recurso;

		#	Modo: Medio.
		elif (nivel == 2):
			self.MODO_MEDIO = recurso;
		
		#	Modo: Dificil.
		elif (nivel == 3):
			self.MODO_DIFICIL = recurso;

		else:
			print("[DEV][GUI][ERROR][SET_dificultad]")
			print("[>] No se encuentra el nivel especificado.");

	#		PARTIDA.
	def GET_partida(self) -> Any:
		return self.PARTIDA;

	def SET_partida(self, nueva_partida) -> None:
		self.PARTIDA = nueva_partida;

	#		NUMERO FICHAS.
	def GET_numero_fichas(self, color_ficha:int) -> int:
		#	CASO: Ficha blanca.
		if (color_ficha == 1):
			return self.NUMERO_BLANCAS;

		#	CASO: Ficha negra.
		elif (color_ficha == 2):
			return self.NUMERO_NEGRAS;

		#	CASO: Error.
		else:
			print("[DEV][GUI][get_numero_fichas] Error al retornar el valor de fichas.");
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
			print("[DEV][GUI][set_fichas] Error al cargar el numero de fichas.");

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
			print("[DEV][GUI][GET_ficha] Error al cargar ficha, color no especificado.");
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
			print("[DEV][GUI][SET_ficha] Error al cargar ficha, color no especificado. ");
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