#	-- Dependencias.
#	Dependencias externas.

#	Dependencias internas.
from CONTROLLER import Controlador;

#	-- Funciones.
#	Definición de funciones.
def main() -> None:
	#	Instancia de la clase.
	mi_controlador:Controlador = Controlador();
	mi_controlador.iniciar_procesos();

#	Inicio de ejecuciones.
if __name__ == "__main__":
	#	Call inicial.
	main();