from constants import *
import os
import pygame
import sys
from pygame.locals import *

class Animation(pygame.sprite.Sprite):

	def __init__(self, image, x, y):
		super().__init__()
		self.image = image
		self.rect = self.image.get_rect(x=x, y=y)



	def update(self):
		self.verificar_limites()
		self.handle_event()
		# check collision with eneny
		#if self.rect.colliderect(enemy.rect):
		#	print("I'm killed by enemy")

	def verificar_limites(self)-> None:
		"""
		Evita que salga de la pantalla.
		"""

		if self.rect.left < 0:
			self.rect.left = 0
			#self.dx *= -1
		elif self.rect.right > WIDTH:
			self.rect.right = WIDTH
			#self.dx *= -1

		if self.rect.top < 0:
			self.rect.top = 0
			#self.dy *= -1
		elif self.rect.bottom > HEIGHT:
			self.rect.bottom = HEIGHT
			#self.dy *= -1

		


	def handle_event(self):
		key = pygame.key.get_pressed()
		if key[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()
				
		if key[pygame.K_DOWN]:
			self.rect.y += DISTANCE

		if key[pygame.K_UP]:
			self.rect.y -= DISTANCE

		if key[pygame.K_RIGHT]:
			self.rect.x += DISTANCE

		if key[pygame.K_LEFT]:
			self.rect.x -= DISTANCE

	def draw(self, surface):
		surface.blit(self.image, self.rect)
