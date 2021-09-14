#	-- Dependencias. --

#	-- Funciones. --

#	-- Definición de clase. --
class InteligenciaArtificial():
	#	Propiedades.
	PUEDE_GENERAR_JUGADAS:bool;

	#	Constructor.
	def __init__(self, verificacion_jugadas:bool) -> None:
		self.PUEDE_GENERAR_JUGADAS = verificacion_jugadas;

	#	Metodos.
	def generador_juegadas_validas(self):
		pass

	def evaluar(self):
		pass

	def estado_final(self):
		pass

	def devolver_estado(self):
		pass

	#	Getters & Setters.
	def GET_puede_generar_jugadas(self) -> bool:
		return self.PUEDE_GENERAR_JUGADAS;

	def SET_puede_generar_jugadas(self, nueva_configuracion) -> None:
		self.PUEDE_GENERAR_JUGADAS = nueva_configuracion;