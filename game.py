import os
import pygame
import sys
from nave import Nave
from constants import *
from pygame.locals import *


class Game:

	def __init__(self):
		pygame.init()
		# centra la ventana en la pantalla.
		os.environ['SDL_VIDEO_CENTERED'] = '3'

		self.window = pygame.display.set_mode((WIDTH, HEIGHT),pygame.NOFRAME)
		self.bg = pygame.image.load(os.path.join("data/image", "space.jpg")).convert()
		# cambia el icono
		self.icon = pygame.image.load(os.path.join("data/image", "asteroid.png"))
		pygame.display.set_icon(self.icon)
		# corre el bucle del juego
		
		#
		self.nav_img = pygame.image.load(os.path.join("data/image", "nave2.png"))
		self.nav_img = pygame.transform.scale(self.nav_img,(128, 128))
		self.run()
		

	

	def run(self)-> None:
		"""
		Bucle principal del juego.
		"""
		self.clock = pygame.time.Clock()
		self.nave = Nave(self.nav_img, 200,400)
		while True:
			self.clock.tick(40)
			
			 # - events -
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			
			 # - draw -			
			self.window.blit(self.bg, (0, 0))
			self.nave.draw(self.window)
			self.nave.update()

			 # - updates -
			pygame.display.update()



if __name__ == '__main__':
	game = Game()
	game.run()