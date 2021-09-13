# Dependencias.
import typing
import sys

# Dependencias locales.
from GUI import *
from CLASE import *
from IA import *


# Definición de funciones.
def main() -> None:
   
   # Ejecución de la interfaz grafica.
   juego=Reversi(ESTADO_JUEGO)
   controlador_interfaz(juego);

   return 0;

# Inicio de ejecuciones.
if __name__ == "__main__":
   main();
