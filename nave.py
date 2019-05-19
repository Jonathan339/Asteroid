from animation import Animation
from constants import *


class Nave(Animation):

	def __init__(self, image, x, y):
		super().__init__(image, x, y)
		self.vida = 3
		self.disparo = []
		self.disparo = []
		

	

	def quitar_vida(self)->int:
		"""
		Resta vida a la nave.
		"""
		if self.vida > 0 and self.vida < 3:
			self.vida -= 1
		else:
			pass
		return self.vida

	def agrega_vida(self)-> int:
		"""
		Agrega vida a la nave.
		"""
		if self.vida > 0 and self.vida < 3:
			self.vida += 1
		else:
			pass
		return self.vida

