import os
import pygame
import sys
from pygame.locals import *

width = 500
height = 200

class Bola(pygame.sprite.Sprite):
	"Representa una bola que rebota en pantalla."

	def __init__(self, x, y, radio, color=(0, 255, 0)):
		
		self.x, self.y = x, y
		self.radio = radio
		self._crear_imagen(radio, color)
		self.rect = self.image.get_rect(self.image)
		self.empujar(0, 0)

	def _crear_imagen(self, radio, color):
		ancho = alto = radio * 2
		self.image = pygame.Surface((ancho, alto)).convert()
		self.image.set_colorkey((0, 0, 0))
		pygame.draw.circle(self.image, color, (radio, radio), radio)

	def update(self):
		self.x += self.dx
		self.y += self.dy
		self.rect.center = (self.x, self.y)
		self.verificar_limites()

	def verificar_limites(self):
		"Evita que una bola salga de la pantalla."

		if self.rect.left < 0:
			self.rect.left = 0
			self.dx *= -1
		elif self.rect.right > width:
			self.rect.right = width
			self.dx *= -1

		if self.rect.top < 0:
			self.rect.top = 0
			self.dy *= -1
		elif self.rect.bottom > height:
			self.rect.bottom = height
			self.dy *= -1

	def empujar(self, dx, dy):
		self.dx = dx
		self.dy = dy

	def colisiona_con(self, otra):
		"""Reacciona si existe una colision con otra bola.

		Retorna True si se produce la colisión, False en caso contrario."""
		x, y, r = self.x, self.y, self.radio

		if hypot((x - otra.x), (y - otra.y)) < r + otra.radio:
			if otra.x - self.x == 0:
				a = pi / 2.0
			else:
				a = atan((self.y - otra.y) / (otra.x - self.x))

			v1r = self.dx * cos(-a) - (self.dy) * sin(-a)
			v1s = self.dx * sin(-a) + (self.dy) * cos(-a)
			v2r = otra.dx * cos(-a) - (otra.dy) * sin(-a)
			v2s = otra.dx * sin(-a) + (otra.dy) * cos(-a)
			v1r,  v2r = v2r,  v1r
			self.dx = v1r * cos(a) - v1s * sin(a)
			self.dy = (v1r * sin(a)) + (v1s * cos(a))
			otra.dx = v2r * cos(a) - v2s * sin(a)
			otra.dy = (v2r * sin(a)) + (v2s * cos(a))
			return True
		else:
			return False

def informar_colisiones(bolas):
	copia_grupo = pygame.sprite.Group(bolas)

	for a in bolas:
		for b in copia_grupo:
			if a != b and a.colisiona_con(b):
				copia_grupo.remove(a)
				copia_grupo.remove(b)

def actualizar_pantalla(screen, bolas):
	screen.fill((0, 0, 0))
	bolas.draw(screen)
	pygame.display.flip()

def main():
	screen = pygame.display.set_mode((width, height))
	bolas = pygame.sprite.Group()

	b1 = Bola(x=400, y=100, radio=10)
	b1.empujar(-1.5, 0.4)

	b2 = Bola(250, 100, 20, color=(255, 0, 0))
	b2.empujar(1.2, 0.4)

	b3 = Bola(40, 100, 10, color=(100, 0, 250))
	b3.empujar(1.5, 0.3)

	bolas.add([b1, b2, b3])

	clock = pygame.time.Clock()

	while True:
		  
		for e in pygame.event.get():
			if e.type == QUIT:
				return
			
		clock.tick(300)
		actualizar_pantalla(screen, bolas)
		bolas.update()
		colisiones = informar_colisiones(bolas)

if __name__ == '__main__':
	main()

