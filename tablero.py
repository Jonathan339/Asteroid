
class Tablero:

	def __init__(self):
		self.vida_nave = None
		self.puntos_nave = None

	def modifica_vida(self, vida):
		self.vida_nave = vida
		return self.vida_nave


	def modifica_puntos(self, puntos):
		self.puntos_nave = puntos
		return self.puntos_nave