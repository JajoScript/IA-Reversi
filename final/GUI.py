#	-- Dependencias.
#	Dependencias externas.
import pygame;
import os;
from typing import Any;

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

	#   Metodos.

	def renderizado_objetos(self) -> None:
		"""..."""

		#   Trayendo la instancia de ventana.
		ventana = self.GET_ventana();
		

	def cargador_assets(self, tipo:str, nombre_archivo:str, es_png:bool= False) -> Any:
		"""..."""

		if (tipo == "img"):
			recurso:Any = pygame.image.load(os.path.join(self.GET_directorio(), 'assets', nombre_archivo));
			recurso.convert();

			if (es_png == True):
				color:Any = recurso.get_at((0, 0));
				recurso.set_colorkey(color, pygame.RLEACCEL);
		
		elif (tipo == "font"):
			pass
			
		else:
			print("[DEV][ERROR] Error al cargar el assets, no hay tipo definido.");
			return None;

	def controlador_ventana(self) -> None:
		"""..."""

		#   Configuración de la ventana.
		pygame.init();
		pygame.font.init();

		ventana:Any = pygame.set_mode((self.GET_ancho_pantalla(), self.GET_alto_pantalla()));
		self.SET_ventana(ventana);
		pygame.display.set_caption("REVERSI");

		# Faltan cosas aqui...


		#	Control de fotogramas.
		FPS = pygame.time.Clock();
		FPS.tick(30);

		#   Ciclo de ejecución.
		while True:
			#   Renderizando los elementos en pantalla.
			self.renderizado_objetos();

			#   Manejo de eventos del usuario.

			#   Implementación de la jugabilidad.



	#	Getters & Setters.
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