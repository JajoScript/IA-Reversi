#	-- Dependencias. --
from GAME import Reversi
import typing, sys, time, os;
from typing import Any;
import pygame;

#	-- Funciones. --
#	-- Definición de clase. --
class InterfazGrafica():
	#	Propiedades.
	ALTO_PANTALLA:int;
	ANCHO_PANTALLA:int;
	DIRECTORIO:str;

	# Jugabilidad.
	TURNO_BLANCA:bool;
	TURNO_NEGRA:bool;
	JUEGO_REVERSI:Reversi;

	# Entidades.
	VENTANA:Any;
	FICHA_BLANCA:Any;
	FICHA_NEGRA:Any;

	#	COORDENADAS
	#	Definidas en -1 como estado inicial.
	TAMAÑO_TABLERO:int = 440;
	COORDENADA_X:int = -1;
	COORDENADA_Y:int = -1; 

	#	Constructor.
	def __init__(self, ALTO:int, ANCHO:int, DIRECTORIO:str, juego:Reversi, turno_blanca:bool, turno_negra:bool) -> None:
		#	Configuración para la ventana.
		self.ALTO_PANTALLA = ALTO;
		self.ANCHO_PANTALLA = ANCHO;

		#	Configuración del directorio.
		self.DIRECTORIO = DIRECTORIO;

		#	Configuración para el manejo de turnos.
		self.TURNO_BLANCA = turno_blanca;
		self.TURNO_NEGRA = turno_negra;

		#	Traemos el objeto REVERSI
		self.JUEGO_REVERSI = juego;

	#	Metodos.
	def controlador_tablero(self) -> None:
		"""..."""
		
		# Estado del juego desde la entidad "juego".
		juego:Reversi = self.GET_juego_reversi();
		estado_juego:list[list[int]] = juego.GET_estado_juego();

		#	Renderizado de las fichas.
		numero_filas:int = juego.GET_numero_filas();
		numero_columnas:int = juego.GET_numero_columnas();
		TAMAÑO_CELDA_ALTO:int = int((self.GET_tamaño_tablero() / numero_filas)); 
		TAMAÑO_CELDA_ANCHO:int = int((self.GET_tamaño_tablero() / numero_columnas));

		#	Iteración de las filas.
		POSICION_Y: int = 220;
		for fila in range(0, juego.GET_numero_filas()):
			#	Iteración de las columnas.
			POSICION_X: int = 80;
			for columna in range(0, juego.GET_numero_columnas()):
				estado_juego:list[list[int]] = juego.GET_estado_juego();

				# CASO 1: celda vacia.

				# CASO 2: celda con FICHA BLANCA.
				if estado_juego[fila, columna] == 1:
					ventana = self.GET_ventana();
					ficha = self.GET_ficha_blanca();
					ventana.blit(ficha, ((POSICION_X + 7), (POSICION_Y + 9)))

				# CASO 3: celda con FICHA NEGRA.
				elif estado_juego[fila, columna] == 2:
					ventana = self.GET_ventana();
					ficha = self.GET_ficha_negra();
					ventana.blit(ficha, ((POSICION_X + 7), (POSICION_Y + 9)))

				POSICION_X += TAMAÑO_CELDA_ANCHO;
			POSICION_Y += TAMAÑO_CELDA_ALTO;


	def controlador_nuevo_juego(self) -> None:
		# Creando un nuevo juego.
		print("[DEV] SE CREO UN NUEVO JUEGO");
		juego:Reversi = self.GET_juego_reversi();
		juego.crear_estado_inicial();


	def controlador_boton_dificultad(self, dificultad:str) -> None:
		"""..."""
		print(f"[DEV] Nueva dificultad: {dificultad}");

		# Cambiando la dificultad ...
		
		# Creando un nuevo juego.
		self.controlador_nuevo_juego()


	def controlador_boton_pista(self) -> None:
		"""..."""
		print("[DEV][EVENT] Se pulso el boton pista");


	def controlador_boton_nuevo_juego(self) -> None:
		"""..."""
		print("[DEV][EVENT] Se pulso el boton 'Nuevo juego'");
		
		# Creando un nuevo juego.
		self.controlador_nuevo_juego()
	

	def controlador_assets(self, tipo_recurso:str, nombre_archivo:str, es_transparente:bool=False, tamaño_fuente:int=20) -> typing.Any:
		""" Función que carga el recurso solicitado, ya sean imagenes (jpg, png, gif, etc.) o fuentes."""
		
		#	Cargando el recurso de la carpeta assets.
		if (tipo_recurso == "img"):
			#	Recordatorio: Manejar los errores del directorio assets.
			recurso:Any = pygame.image.load(os.path.join(self.GET_directorio(), 'assets', nombre_archivo));
			recurso = recurso.convert();

			#	Habilitando la transparencia de fondo (PNG).
			if es_transparente:
				color:Any = recurso.get_at((0, 0));
				recurso.set_colorkey(color, pygame.RLEACCEL);

			return recurso;

		elif(tipo_recurso == "font"):
			recurso = pygame.font.Font(os.path.join(self.GET_directorio(),'assets', nombre_archivo), tamaño_fuente);
			return recurso;
	
		else:
			print("[DEV][ERROR] No se pudo cargar el recurso.");
			return None;


	def controlador_coordenadas_tablero(self, coordenadas:list[int]) -> None:
		"""..."""

		#	Variables locales.
		coordenada_x:int = coordenadas[0];
		coordenada_y:int = coordenadas[1];

		#	Posiciones tablero.
		indice_x: int = 0;
		indice_y: int;

		#	Coordenadas Y: 
		if coordenada_y in range(222, 290):
			indice_y = 0;

		elif coordenada_y in range(290, 364):
			indice_y = 1;

		elif coordenada_y in range(364, 438):
			indice_y = 2;
		
		elif coordenada_y in range(438, 514):
			indice_y = 3;
		
		elif coordenada_y in range(514, 584):
			indice_y = 4;
		
		elif coordenada_y in range(584, 656):
			indice_y = 5;

		#	Coordenadas X:
		if coordenada_x in range(80, 148):
			indice_x = 0;

		elif coordenada_x in range(148, 222):
			indice_x = 1;
		
		elif coordenada_x in range(222, 298):
			indice_x = 2;

		elif coordenada_x in range(298, 370):
			indice_x = 3;

		elif coordenada_x in range(370, 446):
			indice_x = 4;

		elif coordenada_x in range(446, 520):
			indice_x = 5;

		#	Guardando las coordena.
		self.SET_coordenada_x(indice_x);
		self.SET_coordenada_y(indice_y);
		print(f"[DEV] tablero: [{indice_y}][{indice_x}]");


	def controlador_coordenadas(self, coordenadas:list[int]) -> None:
		"""..."""

		#	Variables locales.
		coordenada_x:int = coordenadas[0];
		coordenada_y:int = coordenadas[1];

		#	Controlador: Boton 'Facil'.
		if coordenada_x in range(56, 108) and coordenada_y in range(82, 96):
			self.controlador_boton_dificultad("FACIL");

		#	Controlador: Boton 'Medio'.	
		elif coordenada_x in range(116, 167) and coordenada_y in range(82, 96):
			self.controlador_boton_dificultad("MEDIO");

		#	Controlador: Boton 'Dificil'.	
		elif coordenada_x in range(176, 226) and coordenada_y in range(82, 96):
			self.controlador_boton_dificultad("DIFICIL");

		#	Controlador: Boton 'Pista'.	
		elif coordenada_x in range(242, 392) and coordenada_y in range(40, 70):
			self.controlador_boton_pista();

		#	Controlador: Boton 'Nuevo juego'.	
		elif coordenada_x in range(242, 392) and coordenada_y in range(76, 106):
			self.controlador_boton_nuevo_juego();
		
		#	Controlador: Coordenadas tablero.
		elif coordenada_x in range(78, 520) and coordenada_y in range(222, 660):
			self.controlador_coordenadas_tablero(coordenadas);

		#	Controlador: No se pulso nada.
		else:
			print("[DEV] No se pulso nada.");
			pass


	def controlador_renderizado(self) -> None:
		"""..."""
		pass


	def controlador_ventana(self) -> None:
		"""..."""

		#	Inicio de la ejecución de pygame.
		pygame.init();
		pygame.font.init();

		#	Configuraciones de la ventana.
		ventana:Any = pygame.display.set_mode((self.GET_ancho_pantalla(), self.GET_alto_pantalla()));
		self.SET_ventana(ventana); #	Guardamos la propiedad ventana.

		pygame.display.set_caption("REVERSI");
		icono:Any = self.controlador_assets("img", "icono.jpg", es_transparente=False);
		pygame.display.set_icon(icono);

		#	Cargando los recursos del juego.
		fondo_juego:Any = self.controlador_assets("img", "background.jpg", es_transparente=False);
		ficha_blanca:Any = self.controlador_assets("img", "ficha_j2.png", es_transparente=True);
		self.SET_ficha_blanca(ficha_blanca); #	Guardamos la propiedad ficha blanca.

		ficha_negra:Any = self.controlador_assets("img", "ficha_j1.png", es_transparente=True);
		self.SET_ficha_negra(ficha_negra); # Guardamos la propiedad ficha negra.

		fuente_juego:Any = self.controlador_assets("font", "Roboto-Light.ttf", tamaño_fuente=20);

		#	Control de fotogramas.
		FPS = pygame.time.Clock();
		FPS.tick(30);

		#	Ciclo para correr el juego.
		while True:
			#	Posicionando los recursos en la ventana.
			ventana.blit(fondo_juego, (0,0));

			#	Renderizado de fichas en el tablero.
			self.controlador_tablero();

			#	Control de eventos.
			for evento in pygame.event.get():
				#	Evento: Salir del juego.
				if evento.type == pygame.QUIT:
					sys.exit(0);

				#	Evento: Click en la pantalla.
				if evento.type == pygame.MOUSEBUTTONDOWN:
					#	Capturando las coordenadas.
					posicion_mouse:list[int] = pygame.mouse.get_pos();
					print(f"[DEV] coordenadas: (x: {posicion_mouse[0]}, y: {posicion_mouse[1]})");

					#	Gestionando coordenadas.
					self.controlador_coordenadas(posicion_mouse);

					#	Ejecucion de la jugabilidad.
					#	...

			#	Actualización de la ventana.
			pygame.display.flip();


	#	Getters & Setters.
		#	TAMAÑO TABLERO.
	def GET_tamaño_tablero(self) -> int:
		return self.TAMAÑO_TABLERO;

	def SET_tamaño_tablero(self, tamaño_nuevo) -> None:
		self.TAMAÑO_TABLERO = tamaño_nuevo;

		#	FICHA NEGRA.
	def GET_ficha_negra(self) -> Any:
		return self.FICHA_NEGRA;

	def SET_ficha_negra(self, nueva_ficha) -> None:
		self.FICHA_NEGRA = nueva_ficha;

		#	FICHA BLANCA.
	def GET_ficha_blanca(self) -> Any:
		return self.FICHA_BLANCA;

	def SET_ficha_blanca(self, nueva_ficha) -> None:
		self.FICHA_BLANCA = nueva_ficha;

		#	VENTANA.
	def GET_ventana(self) -> Any:
		return self.VENTANA;

	def SET_ventana(self, nuevo_display:Any) -> None:
		self.VENTANA = nuevo_display;

		#	JUEGO.
	def GET_juego_reversi(self) -> Reversi:
		return self.JUEGO_REVERSI;

	def SET_juego_reversi(self, nueva_instancia) -> None:
		self.JUEGO_REVERSI = nueva_instancia;
	
		#	COORDENADAS.		
	def GET_coordenada_x(self) -> int:
		return self.COORDENADA_X;
	
	def SET_coordenada_x(self, nueva_coordenada:int) -> None:
		self.COORDENADA_X = nueva_coordenada;

	def GET_coordenada_y(self) -> int:
		return self.COORDENADA_Y;
	
	def SET_coordenada_y(self, nueva_coordenada:int) -> None:
		self.COORDENADA_Y = nueva_coordenada;

		#	DIRECTORIO.
	def GET_directorio(self) -> str:
		return self.DIRECTORIO;

	def SET_directorio(self, nuevo_directorio:str) -> None:
		self.DIRECTORIO = nuevo_directorio;
		
		#	ALTO_PANTALLA.
	def GET_alto_pantalla(self) -> int:
		return self.ALTO_PANTALLA;
	
	def SET_alto_pantalla(self, nuevo_alto:int) -> None:
		self.ALTO_PANTALLA = nuevo_alto;

		#	ANCHO_PANTALLA.
	def GET_ancho_pantalla(self) -> int:
		return self.ANCHO_PANTALLA;
	
	def SET_ancho_pantalla(self, nuevo_ancho:int) -> None:
		self.ANCHO_PANTALLA = nuevo_ancho;

		#	COLORES.
	def GET_color_celdas(self):
		return self.COLOR_CELDAS;

	def GET_color_vacio(self):
		return self.COLOR_VACIO;

	def GET_color_texto(self):
		return self.COLOR_TEXTO;

	#	Destructor.

# $mypy --config-file .mypy.ini temp\