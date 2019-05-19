import os
import pygame
import sys
from nave import Nave
from constants import *
from pygame.locals import *


class Game:

	def __init__(self):
		# centra la ventana en la pantalla.
		os.environ['SDL_VIDEO_CENTERED'] = '1'

		self.window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
		self.bg = pygame.image.load(os.path.join("data/image", "space.jpg"))
		# cambia el icono
		self.icon = pygame.image.load(os.path.join("data/image", "asteroid.png"))
		pygame.display.set_icon(self.icon)
		# corre el bucle del juego
		self.run()
		#
		nav_img = pygame.image.load(os.path.join("data/image", "nave2.png"))
		
		self.nave = Nave(nav_img,356,422)
		self.nave.draw()

	def run(self)-> None:
		"""
		Bucle principal del juego.
		"""
		clock = pygame.time.Clock()


		while True:
			clock.tick(60)
			self.window.blit(self.bg, (0, 0))
			pygame.display.update()
			


			# codigo
			self.key_press()

			

	def key_press(self):
		keys = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				keys = pygame.key.get_pressed()
				if keys[pygame.K_ESCAPE]:
					pygame.quit()
					sys.exit()
				elif event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

	

if __name__ == '__main__':
	game = Game()
	game.run()