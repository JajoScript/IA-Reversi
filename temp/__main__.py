#	Dependencias.
import typing;
import sys;
import numpy as np;

#	Dependencias locales.
from GUI import InterfazGrafica;
from GAME import Reversi;
from IA import InteligenciaArtificial;

#	Definición de funciones.
def main() -> None:
	#	Instanciación de la inteligencia artificial.
	mi_IA = InteligenciaArtificial();

	#	Instanciación del juego Reversi.
	mi_reversi = Reversi(numero_columnas=6, numero_filas=6);
	mi_reversi.crear_estado_inicial();

	#	Ejecución de la interfaz grafica.
	#	Turno ficha blanca = False, dado que comienza la ficha negra.

	#	Recordatorio: Cambiar el directorio, a src.
	mi_interfaz = InterfazGrafica(700, 600, "temp", mi_reversi, turno_blanca=False, turno_negra=True);
	mi_interfaz.controlador_ventana();


#	Inicio de ejecuciones.
if __name__ == "__main__":
	main();