#	-- Dependencias.
#	Dependencias externas.

#	Dependencias Internas.
from GUI import Interfaz;
from GAME import Juego;
from IA import Inteligencia;

#   -- Clases.
#	Definición de la clase.
class Controlador():
    #   Propiedades.
    
    #   Constructor.
    def __init__(self) -> None:

        #   Instancias de clases.
        self.mi_inteligencia = Inteligencia();
        self.mi_juego = Juego();
        self.mi_interfaz = Interfaz();


    #   Metodos.
    def iniciar_procesos(self) -> None:
        #   Importando las instancias de cada clase.
        IA = self.GET_inteligencia();
        Reversi = self.GET_juego();
        Grafica = self.GET_interfaz();


        print(f"[DEV] IA: {IA}");
        print(f"[DEV] Reversi: {Reversi}");
        print(f"[DEV] Grafica: {Grafica}");

    #   Getters & Setters.
    #       INTELIGENCIA.
    def GET_inteligencia(self) -> Inteligencia:
        return self.mi_inteligencia;
    
    def SET_inteligencia(self, nueva_IA) -> None:
        self.mi_inteligencia = nueva_IA;

    #       JUEGO.
    def GET_juego(self) -> Juego:
        return self.mi_juego;
    
    def SET_juego(self, nueva_partida) -> None:
        self.mi_juego = nueva_partida;

    #       INTERFAZ.
    def GET_interfaz(self) -> Interfaz:
        return self.mi_interfaz;

    def SET_interfaz(self, nueva_GUI) -> None:
        self.mi_interfaz = nueva_GUI;

    
    