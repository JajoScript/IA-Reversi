# Dependencias.
import typing, pygame, sys
import numpy as np
from pygame.locals import *

# Declaración de variables globales.
NUMERO_FILAS: int = 6;
NUMERO_COLUMNAS: int = 6;
ALTO_PANTALLA: int = 700;
ANCHO_PANTALLA: int = 600;
TAMAÑO_TABLERO: int = 440;

TAMAÑO_CELDA_ALTO: int = (TAMAÑO_TABLERO / NUMERO_FILAS);
TAMAÑO_CELDA_ANCHO: int = (TAMAÑO_TABLERO / NUMERO_COLUMNAS);

COLOR_CELDAS = (13, 171, 118);

# Definición de funciones.
def controlador_tablero(ventana) -> None:
   """ ... """

   # valores por defecto.
   posicion_x = 80
   posicion_y = 220

   for fila in range(0, NUMERO_FILAS):
      posicion_x = 80;
      for columnas in range(0, NUMERO_COLUMNAS):
      
         poligono = [   
            (posicion_x, posicion_y),
            (posicion_x + TAMAÑO_CELDA_ANCHO, posicion_y),
            (posicion_x + TAMAÑO_CELDA_ANCHO, posicion_y + TAMAÑO_CELDA_ALTO),
            (posicion_x, posicion_y + TAMAÑO_CELDA_ALTO)]

         pygame.draw.polygon(ventana, COLOR_CELDAS, poligono, 1);

         # Iteración de las columnas.
         posicion_x += TAMAÑO_CELDA_ANCHO;

      # Iteración de las filas.
      posicion_y += TAMAÑO_CELDA_ALTO;

   pass
   

def cargador_assets(nombre_archivo: str, es_transparente: bool = False) -> typing.Any:
   """ ... """

   # Cargando la imagen solicitada.
   recurso = pygame.image.load(f"./src/assets/{nombre_archivo}");
   recurso = recurso.convert();

   # Habilitando la transparencia de fondo.
   if es_transparente:
      color = recurso.get_at((0,0))
      recurso.set_colorkey(color, RLEACCEL);
   
   return recurso


def controlador_juego() -> None:
   """ ... """
   
   # Inicio de la ejecución de pygame.
   pygame.init()

   # Configuraciones de la ventana.
   ventana = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA));
   pygame.display.set_caption("REVERSI");

   # Cargando los recursos del juego. 
   fondo_juego = cargador_assets("background_base.jpg");

   # Control de fotogramas.
   FPS = pygame.time.Clock();
   FPS.tick(30);

   # Ciclo para correr el juego.
   while True:
      # Control de eventos.
      for evento in pygame.event.get():
         # Evento: salir del juego.
         if evento.type == QUIT:
            sys.exit(0);

         print(evento)

      # Posicionando los recursos en la ventana.
      ventana.blit(fondo_juego, (0,0));
      
      # Definición del tablero.
      controlador_tablero(ventana);

      # Actualización de la ventana.
      pygame.display.update();


def main() -> None:
   """ ... """

   # CALL: controlador_juego()
   controlador_juego();

   pass

# Inicio de las ejecuciones.
if __name__ == "__main__": 
   main();