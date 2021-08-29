#!/usr/bin/env python
# -*- codigon: utf-8 -*-
# Dependencias.
import typing
import sys, pygame
from pygame.locals import *

# Variables globales.
alto: int = 600;
ancho: int = 600;

# Funciones.
def cargarAssets(nombre_archivo: str, transparencia: bool = False) -> typing.Any:
   
   imagen = pygame.image.load(f"./src/assets/{nombre_archivo}");
   imagen = imagen.convert()
   
   # Habilitando la transparencia del fondo.
   if transparencia:
      color = imagen.get_at((0,0))
      imagen.set_colorkey(color, RLEACCEL)
   
   return imagen

def mostrarVentana() -> None:
   # Creación de la ventana del juego.
   ventana = pygame.display.set_mode((alto, ancho));

   # Configuración: Titulo de la ventana.
   pygame.display.set_caption("Reversi game!");

   # Cargando el fondo del juego.
   juego_fondo = cargarAssets('background.jpg', transparencia=False);

   # Ciclo para mostrar constante mente la ventana del juego.
   while True:
      for evento in pygame.event.get():
         # Evento: Salir del juego.
         if evento.type == QUIT:
            sys.exit(0);

         # Posicionando la imagen.
         ventana.blit(juego_fondo, (0,0));
         pygame.display.flip();


def main() -> None:
   # Iniciando el juego.
   pygame.init();

   # Función para mostrar la ventana del juego.
   mostrarVentana();

   # Finalización del juego.
   return 0;

# Inicio de ejecución.
if __name__ == "__main__":
   main();