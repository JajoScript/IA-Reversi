#	-- Dependencias.
#	Dependencias externas.
import time;
from typing import Any;

#	Dependencias Internas.
from GUI import Interfaz;
from GAME import Juego;
from IA import Inteligencia;

#	-- Clases.
#	Definición de la clase.
class Controlador():
	#	Propiedades.
	#	Constructor.
	def __init__(self) -> None:
		#	Instancias de clases.
		self.mi_inteligencia:Inteligencia = Inteligencia();
		self.mi_juego:Juego = Juego(numero_filas=6, numero_columnas=6);
		self.mi_interfaz:Interfaz = Interfaz(DIR="final");


	#	Metodos.
	def log(self, mensaje:Any) -> None:
		"""..."""

		tiempo:Any = time.localtime();
		print(f"[{tiempo.tm_hour}:{tiempo.tm_min}:{tiempo.tm_sec}][DEV] {mensaje}");


	def iniciar_procesos(self) -> None:
		"""..."""

		#	Importando las instancias de cada clase.
		IA:Inteligencia = self.GET_inteligencia();
		Reversi:Juego = self.GET_juego();
		Grafica:Interfaz = self.GET_interfaz();

		#	Definimos el estado inicial del tablero.
		Reversi.definir_estado_inicial();

		#	Montando la interfaz grafica.
		self.log("Iniciando la interfaz grafica");
		Grafica.controlador_ventana(partida=Reversi);

	#	Getters & Setters.
	#		INTELIGENCIA.
	def GET_inteligencia(self) -> Inteligencia:
		return self.mi_inteligencia;
	 
	def SET_inteligencia(self, nueva_IA) -> None:
		self.mi_inteligencia = nueva_IA;

	#		JUEGO.
	def GET_juego(self) -> Juego:
		return self.mi_juego;
	 
	def SET_juego(self, nueva_partida) -> None:
		self.mi_juego = nueva_partida;

	#		INTERFAZ.
	def GET_interfaz(self) -> Interfaz:
		return self.mi_interfaz;

	def SET_interfaz(self, nueva_GUI) -> None:
		self.mi_interfaz = nueva_GUI;